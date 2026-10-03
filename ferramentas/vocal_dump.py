#!/usr/bin/env python3
"""Extrai a linha vocal do MIDI com tempos em compassos/segundos."""
import struct, sys
sys.path.insert(0, '.')
from midi_parse import parse_midi, pname

def tempo_map(tempos, division):
    """Retorna função tick -> segundos (tempos por pulso)."""
    if not tempos:
        tempos = [(0, 500000)]
    tempos.sort()
    def tick_to_sec(tick):
        sec = 0.0
        last_tick, last_us = 0, tempos[0][1]
        for t, us in tempos:
            if t >= tick:
                break
            sec += (t - last_tick) * last_us / division / 1e6
            last_tick, last_us = t, us
        sec += (tick - last_tick) * last_us / division / 1e6
        return sec
    return tick_to_sec

path = 'novemberrain.mid'
fmt, division, tracks, tempos = parse_midi(path)
voc = [t for t in tracks if 'Vocal' in t['name']][0]
t2s = tempo_map(tempos, division)

print(f"{'i':>3} {'compasso':>9} {'beat':>6} {'seg':>7} {'dur(beat)':>9}  nota")
for i, (ch, pitch, start, dur, vel) in enumerate(voc['notes']):
    beat = start / division
    bar = beat // 4 + 1
    beat_in_bar = beat % 4 + 1
    dur_b = dur / division
    print(f"{i:>3} {bar:>6.1f}|{beat_in_bar:<3.0f} {beat:>6.2f} {t2s(start):>7.1f} {dur_b:>9.2f}  {pname(pitch)}")
