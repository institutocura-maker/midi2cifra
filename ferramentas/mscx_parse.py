#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mscx_parse.py — disseca uma partitura MuseScore (.mscz direto ou .mscx solto) e
imprime um relatório musical + dump compasso a compasso (as duas mãos).

Uso:
  python3 mscx_parse.py ARQUIVO.mscz            # relatório completo
  python3 mscx_parse.py ARQUIVO.mscz --dump     # + a música inteira, compacta
  python3 mscx_parse.py ARQUIVO.mscz --dump 12  # + só os 12 primeiros compassos

Saída do dump (uma linha por compasso, por clave):
  m 12 | S1: h[F#5+F#6] h[E#5] q[A#5] ...        (letra = duração)
  m 12 | S2: e[F#2 A#3 C#4] e[F#2 A#3 C#4] ...   (colchetes = notas juntas)
Durações: w=semibreve h=mínima q=semínima e=colcheia s=semicolcheia t=fusa
Extras: → nota presa (tie) · R[...] pausa · . = ponto (ex.: q. = semínima pontuada)
"""
import sys
import io
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter

TPC = {0: 'C', 1: 'G', 2: 'D', 3: 'A', 4: 'E', 5: 'B', 6: 'F#', 7: 'C#',
       8: 'G#', 9: 'D#', 10: 'A#', 11: 'E#', 12: 'B#',
       -1: 'F', -2: 'Bb', -3: 'Eb', -4: 'Ab', -5: 'Db', -6: 'Gb', -7: 'Cb'}
DUR = {'whole': ('w', 4.0), 'half': ('h', 2.0), 'quarter': ('q', 1.0),
       'eighth': ('e', 0.5), '16th': ('s', 0.25), '32nd': ('t', 0.125),
       '64th': ('t', 0.0625), '128th': ('t', 0.03125), 'breve': ('w', 8.0)}
LETRA_INV = {v[0]: k for k, v in DUR.items()}


def nome(pitch, tpc=None):
    if tpc is not None:
        tpc = int(tpc)
        if tpc in TPC:
            return f"{TPC[tpc]}{pitch // 12 - 1}"
    N = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return f"{N[pitch % 12]}{pitch // 12 - 1}"


def load(path):
    if path.lower().endswith('.mscz'):
        z = zipfile.ZipFile(path)
        xml = [n for n in z.namelist() if n.endswith('.mscx')][0]
        return ET.parse(io.BytesIO(z.read(xml))).getroot()
    return ET.parse(path).getroot()


def parse(root):
    """devolve (metas, {staff_id: [medida, ...]}) — medida = dict(voices=[eventos], attrs={})"""
    S = root.find('Score')
    metas = {m.get('name'): (m.text or '') for m in S.findall('metaTag')}
    metas['_versao'] = root.get('version', '?')
    staves = {}
    for st in S.findall('Staff'):
        ms = []
        for m in st.findall('Measure'):
            med = {'voices': [], 'attrs': {}}
            for a in m:
                if a.tag in ('repeatStart', 'repeatEnd', 'irregular', 'endMeasure'):
                    med['attrs'][a.tag] = True
            for v in m.findall('voice'):
                evs = []
                for el in v:
                    if el.tag == 'Chord':
                        dt = el.findtext('durationType')
                        dots = int(el.findtext('dots') or 0)
                        grace = None
                        for c in el:
                            if c.tag in ('acciaccatura', 'appoggiatura'):
                                grace = c.tag
                        notas = []
                        for n in el.findall('Note'):
                            tie = n.find('Tie')
                            notas.append({
                                'pitch': int(n.findtext('pitch')),
                                'tpc': n.findtext('tpc'),
                                'tie': tie.get('type') if tie is not None else None,
                            })
                        evs.append({'t': 'chord', 'dur': dt, 'dots': dots, 'notas': notas,
                                    'grace': grace})
                    elif el.tag == 'Rest':
                        evs.append({'t': 'rest', 'dur': el.findtext('durationType'),
                                    'dots': int(el.findtext('dots') or 0)})
                    elif el.tag == 'location':
                        frac = el.findtext('fractions')       # ex. '1/16' (de semibreve)
                        q = 0.0
                        if frac and '/' in frac:
                            n_, d_ = frac.split('/')
                            q = 4.0 * int(n_) / int(d_)
                        evs.append({'t': 'gap', 'q': q})
                    elif el.tag in ('KeySig', 'TimeSig', 'Tempo', 'Clef'):
                        med['attrs'].setdefault(el.tag, []).append(
                            {c.tag: c.text for c in el})
                    elif el.tag == 'Spanner':
                        med['attrs'].setdefault('Spanner', []).append(el.findtext('type'))
                    elif el.tag in ('Harmony', 'Dynamic', 'StaffText', 'Expression',
                                    'Fermata', 'Breath'):
                        med['attrs'].setdefault(el.tag, []).append(
                            el.findtext('text') or el.tag)
                med['voices'].append(evs)
            ms.append(med)
        staves[st.get('id')] = ms
    return metas, staves


# ─────────────────────────── relatório ───────────────────────────
def _ev_str(ev):
    if ev['t'] == 'rest':
        d = DUR.get(ev['dur'], ('?', 0))[0]
        return d + '.' * ev.get('dots', 0) + 'R'
    if ev['t'] == 'gap':
        return '—'
    d = DUR.get(ev['dur'], ('?', 0))[0]
    pts = [nome(n['pitch'], n['tpc']) + ('→' if n['tie'] == 'start' else '')
           for n in ev['notas']]
    if ev.get('grace'):
        return '~[' + '+'.join(pts) + ']'
    return d + '.' * ev.get('dots', 0) + '[' + '+'.join(pts) + ']'


def _bpm(tempo_attrs):
    for d in tempo_attrs:
        try:
            return round(float(d['tempo']) * 60)
        except (TypeError, ValueError):
            pass
    return None


def relatorio(metas, staves, dump_n=None):
    linhas = []
    L = linhas.append
    L('═' * 72)
    L(f"MuseScore {metas['_versao']} · título: {metas.get('workTitle') or '(sem título)'} "
      f"· compositor: {metas.get('composer') or '?'} · arranjo: {metas.get('arranger') or '?'}")
    ks = ts = tm = None
    clefs = {}
    for sid, ms in sorted(staves.items()):
        for m in ms:
            if ks is None and 'KeySig' in m['attrs']:
                ks = m['attrs']['KeySig']
            if ts is None and 'TimeSig' in m['attrs']:
                ts = m['attrs']['TimeSig']
            if tm is None and 'Tempo' in m['attrs']:
                tm = m['attrs']['Tempo']
            if 'Clef' in m['attrs']:
                clefs.setdefault(sid, []).extend(
                    f"{d.get('concertClefType') or d.get('sign')}" for d in m['attrs']['Clef'])
    if ks:
        n = int(ks[0].get('concertKey') or ks[0].get('accidental') or 0)
        L(f"Armadura: {n} {'sustenidos' if n > 0 else 'bemois'} · "
          f"Compasso: {ts[0]['sigN']}/{ts[0]['sigD']} · Tempo: "
          f"{(tm[0].get('text') or '').strip() if tm else '?'}"
          f"{' (followText)' if tm and tm[0].get('followText') == '1' else ''}")
    L('─' * 72)
    # por clave
    dados = {}
    for sid, ms in sorted(staves.items()):
        notas = [n for m in ms for ev in m['voices'][0] if ev['t'] == 'chord'
                 for n in ev['notas']]
        durs = Counter((ev['dur'], ev.get('dots', 0)) for m in ms
                       for ev in m['voices'][0] if ev['t'] == 'chord')
        if not notas:
            continue
        lo, hi = min(n['pitch'] for n in notas), max(n['pitch'] for n in notas)
        dados[sid] = dict(ms=ms, notas=notas, durs=durs, lo=lo, hi=hi)
        clef = clefs.get(sid, ['?'])
        L(f"Clave {sid} ({clef[0] if clef else '?'}): {len(ms)} compassos · "
          f"{len(notas)} notas · extensão {nome(lo, [n['tpc'] for n in notas if n['pitch']==lo][0])}"
          f"–{nome(hi, [n['tpc'] for n in notas if n['pitch']==hi][0])}")
        tot = sum(DUR.get(d, (0, 0))[1] * (1.5 if dots == 1 else 1) * c
                  for (d, dots), c in durs.items())
        L(f"   durações: " + ' · '.join(
            f"{DUR.get(d, ('?', 0))[0]}{'.' * dots}×{c}"
            for (d, dots), c in sorted(durs.items(), key=lambda x: -x[1])))
        L(f"   notas mais usadas: " + ' · '.join(
            f"{nome(p, t)}×{c}" for (p, t), c in
            Counter((n['pitch'], n['tpc']) for n in notas).most_common(8)))
    L('─' * 72)
    # spanners
    span = Counter(t for d in dados.values() for m in d['ms']
                   for t in m['attrs'].get('Spanner', []))
    L(f"Spanners: {dict(span) or 'nenhum'}")
    # padrões por compasso (assinatura) — repetições e estrutura
    if set(dados) >= {'1', '2'}:
        assin = []
        for i in range(min(len(dados['1']['ms']), len(dados['2']['ms']))):
            sig = (tuple(_ev_str(e) for e in dados['1']['ms'][i]['voices'][0]),
                   tuple(_ev_str(e) for e in dados['2']['ms'][i]['voices'][0]))
            assin.append(sig)
        L("Compassos idênticos (repetições literais, bloco ≥ 2):")
        rep = Counter(assin)
        vistos = set()
        for i, a in enumerate(assin):
            if rep[a] >= 2 and a not in vistos:
                idxs = [j + 1 for j, x in enumerate(assin) if x == a]
                vistos.add(a)
                L(f"  m{idxs[0]} ({len(idxs)}× em {idxs})")
    return linhas


def dump(staves, ate=None):
    linhas = []
    ids = sorted(staves)
    n = min(len(staves[i]) for i in ids)
    if ate:
        n = min(n, ate)
    for i in range(n):
        for sid in ids:
            evs = staves[sid][i]['voices'][0]
            txt = ' '.join(_ev_str(e) for e in evs)
            linhas.append(f"m{i+1:2d} | S{sid}: {txt}")
        linhas.append('')
    return linhas


if __name__ == '__main__':
    arq = sys.argv[1]
    ate = None
    if '--dump' in sys.argv:
        j = sys.argv.index('--dump')
        ate = int(sys.argv[j + 1]) if len(sys.argv) > j + 1 and sys.argv[j + 1].isdigit() else None
    metas, staves = parse(load(arq))
    print('\n'.join(relatorio(metas, staves)))
    if '--dump' in sys.argv:
        print('\n'.join(dump(staves, ate)))
