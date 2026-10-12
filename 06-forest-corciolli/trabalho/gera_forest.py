#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gera_forest.py — fábrica PoC 6 · Forest (Corciolli) · O MODO ANDARILHO

A peça NÃO é um bloco de verso-e-refrão: é uma máquina de recombinar —
campos de pedal (MORADAS) + caminhadas melódicas (TRAVESSIAS) + silêncios
(CLAREIRAS). A gravação é UMA caminhada por esse bornal (A ROTA ORIGINAL);
o Modo Andarilho entrega o bornal aberto: as cartas, a gramática que o
Corciolli usou, e caminhos sorteados.

Fonte única: UN-Forest.mscz (curadoria do usuário: +1 semitom pro piano da
casa, meio tom abaixo do padrão; re-ataques de ouvido; MuseScore 4.70).
Métrica: veredito da sonda B — cada medida 3/4 do arquivo = 1 TEMPO
(♪≈173 por sub-divisão, tempo ≈ 1,04 s); barra sentida = 2 tempos.

Gera em ../saidas/:
  modo-andarilho-forest.html        o mapa (cartas + rota + gramática)
  rota-original.mid                 a peça inteira no tempo real (referência)
  play-along-com-a-gravacao.mid     + 48,3 s de pererecas na frente 🐸
  morada-{NOTA}.mid                 loops de prática das moradas principais
  gestos-todos.mid                  as famílias de gestos, na ordem do mapa
  caminho-do-andarilho-{1,2,3}.mid  passeios sorteados pela gramática

Roda:  python3 06-forest-corciolli/trabalho/gera_forest.py
"""
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent.parent / 'ferramentas'))
from mscx_parse import load, parse, nome, DUR                       # noqa: E402

MSCZ = AQUI / 'UN-Forest.mscz'
SAIDAS = AQUI.parent / 'saidas'
SAIDAS.mkdir(exist_ok=True)

metas, STAVES = parse(load(str(MSCZ)))
S1, S2 = STAVES['1'], STAVES['2']          # as duas claves (a divisão NÃO é mão)
NP = len(S1)                               # 455 pulsos (1 medida do arquivo = 1 tempo)

# ── constantes do tempo real ─────────────────────────────────────────────
NOM = 3.0          # pulsos em unidades do arquivo (3/4)
UNIT = 480         # ticks MIDI por unidade do arquivo
BPM = 173          # unidade real = 0,3467 s (472 s de piano / 1362 unidades)
PULSO_TICKS = int(NOM * UNIT)              # 1440 ticks = 1,04 s
INTRO_TICKS = 46378                        # 48,3 s — o solo de pererecas (medido no MIDI da IA)
SEG_PULSO = 3 * 60.0 / BPM                 # 1,0405 s

NOMES_MORADA = {
    'B4':  ('A Casa',      'o pedal-mor: a peça abre e fecha aqui — morada de retorno'),
    'G#4': ('A Encosta',   'um degrau acima da casa, o campo mais lírico depois do Si'),
    'F#4': ('O Portão',    'a dominante: tensão suave que pede volta pra casa'),
    'C#4': ('O Vale',      'região baixa e quente, quase segredo'),
    'B3':  ('O Porão',     'a casa uma oitava abaixo — a sombra da tônica'),
    'C#5': ('A Torrinha',  'o vale visto de cima'),
    'E5':  ('A Copa',      'região alta, onde entra luz'),
    'F#5': ('O Ninho',     'a dominante no alto — quase o teto da peça'),
    'D#4': ('A Trave',     'a terça da casa: passagem e cor'),
    'E4':  ('A Ponte',     'a submediante: o caminho do meio'),
    'B2':  ('O Chão',      'o piso da mata: a tônica no grave, raiz de tudo'),
    'B5':  ('O Mirante',   'a casa vista do alto: a tônica uma oitava acima, eco do teto'),
    'E3':  ('A Raiz',      'ponte no grave, quando o chão sobe um degrau'),
    'F#3': ('O Porto',     'o portão uma oitava abaixo'),
}


def dur_q(ev):
    if ev['t'] == 'chord':
        if ev.get('grace'):
            return 0.0
        base = DUR.get(ev['dur'], (None, 0))[1]
        if base is None:
            base = 4.0
        d = ev.get('dots', 0)
        return base * (1.5 if d == 1 else 1.75 if d == 2 else 1)
    if ev['t'] == 'rest':
        if ev.get('nominal'):
            return NOM                       # pausa de compasso inteiro
        base = DUR.get(ev['dur'], (None, 0))[1] or 4.0
        d = ev.get('dots', 0)
        return base * (1.5 if d == 1 else 1.75 if d == 2 else 1)
    if ev['t'] == 'gap':
        return ev['q']                       # negativa = salto pra trás
    return 0.0


# ── 1. conteúdo por pulso (eventos ordenados por posição real) ──────────
def eventos_do_pulso(p):
    """[(offset_em_unidades, dur_em_unidades, pitch)] do pulso p, as duas claves."""
    evs = []
    for staff in (S1, S2):
        acc = 0.0
        for e in staff[p - 1]['voices'][0]:
            if e['t'] == 'chord' and not e.get('grace'):
                d = dur_q(e)
                for n in e['notas']:
                    evs.append((acc, d, n['pitch']))
            acc += dur_q(e)
    evs.sort(key=lambda x: (x[0], x[2]))
    return evs


PULSOS = [eventos_do_pulso(p) for p in range(1, NP + 1)]
SETS = [frozenset(ev[2] for ev in evs) for evs in PULSOS]


# ── 2. segmentação: MORADAS · TRAVESSIAS · CLAREIRAS ────────────────────
def run_de(p, pitch):
    """quantos pulsos consecutivos a partir de p têm `pitch` presente"""
    k = p
    while k <= NP and pitch in SETS[k - 1]:
        k += 1
    return k - p


SOLO_COUNT = Counter()
for i in range(NP):
    if len(PULSOS[i]) == 1:
        SOLO_COUNT[PULSOS[i][0][2]] += 1

EPISODIOS = []          # {'tipo','ancora','ini','fim','pulsos'}
p = 1
while p <= NP:
    if not SETS[p - 1]:
        EPISODIOS.append({'tipo': 'clareira', 'ancora': None, 'ini': p, 'fim': p,
                          'pulsos': 1})
        p += 1
        continue
    melhor, tam, melhor_chave = None, 0, None
    for pitch in sorted(SETS[p - 1]):
        L = run_de(p, pitch)
        chave = (L, SOLO_COUNT.get(pitch, 0), -abs(pitch - 60))
        if melhor_chave is None or chave > melhor_chave:
            melhor, tam, melhor_chave = pitch, L, chave
    if tam >= 3:
        EPISODIOS.append({'tipo': 'morada', 'ancora': melhor, 'ini': p,
                          'fim': p + tam - 1, 'pulsos': tam})
        p += tam
    else:
        ini = p
        while p <= NP and SETS[p - 1] and not any(
                run_de(p, pi) >= 3 for pi in SETS[p - 1]):
            p += 1
        EPISODIOS.append({'tipo': 'travessia', 'ancora': None, 'ini': ini,
                          'fim': p - 1, 'pulsos': p - ini})

for i, ep in enumerate(EPISODIOS):
    ep['id'] = i + 1


# ── 3. gestos: famílias por conjunto de notas; ordem fica nas realizações ─
FAMILIAS = defaultdict(Counter)      # chave: tuple(sorted(pitches)) -> realizations
for pi in range(NP):
    evs = PULSOS[pi]
    if len(evs) < 2:
        continue
    chave = tuple(sorted(ev[2] for ev in evs))
    realiz = tuple((round(ev[0], 3), round(ev[1], 3), ev[2]) for ev in evs)
    FAMILIAS[chave][realiz] += 1
FAM_ORD = sorted(FAMILIAS.items(), key=lambda kv: -sum(kv[1].values()))


# ── 4. gramática (transições entre episódios, como o Corciolli andou) ────
def no_do(ep):
    if ep['tipo'] == 'morada':
        return nome(ep['ancora'])
    return {'travessia': 'TRAV', 'clareira': 'CLAR'}[ep['tipo']]


GRAMATICA = defaultdict(Counter)
for a, b in zip(EPISODIOS, EPISODIOS[1:]):
    GRAMATICA[no_do(a)][no_do(b)] += 1

MOR_PULSOS = Counter()
for ep in EPISODIOS:
    if ep['tipo'] == 'morada':
        MOR_PULSOS[ep['ancora']] += ep['pulsos']
MOR_TOP = [m for m, _ in MOR_PULSOS.most_common(8)]


# ── 5. timeline global (grade travada por pulso) → MIDI ─────────────────
def timeline():
    """[(on, off, pitch)] em ticks, com colisões de mesma altura aparadas"""
    evs = []
    for p in range(1, NP + 1):
        base = (p - 1) * PULSO_TICKS
        for off, d, pitch in PULSOS[p - 1]:
            on = base + int(round(off * UNIT))
            evs.append([on, on + max(int(round(d * UNIT)), 60), pitch])
    evs.sort(key=lambda x: (x[0], x[2]))
    out = []
    for ev in evs:
        if out and out[-1][2] == ev[2] and out[-1][1] > ev[0]:
            if out[-1][0] == ev[0]:          # uníssono exato: fica a mais longa
                out[-1][1] = max(out[-1][1], ev[1])
                continue
            out[-1][1] = ev[0]               # apara a nota anterior
        out.append(ev)
    return [tuple(e) for e in out]


TL = timeline()


def _vlq(n):
    b = [n & 0x7F]
    n >>= 7
    while n:
        b.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(b))


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

    tempo = b'\x00\xff\x51\x03' + int(60_000_000 / bpm).to_bytes(3, 'big') + b'\x00\xff\x2f\x00'
    trilhas = [b'MTrk' + len(tempo).to_bytes(4, 'big') + tempo]
    for canal, vel, nome_, evs in vozes:
        trilhas.append(trilha(evs, canal, vel, nome_))
    head = (b'MThd' + (6).to_bytes(4, 'big') + (1).to_bytes(2, 'big')
            + len(trilhas).to_bytes(2, 'big') + UNIT.to_bytes(2, 'big'))
    Path(path).write_bytes(head + b''.join(trilhas))


def trecho(ini, fim):
    """eventos do TL cujo onset cai nos pulsos [ini..fim], relativos ao início"""
    a, b = (ini - 1) * PULSO_TICKS, fim * PULSO_TICKS
    return [(on - a, off - a, pi) for on, off, pi in TL if a <= on < b]


def costura(segmentos, pulso_gap=1):
    """emenda episódios com um pulso de mata entre eles; devolve eventos+tamanho"""
    evs, cursor = [], 0
    for seg in segmentos:
        for on, off, pi in seg:
            evs.append((cursor + on, cursor + off, pi))
        cursor += (max(off for _, off, _ in seg) if seg else 0) + pulso_gap * PULSO_TICKS
    return evs, cursor


def build_midis():
    feitos = []
    escreve_midi(SAIDAS / 'rota-original.mid', BPM,
                 [(0, 78, 'Forest (rota original)', TL)])
    feitos.append('rota-original.mid')

    escreve_midi(SAIDAS / 'play-along-com-a-gravacao.mid', BPM,
                 [(0, 78, 'Forest (play-along)',
                   [(on + INTRO_TICKS, off + INTRO_TICKS, pi) for on, off, pi in TL])])
    feitos.append('play-along-com-a-gravacao.mid')

    # moradas: o episódio mais longo da âncora, repetido até ~24 s
    for m in MOR_TOP:
        eps = [e for e in EPISODIOS if e['tipo'] == 'morada' and e['ancora'] == m]
        ep = max(eps, key=lambda e: e['pulsos'])
        seg = trecho(ep['ini'], ep['fim'])
        reps = max(2, int(round(24 / (ep['pulsos'] * SEG_PULSO))))
        evs, _ = costura([seg] * reps, pulso_gap=1)
        arq = f'morada-{nome(m)}.mid'
        escreve_midi(SAIDAS / arq, BPM, [(0, 78, f'Morada {nome(m)}', evs)])
        feitos.append(arq)

    # gestos: as 28 famílias mais comuns, na ordem do mapa
    gestos = []
    cursor = 0
    for chave, _cnt in FAM_ORD[:28]:
        realiz = _cnt.most_common(1)[0][0]
        for off, d, pi in realiz:
            on = cursor + int(round(off * UNIT))
            gestos.append((on, on + max(int(round(d * UNIT)), 60), pi))
        cursor += int(round((max(r[0] + r[1] for r in realiz) + 1) * UNIT))
    escreve_midi(SAIDAS / 'gestos-todos.mid', BPM,
                 [(0, 80, 'Gestos (ordem do mapa)', gestos)])
    feitos.append('gestos-todos.mid')

    # caminhos do andarilho: passeios pela gramática (semente fixa = regenerável)
    eps_por_no = defaultdict(list)
    for ep in EPISODIOS:
        eps_por_no[no_do(ep)].append(ep)
    for k, (alvo, seed) in enumerate(((100, 42), (130, 43), (160, 44)), 1):
        rng = random.Random(seed)
        atual = rng.choice([e for e in EPISODIOS
                            if e['tipo'] == 'morada' and e['ancora'] == MOR_TOP[0]])
        caminho, usados, total = [atual], {atual['id']}, atual['pulsos']
        alvo_pulsos = alvo / SEG_PULSO
        while total < alvo_pulsos:
            opcoes = [n for n in GRAMATICA[no_do(atual)] if eps_por_no.get(n)]
            if not opcoes:
                opcoes = [no_do(e) for e in EPISODIOS if e['tipo'] == 'morada'][:3]
            no = rng.choice(opcoes)
            cand = [e for e in eps_por_no[no] if e['id'] not in usados] or eps_por_no[no]
            atual = rng.choice(cand)
            caminho.append(atual)
            usados.add(atual['id'])
            total += atual['pulsos'] + 1
        if eps_por_no.get('CLAR'):
            caminho.append(max(eps_por_no['CLAR'], key=lambda e: e['pulsos']))
        finais = [e for e in eps_por_no.get(nome(MOR_TOP[0]), [])
                  if e['pulsos'] <= 6] or eps_por_no[nome(MOR_TOP[0])]
        caminho.append(min(finais, key=lambda e: e['pulsos']))
        evs, tam = costura([trecho(e['ini'], e['fim']) for e in caminho])
        arq = f'caminho-do-andarilho-{k}.mid'
        escreve_midi(SAIDAS / arq, BPM, [(0, 78, f'Caminho do andarilho {k}', evs)])
        feitos.append(arq)
        print(f"  caminho-{k}: {len(caminho)} episódios · {tam / UNIT * SEG_PULSO / 3:.0f} s")
    return feitos


# ── 6. sanity ────────────────────────────────────────────────────────────
def sanity():
    ok = True
    b = lambda x: '✓' if x else '✗'
    print(f"  [{b(len(S1) == len(S2) == 455)}] 455 pulsos × 2 claves")
    ok &= len(S1) == len(S2) == 455
    todo = [pi for evs in PULSOS for pi in (ev[2] for ev in evs)]
    print(f"  [{b(min(todo) == 40 and max(todo) == 88)}] extensão E2–E6 "
          f"({nome(min(todo))}–{nome(max(todo))})")
    ok &= (min(todo), max(todo)) == (40, 88)
    fora = {p % 12 for p in todo} - {11, 1, 3, 4, 6, 8, 10}
    print(f"  [{b(not fora)}] tudo dentro de Si maior (pcs fora: {fora or 'nenhum'})")
    ok &= not fora
    solo = [SETS[i] for i in range(NP) if len(PULSOS[i]) == 1]
    b4 = sum(1 for s in solo if list(s)[0] == 71)
    print(f"  [{b(len(solo) == 106 and b4 == 34)}] pulsos de nota única: {len(solo)} "
          f"(B4 sozinho: {b4})")
    ok &= len(solo) == 106 and b4 == 34
    cob = sum(e['pulsos'] for e in EPISODIOS)
    tipos = Counter(e['tipo'] for e in EPISODIOS)
    print(f"  [{b(cob == 455)}] episódios cobrem os 455 pulsos: "
          f"{dict(tipos)} (total {len(EPISODIOS)})")
    ok &= cob == 455
    print(f"  [{b(len(TL) >= 1090)}] timeline: {len(TL)} notas (fonte 1098; "
          f"fim {TL[-1][1] / UNIT / 3 * SEG_PULSO:.0f} s)")
    ok &= len(TL) >= 1090
    return ok


# ── 7. chat ──────────────────────────────────────────────────────────────
def imprime_chat():
    print('═' * 74)
    print('FOREST (Corciolli) — O MODO ANDARILHO')
    print('Si maior (o tom do piano da casa) · pulso ~1 s (♪=173) · barra sentida ~2 s')
    print(f'{NP} pulsos = 7:52 de piano · 48 s + 40 s de pererecas na gravação')
    print('═' * 74)
    print('\nMORADAS (por total de pulsos):')
    for m, v in MOR_PULSOS.most_common(10):
        nm = NOMES_MORADA.get(nome(m), (nome(m), ''))[0]
        eps = sum(1 for e in EPISODIOS if e['tipo'] == 'morada' and e['ancora'] == m)
        print(f"  {nome(m):4} {nm:12} {v:3} pulsos em {eps} episódios")
    tr = Counter(e['pulsos'] for e in EPISODIOS if e['tipo'] == 'travessia')
    print(f"\nTRAVESSIAS: {tipos_get('travessia')} · CLAREIRAS: {tipos_get('clareira')}")
    print('\nGESTOS (top 10 famílias):')
    for chave, cnt in FAM_ORD[:10]:
        print(f"  {'·'.join(nome(p) for p in chave):28} ×{sum(cnt.values())}")
    print('\nGRAMÁTICA (para onde o Corciolli foi):')
    for no_, destinos in sorted(GRAMATICA.items(), key=lambda kv: -sum(kv[1].values()))[:8]:
        print(f"  {no_:5} → " + ', '.join(f'{d}×{v}' for d, v in destinos.most_common(6)))


def tipos_get(t):
    return sum(1 for e in EPISODIOS if e['tipo'] == t)


# ── 8. HTML ──────────────────────────────────────────────────────────────
CSS = """
body{background:#07160d;color:#d9ecd9;font-family:Georgia,'Times New Roman',serif;margin:0;padding:26px 14px;}
.wrap{max-width:1060px;margin:0 auto;}
h1{color:#9fe388;font-size:28px;margin:6px 0 4px;}
.sub{color:#7fa887;font-style:italic;margin:0 0 6px;font-size:15px;}
.chips{margin:12px 0 20px;}
.chip{display:inline-block;background:#0d2416;border:1px solid #1d4626;color:#cfe8c8;border-radius:20px;
padding:4px 13px;margin:3px 6px 3px 0;font-size:12.5px;font-family:Verdana,Arial,sans-serif;}
.card{background:#0d2416;border:1px solid #1d4626;border-radius:14px;padding:16px 20px;margin:14px 0;}
h2{color:#9fe388;font-size:19px;margin:0 0 2px;}
h3{color:#cfe8c8;font-size:15.5px;margin:16px 0 6px;font-weight:normal;}
.sub2{color:#7fa887;font-size:12.5px;font-family:Verdana,Arial,sans-serif;margin:0 0 10px;}
p,li{line-height:1.55;font-size:14px;}
b.gold{color:#ffd166;} b.leaf{color:#8fe388;} b.mist{color:#a8cfe0;}
.mor-cards{display:flex;flex-wrap:wrap;gap:10px;}
.mor-card{background:#112b19;border:1px solid #2a5a35;border-radius:11px;padding:10px 14px;min-width:215px;flex:1;}
.mor-card h4{margin:0 0 4px;color:#ffd166;font-size:14px;font-family:Verdana,Arial,sans-serif;}
.mor-card .nm{font-family:Verdana,Arial,sans-serif;font-size:13px;color:#d9ecd9;}
.mor-card .meta{color:#7fa887;font-size:11.5px;font-family:Verdana,Arial,sans-serif;}
.mor-card .animo{color:#cfe8c8;font-size:12px;font-style:italic;margin-top:4px;}
table{border-collapse:collapse;width:100%;font-family:Verdana,Arial,sans-serif;font-size:12px;}
th,td{border:1px solid #1d4626;padding:4px 7px;text-align:left;}
th{color:#9fe388;font-weight:normal;background:#112b19;}
td.n{color:#7fa887;}
td.mor{color:#ffd166;} td.trav{color:#8fe388;} td.clar{color:#a8cfe0;}
.rota-strip{display:flex;height:34px;border-radius:8px;overflow:hidden;border:1px solid #1d4626;}
.rota-strip div{min-width:3px;}
.midi{font-family:Verdana,Arial,sans-serif;font-size:12.5px;color:#cfe8c8;background:#112b19;
border:1px solid #1d4626;border-radius:8px;padding:6px 11px;display:inline-block;margin:3px;}
.foot{color:#6f9279;font-size:12px;line-height:1.6;margin-top:24px;border-top:1px solid #1d4626;padding-top:13px;}
.regras li{margin:7px 0;}
"""

CORES_MOR = {}  # âncora → cor (tons de dourado/âmbar variando)


def keyboard_svg():
    moradas = {m for m in MOR_PULSOS}
    gestos_pcs = {pi for chave, _ in FAM_ORD[:40] for pi in chave}
    baixo = {ev[2] for evs in PULSOS for ev in evs if ev[2] < 48}
    lo, hi = 40, 88
    whites = [p for p in range(lo, hi + 1) if p % 12 in (0, 2, 4, 5, 7, 9, 11)]
    blacks = [p for p in range(lo, hi + 1) if p % 12 in (1, 3, 6, 8, 10)]
    WW, BW, TOP, H = 32, 19, 60, 118
    x_pos, x = {}, 8
    s = [f'<svg viewBox="0 0 {8 + len(whites) * WW + 8} 216" xmlns="http://www.w3.org/2000/svg" '
         f'style="width:100%;max-width:980px;">']
    for p in whites:
        if p in moradas:
            fill, tcol = '#ffd166', '#3a2c05'
        elif p in gestos_pcs:
            fill, tcol = '#4e7d55', '#d9ecd9'
        else:
            fill, tcol = '#f2f7f2', '#5b8365'
        s.append(f'<rect x="{x}" y="{TOP}" width="{WW-2}" height="{H}" rx="4" fill="{fill}" '
                 f'stroke="#0a1f10"/>')
        if p in moradas or p in gestos_pcs:
            s.append(f'<text x="{x+WW/2-1}" y="{TOP+H-7}" text-anchor="middle" font-size="9.5" '
                     f'font-family="Verdana" fill="{tcol}">{nome(p)}</text>')
        if p == 71:                      # B4 — A CASA
            cx = x + WW / 2
            s.append(f'<circle cx="{cx}" cy="{TOP+22}" r="8.5" fill="none" stroke="#ffffff" '
                     f'stroke-width="2"/>')
        x_pos[p] = x
        x += WW
    for p in blacks:
        bx = x_pos[p - 1] + WW - BW / 2 - 1
        if p in moradas:
            fill, tcol = '#d9a935', '#241505'
        elif p in gestos_pcs:
            fill, tcol = '#35593c', '#cfe8c8'
        else:
            fill, tcol = '#101c12', None
        s.append(f'<rect x="{bx}" y="{TOP}" width="{BW}" height="{int(H*0.62)}" rx="3" '
                 f'fill="{fill}" stroke="#04160a"/>')
        if tcol:
            s.append(f'<text x="{bx+BW/2}" y="{TOP+int(H*0.62)-5}" text-anchor="middle" '
                     f'font-size="8.5" font-family="Verdana" fill="{tcol}">{nome(p)}</text>')
        x_pos[p] = bx
    def call(p, txt, ty, cor='#9fe388', anchor='middle'):
        cx = x_pos[p] + (WW / 2 if p in whites else BW / 2)
        tx = cx if anchor == 'middle' else (cx - 6 if anchor == 'end' else cx + 6)
        s.append(f'<line x1="{cx}" y1="{ty+5}" x2="{cx}" y2="{TOP-3}" stroke="{cor}" '
                 f'stroke-width="1" stroke-dasharray="2,2"/>')
        s.append(f'<text x="{tx}" y="{ty}" text-anchor="{anchor}" font-size="10.5" '
                 f'font-family="Verdana" fill="{cor}">{txt}</text>')
    call(71, 'B4 — A CASA: o pedal-mor', 38, '#ffffff')
    call(88, '▲ E6: o teto (raro, é gala)', 38, '#ffd166', 'end')
    s.append(f'<line x1="{x_pos[47]+BW/2}" y1="{TOP+H+3}" x2="{x_pos[47]+BW/2+14}" y2="192" '
             f'stroke="#8a6d2f" stroke-width="1" stroke-dasharray="2,2"/>')
    s.append(f'<text x="{x_pos[47]+BW/2+20}" y="200" font-size="10.5" font-family="Verdana" '
             f'fill="#a08a4a">▼ B2: o chão (a mão grave anda por aqui e mais abaixo)</text>')
    s.append('</svg>')
    return ''.join(s)


def rota_strip():
    segs = []
    paleta = {'travessia': '#2e5c38', 'clareira': '#a8cfe0'}
    for ep in EPISODIOS:
        if ep['tipo'] == 'morada':
            cor = CORES_MOR.setdefault(ep['ancora'],
                                       f'hsl({43 + (len(CORES_MOR)*23) % 25}, 70%, '
                                       f'{58 - (len(CORES_MOR)*7) % 22}%)')
        else:
            cor = paleta[ep['tipo']]
        det = (f"#{ep['id']} · {'p'+str(ep['ini'])+'–'+str(ep['fim'])} · "
               f"{ep['pulsos']} pulsos (~{ep['pulsos']*SEG_PULSO:.0f}s) · "
               + (nome(ep['ancora']) if ep['ancora'] else
                  {'travessia': 'travessia', 'clareira': 'clareira'}[ep['tipo']]) + '"')
        segs.append(f'<div style="flex:{ep["pulsos"]} 1 0;background:{cor};" title="{det}"></div>')
    return ('<div class="rota-strip">' + ''.join(segs) + '</div>')


def build_html():
    for i, (m, _) in enumerate(MOR_PULSOS.most_common(8)):
        CORES_MOR[m] = f'hsl({43 + i*24}, 72%, {60 - i*5}%)'

    H = ['<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">',
         '<title>Forest — O Modo Andarilho · Corciolli</title>',
         f'<style>{CSS}</style></head><body><div class="wrap">']
    H.append('<h1>🌲 Forest — O Modo Andarilho</h1>')
    H.append('<div class="sub">Corciolli, 2001 (Floresta, do álbum A Tranquilidade dos Sons '
             'da Natureza) · o mapa pra TOCAR SEM PARAR: a peça como bornal de cartas, não '
             'como linha reta</div>')
    H.append('<div class="chips">'
             '<span class="chip">Si maior — o tom do SEU piano (meio tom acima da gravação)</span>'
             '<span class="chip">pulso ~1 s · barra sentida ~2 s (veredito da sonda B)</span>'
             '<span class="chip">455 pulsos = 7:52 + 88 s de pererecas na gravação</span>'
             '<span class="chip">33% da peça é repetição literal — nasceu pra recombinar</span>'
             '<span class="chip">sem partitura publicada — a fonte é a transcrição da casa</span></div>')

    # o jogo
    H.append('<div class="card"><h2>🎲 Como se joga o Modo Andarilho</h2>'
             '<div class="sub2">dois dados, uma lei, e a mata por conta das pererecas</div>'
             '<ol class="regras">'
             '<li><b class="gold">Escolha uma MORADA</b> (carta dourada) e deixe o pedal soar '
             '— re-atacado a cada pulso, como na gravação.</li>'
             '<li>Sobre ela, solte <b class="leaf">GESTOS</b> — as figuras verdes. Os da '
             '<b>gramática</b> dessa morada são os seguros (o Corciolli usou-os ali).</li>'
             '<li>Quando quiser, <b>atravesse</b>: caminhe pela escala de Si maior em notas '
             'miúdas — é assim que as travessias da peça andam.</li>'
             '<li>Chegue na próxima morada — pela gramática (modo seguro) ou livre '
             '(<b>a única lei é o pedal</b>).</li>'
             '<li>Respire nas <b class="mist">CLAREIRAS</b>: um ou dois tempos de mata '
             'sozinha. Não encha — o silêncio é escrito.</li>'
             '<li>Pra fechar: volte pra <b class="gold">Casa (Si)</b> e deixe soar.</li>'
             '</ol>'
             '<p><b>Os três modos de tocar:</b> ① <b>A Rota</b> — como gravado (fidelidade, '
             'com MIDI de referência); ② <b>A Gramática do Corciolli</b> — recombine andando '
             'só onde ele andou; ③ <b>O Andarilho livre</b> — dados na mesa, qualquer carta, '
             'a lei do pedal. <i>Deturpar? Não: a peça é 33% repetição e o pedal de Si volta '
             '23 vezes — ela NASCEU recombinada. A rota original fica aqui, intacta, pra '
             'sempre.</i></p></div>')

    # teclado
    H.append('<div class="card"><h2>⌨️ O teclado da mata</h2>'
             '<div class="sub2">dourado = as moradas (B4 com círculo: A CASA) · verde = as '
             'notas dos gestos · o resto é estrada</div>' + keyboard_svg() + '</div>')

    # moradas
    cards = []
    for m, v in MOR_PULSOS.most_common(10):
        nm, animo = NOMES_MORADA.get(nome(m), (nome(m), 'morada rara — visita rápida'))
        eps = [e for e in EPISODIOS if e['tipo'] == 'morada' and e['ancora'] == m]
        maior = max(e['pulsos'] for e in eps)
        cards.append(f'<div class="mor-card"><h4>{nm} · {nome(m)}</h4>'
                     f'<div class="nm">pedal de {nome(m)}</div>'
                     f'<div class="meta">{v} pulsos · {len(eps)} episódios · '
                     f'morada mais longa: {maior} pulsos (~{maior*SEG_PULSO:.0f}s)</div>'
                     f'<div class="animo">{animo}</div></div>')
    H.append('<div class="card"><h2>🏠 As moradas — onde se mora</h2>'
             '<div class="sub2">um campo de pedal é uma morada: a nota mora, re-atacada, '
             'enquanto os gestos passam</div><div class="mor-cards">' + ''.join(cards)
             + '</div></div>')

    # gestos
    linhas = []
    for i, (chave, cnt) in enumerate(FAM_ORD[:28], 1):
        tot = sum(cnt.values())
        linhas.append(f'<tr><td class="n">{i}</td>'
                      f'<td class="trav">{" · ".join(nome(p) for p in chave)}</td>'
                      f'<td class="n">×{tot}</td>'
                      f'<td class="n">{" ".join(f"{r[2]}" for r in cnt.most_common(1)[0][0])}'
                      f' — dur {" ".join(str(r[1]) for r in cnt.most_common(1)[0][0])}</td></tr>')
    H.append('<div class="card"><h2>🍃 Os gestos — o que se fala</h2>'
             '<div class="sub2">as 28 famílias mais usadas (contorno do pulso, na ordem em '
             'que tocam no gestos-todos.mid) · centenas de variantes únicas existem: elas são '
             'o seu espaço de improviso, não erro</div>'
             '<table><tr><th>#</th><th>contorno</th><th>vezes</th><th>realização mais comum (nota · duração em tempos)</th></tr>'
             + ''.join(linhas) + '</table></div>')

    # rota
    H.append('<div class="card"><h2>🥾 A rota original — a caminhada que foi gravada</h2>'
             '<div class="sub2">a fidelidade mora aqui: cada faixa é um episódio (largura ∝ '
             'pulsos; dourado=morada, verde=travessia, azul=clareira; passe o mouse)</div>'
             + rota_strip())
    linhas = []
    for ep in EPISODIOS:
        if ep['tipo'] == 'morada':
            cls, det = 'mor', f"morada — {NOMES_MORADA.get(nome(ep['ancora']), (nome(ep['ancora']),))[0]} ({nome(ep['ancora'])})"
        elif ep['tipo'] == 'travessia':
            cls, det = 'trav', 'travessia'
        else:
            cls, det = 'clar', 'clareira (a mata canta sozinha)'
        linhas.append(f'<tr><td class="n">{ep["id"]}</td><td class="{cls}">{det}</td>'
                      f'<td class="n">p{ep["ini"]}–{ep["fim"]}</td>'
                      f'<td class="n">{ep["pulsos"]} (~{ep["pulsos"]*SEG_PULSO:.0f}s)</td></tr>')
    H.append('<table><tr><th>#</th><th>episódio</th><th>pulsos</th><th>duração</th></tr>'
             + ''.join(linhas) + '</table></div>')

    # gramática
    linhas = []
    for m, _ in MOR_PULSOS.most_common(8):
        nm = NOMES_MORADA.get(nome(m), (nome(m), ''))[0]
        dest = GRAMATICA.get(nome(m))
        if dest:
            linhas.append(f'<tr><td class="mor">{nm} ({nome(m)})</td><td>'
                          + ', '.join(f'{d} ×{v}' for d, v in dest.most_common(8))
                          + '</td></tr>')
    H.append('<div class="card"><h2>🧭 A gramática do Corciolli</h2>'
             '<div class="sub2">depois de cada morada, para onde ele foi (o modo seguro do '
             'andarilho: ande só onde ele andou)</div>'
             '<table><tr><th>morada</th><th>destinos seguintes (TRAV = travessia, CLAR = '
             'clareira)</th></tr>' + ''.join(linhas) + '</table></div>')

    # midis
    mids = ''.join(f'<span class="midi">🎵 {f}</span>' for f in sorted(SAIDAS.glob('*.mid')))
    H.append('<div class="card"><h2>🎧 Os MIDIs</h2>'
             '<div class="sub2">todos no tempo real (♪=173 por sub-divisão) · os caminhos '
             'foram sorteados pela gramática com semente fixa — regeneráveis</div>'
             '<p>• <b>morada-*.mid</b> — loops de prática (a morada mais longa, repetida '
             '~24 s) · • <b>gestos-todos.mid</b> — as 28 famílias na ordem da tabela acima '
             '(ouça acompanhando) · • <b>caminho-do-andarilho-1/2/3.mid</b> — passeios '
             'exemplo pela gramática · • <b>rota-original.mid</b> — a peça como gravada · '
             '• <b>play-along-com-a-gravacao.mid</b> — com 48,3 s de pererecas na frente: '
             'aperte junto com o vídeo e fique preso nele 🐸</p>' + mids + '</div>')

    # rodapé
    H.append('<div class="foot"><b>Fonte única:</b> UN-Forest.mscz — transcrição de IA '
             '(piano isolado da gravação) <b>curada pelo usuário</b>: +1 semitom porque o '
             'piano da casa está meio tom abaixo (a gravação real soa em Si♭; este mapa em '
             'Si soa certo NO SEU piano — num piano afinado, toque 1 semitom abaixo), '
             're-ataques das notas sustentadas de ouvido, quantização na grade. Métrica '
             'ratificada pelo ouvido do usuário (sonda B: pulso ~1 s, barra ~2 s). '
             'Anomalias da fonte (5 saltos pra trás, 1 compasso superlotado, pausas de '
             'compasso) tratadas com grade travada por pulso. <b>Forest não tem partitura '
             'publicada</b> — até onde sabemos, esta é a primeira notação da peça. '
             'O Modo Andarilho é licença DECLARADA: a rota original acima preserva a '
             'fidelidade; o resto é a mata aberta.<br>'
             '<b>Regenera:</b> <code>python3 06-forest-corciolli/trabalho/gera_forest.py</code></div>')
    H.append('</div></body></html>')
    html = '\n'.join(H)
    (SAIDAS / 'modo-andarilho-forest.html').write_text(html, encoding='utf-8')
    return html


# ── main ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    ok = sanity()
    print()
    imprime_chat()
    feitos = build_midis()
    html = build_html()
    print('\n' + '═' * 74)
    print(f'{len(feitos)} MIDIs · HTML modo-andarilho-forest.html · {len(html):,} caracteres')
    for t in ('div', 'span', 'svg', 'text', 'table', 'tr'):
        a, f_ = html.count('<' + t), html.count('</' + t + '>')
        if a != f_:
            print(f'  ⚠ <{t}>: {a} abre vs {f_} fecha'); ok = False
    sys.exit(0 if ok else 1)
