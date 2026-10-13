#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gera_billie_jean.py — fábrica PoC 7 · Billie Jean (Michael Jackson, 1982)
                    versão lírica de piano de Romain Olivieri (Retalianist, 2013)

GERA:  ../saidas/mapa-musical-billie-jean.html   (o mapa)
       ../saidas/teclado-billie.png              (teclado-guia p/ DOCX)
       ../saidas/estudo-{esquerda,direita,juntas}-{55,65,75}.mid  (×9, os estudos)
       ../saidas/a-assinatura.mid                (o loop de treino do riff)

FONTE ÚNICA DE VERDADE = trabalho/notas.json (a dissecção nota-a-nota do PDF oficial
Finale/Maestro, validada de ouvido pelo user em 13/10/2026 — 87% dos compassos exatos,
contraprova IA do vídeo batendo os topos). Este script NÃO re-disseca o PDF: só vira
mapa aquilo que já foi extraído e ouvido.

A PEÇA EM UMA FRASE: o groove mais famoso do pop, desacelerado à metade (♩=75 vs ~115
do disco), no mesmo tom (Fá# menor) — e o riff que no disco é baixo vira, nas mãos do
arranjista, umacantiga: primeiro melodia, depois baixo, depois refrão inteiro.
"""
import json
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SAIDAS = AQUI.parent / 'saidas'
NOTAS = AQUI / 'notas.json'
PPQ = 480

sys.path.insert(0, str(AQUI.parent.parent / 'ferramentas'))
from mscx_parse import nome as nm          # nome(pitch) → 'F#4'

# ═════════════════════════ 1. A CAMA (fatos fixos da peça) ═════════════════════════

TOM = 'Fá# menor (3 sustenidos: Fá#, Dó#, Sol#)'
BPM = 75
DURACAO_Q = 60.0 / BPM                      # 0,8 s por tempo

RIFF = [66, 61, 64, 66, 64, 61, 59, 61]     # F#4 C#4 E4 F#4 | E4 C#4 B3 C#4
RIFF_ROTULO = 'Fá#4 · Dó#4 · Mi4 · Fá#4 · Mi4 · Dó#4 · Si3 · Dó#4'
RIFF_NOTAS = 'quatro notas — Fá#, Dó#, Mi e Si: a escala de Fá#m cabendo numa mão'

# seções: letra → (sistema 1-based onde a letra está impressa no PDF)
LETRAS_SIS = {3: 'A', 7: 'B', 9: 'C', 10: 'D', 14: 'E', 16: 'F', 23: 'G', 26: 'H'}

# texto editorial (tradução de ouvido — o user não lê teoria)
EDITORIAL = {
 'INTRO': ('A assinatura, sozinha no palco',
   'O riff que você conhece de cor — só que devagar, em colcheias calmas, na mão direita, '
   'enquanto a esquerda deita acordes inteiros descendo <b>Fá#m → Mi → Ré → Si</b>. '
   'Seis voltas do riff (c1–3 e c5–7). Você reconhece a música no primeiro segundo; '
   'só não reconhece o andamento.'),
 'A': ('A melodia nasce do riff',
   'A cantiga do arranjo emana das mesmas quatro notas. Meio da seção: a primeira grande '
   'virada de cenário — em c16–17 <b>o riff desce pra mão esquerda</b> e a direita passa a '
   'segurar notas longas. Tem o compasso de 1 tempo (c14), o fôlego duplo (c14–15) e as '
   'primeiras cores escuras: Mi♯ em c12 e, em c23, <b>o único Fá natural da peça</b> '
   '(com um Mi♯ do lado — o momento mais picante da harmonia).'),
 'B': ('Um andar acima',
   'A melodia muda de morada: passa a circular no Lá3–Fá#4, a cama esquenta com o Si. '
   'É o trecho mais “cantado” até aqui — a mão direita frasa como voz.'),
 'C': ('O relâmpago de memória',
   'Quatro compassos só: <b>o riff volta à tona na mão direita</b> (c34–36), a esquerda '
   'quase silencia. É o disco inteiro passando num flash dentro da versão lenta.'),
 'D': ('O porão',
   'A seção mais grave e mais cheia: o baixo toma conta (121 eventos na esquerda!) e a '
   'peça desce ao <b>porão: Sol#1 em c52</b>, a nota mais grave. O riff ronca no fundão '
   '(c45–47, c53). Compasso de 1 tempo em c39, Mi♯ em c50.'),
 'E': ('De volta ao ar',
   'A melodia volta a respirar no alto (Fá#4, Lá3), a cama volta ao Fá#. Uma rampa '
   'tranquila — a calma antes da campeã. Mi♯ em c62 fecha a família das cores escuras.'),
 'F': ('A SEÇÃO CAMPEÃ — o refrão do arranjador',
   'Vinte e nove compassos, um terço da peça. Primeiro o desenho sincopado com o pedal de '
   'Sol#4 em cima (c63–67); a partir de c77, <b>o riff no agudo, doze vezes seguidas, '
   'sem parar</b> — a mão esquerda gira o carrossel Fá#–Mi–Ré com inversões pra cima e '
   'pra baixo. É a Billie Jean original enfim “acordando” por dentro da versão lenta.'),
 'G': ('A ponte — outro mundo',
   'Fôlego duplo em c92 e a harmonia muda de cor (o baixo muda pra Ré/Lá). Aqui moram as '
   '<b>fusas em oitonas</b> (c93–99): pares de notas velozes, uma em cada oitava, subindo '
   'e caindo como escadas rolantes — o único momento de “vertigem” da peça. A mão direita '
   'toca o teto E5.'),
 'H': ('A despedida',
   'O final abre o leque: é aqui que a direita <b>toca o teto da peça, Fá#5 em c105</b>. '
   'O riff dá a última aparição em c113 — uma última volta do carrossel — e a peça '
   'termina assentando no Fá#.'),
}

# ═════════════════════════ 2. DADOS DINÂMICOS ═════════════════════════

def carrega():
    d = json.load(open(NOTAS))
    return d['eventos'], d['restos'], d['rel']


def secoes(rel):
    """[(rótulo, m0, m1)] contíguos 1..n, com INTRO antes da letra A."""
    n = rel['n_compassos']
    # 1º compasso de cada sistema, pelo mesmos critérios do dissector (barras ≥8pt)
    est = json.load(open(AQUI / 'estrutura.json'))['sistemas']
    tot, m0_sis = 1, {}
    for i, sis in enumerate(est, 1):
        bf = [sis['barras'][0]]
        for x in sis['barras'][1:]:
            if x - bf[-1] >= 8:
                bf.append(x)
        m0_sis[i] = tot
        tot += len(bf) - 1
    marcas = [(letra, m0_sis[sis]) for sis, letra in sorted(LETRAS_SIS.items(), key=lambda kv: kv[1])]
    out = [('INTRO', 1, marcas[0][1] - 1)]
    for j, (letra, m0) in enumerate(marcas):
        m1 = marcas[j + 1][1] - 1 if j + 1 < len(marcas) else n
        out.append((letra, m0, m1))
    return out


def pc(p):
    return p % 12


def acha_riffs(evs):
    """aparições do riff completo (8 colcheias seguidas, mesmas classes de altura)"""
    alvo = [pc(p) for p in RIFF]
    out = []
    for mao in 'DE':
        sel = [e for e in evs if e['mao'] == mao and e['dur'] == 0.5]
        sel.sort(key=lambda e: (e['m'], e['onset']))
        i = 0
        while i <= len(sel) - 8:
            jan = sel[i:i + 8]
            if len({e['m'] for e in jan}) > 2:
                i += 1
                continue
            ok = True
            for e, want in zip(jan, alvo):
                if not (e['pitches'] and all(pc(p) == want for p in e['pitches'])):
                    ok = False
                    break
            if ok:
                out.append({'mao': mao, 'm': jan[0]['m'],
                            'grau': jan[0]['pitches'][0]})
                i += 8
            else:
                i += 1
    return out


def nome_acorde(pitches):
    """nome de acorde tolerante (com inversão e quinta aberta)"""
    N = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    pcs = sorted({p % 12 for p in pitches})
    baixo = min(pitches) % 12
    melhor = None
    for cand in pcs:
        ter = (cand + 4) % 12 in pcs
        men = (cand + 3) % 12 in pcs
        qui = (cand + 7) % 12 in pcs
        if (ter or men) and qui:
            pontos = 2 + (ter or men) + 0
            if melhor is None or pontos > melhor[0]:
                melhor = (pontos, cand, men and not ter)
    if melhor:
        _, cand, menor = melhor
        rot = N[cand] + ('m' if menor else '')
        if cand != baixo:
            rot += f'/{N[baixo]}'
        return rot
    if len(pcs) == 2 and (pcs[1] - pcs[0]) % 12 == 7:
        return N[pcs[0]] + '5'
    return '+'.join(N[p] for p in pcs)


def stats(evs, riffs):
    geral = {}
    ps = [p for e in evs for p in e['pitches']]
    geral['n_notas'] = len(ps)
    geral['ext'] = (min(ps), max(ps))
    geral['moradas'] = Counter(nm(p) for p in ps).most_common(10)
    por_mao = {}
    for mao in 'DE':
        pm = [p for e in evs if e['mao'] == mao for p in e['pitches']]
        por_mao[mao] = {'n': len(pm), 'ext': (min(pm), max(pm)),
                        'top': Counter(nm(p) for p in pm).most_common(5)}
    # momentos raros
    raros = {
        'mi_sustenido': sorted({e['m'] for e in evs
                                if any(pc(p) == 5 for p in e['pitches'])}),
        'porao': sorted(e['m'] for e in evs if 32 in e['pitches']),
        'teto': sorted(e['m'] for e in evs if 78 in e['pitches']),
        'fusas': sorted({e['m'] for e in evs if e['dur'] <= 0.126}),
        'um_tempo': sorted({e['m'] for e in evs if e['mdur'] == 1.0}),
    }
    # respirações: ambas as mãos terminam cedo
    fim = {}
    for e in evs:
        k = (e['m'], e['mao'])
        fim[k] = max(fim.get(k, 0.0), e['onset'] + e['dur'])
    raros['respiros'] = [m for m in range(1, 115)
                         if (m, 'D') in fim and (m, 'E') in fim
                         and fim[(m, 'D')] < 3.8 and fim[(m, 'E')] < 3.8]
    return geral, por_mao, raros


def cama_por_secao(evs, secs):
    """os acordes longos (≥ mínima) da mão esquerda, por seção"""
    out = {}
    for rot, a, b in secs:
        longos = [e for e in evs if a <= e['m'] <= b and e['mao'] == 'E' and e['dur'] >= 1.5]
        cont = Counter(nome_acorde(e['pitches']) for e in longos)
        # raízes (sem inversão) p/ ler o carrossel
        raizes = Counter(c.split('/')[0] for c in cont.elements())
        out[rot] = (cont.most_common(5), raizes.most_common(4))
    return out


# ═════════════════════════ 3. SANITY ═════════════════════════

def sanity(evs, rel, secs, riffs, geral):
    assert rel['n_compassos'] == 114, f"compassos {rel['n_compassos']} ≠ 114"
    a0 = secs[0][1]
    assert a0 == 1 and secs[-1][2] == 114, f"seções não cobrem 1–114: {secs}"
    for (r1, _, b1), (r2, a2, _) in zip(secs, secs[1:]):
        assert b1 == a2 - 1, f"buraco entre {r1} e {r2}"
    assert geral['n_notas'] == 1690, f"notas {geral['n_notas']} ≠ 1690"
    assert geral['ext'] == (32, 78), f"extensão {geral['ext']} ≠ (G#1, F#5)"
    assert len(riffs) >= 29, f"riff só {len(riffs)}× (esperado ≥29)"
    maos = Counter(r['mao'] for r in riffs)
    assert maos['D'] >= 20 and maos['E'] >= 5, f"riff por mão estranho: {maos}"
    top1 = geral['moradas'][0][0]
    assert top1 == 'F#4', f"morada nº1 {top1} ≠ F#4"
    return True


# ═════════════════════════ 4. MIDIs ═════════════════════════

def _vlq(n):
    b = [n & 0x7F]
    n >>= 7
    while n:
        b.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(b))


def escreve_midi(path, bpm, vozes):
    """vozes = [(canal, vel, nome, [(on, off, pitch)])] em ticks"""
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
            + len(trilhas).to_bytes(2, 'big') + PPQ.to_bytes(2, 'big'))
    Path(path).write_bytes(head + b''.join(trilhas))


def timeline(evs, mao, med, minicio):
    out = []
    for e in sorted([e for e in evs if e['mao'] == mao], key=lambda e: (e['m'], e['onset'])):
        t0 = int(round((minicio[e['m']] + e['onset']) * PPQ))
        dt = int(round(e['dur'] * PPQ))
        for p in e['pitches']:
            out.append((t0, t0 + dt, p))
    return out


def build_midis(evs, rel):
    med = {int(k): v for k, v in rel['medidas'].items()}
    minicio, t = {}, 0.0
    for m in range(1, rel['n_compassos'] + 1):
        minicio[m] = t
        t += med.get(m, 4.0)
    td = timeline(evs, 'D', med, minicio)
    te = timeline(evs, 'E', med, minicio)
    feitos = []
    for bpm in (55, 65, 75):
        escreve_midi(SAIDAS / f'estudo-esquerda-{bpm}.mid', bpm,
                     [(1, 72, 'Billie Jean - mao esquerda', te)])
        escreve_midi(SAIDAS / f'estudo-direita-{bpm}.mid', bpm,
                     [(0, 84, 'Billie Jean - mao direita', td)])
        escreve_midi(SAIDAS / f'estudo-juntas-{bpm}.mid', bpm,
                     [(0, 84, 'Billie Jean - mao direita', td),
                      (1, 72, 'Billie Jean - mao esquerda', te)])
        feitos += [f'estudo-esquerda-{bpm}.mid', f'estudo-direita-{bpm}.mid',
                   f'estudo-juntas-{bpm}.mid']
    # ── a assinatura: o loop de treino (c1–4 reais ×4 voltas, ♩=75) ──
    assin_d, assin_e = [], []
    for volta in range(4):
        base = volta * 16 * PPQ                      # 4 compassos × 4 tempos
        for mao, dest in (('D', assin_d), ('E', assin_e)):
            for e in evs:
                if e['mao'] != mao or e['m'] > 4:
                    continue
                t0 = base + int(round(((e['m'] - 1) * 4 + e['onset']) * PPQ))
                dt = int(round(e['dur'] * PPQ))
                for p in e['pitches']:
                    dest.append((t0, t0 + dt, p))
    escreve_midi(SAIDAS / 'a-assinatura.mid', BPM,
                 [(0, 84, 'A assinatura (treino do riff)', assin_d),
                  (1, 72, 'A assinatura (cama)', assin_e)])
    feitos.append('a-assinatura.mid')
    return feitos, len(td), len(te)


# ═════════════════════════ 5. TECLADO PNG (p/ DOCX) ═════════════════════════

def teclado_png(path, moradas, ext, riffs):
    from PIL import Image, ImageDraw, ImageFont
    WW, H = 30, 120
    brancas = [p for p in range(31, 85) if pc(p) in (0, 2, 4, 5, 7, 9, 11)]
    pretas = [p for p in range(31, 85) if pc(p) in (1, 3, 6, 8, 10)]
    W = 20 + len(brancas) * WW
    TOP = 56
    img = Image.new('RGB', (W, TOP + H + 78), '#14182b')
    d = ImageDraw.Draw(img)

    def fonte(sz, bold=False):
        for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
                  if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',):
            try:
                return ImageFont.truetype(p, sz)
            except OSError:
                pass
        return ImageFont.load_default()

    cont = {nm_rev(k): v for k, v in moradas}
    x_pos, x = {}, 20
    for p in brancas:
        n = cont.get(p, 0)
        fill = '#f5b942' if n >= 100 else ('#c8a557' if n >= 50 else '#e8e4da')
        d.rectangle([x, TOP, x + WW - 2, TOP + H], fill=fill, outline='#0c0e18')
        if n:
            d.text((x + WW / 2 - 1, TOP + H - 16), str(n), font=fonte(10), anchor='ma',
                   fill='#232742')
        d.text((x + WW / 2 - 1, TOP + H - 5), nm(p), font=fonte(9), anchor='ma',
               fill='#565b75')
        x_pos[p] = x
        x += WW
    for p in pretas:
        bx = x_pos[p - 1] + WW - 9
        n = cont.get(p, 0)
        fill = '#f5b942' if n >= 100 else ('#8a6d2f' if n >= 50 else '#171b2e')
        d.rectangle([bx, TOP, bx + 18, TOP + int(H * 0.62)], fill=fill, outline='#000')
        if n:
            d.text((bx + 9, TOP + int(H * 0.62) - 4), str(n), font=fonte(9), anchor='ma',
                   fill='#ffe9b0' if n < 100 else '#232742')
        x_pos[p] = bx

    def balao(p, txt, ty, cor='#ffd166'):
        cx = x_pos[p] + (WW / 2 if p in brancas else 9)
        d.line([cx, TOP - 3, cx, ty + 4], fill=cor, width=1)
        d.text((cx, ty - 4), txt, font=fonte(11, bold=True), anchor='ma', fill=cor)

    balao(66, '▲ a morada nº1 (Fá#4 ×186)', 12)
    balao(78, '▲ teto: Fá#5 (c105)', 30, '#9fd8ff')
    balao(32, 'porão: Sol#1 (c52) →', 30, '#9fd8ff')
    d.text((20, 8), 'BILLIE JEAN (versão Retalianist) — onde a peça mora no teclado '
                    '(nº = notas tocadas)', font=fonte(12, bold=True), fill='#f2ead8')
    d.text((20, TOP + H + 12),
           'dourado forte = +100 notas · dourado suave = 50–99 · '
           f'extensão da peça: {nm(ext[0])}–{nm(ext[1])} · '
           f"riff: {len(riffs)} aparições (D {Counter(r['mao'] for r in riffs)['D']}× · "
           f"E {Counter(r['mao'] for r in riffs)['E']}×)",
           font=fonte(11), fill='#aab2cc')
    img.save(path)
    return path


def nm_rev(rotulo):
    """'F#4' → 66"""
    N = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    o = int(rotulo[-1])
    return 12 * (o + 1) + N.index(rotulo[:-1])


# ═════════════════════════ 6. HTML ═════════════════════════

CSS = """
 body{margin:0;background:#0b0d18;color:#e8e6df;font-family:Verdana,Geneva,sans-serif;
      line-height:1.55}
 .wrap{max-width:960px;margin:0 auto;padding:26px 20px 70px}
 h1{font-size:30px;margin:6px 0 2px;color:#f5b942;letter-spacing:.5px}
 h2{font-size:20px;margin:38px 0 10px;color:#f5b942;border-bottom:1px solid #2a3050;
    padding-bottom:6px}
 h3{font-size:15px;margin:18px 0 6px;color:#ffd97a}
 p,li{font-size:14px}
 .sub{color:#aab2cc;font-size:15px;margin-bottom:18px}
 .card{background:#131730;border:1px solid #272e52;border-radius:10px;
       padding:14px 18px;margin:12px 0}
 .ouro{color:#f5b942;font-weight:bold}
 .azul{color:#9fd8ff;font-weight:bold}
 .tag{display:inline-block;background:#1d2342;border:1px solid #34406e;border-radius:20px;
      padding:1px 10px;font-size:12px;color:#c9d2f0;margin:0 6px 6px 0}
 table{border-collapse:collapse;width:100%;font-size:13px;margin:10px 0}
 th,td{border:1px solid #2a3158;padding:6px 9px;text-align:left;vertical-align:top}
 th{background:#1a2044;color:#ffd97a}
 tr:nth-child(even) td{background:#101428}
 .peq{font-size:12px;color:#8b93a7}
 .faixa{display:flex;gap:0;margin:8px 0 2px}
 .faixa div{flex:1;text-align:center;font-size:11px;padding:5px 2px;color:#cfd6ee}
"""


def svg_teclado_html(moradas, ext):
    WW, BW, TOP, H = 30, 18, 58, 118
    brancas = [p for p in range(31, 85) if pc(p) in (0, 2, 4, 5, 7, 9, 11)]
    pretas = [p for p in range(31, 85) if pc(p) in (1, 3, 6, 8, 10)]
    W = 10 + len(brancas) * WW
    cont = dict(moradas)
    x_pos, x = {}, 10
    s = [f'<svg viewBox="0 0 {W + 10} 240" xmlns="http://www.w3.org/2000/svg" '
         f'style="width:100%;max-width:900px;">']
    for p in brancas:
        n = cont.get(nm(p), 0)
        fill = '#f5b942' if n >= 100 else ('#c8a557' if n >= 50 else '#e9e5da')
        s.append(f'<rect x="{x}" y="{TOP}" width="{WW-2}" height="{H}" rx="3" '
                 f'fill="{fill}" stroke="#10131f"/>')
        if n:
            s.append(f'<text x="{x+WW/2-1}" y="{TOP+H-16}" text-anchor="middle" '
                     f'font-size="10" fill="#232742" font-weight="bold">{n}</text>')
        s.append(f'<text x="{x+WW/2-1}" y="{TOP+H-4}" text-anchor="middle" '
                 f'font-size="9" fill="#565b75">{nm(p)}</text>')
        x_pos[p] = x
        x += WW
    for p in pretas:
        bx = x_pos[p - 1] + WW - BW / 2 - 1
        n = cont.get(nm(p), 0)
        fill = '#f5b942' if n >= 100 else ('#8a6d2f' if n >= 50 else '#141926')
        s.append(f'<rect x="{bx}" y="{TOP}" width="{BW}" height="{int(H*0.62)}" rx="2" '
                 f'fill="{fill}" stroke="#000"/>')
        if n:
            s.append(f'<text x="{bx+BW/2}" y="{TOP+int(H*0.62)-6}" text-anchor="middle" '
                     f'font-size="9" fill="{"#232742" if n>=100 else "#ffe9b0"}">{n}</text>')
        x_pos[p] = bx

    def call(p, txt, ty, cor='#ffd166'):
        cx = x_pos[p] + (WW / 2 if p in brancas else BW / 2)
        s.append(f'<line x1="{cx}" y1="{TOP-3}" x2="{cx}" y2="{ty+5}" stroke="{cor}" '
                 f'stroke-width="1" stroke-dasharray="2,2"/>')
        s.append(f'<text x="{cx}" y="{ty}" text-anchor="middle" font-size="11" '
                 f'fill="{cor}" font-weight="bold">{txt}</text>')
    call(66, '▲ a morada nº1 · Fá#4 ×186', 14)
    call(61, 'Dó#4 ×167', 32, '#c9d2f0')
    call(54, 'Fá#3 ×134', 14, '#c9d2f0')
    call(78, '▲ teto Fá#5 (c105)', 50, '#9fd8ff')
    call(32, 'porão Sol#1 (c52)', 50, '#9fd8ff')
    s.append(f'<text x="{W/2}" y="{TOP+H+22}" text-anchor="middle" font-size="12" '
             f'fill="#aab2cc">dourado forte = mais de 100 notas · dourado suave = 50–99 · '
             f'número = quantas vezes a nota soa</text>')
    s.append('</svg>')
    return ''.join(s)


def svg_riff_rua(riffs, secs):
    """a linha do tempo m1–114 com as aparições do riff (a 'rua da assinatura')"""
    n = 114
    W, H = 940, 132
    mm = lambda m: 26 + (m - 1) * (W - 40) / n
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
         f'style="width:100%;max-width:940px;">']
    # trilho
    s.append(f'<rect x="26" y="58" width="{W-40}" height="20" rx="9" fill="#161b34" '
             f'stroke="#2a3158"/>')
    # marcas de seção
    rotulos = {r: (a, b) for r, a, b in secs}
    for rot, (a, b) in rotulos.items():
        xa, xb = mm(a), mm(b)
        s.append(f'<line x1="{xa}" y1="46" x2="{xa}" y2="90" stroke="#3a4270" '
                 f'stroke-width="1"/>')
        s.append(f'<text x="{(xa+xb)/2}" y="40" text-anchor="middle" font-size="10" '
                 f'fill="#8b93a7">{rot}</text>')
        s.append(f'<line x1="{xa}" y1="88" x2="{xb}" y2="88" stroke="#232a4e" '
                 f'stroke-width="2"/>')
    # números de compasso a cada 12
    for m in range(1, n + 1, 12):
        s.append(f'<text x="{mm(m)}" y="104" text-anchor="middle" font-size="9" '
                 f'fill="#565b75">{m}</text>')
    # aparições do riff
    for r in riffs:
        x = mm(r['m'])
        if r['mao'] == 'D':
            s.append(f'<circle cx="{x+4}" cy="56" r="5" fill="#f5b942" stroke="#0b0d18"/>')
        else:
            s.append(f'<circle cx="{x+4}" cy="80" r="5" fill="#7bd88f" stroke="#0b0d18"/>')
    s.append(f'<text x="26" y="30" font-size="11" fill="#f5b942">● mão direita '
             f'(agudo)</text>')
    s.append(f'<text x="26" y="{H-8}" font-size="11" fill="#7bd88f">● mão esquerda '
             f'(grave — o riff emigra!)  ·  114 compassos → 6:00 a ♩=75</text>')
    s.append('</svg>')
    return ''.join(s)


def build_html(evs, rel, secs, riffs, geral, por_mao, raros, cama, feitos):
    dur = lambda a, b: (sum(4.0 if m not in raros['um_tempo'] else 1.0
                            for m in range(a, b + 1)) * DURACAO_Q)
    S = ['<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>Billie Jean — o mapa musical (versão Retalianist)</title>',
         f'<style>{CSS}</style></head><body><div class="wrap">']

    S.append('<h1>🕺 Billie Jean — o mapa musical</h1>')
    S.append('<div class="sub">Michael Jackson (1982) · versão lírica de piano de '
             '<b>Romain Olivieri — Retalianist</b> (2013) · Prova de Conceito nº 7 · '
             'nota-a-nota do PDF oficial do arranjador</div>')

    # ── a ideia em 1 minuto ──
    S.append('<h2>💡 A ideia em 1 minuto</h2>')
    S.append('<div class="card"><p>O arranjador pegou <b>o groove mais famoso do pop</b> '
             'e o desacelerou à metade: o disco corre a ~115 bpm, aqui são <b>♩=75</b> — '
             'andamento de canção de madrugada. E fez uma mudança de papel genial: '
             '<b>o riff que no disco é do baixo vira matéria-prima de tudo</b> — primeiro '
             'é melodia na mão direita, depois emigra pra mão esquerda, no fim vira '
             'refrão inteiro. Mesmo tom do disco: <span class="ouro">' + TOM + '</span>. '
             f'A peça tem <b>{rel["n_compassos"]} compassos · {geral["n_notas"]} notas</b> '
             f'· extensão <span class="azul">{nm(geral["ext"][0])}–{nm(geral["ext"][1])}'
             '</span> · 6:00 tocada reta.</p></div>')

    # ── a assinatura ──
    S.append('<h2>🎹 A assinatura — o riff</h2>')
    S.append('<div class="card">')
    S.append(f'<p style="font-size:17px;letter-spacing:1px" class="ouro">'
             f'{RIFF_ROTULO}</p>')
    S.append(f'<p>Oito colcheias, <b>{RIFF_NOTAS}</b>. No disco, isso é o baixo; aqui é '
             'a primeira coisa que você ouve — e a semente de onde a melodia inteira '
             'vai nascer. Ouça no <b>a-assinatura.mid</b>: o compasso 1 repetido em '
             'loop, com a cama descendo Fá#m → Mi → Ré → Si.</p>')
    S.append('<div style="display:flex;gap:6px;flex-wrap:wrap;margin:8px 0 4px">')
    for i, p in enumerate(RIFF):
        forte = i in (0, 5)
        S.append(f'<div style="background:{"#f5b942" if forte else "#1d2342"};'
                 f'color:{"#232742" if forte else "#ffd97a"};border:1px solid #34406e;'
                 f'border-radius:8px;padding:8px 13px;font-weight:bold;font-size:15px">'
                 f'{nm(p)}</div>')
    S.append('</div>')
    S.append('<p class="peq">as duas notas destacadas (Fá#4 e Si3) são as âncoras do '
             'ouvido: começa na tônica, passeia, encosta no Si (a sensível invertida) '
             'e volta pro Dó#.</p>')
    S.append('</div>')

    # ── teclado-guia ──
    S.append('<h2>⌨️ O teclado-guia — onde a peça mora</h2>')
    S.append(svg_teclado_html(geral['moradas'], geral['ext']))
    S.append(f'<p class="peq">As três moradas principais: <b>Fá#4 (×186)</b>, '
             f'<b>Dó#4 (×167)</b> e <b>Fá#3 (×134)</b> — tônica e quinta de Fá#m em dois '
             f'andares. A mão direita mora entre {nm(por_mao["D"]["ext"][0])} e '
             f'{nm(por_mao["D"]["ext"][1])}; a esquerda entre '
             f'{nm(por_mao["E"]["ext"][0])} e {nm(por_mao["E"]["ext"][1])}.</p>')

    # ── a rua do riff ──
    S.append(f'<h2>🛣️ A rua da assinatura — as {len(riffs)} aparições do riff</h2>')
    S.append(svg_riff_rua(riffs, secs))
    S.append('<p class="peq">Cada bolinha é uma aparição completa do riff (8 colcheias). '
             'Dourado = mão direita, verde = mão esquerda. A leitura: <b>ele nasce no '
             'agudo (INTRO), emigra pro grave na seção A, volta ao agudo como relâmpago '
             'na seção C, ronca no porão na D — e na seção F explode: 12 vezes seguidas '
             '(c77–91), o coração do refrão do arranjador.</b></p>')

    # ── a cama ──
    S.append('<h2>🛏️ A cama — o carrossel Fá# · Mi · Ré</h2>')
    S.append('<div class="card"><p>Quase toda a harmonia da peça gira num carrossel de '
             'três acordes que você conhece do disco: <b>Fá#m → Mi → Ré</b> (com o Si '
             'fazendo a virada). Na seção F o carrossel roda com as inversões do baixo '
             '— o mesmo movimento do baixo caminhante do original, em câmera lenta.</p>')
    S.append('<table><tr><th>seção</th><th>a cama (acordes da mão esquerda)</th></tr>')
    for rot, a, b in secs:
        cont5, raizes = cama[rot]
        if cont5:
            S.append(f'<tr><td><b>{rot}</b><br><span class="peq">c{a}–{b}</span></td>'
                     f'<td>{", ".join(f"{c} ×{n}" for c, n in cont5)}</td></tr>')
        else:
            S.append(f'<tr><td><b>{rot}</b><br><span class="peq">c{a}–{b}</span></td>'
                     f'<td class="peq">sem acordes longos — a esquerda trabalha em '
                     'notas curtas</td></tr>')
    S.append('</table><p class="peq">"Fá#5" = quinta aberta (sem a terça) — o som '
             '"redondo" que o arranjador prefere no fundo.</p></div>')

    # ── a jornada ──
    S.append('<h2>🗺️ A jornada — seção a seção</h2>')
    for rot, a, b in secs:
        titulo, texto = EDITORIAL[rot]
        ps = [p for e in evs if a <= e['m'] <= b for p in e['pitches']]
        ext_s = f'{nm(min(ps))}–{nm(max(ps))}' if ps else '—'
        top = Counter(nm(p) for p in ps).most_common(3)
        n_riff = len([r for r in riffs if a <= r['m'] <= b])
        tags = [f'c{a}–{b}', f'{dur(a, b):.0f} s',
                f'extensão {ext_s}'] + [f'{t} ×{n}' for t, n in top]
        if n_riff:
            tags.append(f'riff ×{n_riff}')
        S.append(f'<div class="card"><h3>{rot} — {titulo}</h3>')
        S.append('<div>' + ''.join(f'<span class="tag">{t}</span>' for t in tags)
                 + '</div>')
        S.append(f'<p>{texto}</p></div>')

    # ── momentos raros ──
    S.append('<h2>✨ Os momentos raros — o que procurar de ouvido</h2>')
    S.append('<div class="card"><table>'
             '<tr><th>momento</th><th>onde</th><th>o que você ouve</th></tr>')
    S.append(f'<tr><td>o único Fá natural + Mi♯</td><td>c23</td>'
             '<td>a cor "fora" da peça: o arranjador pinta o Fá natural contra o Mi♯ '
             '(sensível) — um instante de clima de filme</td></tr>')
    S.append(f'<tr><td>a família Mi♯</td><td>c12 · c23 · c33 · c50 · c62</td>'
             '<td>a sensível da Fá#m harmônica espalhada pela peça — o "tempero" '
             'clássico do tom menor</td></tr>')
    S.append('<tr><td>o porão</td><td>Sol#1 em c52</td>'
             '<td>a nota mais grave da peça, no fundo da seção D</td></tr>')
    S.append('<tr><td>o teto</td><td>Fá#5 em c105</td>'
             '<td>a nota mais aguda, na despedida — a direita abre o leque no fim</td>'
             '</tr>')
    S.append(f'<tr><td>as fusas em oitonas</td><td>c93–99</td>'
             '<td>pares velozes em duas oitavas — a única "vertigem" da peça, na '
             'ponte</td></tr>')
    S.append(f'<tr><td>os compassos de 1 tempo</td><td>c14 e c39</td>'
             '<td>a música "pisa no freio": um compasso inteiro dura um só tempo — '
             'são as viradas de cenário</td></tr>')
    S.append(f'<tr><td>as respirações</td><td>c14–15 · c39 · c92</td>'
             '<td>as duas mãos param juntas antes da barra — fôlego antes das '
             'grandes viradas</td></tr>')
    S.append('</table></div>')

    # ── as mãos ──
    S.append('<h2>🖐️ O diálogo das mãos</h2>')
    S.append('<div class="card">')
    for mao, rot in (('D', 'a mão direita'), ('E', 'a mão esquerda')):
        pm = por_mao[mao]
        S.append(f'<p><b>{rot.capitalize()}</b> — {pm["n"]} notas, moradias '
                 f'{", ".join(f"{t} ×{n}" for t, n in pm["top"])}.</p>')
    S.append('<p>O diálogo é a dramaturgia da peça: <b>a direita começa cantando o riff; '
             'na seção A o riff desce pro porão da esquerda enquanto a direita vira '
             'voz; na F eles se juntam — o riff no alto, o carrossel embaixo — e a peça '
             'vira, por 15 compassos, a si mesma em câmera dupla.</b></p></div>')

    # ── transparência ──
    S.append('<h2>🎚️ Transparência da fábrica</h2>')
    S.append('<div class="card"><ul>'
             '<li><b>Fonte da verdade:</b> o PDF oficial do arranjador (Finale 2012/'
             'Maestro, 6 p.) — dissecado nota-a-nota por leitura vetorial '
             '(<span class="peq">trabalho/pdf_dissect.py</span>): 1690 notas, '
             '87% dos compassos fechando exato no 4/4, o resto são pausas de respiração '
             'reais e ±meia-colcheia de ambiguidade de gravação.</li>'
             '<li><b>Contraprova:</b> transcrição IA do vídeo do Retalianist — mesmas '
             'notas mais tocadas (Fá#4, Dó#4, Lá3, Mi4), mesmo tom.</li>'
             '<li><b>Validação final:</b> a sonda MIDI (a partitura tocada reta) foi '
             'ouvida e confirmada nota a nota contra o vídeo pelo juiz final '
             '(13/10/2026) ✓.</li>'
             '<li><b>Arquivos desta fábrica:</b> ' + ', '.join(feitos) + ' + este HTML '
             '+ teclado-billie.png + mapa-musical-billie-jean.docx.</li>'
             '</ul></div>')

    # ── guia de montagem ──
    S.append('<h2>🧩 Guia de montagem — a ordem de estudar</h2>')
    S.append('<div class="card"><ol>'
             '<li><b>A assinatura primeiro.</b> Estude o riff sozinho no teclado '
             '(quatro notas!) e com <b>a-assinatura.mid</b> — 4 voltas do compasso 1 '
             'com a cama. Quando a mão "decorar o endereço" (Fá#–Dó#–Mi–Si), o resto '
             'da peça já está meio aprendido.</li>'
             '<li><b>A cama.</b> <b>estudo-esquerda-55.mid</b>: acompanhe o carrossel '
             'Fá#m–Mi–Ré–Si da INTRO com a mão esquerda. É o mesmo desenho do disco — '
             'só devagar.</li>'
             '<li><b>A cantiga.</b> <b>estudo-direita-55.mid</b>: a melodia da seção A '
             'nasce do riff — note que você já sabe "metade" dela.</li>'
             '<li><b>Juntas, devagar.</b> <b>estudo-juntas-55.mid</b> até sentir o '
             'diálogo; depois 65 e 75 (o andamento escrito).</li>'
             '<li><b>As vitrines.</b> Pontos de prova de ouvido: a emigração do riff '
             '(c16), o porão (c52), a campeã (c77–91), as fusas (c93–99) e o teto '
             '(c105).</li></ol></div>')

    S.append('<p class="peq" style="margin-top:40px">PoC 7 · Instituto Cura · '
             'mapa gerado por gera_billie_jean.py a partir da dissecção validada — '
             '13/10/2026.</p>')
    S.append('</div></body></html>')
    (SAIDAS / 'mapa-musical-billie-jean.html').write_text(''.join(S),
                                                          encoding='utf-8')
    return SAIDAS / 'mapa-musical-billie-jean.html'


# ═════════════════════════ 7. CHAT ═════════════════════════

def imprime_chat(evs, rel, secs, riffs, geral, raros, n_d, n_e):
    print('═' * 62)
    print('BILLIE JEAN (versão Retalianist) — MAPA MUSICAL · fábrica executada')
    print('═' * 62)
    print(f"peça: {rel['n_compassos']} compassos · {geral['n_notas']} notas · "
          f"extensão {nm(geral['ext'][0])}–{nm(geral['ext'][1])} · ♩={BPM}")
    print(f"riff: {len(riffs)} aparições — D {Counter(r['mao'] for r in riffs)['D']}× · "
          f"E {Counter(r['mao'] for r in riffs)['E']}×")
    print(f"moradas: {geral['moradas'][:5]}")
    print(f"raros: Mi♯ {raros['mi_sustenido']} · porão {raros['porao']} · "
          f"teto {raros['teto']} · fusas {raros['fusas']}")
    print(f"seções: {' · '.join(f'{r} c{a}–{b}' for r, a, b in secs)}")
    print(f"MIDIs: mão D {n_d} notas · mão E {n_e} notas · 10 arquivos em saidas/")
    print('saídas: mapa-musical-billie-jean.html · teclado-billie.png · '
          '10 MIDIs · (DOCX: gera_billie_jean_docx.py)')
    print('═' * 62)


def main():
    SAIDAS.mkdir(exist_ok=True)
    evs, restos, rel = carrega()
    secs = secoes(rel)
    riffs = acha_riffs(evs)
    geral, por_mao, raros = stats(evs, riffs)
    cama = cama_por_secao(evs, secs)
    assert sanity(evs, rel, secs, riffs, geral)
    feitos, n_d, n_e = build_midis(evs, rel)
    teclado_png(SAIDAS / 'teclado-billie.png', geral['moradas'], geral['ext'], riffs)
    html = build_html(evs, rel, secs, riffs, geral, por_mao, raros, cama, feitos)
    imprime_chat(evs, rel, secs, riffs, geral, raros, n_d, n_e)
    return html


if __name__ == '__main__':
    main()
