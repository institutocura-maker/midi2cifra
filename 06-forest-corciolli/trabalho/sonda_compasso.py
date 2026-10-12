#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sonda_compasso.py — PoC 6 (Forest, Corciolli) · a sonda do fôlego

O arquivo diz 3/4, mas a unidade real da grade é 0,347 s — e o fôlego da música
pode ser o compasso de 3 unidades (~1 s, valsa rápida) ou de 6 (~2 s, 6/8).
Quem decide é o OUVIDO (o usuário toca de ouvido — a casa não discute teoria
com quem escuta melhor). Esta sonda renderiza os compassos 1–48 no tempo real
(173 bpm por unidade) em três versões:

  sonda-0-piano-sozinho.mid  — só o piano (referência)
  sonda-A-compasso-1s.mid    — madeira forte a cada 3 unidades  (compasso ~1 s)
  sonda-B-compasso-2s.mid    — madeira forte a cada 6 unidades  (compasso ~2 s,
                               batida fraca no meio — o balanço 6/8)

Cobertura: m1–48 (~50 s), incluindo as clareiras m30, m37–38 e m44 (na
gravação, solo de pererecas 🐸).

Timeline com as correções que o parser genérico ainda não tem embutidas
(aqui vive o protótipo): pausa de compasso (`durationType="measure"`) =
comprimento nominal (3.0); `<location>` negativa = salto pra trás (funciona
por construção — basta somar).

Roda:  python3 06-forest-corciolli/trabalho/sonda_compasso.py
"""
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent.parent / 'ferramentas'))
from mscx_parse import load, parse, nome, DUR                       # noqa: E402

MSCZ = AQUI / 'UN-Forest.mscz'
SAIDAS = AQUI.parent / 'saidas'
SAIDAS.mkdir(exist_ok=True)

NOM = 3.0        # compasso nominal do arquivo (3/4)
UNIT = 480       # 1 unidade da grade = 1 semínima MIDI (PPQ 480)
BPM = 173        # 60 / 0,3467 s — unidade medida contra a gravação (472 s / 1362 q)
FIM = 48         # compassos da sonda

metas, ST = parse(load(str(MSCZ)))
S1, S2 = ST['1'], ST['2']


def dur_q(ev):
    """duração em unidades de grade (grace=0; pausa de compasso=nominal; gap=valor,
    negativo = salto pra trás)"""
    if ev['t'] == 'chord':
        if ev.get('grace'):
            return 0.0
        base = DUR.get(ev['dur'], (None, 0))[1]
        if base is None:
            base = 4.0
        d = ev.get('dots', 0)
        return base * (1.5 if d == 1 else 1.75 if d == 2 else 1)
    if ev['t'] == 'rest':
        if ev['dur'] == 'measure':
            return NOM
        base = DUR.get(ev['dur'], (None, 0))[1] or 4.0
        d = ev.get('dots', 0)
        return base * (1.5 if d == 1 else 1.75 if d == 2 else 1)
    if ev['t'] == 'gap':
        return ev['q']
    return 0.0


def timeline(staff):
    """[(tick_on, tick_off, pitch)] na grade da sonda"""
    out, t = [], 0.0
    for m in staff:
        acc = t
        for e in m['voices'][0]:
            if e['t'] == 'chord' and not e.get('grace'):
                d = dur_q(e)
                for n in e['notas']:
                    out.append((int(round(acc * UNIT)), int(round((acc + d) * UNIT)),
                                n['pitch']))
            acc += dur_q(e)
        t += sum(dur_q(e) for e in m['voices'][0])
    return out


# ── escrita MIDI (format 1 · PPQ 480 · trilha de tempo + trilhas de notas)
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
    head = (b'MThd' + (6).to_bytes(4, 'big') + (1).to_bytes(2, 'big')
            + len(trilhas).to_bytes(2, 'big') + UNIT.to_bytes(2, 'big'))
    Path(path).write_bytes(head + b''.join(trilhas))


def main():
    fim_ticks = FIM * 3 * UNIT
    brutas = timeline(S1) + timeline(S2)
    notas = [(on, min(off, fim_ticks), p) for on, off, p in brutas if on < fim_ticks]
    notas.sort()

    escreve_midi(SAIDAS / 'sonda-0-piano-sozinho.mid', BPM,
                 [(0, 78, 'Piano', notas)])

    # A: compasso de 3 unidades — forte no início de cada compasso, fraco nos outros
    metroA = []
    for u in range(FIM * 3):
        on = u * UNIT
        if u % 3 == 0:
            metroA.append((on, on + UNIT // 2, 76))    # madeira alta
        else:
            metroA.append((on, on + UNIT // 3, 77))    # madeira baixa
    escreve_midi(SAIDAS / 'sonda-A-compasso-1s.mid', BPM,
                 [(0, 78, 'Piano', notas), (9, 104, 'Compasso', metroA)])

    # B: compasso de 6 unidades — forte a cada 6 (alinhado ao ostinato do m2),
    #    fraca no meio: o balanço "forte-fraco" do 6/8
    metroB = []
    for u in range(FIM * 3):
        on = u * UNIT
        if u % 6 == 3:
            metroB.append((on, on + UNIT // 2, 76))
        elif u % 6 == 0:
            metroB.append((on, on + UNIT // 3, 77))
    escreve_midi(SAIDAS / 'sonda-B-compasso-2s.mid', BPM,
                 [(0, 78, 'Piano', notas), (9, 104, 'Compasso', metroB)])

    dur_s = FIM * 3 * 0.34668
    print('═' * 74)
    print(f'SONDA DO FÔLEGO · Forest (Corciolli) · m1–{FIM} · ♩={BPM}/unidade · '
          f'{dur_s:.0f} s de música')
    print(f'  sonda-0-piano-sozinho.mid · {len(notas)} notas (referência, sem marcação)')
    print(f'  sonda-A-compasso-1s.mid · madeira forte a cada ~1 s  (compasso = 3 unidades)')
    print(f'  sonda-B-compasso-2s.mid · madeira forte a cada ~2 s  (compasso = 6 unidades)')
    print(f'  clareiras incluídas: m30, m37–38, m44 (silêncio de propósito — na gravação,')
    print(f'  é onde as pererecas cantam sozinhas)')


if __name__ == '__main__':
    main()
