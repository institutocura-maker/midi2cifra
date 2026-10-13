#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pdf_dissect.py — dissecção forense do PDF Finale/Maestro da Billie Jean (PoC 7).

O PDF do Olivieri é vetorial: CADA glifo musical é um bloco `BT Tm Tf Tj ET`
próprio, com coordenada exata (espaço interno escalado por cm 0.12); pautas,
barras e hastes são traços `m/l/S`; feixes e ligaduras são preenchimentos `f`.

Fases:
  1. varre os content streams das 6 páginas (matrizes q/Q/cm, texto Tm/Tf/Tj/TJ);
  2. detecta sistemas (par de pautas) pelas BARRAS de compasso (verticais que
     atravessam agudo+grave) e as linhas de pauta (traços horizontais);
  3. inventaria glifos Maestro por BYTE BRUTO (os subsets T1.0/T1.1 têm
     ToUnicode diferentes — o byte é a chave canônica);
  4. (__main__) relatório + estrutura.json.

Roda:  python3 07-billie-jean-retalianist/trabalho/pdf_dissect.py
Requer: pip install pypdf
"""
import json
import sys
import re
from collections import Counter, defaultdict
from pathlib import Path

from pypdf import PdfReader
from pypdf.generic import ContentStream

AQUI = Path(__file__).resolve().parent
PDF = AQUI / 'billie-jean-retalianist.pdf'
SAIDAS = AQUI.parent / 'saidas'
SAIDAS.mkdir(exist_ok=True)

DIAT = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


# ── matrizes [a b c d e f] ────────────────────────────────────────────────
def mmul(m, n):
    return [m[0] * n[0] + m[1] * n[2], m[0] * n[1] + m[1] * n[3],
            m[2] * n[0] + m[3] * n[2], m[2] * n[1] + m[3] * n[3],
            m[0] * n[4] + m[2] * n[5] + m[4], m[1] * n[4] + m[3] * n[5] + m[5]]


def parse_tounicode(data):
    m = {}
    txt = data.decode('latin-1', 'replace')
    for bloco in re.findall(r'beginbfchar(.*?)endbfchar', txt, re.S):
        for src, dst in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', bloco):
            if len(src) <= 2:
                try:
                    m[int(src, 16)] = chr(int(dst[:4], 16))
                except Exception:
                    pass
    for bloco in re.findall(r'beginbfrange(.*?)endbfrange', txt, re.S):
        for lo, hi, dst in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>',
                                      bloco):
            try:
                lo_i, hi_i, base = int(lo, 16), int(hi, 16), int(dst[:4], 16)
            except Exception:
                continue
            for c in range(lo_i, min(hi_i, lo_i + 500) + 1):
                m[c] = chr(base + c - lo_i)
    return m


class Pagina:
    def __init__(self, reader, pageno):
        self.n = pageno
        self.glyphs = []       # dict(pag, x, y, size, uni, raw, font, base)
        self.strokes = []      # ((x0,y0),(x1,y1)) em pt device
        self.fills = []        # dict(pts, curved, rect)
        self._parse(reader, pageno)

    def _parse(self, reader, pageno):
        pg = reader.pages[pageno]
        fonts = {}
        fd = pg['/Resources'].get('/Font')
        if fd is not None:
            for nome in fd:
                f = fd[nome].get_object()
                widths = [float(w) for w in f.get('/Widths', [])] if '/Widths' in f else []
                first = int(f.get('/FirstChar', 0))
                tou = {}
                if '/ToUnicode' in f:
                    try:
                        tou = parse_tounicode(f['/ToUnicode'].get_object().get_data())
                    except Exception:
                        pass
                fonts[str(nome)] = {'base': str(f.get('/BaseFont', '?')).split('+')[-1],
                                    'widths': widths, 'first': first, 'tou': tou}
        self.fonts = fonts
        cs = ContentStream(pg.get_contents(), reader)
        ctm = [1, 0, 0, 1, 0, 0]
        stack = []
        path, curved, rectflag = [], False, False
        tm = [1, 0, 0, 1, 0, 0]
        tfs, tfname, tc = 1.0, None, 0.0

        def dev(x, y):
            return (ctm[0] * x + ctm[2] * y + ctm[4], ctm[1] * x + ctm[3] * y + ctm[5])

        for operands, op in cs.operations:
            o = op.decode('latin-1') if isinstance(op, bytes) else str(op)
            if o == 'q':
                stack.append(ctm[:])
            elif o == 'Q':
                if stack:
                    ctm = stack.pop()
            elif o == 'cm':
                ctm = mmul([float(x) for x in operands[:6]], ctm)
            elif o == 'BT':
                tm = [1, 0, 0, 1, 0, 0]
            elif o == 'Tf' and len(operands) >= 2:
                tfname, tfs = str(operands[0]), float(operands[1])
            elif o == 'Tm':
                tm = [float(x) for x in operands[:6]]
            elif o == 'Td':
                tm = mmul([1, 0, 0, 1, float(operands[0]), float(operands[1])], tm)
            elif o == 'Tc':
                tc = float(operands[0])
            elif o in ('Tj', 'TJ', "'", '"'):
                if o == 'TJ':
                    arr = operands[0]
                    try:
                        arr = arr.get_object()
                    except Exception:
                        pass
                    itens = list(arr)
                    parts = [('n', float(x)) if not isinstance(x, (bytes, str))
                             else ('s', x) for x in itens]
                else:
                    args = list(operands)
                    if o != 'Tj' and len(args) >= 3:
                        parts = [('n', float(args[0])), ('n', float(args[1])),
                                 ('s', args[-1])]
                    else:
                        parts = [('s', args[0])]
                fonte = fonts.get(tfname, {'widths': [], 'first': 0, 'tou': {},
                                           'base': '?'})
                tx = 0.0
                base_size = abs(tm[0]) if abs(tm[0]) > 0.01 else tfs
                for kind, x in parts:
                    if kind == 'n':
                        tx -= x * tfs / 1000.0
                        continue
                    raw_b = x if isinstance(x, bytes) else x.encode('latin-1', 'replace')
                    for b in raw_b:
                        m = mmul(ctm, mmul(tm, [1, 0, 0, 1, tx, 0]))
                        uni = fonte['tou'].get(b) or chr(b)
                        adv = tfs
                        idx = b - fonte['first']
                        if fonte['widths'] and 0 <= idx < len(fonte['widths']):
                            adv = fonte['widths'][idx] / 1000.0 * tfs
                        self.glyphs.append({'pag': self.n, 'x': m[4], 'y': m[5],
                                            'size': base_size * abs(ctm[0]),
                                            'uni': uni, 'raw': b,
                                            'font': tfname or '?',
                                            'base': fonte['base']})
                        tx += adv + tc
            elif o == 'm':
                path, curved, rectflag = [dev(float(operands[0]), float(operands[1]))], False, False
            elif o == 'l':
                path.append(dev(float(operands[0]), float(operands[1])))
            elif o == 'c':
                curved = True
                for j in range(0, 6, 2):
                    path.append(dev(float(operands[j]), float(operands[j + 1])))
            elif o == 're':
                rectflag = True
                x, y, w, h = (float(v) for v in operands[:4])
                for cx, cy in ((x, y), (x + w, y), (x + w, y + h), (x, y + h)):
                    path.append(dev(cx, cy))
            elif o in ('S', 's', 'f', 'F', 'f*', 'B', 'B*', 'b', 'b*', 'n'):
                if o in ('S', 's') and len(path) >= 2:
                    for i in range(1, len(path)):
                        self.strokes.append((path[i - 1], path[i]))
                elif o in ('f', 'F', 'f*', 'B', 'B*', 'b', 'b*') and path:
                    self.fills.append({'pts': path[:], 'curved': curved, 'rect': rectflag})
                path, curved, rectflag = [], False, False


# ── estrutura: pautas, sistemas, barras ──────────────────────────────────
def detecta_estrutura(pags):
    hlinhas, vlinhas = [], []
    for pg in pags:
        for (x0, y0), (x1, y1) in pg.strokes:
            if abs(y1 - y0) < 0.06 and abs(x1 - x0) > 60:
                hlinhas.append({'pag': pg.n, 'y': (y0 + y1) / 2, 'x0': min(x0, x1),
                                'x1': max(x0, x1)})
            elif abs(x1 - x0) < 0.06 and abs(y1 - y0) > 2:
                vlinhas.append({'pag': pg.n, 'x': (x0 + x1) / 2, 'y0': min(y0, y1),
                                'y1': max(y0, y1)})
    # barras de sistema: verticais que atravessam as duas pautas (>40 pt)
    barras_sys = [v for v in vlinhas if v['y1'] - v['y0'] > 40]
    sistemas = []
    for v in sorted(barras_sys, key=lambda v: (v['pag'], -v['y1'])):
        for sis in sistemas:
            if sis['pag'] == v['pag']:
                ys, yi = sis['ytop'], sis['ybot']
                if min(v['y1'], ys) - max(v['y0'], yi) > 0.7 * (v['y1'] - v['y0']):
                    sis['barras'].append(v['x'])
                    sis['ytop'] = max(ys, v['y1'])
                    sis['ybot'] = min(yi, v['y0'])
                    break
        else:
            sistemas.append({'pag': v['pag'], 'ytop': v['y1'], 'ybot': v['y0'],
                             'barras': [v['x']]})
    sistemas.sort(key=lambda s: (s['pag'], -s['ytop']))
    for sis in sistemas:
        linhas = sorted([h for h in hlinhas
                         if h['pag'] == sis['pag']
                         and sis['ybot'] - 3 <= h['y'] <= sis['ytop'] + 3],
                        key=lambda p: -p['y'])
        for nome, cinco in (('cima', linhas[:5]), ('baixo', linhas[5:10])):
            if len(cinco) == 5:
                vãos = [cinco[i]['y'] - cinco[i + 1]['y'] for i in range(4)]
                sis[nome] = {'ytop': cinco[0]['y'], 'ybot': cinco[4]['y'],
                             'gap': sum(vãos) / 4,
                             'x0': max(c['x0'] for c in cinco),
                             'x1': min(c['x1'] for c in cinco)}
            else:
                sis[nome] = None
        sis['barras'] = sorted(set(round(b, 1) for b in sis['barras']))
    sistemas = [s for s in sistemas if s['cima'] and s['baixo']]
    return sistemas, hlinhas, vlinhas


def main():
    reader = PdfReader(str(PDF))
    pags = [Pagina(reader, i) for i in range(len(reader.pages))]
    sistemas, hlinhas, vlinhas = detecta_estrutura(pags)

    print(f"páginas: {len(pags)}")
    print(f"sistemas (par agudo+grave): {len(sistemas)}")
    total_barras = 0
    for i, sis in enumerate(sistemas, 1):
        total_barras += len(sis['barras'])
        print(f"  sis{i:>2} p{sis['pag']+1} y {sis['cima']['ytop']:.1f}/{sis['baixo']['ybot']:.1f}"
              f" vão {sis['cima']['gap']:.2f} x {sis['cima']['x0']:.0f}–{sis['cima']['x1']:.0f}"
              f" · barras: {len(sis['barras'])} → {sis['barras'][:6]}{'…' if len(sis['barras']) > 6 else ''}")
    vcurtos = [v for v in vlinhas if 8 < v['y1'] - v['y0'] < 40]
    print(f"traços verticais: {len(vlinhas)} · hastes: {len(vcurtos)} · barras: "
          f"{len(vlinhas) - len(vcurtos)} (total posições de barra: {total_barras})")
    print(f"preenchimentos: {sum(len(p.fills) for p in pags)} "
          f"(curvos: {sum(1 for p in pags for f in p.fills if f['curved'])})")

    # inventário Maestro por BYTE BRUTO
    inv = defaultdict(Counter)      # raw -> Counter(base) e posições
    posicoes = defaultdict(list)
    for pg in pags:
        for g in pg.glyphs:
            if g['base'] == 'Maestro':
                inv[g['raw']][g['font']] += 1
                posicoes[g['raw']].append(g)
    print(f"\nINVENTÁRIO MAESTRO (byte bruto · unicode · vezes · fonte):")
    for raw, cnt in sorted(inv.items(), key=lambda kv: -sum(kv[1].values())):
        total = sum(cnt.values())
        g = posicoes[raw][0]
        print(f"  0x{raw:02X} {g['uni']!r:<8} ×{total:<5} {dict(cnt)} "
              f"· ex p{g['pag']+1}({g['x']:.1f},{g['y']:.1f})")

    # fontes de texto (não-Maestro): junta por base
    txts = Counter()
    for pg in pags:
        for g in pg.glyphs:
            if g['base'] != 'Maestro':
                txts[(g['base'], g['uni'])] += 1
    print(f"\nFONTES DE TEXTO ({len({b for b, _ in txts})}):")
    for (base, uni), n in txts.most_common(20):
        print(f"  {base:<28} {uni!r:<8} ×{n}")

    dados = {'sistemas': [
        {'pag': sis['pag'], 'barras': sis['barras'],
         'cima': {k: v for k, v in sis['cima'].items()},
         'baixo': {k: v for k, v in sis['baixo'].items()}} for sis in sistemas]}
    (AQUI / 'estrutura.json').write_text(json.dumps(dados, indent=1, ensure_ascii=False))
    print(f"\n→ estrutura.json ({len(sistemas)} sistemas)")

    # ── FASE 2: extração musical ─────────────────────────────────────────
    feixes, outros_fill = classifica_feixes(pags)
    print(f"\nFEIXES (preenchimentos retos, espessura ~meio espaço): {len(feixes)} "
          f"(outros fills retos: {outros_fill})")

    eventos, restos, rel = extrai(pags, sistemas, feixes)
    print(f"\nEXTRAÇÃO: {rel['n_compassos']} compassos · {rel['n_acordes']} acordes · "
          f"{rel['n_notas']} notas · {rel['n_restos']} pausas · "
          f"{rel['n_acidentes']} acidentes locais · sem pauta: {rel['sem_staff']}")
    por_dur = Counter((e['base'], e['feixes'], e['flags'], e['pontos']) for e in eventos)
    print("acordes por (figura, feixes, bandeiras, pontos):")
    for k, n in sorted(por_dur.items(), key=lambda kv: -kv[1])[:10]:
        print(f"  figura {k[0]}q · feixes {k[1]} · bandeiras {k[2]} · pontos {k[3]}  ×{n}")

    fins, ok, under, over, nvox = valida_compassos(eventos, rel['n_compassos'])
    n_slots = len(fins)
    print(f"\nVALIDAÇÃO: {ok}/{n_slots} pautas-compasso com notas fecham exato "
          f"({100*ok/max(n_slots,1):.0f}%) · 2 vozes: {nvox} · "
          f"sobrando: {len(under)} · transbordando: {len(over)}")
    if under:
        print("  sobrando (fim antes do compasso):", dict(list(sorted(under.items()))[:10]))
    if over:
        print("  transbordando:", dict(list(sorted(over.items()))[:10]))

    # extensão e histograma
    sys.path.insert(0, str(AQUI.parent.parent / 'ferramentas'))
    from mscx_parse import nome as nm
    pitches_todos = [p for e in eventos for p in e['pitches']]
    if pitches_todos:
        print(f"\nextensão: {nm(min(pitches_todos))}–{nm(max(pitches_todos))} "
              f"({min(pitches_todos)}–{max(pitches_todos)}) · {len(pitches_todos)} notas")
        hist = Counter(nm(p) for p in pitches_todos)
        print("top notas:", hist.most_common(10))
        pcs = Counter(p % 12 for p in pitches_todos)
        nomes_pc = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        print("pitch classes:", {nomes_pc[k]: v for k, v in sorted(pcs.items())})

    # ── sonda MIDI (onsets do mapa x→tempo, ♩=75) ────────────────────────
    med = {int(k): v for k, v in rel['medidas'].items()}
    minicio, t = {}, 0.0
    for m in range(1, rel['n_compassos'] + 1):
        minicio[m] = t
        t += med.get(m, 4.0)
    vozes = {'D': [], 'E': []}
    for mao in 'DE':
        for e in sorted([e for e in eventos if e['mao'] == mao],
                        key=lambda e: (e['m'], e['onset'])):
            t0 = int(round((minicio[e['m']] + e['onset']) * 480))
            dt = int(round(e['dur'] * 480))
            for p in e['pitches']:
                vozes[mao].append((t0, t0 + dt, p))
    escreve_midi(SAIDAS / 'sonda-reconstrucao-pdf.mid', 75,
                 [(0, 80, 'Billie Jean - mao direita (PDF)', vozes['D']),
                  (1, 72, 'Billie Jean - mao esquerda (PDF)', vozes['E'])])
    fim = max(off for mao in vozes.values() for _, off, _ in mao)
    print(f"\n→ sonda-reconstrucao-pdf.mid  ({len(vozes['D'])}+{len(vozes['E'])} notas, "
          f"fim em {fim/480/75*60:.1f} s)")

    # ── contraprova: transcrição IA do vídeo ─────────────────────────────
    IA = AQUI / 'billie-jean-video-ia.mscz'
    if IA.exists():
        from mscx_parse import load as _load, parse as _parse
        metas, STAVES = _parse(_load(str(IA)))
        ia = {}
        for sid, rotulo in (('1', 'D'), ('2', 'E')):
            notas = [n for m in STAVES[sid] for v in m['voices'] for e in v
                     if e['t'] == 'chord' for n in e['notas']]
            ia[rotulo] = [n['pitch'] for n in notas]
        npdf = {r: [p for e in eventos if e['mao'] == r for p in e['pitches']]
                for r in 'DE'}
        print(f"\nCONTRAPROVA IA (vídeo): IA D={len(ia['D'])} notas vs PDF D={len(npdf['D'])}"
              f" · IA E={len(ia['E'])} vs PDF E={len(npdf['E'])}")
        for rot in ('D', 'E'):
            print(f"  mão {rot}: IA top {Counter(nm(p) for p in ia[rot]).most_common(5)}")
            print(f"          PDF top {Counter(nm(p) for p in npdf[rot]).most_common(5)}")

    # notas.json p/ a fábrica
    (AQUI / 'notas.json').write_text(json.dumps(
        {'rel': rel, 'eventos': eventos, 'restos': restos}, ensure_ascii=False))
    print(f"\n→ notas.json ({len(eventos)} eventos)")
    return eventos, restos, rel




# ══════════════════════════════════════════════════════════════════════════
# FASE 2 — extração musical
# ══════════════════════════════════════════════════════════════════════════
SEMIS = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
RAW_NOTE = {0xCF: 1.0, 0xFA: 2.0, 0x77: 4.0}     # cheio, mínima, semibreve (semínimas)
RAW_FLAG = {0x6A: 1, 0x4A: 2}                      # bandeiras: colcheia (j), semicolcheia (J)
RAW_DOT = 0x2E
RAW_SHARP, RAW_NAT = 0x23, 0x6E
RAW_RESTO = {0x21: 4.0, 0x22: 2.0,                 # T1.1: semibreve, mínima
             0xCE: 1.0, 0xE4: 0.5}                 # Maestro: semínima, colcheia
TOPO_CIMA, TOPO_BAIXO = 38, 26                     # F5 e A3 (índice diatônico)
ARMADURA = {'F': 1, 'C': 1, 'G': 1}                # Fá#, Dó#, Sol#


def _vlq(n):
    out = bytearray([n & 0x7F])
    n >>= 7
    while n:
        out.insert(0, 0x80 | (n & 0x7F))
        n >>= 7
    return bytes(out)


def escreve_midi(path, bpm, vozes):
    def trilha(eventos, canal, vel, nome):
        linhas = []
        for on, off, pitch in eventos:
            linhas.append((on, 1, bytes([0x90 | canal, pitch, vel])))
            linhas.append((off, 0, bytes([0x80 | canal, pitch, 0])))
        linhas.sort(key=lambda x: (x[0], x[1]))
        data = b'\x00\xff\x03' + bytes([len(nome)]) + nome.encode('ascii')
        last = 0
        for tick, _, msg in linhas:
            data += _vlq(tick - last) + msg
            last = tick
        data += _vlq(0) + b'\xff\x2f\x00'
        return b'MTrk' + len(data).to_bytes(4, 'big') + data

    tempo = (b'\x00\xff\x51\x03' + int(60_000_000 / bpm).to_bytes(3, 'big')
             + b'\x00\xff\x2f\x00')
    trilhas = [b'MTrk' + len(tempo).to_bytes(4, 'big') + tempo]
    for canal, vel, nome_, evs in vozes:
        trilhas.append(trilha(evs, canal, vel, nome_))
    head = (b'MThd' + (6).to_bytes(4, 'big') + (1).to_bytes(2, 'big')
            + len(trilhas).to_bytes(2, 'big') + (480).to_bytes(2, 'big'))
    Path(path).write_bytes(head + b''.join(trilhas))


def classifica_feixes(pags):
    """preenchimentos retos com espessura ~meio espaço = feixes de colcheia/semicolcheia.
    Usa a espessura REAL do paralelogramo (à prova de feixe inclinado), não a bbox."""
    feixes, outros = [], 0
    for pg in pags:
        for f in pg.fills:
            if f['curved']:
                continue
            pts = f['pts']
            xs = [p[0] for p in pts]
            w = max(xs) - min(xs)
            if w < 3 or len(pts) not in (4, 5):
                outros += 1
                continue
            xmin, xmax = min(xs), max(xs)
            esq = [p[1] for p in pts if p[0] < xmin + 0.35 * (xmax - xmin) + 0.5]
            dire = [p[1] for p in pts if p[0] > xmax - 0.35 * (xmax - xmin) - 0.5]
            if len(esq) < 2 or len(dire) < 2:
                outros += 1
                continue
            t = (max(esq) - min(esq) + max(dire) - min(dire)) / 2
            if 0.9 < t < 4.5:
                ys = [p[1] for p in pts]
                feixes.append({'pag': pg.n, 'x0': xmin, 'x1': xmax,
                               'y0': min(ys), 'y1': max(ys)})
            else:
                outros += 1
    return feixes, outros


def extrai(pags, sistemas, feixes):
    """devolve (eventos, relatório). evento = dict(compasso, x, mao, pitches,
    dur, pontos, bandeiras, feixes_n, tipo)."""
    # glifos musicais indexados
    todos = [g for pg in pags for g in pg.glyphs]
    musica = [g for g in todos if g['base'] == 'Maestro']
    notes = [g for g in musica if g['raw'] in RAW_NOTE]

    # pitch de cada notehead
    def passo_info(g):
        """(sis_idx, papel, passo) do glifo, ou None."""
        melhor, dist = None, 1e9
        for i, sis in enumerate(sistemas):
            if sis['pag'] != g['pag']:
                continue
            for papel in ('cima', 'baixo'):
                st = sis[papel]
                if not (st['x0'] - 12 <= g['x'] <= st['x1'] + 12):
                    continue
                d = abs(g['y'] - (st['ytop'] + st['ybot']) / 2)
                if d < dist:
                    dist, melhor = d, (i, papel)
        if melhor is None:
            return None
        i, papel = melhor
        st = sistemas[i][papel]
        passo = round((st['ytop'] - g['y']) / (st['gap'] / 2))
        topo = TOPO_CIMA if papel == 'cima' else TOPO_BAIXO
        return i, papel, topo - passo

    for g in notes:
        info = passo_info(g)
        if info is None:
            continue
        g['sis'], g['papel'], g['passo'] = info
        idx = g['passo']                     # já é o índice diatônico absoluto
        g['letra'] = DIAT[idx % 7]
        g['octava'] = idx // 7
        g['pitch'] = 12 * (g['octava'] + 1) + SEMIS[g['letra']]

    sem_staff = [g for g in notes if 'sis' not in g]

    # acidentes locais (fora da coluna de armadura)
    acidentes = []
    for g in musica:
        if g['raw'] not in (RAW_SHARP, RAW_NAT):
            continue
        info = passo_info(g)
        if info is None:
            continue
        i, papel, passo = info
        st = sistemas[i][papel]
        if g['x'] < st['x0'] + 60:          # coluna de armadura
            continue
        acidentes.append({'sis': i, 'papel': papel, 'passo': passo,
                          'x': g['x'], 'alt': 1 if g['raw'] == RAW_SHARP else 0})

    # acordes: noteheads no mesmo sistema/pauta/x
    # número do 1º compasso de cada sistema (ordem de leitura)
    # barras filtradas: par de traços <8pt = barra dupla final, não compasso
    sis_idx_iniciais, barras_f = [], []
    total = 1
    for sis in sistemas:
        bf = [sis['barras'][0]]
        for x in sis['barras'][1:]:
            if x - bf[-1] >= 8:
                bf.append(x)
        barras_f.append(bf)
        sis_idx_iniciais.append(total)
        total += len(bf) - 1
    n_compassos = total - 1

    # início da música no 1º compasso de cada sistema (fim de clave+armadura+compasso)
    def x0_musica(sis_idx, papel):
        sis = sistemas[sis_idx]
        st = sis[papel]
        fim = barras_f[sis_idx][0]
        for g in pags[sis['pag']].glyphs:
            if g['base'] != 'Maestro' or g['raw'] not in (0x26, 0x3F, 0x23, 0x34):
                continue
            if not (st['ybot'] - 14 <= g['y'] <= st['ytop'] + 14):
                continue
            if barras_f[sis_idx][0] - 2 <= g['x'] <= barras_f[sis_idx][0] + 80:
                fim = max(fim, g['x'] + 9)
        return fim

    def compasso_de(x, sis_idx):
        b = barras_f[sis_idx]
        for k in range(len(b) - 1):
            if b[k] - 0.5 <= x < b[k + 1]:
                dur = 1.0 if b[k + 1] - b[k] < 45 else 4.0
                return sis_idx_iniciais[sis_idx] + k, k, b[k], b[k + 1], dur
        if x >= b[-1] - 0.5:
            dur = 1.0 if b[-1] - b[-2] < 45 else 4.0
            return sis_idx_iniciais[sis_idx] + len(b) - 2, len(b) - 2, b[-2], b[-1], dur
        return None, None, None, None, None

    acordes = []
    for g in sorted([n for n in notes if n.get('sis') is not None],
                    key=lambda n: (n['pag'], n['x'], -n['y'])):
        if acordes and acordes[-1]['pag'] == g['pag'] and acordes[-1]['sis'] == g['sis'] \
                and acordes[-1]['papel'] == g['papel'] \
                and (abs(acordes[-1]['x'] - g['x']) < 0.7
                     or (0 <= g['x'] - acordes[-1]['x'] < 7
                         and any(n['raw'] == g['raw'] for n in acordes[-1]['notas']))):
            acordes[-1]['notas'].append(g)
            acordes[-1]['ymin'] = min(acordes[-1]['ymin'], g['y'])
        else:
            acordes.append({'pag': g['pag'], 'sis': g['sis'], 'papel': g['papel'],
                            'x': g['x'], 'ymin': g['y'], 'notas': [g]})
    # acordes de segundas (x deslocado) — junta se dx < 2.2 e mesma pauta/medida
    fundidos = []
    for a in acordes:
        if fundidos and fundidos[-1]['pag'] == a['pag'] and fundidos[-1]['sis'] == a['sis'] \
                and fundidos[-1]['papel'] == a['papel'] \
                and 0 <= a['x'] - fundidos[-1]['x'] < 2.2 \
                and abs(a['ymin'] - fundidos[-1]['ymin']) < 6:
            fundidos[-1]['notas'] += a['notas']
            fundidos[-1]['x2'] = a['x']
        else:
            a['x2'] = a['x']
            fundidos.append(a)
    acordes = fundidos

    # durações
    dots = [g for g in musica if g['raw'] == RAW_DOT]
    flags = [g for g in musica if g['raw'] in RAW_FLAG]
    # hastes: traços verticais curtos (p/ casar feixes pela ponta)
    hastes = []
    for pg in pags:
        for (x0, y0), (x1, y1) in pg.strokes:
            if abs(x1 - x0) < 0.06 and 8 < abs(y1 - y0) < 40:
                hastes.append({'pag': pg.n, 'x': (x0 + x1) / 2,
                               'y0': min(y0, y1), 'y1': max(y0, y1)})

    # vozes: no mesmo x, cabeças de figuras diferentes = vozes diferentes
    acordes_v = []
    for a in acordes:
        por_fig = {}
        for n in a['notas']:
            por_fig.setdefault(RAW_NOTE[n['raw']], []).append(n)
        for fig in sorted(por_fig, reverse=True):
            b = dict(a)
            b['notas'] = por_fig[fig]
            b['ymin'] = min(n['y'] for n in b['notas'])
            acordes_v.append(b)
    acordes = acordes_v

    eventos = []
    for a in acordes:
        m, k, bx0, bx1, dur_m = compasso_de(a['x'], a['sis'])
        if m is None:
            continue
        bx0e = x0_musica(a['sis'], a['papel']) if k == 0 else bx0
        stf = sistemas[a['sis']][a['papel']]
        base = max(RAW_NOTE[n['raw']] for n in a['notas'])
        # ponto de aumento: cada ponto casado com a cabeça mais próxima
        # (ponto em nota de LINHA desloca ~2.1pt; em espaço, fica na altura)
        dots_do = {}
        for d in dots:
            if d['pag'] != a['pag'] or not (a['x'] + 0.5 < d['x'] < a['x'] + 13):
                continue
            if not (stf['ybot'] - 25 <= d['y'] <= stf['ytop'] + 25):
                continue
            melhor, dm = None, 2.7
            for n in a['notas']:
                dd = abs(d['y'] - n['y'])
                if dd < 0.9:
                    melhor = n
                    break
                if dd < dm:
                    melhor, dm = n, dd
            if melhor is not None:
                dots_do[id(melhor)] = dots_do.get(id(melhor), 0) + 1
        npt = min(max(dots_do.values(), default=0), 2)
        # haste: à direita da cabeça quando sobe, à esquerda quando desce (±6.4pt)
        ymax = max(n['y'] for n in a['notas'])
        centro = (a['ymin'] + ymax) / 2
        tip, stem_x = None, a['x']
        for h in hastes:
            if h['pag'] != a['pag'] or abs(h['x'] - a['x']) > 8.5:
                continue
            if not (stf['ybot'] - 40 <= h['y0'] and h['y1'] <= stf['ytop'] + 40):
                continue
            if min(min(abs(h['y0'] - n['y']), abs(h['y1'] - n['y']))
                   for n in a['notas']) > 4:
                continue
            d_top, d_bot = h['y1'] - centro, centro - h['y0']
            sobe = d_top > d_bot
            tip = h['y1'] if sobe else h['y0']
            stem_x = h['x']
            break
        # feixes: cobrem a HASTE; a 2ª haste empilha ~5pt além da ponta
        nfx = 0
        if tip is not None:
            lo, hi = ((tip - 8.0, tip + 3.0) if sobe else (tip - 3.0, tip + 8.0))
            nfx = sum(1 for fx in feixes
                      if fx['pag'] == a['pag'] and fx['x0'] - 1.0 <= stem_x <= fx['x1'] + 1.0
                      and fx['y0'] <= hi and fx['y1'] >= lo)
            nfl = sum(RAW_FLAG[f['raw']] for f in flags
                      if f['pag'] == a['pag'] and abs(f['x'] - stem_x) < 3.5
                      and abs(f['y'] - tip) < 7.0)
        else:
            nfl = sum(RAW_FLAG[f['raw']] for f in flags
                      if f['pag'] == a['pag'] and abs(f['y'] - a['ymin']) < 27
                      and a['x'] - 7.5 < f['x'] < a['x'] + 7.5)
        divis = 2 ** max(nfl, nfx)
        dur = base / divis * (1.5 ** npt)
        pitches = []
        for n in a['notas']:
            alt = ARMADURA.get(n['letra'], 0)
            for ac in acidentes:
                if (ac['sis'] == a['sis'] and ac['papel'] == a['papel']
                        and ac['passo'] == n['passo']
                        and n['x'] - 10 < ac['x'] <= n['x']):
                    alt = ac['alt']
            pitches.append(12 * (n['octava'] + 1) + SEMIS[n['letra']] + alt)
        eventos.append({'m': m, 'x': a['x'], 'mao': 'D' if a['papel'] == 'cima' else 'E',
                        'pitches': sorted(set(pitches)), 'dur': dur, 'base': base,
                        'pontos': npt, 'flags': nfl, 'feixes': nfx,
                        'bx0e': bx0e, 'bx1': bx1, 'mdur': dur_m})

    # pausas (todos os glifos: há pausas em Maestro e em T1.1)
    restos = []
    for g in todos:
        if g['raw'] not in RAW_RESTO:
            continue
        info = passo_info(g)
        if info is None:
            continue
        m, k, bx0, bx1, dur_m = compasso_de(g['x'], info[0])
        if m is None:
            continue
        bx0e = x0_musica(info[0], info[1]) if k == 0 else bx0
        restos.append({'m': m, 'x': g['x'], 'mao': 'D' if info[1] == 'cima' else 'E',
                       'dur': RAW_RESTO[g['raw']], 'bx0e': bx0e, 'bx1': bx1, 'mdur': dur_m})

    # ── onsets: cadeia de durações por voz; o x ancora e ordena ──────────
    por_m = {}
    for e in eventos + restos:
        por_m.setdefault((e['m'], e['mao']), []).append(e)
    for (m, mao), evs in por_m.items():
        dur_m = evs[0]['mdur']
        evs.sort(key=lambda e: e['x'])
        # estimativa grossa x→tempo do compasso (só para ancorar as vozes)
        xs = sorted(set(round(e['x'], 2) for e in evs))
        clusters = []
        for x in xs:
            if clusters and x - clusters[-1][-1] <= 3.0:
                clusters[-1].append(x)
            else:
                clusters.append([x])
        x0c = clusters[0][0]
        bx0e, bx1 = evs[0]['bx0e'], evs[0]['bx1']
        if x0c - bx0e > 22:              # compasso começa com pausa
            W = (bx1 - bx0e - 8) / dur_m
            x0c = bx0e + 8
        else:
            W = (bx1 - x0c) / dur_m
        est = {x: round((sum(cl) / len(cl) - x0c) / W * 4) / 4
               for cl in clusters for x in cl}
        est = {x: (0.0 if v < 0.26 else v) for x, v in est.items()}
        # cadeia: cada evento encosta no fim da voz mais cheia que ele alcança
        fins = []                        # fim de cada voz
        for e in evs:
            te = est[round(e['x'], 2)]
            alvo = None
            for vf in sorted(fins, reverse=True):
                if vf <= te + 0.30:
                    alvo = vf
                    break
            if alvo is None and fins and min(fins) <= te + 0.55 \
                    and min(fins) + e['dur'] <= dur_m + 0.01:
                alvo = min(fins)          # estimativa defasada: encadeia na 1ª voz
            if alvo is None:                          # nova voz
                e['onset'] = max(0.0, min(te, dur_m - e['dur']))
                fins.append(e['onset'] + e['dur'])
                fins.sort()
            elif te > alvo + 0.30 and te + e['dur'] <= dur_m + 0.01:
                e['onset'] = te                       # pausa antes, mesma voz
                fins[fins.index(alvo)] = te + e['dur']
            else:                                     # encadeia (corrige estimativa)
                e['onset'] = alvo
                fins[fins.index(alvo)] = alvo + e['dur']
        # retrofit: nada atravessa a barra final (meia nota no fim TERMINA na barra)
        for e in evs:
            if e['onset'] + e['dur'] > dur_m + 0.01:
                novo = max(0.0, dur_m - e['dur'])
                if novo <= e['onset']:
                    e['onset'] = novo

    medidas = {}
    for i, sis in enumerate(sistemas):
        b = barras_f[i]
        for k in range(len(b) - 1):
            medidas[sis_idx_iniciais[i] + k] = 1.0 if b[k + 1] - b[k] < 45 else 4.0
    rel = {'n_compassos': n_compassos, 'sem_staff': len(sem_staff),
           'n_acordes': len(eventos), 'n_notas': sum(len(e['pitches']) for e in eventos),
           'n_restos': len(restos), 'n_acidentes': len(acidentes),
           'medidas': {str(k): v for k, v in medidas.items()}}
    return eventos, restos, rel


def valida_compassos(eventos, n_compassos):
    """por pauta-compasso: fim da cadeia (máx onset+dur), transbordos e buracos."""
    fins, over, under, nvox = {}, {}, {}, 0
    for e in eventos:
        chave = (e['m'], e['mao'])
        fins[chave] = max(fins.get(chave, 0.0), e['onset'] + e['dur'])
        if e['onset'] + e['dur'] > e['mdur'] + 0.01:
            over[chave] = round(e['onset'] + e['dur'] - e['mdur'], 2)
    # medidas com 2 vozes (eventos sobrepostos na mesma mão)
    por_m = {}
    for e in eventos:
        por_m.setdefault((e['m'], e['mao']), []).append(e)
    for chave, evs in por_m.items():
        evs = sorted(evs, key=lambda e: (e['onset'], -e['dur']))
        livre = -1.0
        duas = False
        for e in evs:
            if e['onset'] < livre - 0.01:
                duas = True
            livre = max(livre, e['onset'] + e['dur'])
        if duas:
            nvox += 1
        if chave not in over and fins[chave] < evs[0]['mdur'] - 0.126:
            under[chave] = round(evs[0]['mdur'] - fins[chave], 2)
    ok = sum(1 for k, v in fins.items() if abs(v - 4.0) < 0.01)
    return fins, ok, under, over, nvox

if __name__ == "__main__":
    main()
