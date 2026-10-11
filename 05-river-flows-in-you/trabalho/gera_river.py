#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gera_river.py — fábrica PoC 5 · River Flows in You (Yiruma)
Plano pedagógico completo: as duas mãos, do primeiro contato à peça inteira.

Fonte única de verdade: river-flow-in-you.mscz (partitura MuseScore 4.40 subida
pelo usuário), lida pelo parser genérico ferramentas/mscx_parse.py.
Camadas de interpretação (seções, células do rio, dedilhados, fases) vivem AQUI,
sempre checadas contra a fonte no sanity().

Gera em ../saidas/:
  • mapa-pedagogico-river-flows-in-you.html  (o mapa: célula a célula, 2 mãos)
  • estudo-{esquerda,direita,juntas}-{60,70,78}.mid  (os MIDIs de estudo ×9)

Roda de qualquer lugar:  python3 05-river-flows-in-you/trabalho/gera_river.py
"""
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent.parent / 'ferramentas'))
from mscx_parse import load, parse, nome, DUR                       # noqa: E402

MSCZ = AQUI / 'river-flow-in-you.mscz'
SAIDAS = AQUI.parent / 'saidas'
SAIDAS.mkdir(exist_ok=True)

metas, STAVES = parse(load(str(MSCZ)))
S1, S2 = STAVES['1'], STAVES['2']          # clave de Sol (mão direita) · clave de Fá (esquerda)

# ═══════════════════ 1. AS CAMADAS DE INTERPRETAÇÃO ═══════════════════
SECOES = [
    ('A1',   1,  4, 'O convite',
     'o tema no estado puro — 8 colcheias por frase, o rio em duas células (F#m · D) e um E '
     'que segura o compasso inteiro (m2/m4). É por aqui que se entra na peça (Fase 2 do plano).'),
    ('A2',   5, 12, 'O tema tecido',
     'o mesmo tema, agora com o polegar morando no A4: melodia e pedal tecidos. m10: a melodia '
     'sobe ao C#6 com notas de graça. As formas de mão da casa: a onda e a resposta.'),
    ('B',   13, 21, 'O rio na direita',
     'as semicolcheias contínuas passam pra mão direita: a ONDA (A5·A4·E5·A4) e a CASCATA '
     '(A5-B5-C#6-D6-E6 — o teto). A esquerda desce ao F#2/E2: o rio mais fundo. m21: a '
     'respiração — meio compasso de silêncio de propósito.'),
    ('A3',  22, 29, 'O tema de novo',
     'reciclagem: m22 = m5 nota a nota, e o resto segue o molde do A2. Quem fez o A2 faz o A3 '
     'pagando metade do preço.'),
    ('B\u2032', 30, 38, 'O rio mais fundo',
     'a segunda volta do rio, com o baixo ainda mais grave (E2) e a textura mais cheia. '
     'm38: a segunda respiração — o silêncio antes do adeus.'),
    ('CODA', 39, 47, 'O convite que não volta',
     'o tema do começo retorna (m39 = m1 nota a nota)… e a peça termina SUSPENSA: B4 sobre E4, '
     'semibreve inteira no E — o dominante. Ela não fecha: flutua. Deixe o acorde soar.'),
]

RIO_PCS = {'F#m': {6, 1, 9}, 'D': {2, 9, 4}, 'A': {9, 4, 1}, 'E': {4, 11, 8}}
RIO_ROOT = {'F#m': 6, 'D': 2, 'A': 9, 'E': 4}   # pc da fundamental (desempate pelo baixo)

RIO_CELULAS = {   # as 4 células canônicas (registro normal) — o coração do plano
    'F#m': dict(notas=['F#3', 'C#4', 'F#4'], dedos=['3', '2', '1'], acorde='Fá# menor (vi)'),
    'D':  dict(notas=['D3', 'A3', 'E4'],     dedos=['3', '2', '1'], acorde='Ré maior (IV)'),
    'A':  dict(notas=['A2', 'E3', 'C#4'],    dedos=['5', '2', '1'], acorde='Lá maior (I — a casa)'),
    'E':  dict(notas=['E3', 'B3', 'E4'],     dedos=['3', '2', '1'], acorde='Mi maior (V)'),
}
RIO_GRAVES = {    # as variantes fundas das seções B
    'F#m': ['F#2', 'C#3', 'F#3'], 'E': ['E2', 'B2', 'G#3'],
}

PADROES_MD = [    # as formas de mão da mão direita (sugestão — validar na prática)
    ('O TEMA', 'A5 G#5 A5 G#5 A5 E5 A5 D5', '5 · 4 · 5 · 4 · 5 · 2 · 5 · 2',
     'a frase que abre a peça (m1) — quase só a alternância 5-4 com duas escapadas ao 2'),
    ('A ONDA', 'A5 · A4 · E5 · A4  (e volta)', '4 · 1 · 2 · 1',
     'o polegar PREGADO no A4; 4 e 2 tocam a melodia em cima (seções B, m13+)',),
    ('A CASCATA', 'A5 B5 C#6 D6 E6 (e desce)', '1 · 2 · 3 · 4 · 5  (volta 3·2·1)',
     'o polegar no A5 dispara a subida até o teto E6 (m14/16) — cinco notas, cinco dedos'),
    ('O PEDAL', 'A4 (o tempo todo)', '1',
     'o polegar mora no A4 quase a peça inteira — é ele que faz o tecido'),
]

FASES = [
    ('F0', 'O terreno', 'semana 0',
     ['As teclas da peça no mapa do teclado (só elas existem por enquanto)',
      'Os 4 acordes do rio tocados EM BLOCO, mão esquerda',
      'O pulso 4/4 contando alto com a gravação',
      'Escuta ativa: ouvir a peça inteira apontando as 6 seções']),
    ('F1', 'O rio — mão esquerda', 'semanas 1–2',
     ['Cada célula como ritual: bloco → quebrado → loop no metrônomo',
      'O loop F#m–D–A–E contínuo (a harmonia da peça inteira)',
      'SAÍDA: 8 voltas do loop sem olhar as mãos, a 60 bpm']),
    ('F2', 'A melodia — mão direita', 'semanas 2–3',
     ['O tema A1 cantado e tocado (m1–4)',
      'O tema A2 primeiro SEM o pedal (só melodia)',
      'Depois COM o pedal (o polegar entra no A4)',
      'SAÍDA: A1+A2 com metrônomo a 60, sem travar']),
    ('F3', 'O tecido — mãos juntas', 'semanas 4–6',
     ['Lego de 2 compassos por vez: A1 junto, depois A2 junto',
      'B: a onda e a cascata com a esquerda grave, a 50% do andamento',
      'A3 e B\u2032 saem de graça (reciclagem)',
      'SAÍDA: a peça inteira, lenta (60), sem parar']),
    ('F4', 'A montagem e o voo', 'semanas 7–9',
     ['Escada de andamento: 60 → 65 → 70 → 78 (degrau só com 3 execuções limpas)',
      'Dinâmica e fraseado: a cascata cresce, as respirações (m21/m38) silenciam',
      'Recital do sofá: gravação semanal pro pai',
      'SAÍDA: a peça inteira a 78, com o final suspenso bem suspenso']),
]

COSTURAS = [
    ('A1 → A2', 'o rio enche: o mesmo tema volta com o pedal tecido (o polegar acorda).'),
    ('A2 → B', 'as mãos TROCAM DE PAPEL: a direita vira o rio e a esquerda desce ao fundo.'),
    ('B → A3', 'a respiração de m21… e o tema volta tecido (quem sabe A2, sabe).'),
    ('A3 → B\u2032', 'o rio de novo, mais fundo e mais cheio — mesma água, outro leito.'),
    ('B\u2032 → CODA', 'a segunda respiração (m38)… e o convite do começo retorna.'),
    ('O final', 'B4 sobre E4 e DEIXAR SOAR: a peça termina no dominante — não resolve, flutua. '
     'Resistir à tentação de tocar um A final “pra fechar”.'),
]

# ═══════════════════ 2. LEITURAS DERIVADAS (sempre da fonte) ═══════════════════
def dur_q(ev):
    """duração em semínimas (grace = 0; gap = seu valor)"""
    if ev['t'] == 'chord':
        if ev.get('grace'):
            return 0.0
        base = DUR.get(ev['dur'], (None, 0))[1]
        if base is None:
            base = 4.0
        d = ev.get('dots', 0)
        return base * (1.5 if d == 1 else 1.75 if d == 2 else 1)
    if ev['t'] == 'rest':
        base = DUR.get(ev['dur'], (None, 0))[1] or 4.0
        d = ev.get('dots', 0)
        return base * (1.5 if d == 1 else 1.75 if d == 2 else 1)
    if ev['t'] == 'gap':
        return ev['q']
    return 0.0


def dur_letra(ev):
    if ev['t'] == 'gap':
        return '—'
    if ev['t'] == 'rest':
        return DUR.get(ev['dur'], ('?',))[0] + '.' * ev.get('dots', 0) + 'R'
    return DUR.get(ev['dur'], ('?',))[0] + '.' * ev.get('dots', 0)


def notas_mao(staff):
    return [n for m in staff for ev in m['voices'][0]
            if ev['t'] == 'chord' for n in ev['notas']]


def celulas_medida(m):
    """segmenta a clave de Fá em células do rio (por conjuntos de classes de altura)"""
    evs = [e for e in m['voices'][0] if e['t'] == 'chord' and not e.get('grace')]
    segs, cur, cur_pcs = [], [], set()
    for ev in evs:
        pcs = {n['pitch'] % 12 for n in ev['notas']}
        viola = not any((cur_pcs | pcs) <= allowed for allowed in RIO_PCS.values())
        if cur and (len(cur) >= 4 or viola):
            segs.append(cur)
            cur, cur_pcs = [], set()
        cur.append(ev)
        cur_pcs |= pcs
    if cur:
        segs.append(cur)
    rotulos = []
    for seg in segs:
        pcs = {n['pitch'] % 12 for e in seg for n in e['notas']}
        bass = min(n['pitch'] for e in seg for n in e['notas'])
        cands = [r for r, s in RIO_PCS.items() if pcs <= s]
        # desempate: a fundamental da célula aparece como baixo (ex. E4 sozinho no
        # compasso final pertence a E, não a D — pc de E está nos dois conjuntos)
        rotulo = next((r for r in cands if RIO_ROOT[r] == bass % 12), cands[0] if cands else '?')
        if bass < 45:
            rotulo += '\u207b'
        rotulos.append(rotulo)
    return rotulos


RIO_MAPA = {i: celulas_medida(m) for i, m in enumerate(S2, 1)}


# ═══════════════════ 3. TIMELINE → MIDI ═══════════════════
PPQ = 480
GRAça = int(0.125 * PPQ)     # as notas de graça viram "crush" de 1/8 de semínima antes da nota


def timeline(staff):
    """[(tick_on, tick_off, pitch)] — graces esmagadas antes da nota principal"""
    evs, pend = [], []
    t = 0
    for mi, m in enumerate(staff):
        base = mi * 4 * PPQ
        t = base
        for ev in m['voices'][0]:
            if ev['t'] in ('rest', 'gap'):
                t += int(round(dur_q(ev) * PPQ))
                continue
            if ev['t'] != 'chord':
                continue
            if ev.get('grace'):
                pend.extend(n['pitch'] for n in ev['notas'])
                continue
            for i, p in enumerate(pend):          # graces: crush imediatamente antes
                on = t - (len(pend) - i) * GRAça
                evs.append((max(0, on), max(0, on) + GRAça - 5, p))
            pend = []
            d = int(round(dur_q(ev) * PPQ))
            for n in ev['notas']:
                evs.append((t, t + d, n['pitch']))
            t += d
    for i, p in enumerate(pend):                  # sobras no fim (não deve ocorrer)
        evs.append((t + i * GRAça, t + i * GRAça + GRAça - 5, p))
    return evs


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

    tempo = b'\x00\xff\x51\x03' + int(60_000_000 / bpm).to_bytes(3, 'big') + b'\x00\xff\x2f\x00'
    trilhas = [b'MTrk' + len(tempo).to_bytes(4, 'big') + tempo]
    for canal, vel, nome, evs in vozes:
        trilhas.append(trilha(evs, canal, vel, nome))
    head = b'MThd' + (6).to_bytes(4, 'big') + (1).to_bytes(2, 'big') \
        + len(trilhas).to_bytes(2, 'big') + PPQ.to_bytes(2, 'big')
    Path(path).write_bytes(head + b''.join(trilhas))


def build_midis():
    md = timeline(S1)
    me = timeline(S2)
    feitos = []
    for bpm in (60, 70, 78):
        escreve_midi(SAIDAS / f'estudo-esquerda-{bpm}.mid', bpm,
                     [(1, 64, 'Rio (mao esquerda)', me)])
        escreve_midi(SAIDAS / f'estudo-direita-{bpm}.mid', bpm,
                     [(0, 84, 'Melodia (mao direita)', md)])
        escreve_midi(SAIDAS / f'estudo-juntas-{bpm}.mid', bpm,
                     [(0, 84, 'Melodia', md), (1, 64, 'Rio', me)])
        feitos += [f'estudo-esquerda-{bpm}.mid', f'estudo-direita-{bpm}.mid',
                   f'estudo-juntas-{bpm}.mid']
    return feitos, len(md), len(me)


# ═══════════════════ 4. SANITY ═══════════════════
def sanity():
    ok = True
    # 1. 47 compassos por clave, todos somando 4.0
    for sid, staff in (('Sol', S1), ('Fá', S2)):
        somas = [sum(dur_q(ev) for ev in m['voices'][0]) for m in staff]
        if len(staff) != 47 or any(abs(s - 4.0) > 1e-9 for s in somas):
            print(f"  [✗] clave de {sid}: {len(staff)} compassos, somas estranhas"); ok = False
        else:
            print(f"  [✓] clave de {sid}: 47 compassos × 4.0 exatos")
    # 2. extensões
    md, me = notas_mao(S1), notas_mao(S2)
    ext_md = (min(n['pitch'] for n in md), max(n['pitch'] for n in md))
    ext_me = (min(n['pitch'] for n in me), max(n['pitch'] for n in me))
    print(f"  [{'✓' if ext_md == (61, 88) else '✗'}] mão direita C#4–E6 "
          f"(esperado C#4–E6 = MIDI 61..88) — {ext_md}")
    print(f"  [{'✓' if ext_me == (40, 68) else '✗'}] mão esquerda E2–G#4 "
          f"(esperado E2–G#4) — {ext_me}")
    ok &= ext_md == (61, 88) and ext_me == (40, 68)
    # 3. células do rio: nenhuma '?', todas no loop
    rotulos = {r for rs in RIO_MAPA.values() for r in rs}
    limpo = rotulos <= {'F#m', 'D', 'A', 'E', 'F#m\u207b', 'E\u207b'}
    print(f"  [{'✓' if limpo else '✗'}] células inferidas: {sorted(rotulos)} "
          f"(só o loop F#m·D·A·E ± graves)")
    ok &= limpo
    # 4. repetições literais conhecidas
    sig = lambda m: tuple(dur_letra(e) + ''.join(nome(n['pitch'], n['tpc'])
                          for n in e.get('notas', [])) for e in m['voices'][0])
    for a, b in ((1, 3), (1, 39), (2, 4), (5, 9), (5, 22)):
        igual = sig(S1[a-1]) == sig(S1[b-1])
        print(f"  [{'✓' if igual else '✗'}] m{a} = m{b} (literal)")
        ok &= igual
    # 5. o pedal A4 existe mesmo
    n_a4 = sum(1 for n in md if n['pitch'] == 69)
    print(f"  [{'✓' if n_a4 > 50 else '✗'}] o pedal A4 na direita: {n_a4} ocorrências")
    ok &= n_a4 > 50
    # 6. o final suspenso: B4 sobre E4, semibreve
    fim_d = [(e['dur'], [nome(n['pitch'], n['tpc']) for n in e['notas']])
             for e in S1[46]['voices'][0] if e['t'] == 'chord']
    fim_e = [(e['dur'], [nome(n['pitch'], n['tpc']) for n in e['notas']])
             for e in S2[46]['voices'][0] if e['t'] == 'chord']
    ok_fim = fim_d == [('whole', ['B4'])] and fim_e == [('whole', ['E4'])]
    print(f"  [{'✓' if ok_fim else '✗'}] final suspenso: B4/E4 em semibreve — {fim_d} {fim_e}")
    ok &= ok_fim
    return ok


# ═══════════════════ 5. CHAT ═══════════════════
def imprime_chat():
    print('═' * 74)
    print("RIVER FLOWS IN YOU — Yiruma · o mapa pedagógico (PoC 5)")
    print("Lá maior (o tom original) · 4/4 · ♩=78 (ed. oficial: 65) · 47 compassos · 6 seções")
    print("Aluno: iniciante · não lê partitura · objetivo: a versão integral · 30 min/dia")
    print('═' * 74)
    for nom, i0, i1, tit, _ in SECOES:
        print(f"\n◈ {nom} · m{i0}–{i1} · {tit}")
        print(f"   rio: {' | '.join('-'.join(RIO_MAPA[m]) or '(pausa)' for m in range(i0, i1+1))}")
    print("\nO LOOP: F#m → D → A → E (vi–IV–I–V de Lá) — a peça inteira, sem modulação.")
    print("O FINAL: suspenso no E — a peça flutua, não fecha.")


# ═══════════════════ 6. HTML ═══════════════════
CSS = """
body{background:#06181f;color:#dceef2;font-family:Georgia,'Times New Roman',serif;margin:0;padding:26px 14px;}
.wrap{max-width:1060px;margin:0 auto;}
h1{color:#6fe3ff;font-size:29px;margin:6px 0 4px;letter-spacing:.4px;}
.sub{color:#7fa3ad;font-style:italic;margin:0 0 6px;font-size:15px;}
.chips{margin:12px 0 20px;}
.chip{display:inline-block;background:#0b2733;border:1px solid #16414f;color:#9beefc;border-radius:20px;
padding:4px 13px;margin:3px 6px 3px 0;font-size:12.5px;font-family:Verdana,Arial,sans-serif;}
.card{background:#0b2733;border:1px solid #16414f;border-radius:14px;padding:16px 20px;margin:14px 0;}
h2{color:#6fe3ff;font-size:19px;margin:0 0 2px;}
h3{color:#9beefc;font-size:15.5px;margin:16px 0 6px;font-weight:normal;}
.sub2{color:#7fa3ad;font-size:12.5px;font-family:Verdana,Arial,sans-serif;margin:0 0 10px;}
p{line-height:1.55;font-size:14px;}
.med{margin:13px 0 16px;}
.mtag{font-family:Verdana,Arial,sans-serif;font-size:12px;color:#7fa3ad;margin-bottom:4px;}
.mtag b{color:#9beefc;}
.mtag .rio{color:#ffd166;}
.linha{display:flex;flex-wrap:wrap;gap:3px;margin:2px 0;}
.linha .mao{writing-mode:vertical-rl;transform:rotate(180deg);font-size:10px;color:#5b8391;
font-family:Verdana,Arial,sans-serif;text-align:center;margin-right:2px;}
.ev{background:#0e2f3d;border:1px solid #1c4a5a;border-radius:7px;min-width:40px;padding:4px 6px 3px;text-align:center;}
.ev .d{display:block;font-size:9.5px;color:#5b8391;font-family:Verdana,Arial,sans-serif;}
.nota{display:block;font-size:12.5px;font-family:Verdana,Arial,sans-serif;line-height:1.25;}
.nota.mel{color:#9beefc;}
.nota.pedal{color:#4e93a8;}
.nota.esq{color:#ffd166;}
.nota.teto{color:#ff8f8f;font-weight:bold;}
.ev.rest{opacity:.45;}
.ev.gap{opacity:.4;border-style:dashed;}
.ev.grace{border-style:dotted;opacity:.9;}
.ev.grace .d{color:#4e93a8;}
.legenda{color:#7fa3ad;font-size:12px;margin:6px 0 0;font-family:Verdana,Arial,sans-serif;}
.rio-cards{display:flex;flex-wrap:wrap;gap:10px;}
.rio-card{background:#0e2f3d;border:1px solid #1c4a5a;border-radius:11px;padding:10px 14px;min-width:200px;flex:1;}
.rio-card h4{margin:0 0 4px;color:#ffd166;font-size:14px;font-family:Verdana,Arial,sans-serif;}
.rio-card .notas{font-family:Verdana,Arial,sans-serif;font-size:13px;color:#dceef2;}
.rio-card .dedos{font-family:Verdana,Arial,sans-serif;font-size:15px;color:#6fe3ff;letter-spacing:3px;}
.rio-card .acorde{color:#7fa3ad;font-size:11.5px;}
.pcheck{margin:6px 0;}
.pcheck li{margin:5px 0;font-size:13.5px;}
.fase{border-left:3px solid #6fe3ff;}
.fase h4{margin:0;color:#9beefc;font-size:14px;font-family:Verdana,Arial,sans-serif;}
.fase .quando{color:#7fa3ad;font-size:11.5px;font-family:Verdana,Arial,sans-serif;}
.midi{font-family:Verdana,Arial,sans-serif;font-size:12.5px;color:#9beefc;background:#0e2f3d;
border:1px solid #1c4a5a;border-radius:8px;padding:6px 11px;display:inline-block;margin:3px;}
.foot{color:#5b8391;font-size:12px;line-height:1.6;margin-top:24px;border-top:1px solid #16414f;padding-top:13px;}
b.gold{color:#ffd166;} b.cyan{color:#9beefc;}
"""

TECLADO_NOTAS_ESQ = set()   # preenchido no build (dourado)
TECLADO_NOTAS_DIR = set()


def keyboard_svg():
    lo, hi = 40, 88                     # E2..E6
    whites = [p for p in range(lo, hi + 1) if p % 12 in (0, 2, 4, 5, 7, 9, 11)]
    blacks = [p for p in range(lo, hi + 1) if p % 12 in (1, 3, 6, 8, 10)]
    WW, BW, TOP, H = 32, 19, 60, 118
    x_pos, x = {}, 8
    s = [f'<svg viewBox="0 0 {8 + len(whites) * WW + 8} 216" xmlns="http://www.w3.org/2000/svg" '
         f'style="width:100%;max-width:980px;">']
    for p in whites:
        if p in TECLADO_NOTAS_ESQ:
            fill, tcol = '#ffd166', '#3a2c05'
        elif p in TECLADO_NOTAS_DIR:
            fill, tcol = '#6fe3ff', '#06222c'
        else:
            fill, tcol = '#f2f7f8', '#5b8391'
        s.append(f'<rect x="{x}" y="{TOP}" width="{WW-2}" height="{H}" rx="4" fill="{fill}" '
                 f'stroke="#0a2830"/>')
        if p in TECLADO_NOTAS_ESQ or p in TECLADO_NOTAS_DIR:
            nm = nome(p)
            s.append(f'<text x="{x+WW/2-1}" y="{TOP+H-7}" text-anchor="middle" font-size="9.5" '
                     f'font-family="Verdana" fill="{tcol}">{nm}</text>')
        if p == 69:                      # A4 — o ponto de encontro
            cx = x + WW / 2
            s.append(f'<circle cx="{cx}" cy="{TOP+22}" r="8.5" fill="none" stroke="#ffffff" '
                     f'stroke-width="2"/>')
        x_pos[p] = x
        x += WW
    for p in blacks:
        bx = x_pos[p - 1] + WW - BW / 2 - 1
        if p in TECLADO_NOTAS_ESQ:
            fill, tcol = '#d9a935', '#241505'
        elif p in TECLADO_NOTAS_DIR:
            fill, tcol = '#3fb9d8', '#06222c'
        else:
            fill, tcol = '#0d2129', None
        s.append(f'<rect x="{bx}" y="{TOP}" width="{BW}" height="{int(H*0.62)}" rx="3" '
                 f'fill="{fill}" stroke="#04161c"/>')
        if tcol:
            s.append(f'<text x="{bx+BW/2}" y="{TOP+int(H*0.62)-5}" text-anchor="middle" '
                     f'font-size="8.5" font-family="Verdana" fill="{tcol}">{nome(p)}</text>')
        x_pos[p] = bx
    def call(p, txt, ty, cor='#9beefc', anchor='middle'):
        cx = x_pos[p] + (WW / 2 if p in whites else BW / 2)
        tx = cx if anchor == 'middle' else (cx - 6 if anchor == 'end' else cx + 6)
        s.append(f'<line x1="{cx}" y1="{ty+5}" x2="{cx}" y2="{TOP-3}" stroke="{cor}" '
                 f'stroke-width="1" stroke-dasharray="2,2"/>')
        s.append(f'<text x="{tx}" y="{ty}" text-anchor="{anchor}" font-size="10.5" '
                 f'font-family="Verdana" fill="{cor}">{txt}</text>')
    call(81, 'A5: a melodia mora aqui', 14, '#9beefc')
    call(69, 'A4: o polegar mora aqui', 38, '#ffffff')
    call(88, '▲ o teto — E6, a cascata', 38, '#ff8f8f', 'end')
    # E2 — abaixo do teclado (a tecla fica na borda esquerda)
    s.append(f'<line x1="24" y1="{TOP+H+3}" x2="38" y2="192" stroke="#ffd166" '
             f'stroke-width="1" stroke-dasharray="2,2"/>')
    s.append(f'<text x="42" y="200" font-size="10.5" font-family="Verdana" fill="#ffd166">'
             f'▼ E2 — o fundo do rio (a mão esquerda desce aqui nas seções B)</text>')
    s.append('</svg>')
    return ''.join(s)


def _ev_html(ev, mao):
    if ev['t'] == 'gap':
        return '<div class="ev gap"><span class="d">—</span><span class="nota esq">·</span></div>'
    if ev['t'] == 'rest':
        return f'<div class="ev rest"><span class="d">{dur_letra(ev)}</span><span class="nota">rest</span></div>'
    notas = sorted(ev['notas'], key=lambda n: n['pitch'])
    grace = ' grace' if ev.get('grace') else ''
    d = f'<span class="d">~</span>' if ev.get('grace') else f'<span class="d">{dur_letra(ev)}</span>'
    spans = []
    for j, n in enumerate(notas):
        nm = nome(n['pitch'], n['tpc'])
        if mao == 'E':
            cls = 'nota esq'
        elif n['pitch'] == 88:
            cls = 'nota teto'                # E6 — o teto da cascata
        elif n['pitch'] == 69:
            cls = 'nota pedal'               # A4 — o polegar mora aqui
        elif len(notas) > 1 and j == 0:
            cls = 'nota pedal'               # o grave da díade vira o "companheiro" do pedal
        else:
            cls = 'nota mel'
        spans.append(f'<span class="{cls}">{nm}</span>')
    return f'<div class="ev{grace}">{d}{"".join(spans)}</div>'


def _med_html(i):
    m1, m2 = S1[i - 1], S2[i - 1]
    rio = ' · '.join(RIO_MAPA.get(i, [])) or '—'
    return (f'<div class="med"><div class="mtag">m{i} · <span class="rio">rio: {rio}</span></div>'
            f'<div class="linha"><span class="mao">MD</span>'
            + ''.join(_ev_html(e, 'D') for e in m1['voices'][0]) + '</div>'
            f'<div class="linha"><span class="mao">ME</span>'
            + ''.join(_ev_html(e, 'E') for e in m2['voices'][0]) + '</div></div>')


def build_html():
    # teclado: notas usadas por mão
    TECLADO_NOTAS_ESQ.clear()
    TECLADO_NOTAS_ESQ.update(n['pitch'] for n in notas_mao(S2))
    TECLADO_NOTAS_DIR.clear()
    TECLADO_NOTAS_DIR.update(n['pitch'] for n in notas_mao(S1) if n['pitch'] != 69)

    H = ['<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">',
         '<title>River Flows in You — o mapa pedagógico · Yiruma</title>',
         f'<style>{CSS}</style></head><body><div class="wrap">']

    H.append('<h1>🌊 River Flows in You — o mapa pedagógico</h1>')
    H.append('<div class="sub">Yiruma, 2001 · o primeiro mapa da casa feito pra ALUNO — '
             'do primeiro contato à peça inteira, as duas mãos</div>')
    H.append('<div class="chips">'
             '<span class="chip">tom: LÁ MAIOR — o original (tocar junto com o Yiruma funciona)</span>'
             '<span class="chip">4/4 · ♩=78 (a escada: 60→65→70→78)</span>'
             '<span class="chip">47 compassos · 6 seções · 854 notas</span>'
             '<span class="chip">aluno: iniciante · não lê partitura — o mapa é a partitura</span>'
             '<span class="chip">sem oitavas simultâneas ✓ (mão pequena bem-vinda)</span>'
             '<span class="chip">9 MIDIs de estudo inclusos</span></div>')

    # como usar
    H.append('<div class="card"><h2>📖 Como usar este mapa (sem ler uma nota de partitura)</h2>'
             '<div class="sub2">o mapa é a partitura: célula a célula, com nome, nota e dedo</div>'
             '<p>• Cada compasso tem <b class="cyan">duas linhas</b>: <b>MD</b> (mão direita, '
             'clave de Sol) e <b>ME</b> (mão esquerda, clave de Fá — <b class="gold">o rio, em '
             'dourado</b>).<br>'
             '• Cada quadradinho = uma coisa que toca: a(s) <b>nota(s)</b> em cima, a '
             '<b>duração</b> embaixo (<b>e</b>=colcheia · <b>s</b>=semicolcheia · <b>t</b>=fusa · '
             '<b>q</b>=semínima · <b>h</b>=mínima · <b>w</b>=semibreve · <b>~</b>=nota de graça, '
             'rapidinha antes da seguinte · <b>·</b>=pausa).<br>'
             '• O <b>rio</b> de cada compasso está no rótulo: as células <b class="gold">F#m · '
             'D · A · E</b> — quem aprendeu as 4 células sabe a esquerda da peça inteira.<br>'
             '• Os símbolos na partitura viram sons nos <b>MIDIs de estudo</b>: ouvir → tocar '
             'junto → tocar sozinho. É assim que se estuda sem ler.</p></div>')

    # teclado
    H.append('<div class="card"><h2>⌨️ O teclado da peça</h2>'
             '<div class="sub2">a geografia inteira: só estas teclas existem em River Flows in You</div>'
             + keyboard_svg() +
             '<div class="legenda"><b class="gold">dourado</b> = a mão esquerda (as 4 células do '
             'rio) · <b class="cyan">ciano</b> = a mão direita (melodia e pedal) · o <b>círculo '
             'branco no A4</b> = o ponto de encontro: o polegar da direita mora ali quase a '
             'peça inteira.</div></div>')

    # os 4 rituais do rio
    cards = []
    for r, info in RIO_CELULAS.items():
        grave = ' <span style="color:#7fa3ad">(versão funda: ' + '-'.join(RIO_GRAVES[r]) + ')</span>' \
                if r in RIO_GRAVES else ''
        cards.append(
            f'<div class="rio-card"><h4>RIO {r}</h4>'
            f'<div class="notas">{" · ".join(info["notas"])}{grave}</div>'
            f'<div class="dedos">{"·".join(info["dedos"])}</div>'
            f'<div class="acorde">{info["acorde"]}</div></div>')
    H.append('<div class="card"><h2>🛏️ Os 4 rituais do rio — a mão esquerda inteira em 4 formas</h2>'
             '<div class="sub2">bloco → quebrado → loop: cada célula vira um ritual de mão (Fase 1 '
             'do plano). Dedilhado sugerido — porta, não lei: validar com a mão dele na 1ª semana.</div>'
             '<div class="rio-cards">' + ''.join(cards) + '</div>'
             '<p style="margin:10px 0 0">O loop <b class="gold">F#m → D → A → E</b> é a harmonia '
             'da peça INTEIRA (vi–IV–I–V de Lá maior) — sem uma única modulação. Quem automatiza '
             'o loop acompanha a peça toda.</p></div>')

    # formas de mão da direita
    pc = ''.join(f'<div class="rio-card"><h4>{n}</h4><div class="notas">{ns}</div>'
                 f'<div class="dedos">{d}</div><div class="acorde">{obs}</div></div>'
                 for n, ns, d, obs in PADROES_MD)
    H.append('<div class="card"><h2>🖐️ As formas de mão da direita</h2>'
             '<div class="sub2">a peça inteira é feita com estas 4 formas (sugestão de dedilhado '
             '— ajustar à mão)</div><div class="rio-cards">' + pc + '</div></div>')

    # o quebra-cabeça
    H.append('<h3 style="font-size:17px;color:#6fe3ff;margin:24px 0 4px;">🧩 O quebra-cabeça — '
             'a peça inteira em 6 blocos</h3>')
    for nom, i0, i1, tit, desc in SECOES:
        extra = ' <span style="color:#4e93a8">(recicla o A2)</span>' if nom == 'A3' else \
                ' <span style="color:#4e93a8">(recicla o B)</span>' if nom == 'B\u2032' else ''
        H.append(f'<div class="card"><h2>{nom} · m{i0}–{i1} · {tit}{extra}</h2>'
                 f'<div class="sub2">rio: {" · ".join("-".join(RIO_MAPA[m]) for m in range(i0, i1+1))}</div>'
                 f'<p>{desc}</p></div>')

    # compasso a compasso
    H.append('<h3 style="font-size:17px;color:#6fe3ff;margin:24px 0 4px;">🌊 A peça, compasso a '
             'compasso</h3><div class="sub2">MD = mão direita (ciano melodia · azul-petróleo '
             'pedal) · ME = mão esquerda (dourado) · vermelho = o teto E6</div>')
    for nom, i0, i1, tit, desc in SECOES:
        H.append(f'<div class="card"><h2>{nom} — {tit} · m{i0}–{i1}</h2>'
                 f'<div class="sub2">{desc}</div>')
        for i in range(i0, i1 + 1):
            H.append(_med_html(i))
        H.append('</div>')

    # MIDIs
    mids = ''.join(f'<span class="midi">🎵 estudo-{m}-{b}.mid</span>'
                   for b in (60, 70, 78) for m in ('esquerda', 'direita', 'juntas'))
    H.append('<div class="card"><h2>🎧 Os MIDIs de estudo — o professor que toca junto</h2>'
             '<div class="sub2">mesma partitura, 3 andamentos × 3 versões (gerados pela fábrica, '
             'na fonte única)</div>'
             '<p>• <b>esquerda</b>: só o rio — pra tocar a meloria por cima e vice-versa; '
             '• <b>direita</b>: só a melodia; • <b>juntas</b>: a peça inteira.<br>'
             '• Comece no <b>60</b>, suba pra <b>70</b>, chegue ao <b>78</b>. Nas notas de graça '
             'os MIDIs tocam um "crush" rapidinho antes da nota principal (transparência: é uma '
             'escolha de estudo, não ornamentação literária).</p>'
             + mids + '</div>')

    # o plano
    fases = ''.join(
        f'<div class="card fase"><h4>{cod} · {nom} <span class="quando">({quando})</span></h4>'
        f'<ul class="pcheck">' + ''.join(f'<li>{c}</li>' for c in check) + '</ul></div>'
        for cod, nom, quando, check in FASES)
    H.append('<h3 style="font-size:17px;color:#6fe3ff;margin:24px 0 4px;">🗺️ O plano — 5 fases, '
             '~9 semanas, 30 min/dia</h3><div class="sub2">10\u2032 rio (esquerda) · '
             '15\u2032 frase do dia (direita → juntas) · 5\u2032 revisão do que já estava bom</div>'
             + fases)

    # costuras
    H.append('<div class="card"><h2>🧵 As costuras — onde a peça vira</h2><div class="sub2">as '
             '6 dobras que sustentam a montagem</div><ul class="pcheck">'
             + ''.join(f'<li><b>{a}:</b> {b}</li>' for a, b in COSTURAS) + '</ul></div>')

    # footer
    H.append('<div class="foot"><b>Fonte única:</b> river-flow-in-you.mscz (partitura MuseScore '
             '4.40, subida pelo usuário via upload/), parseada por ferramentas/mscx_parse.py — '
             'nenhuma nota foi digitada à mão: as 854 notas do mapa vêm direto da partitura. '
             'Camadas de interpretação (seções, células, dedilhados, fases): sugestões '
             'pedagógicas da casa, a validar na prática.<br>'
             '<b>Referências:</b> Musicnotes MN0073222 (original publicado em Lá maior — o mesmo '
             'tom desta partitura) · metrônomo oficial q=65; a marca ♩=78 é do arquivo subido. '
             '19 notas de graça e 1 gap de 1/16 (m19, clave de Sol) tratados na fábrica.<br>'
             '<b>Regenera:</b> <code>python3 05-river-flows-in-you/trabalho/gera_river.py</code> '
             '— reconfere o sanity, reimprime e regenera o HTML + os 9 MIDIs.</div>')

    H.append('</div></body></html>')
    html = '\n'.join(H)
    (SAIDAS / 'mapa-pedagogico-river-flows-in-you.html').write_text(html, encoding='utf-8')
    return html


# ═══════════════════ main ═══════════════════
if __name__ == '__main__':
    ok = sanity()
    print()
    imprime_chat()
    feitos, n_md, n_me = build_midis()
    print('\n' + '═' * 74)
    print(f'MIDIs de estudo: {len(feitos)} arquivos · MD {n_md} notas · ME {n_me} notas '
          f'(fonte: 556 + 298 = 854 ✓)' if n_md + n_me == 854 else
          f'⚠ MIDI notas: MD {n_md} + ME {n_me} ≠ 854')
    html = build_html()
    for t in ('div', 'span', 'svg', 'text'):
        a, f_ = html.count('<' + t), html.count('</' + t + '>')
        if a != f_:
            print(f'  ⚠ <{t}>: {a} abre vs {f_} fecha'); ok = False
    print(f'HTML: mapa-pedagogico-river-flows-in-you.html · {len(html):,} caracteres · '
          f'{html.count(chr(34) + "ev" + chr(34))} eventos')
    sys.exit(0 if ok else 1)
