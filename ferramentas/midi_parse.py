#!/usr/bin/env python3
"""Parser MIDI minimalista - extrai notas por pista."""
import struct, sys

def read_varlen(f):
    d = f.read(1)[0]
    value = d & 0x7F
    while d & 0x80:
        d = f.read(1)[0]
        value = (value << 7) | (d & 0x7F)
    return value

def parse_midi(path):
    with open(path, 'rb') as f:
        data = f.read()
    pos = 0
    # Header
    assert data[pos:pos+4] == b'MThd', "não é MIDI"
    hlen = struct.unpack('>I', data[pos+4:pos+8])[0]
    fmt, ntrk, division = struct.unpack('>HHH', data[pos+8:pos+14])
    pos += 8 + hlen
    tracks = []
    tempos = []  # (tick, us_per_quarter)
    for t in range(ntrk):
        assert data[pos:pos+4] == b'MTrk', f"pista {t}: sem MTrk"
        tlen = struct.unpack('>I', data[pos+4:pos+8])[0]
        pos += 8
        end = pos + tlen
        tick = 0
        running = None
        notes_open = {}  # (ch, pitch) -> list of start ticks
        notes = []
        name = ''
        instruments = set()
        while pos < end:
            delta = read_varlen_stream(data, pos)
            p = delta[1]
            delta = delta[0]
            pos = p
            tick += delta
            b = data[pos]
            if b == 0xFF:  # meta
                mtype = data[pos+1]
                mlen = read_varlen_stream(data, pos+2)
                pos = mlen[1]
                mdata = data[pos:pos+mlen[0]]
                pos += mlen[0]
                if mtype == 0x03:
                    name = mdata.decode('latin-1', 'replace')
                elif mtype == 0x51 and len(mdata) == 3:
                    us = (mdata[0]<<16)|(mdata[1]<<8)|mdata[2]
                    tempos.append((tick, us))
                elif mtype == 0x2F:
                    break
            elif b in (0xF0, 0xF7):  # sysex
                slen = read_varlen_stream(data, pos+1)
                pos = slen[1] + slen[0]
            else:
                if b & 0x80:
                    status = b; pos += 1
                    running = status
                else:
                    status = running
                typ = status & 0xF0
                ch = status & 0x0F
                if typ in (0x80, 0x90, 0xA0, 0xB0, 0xE0):
                    d1, d2 = data[pos], data[pos+1]; pos += 2
                    if typ == 0x90 and d2 > 0:
                        notes_open.setdefault((ch, d1), []).append((tick, d2))
                    elif typ in (0x80,) or (typ == 0x90 and d2 == 0):
                        key = (ch, d1)
                        if key in notes_open:
                            st = notes_open[key].pop()
                            notes.append((ch, d1, st[0], tick - st[0], st[1]))
                elif typ in (0xC0, 0xD0):
                    d1 = data[pos]; pos += 1
                    if typ == 0xC0:
                        instruments.add(d1)
        # fecha notas pendentes
        for (ch, pitch), lst in notes_open.items():
            for st in lst:
                notes.append((ch, pitch, st[0], end - st[0], st[1]))
        tracks.append({'name': name, 'channel': ch if notes else None,
                       'notes': sorted(notes, key=lambda n: n[2]),
                       'instruments': instruments})
        pos = end
    return fmt, division, tracks, tempos

def read_varlen_stream(data, pos):
    d = data[pos]; pos += 1
    value = d & 0x7F
    while d & 0x80:
        d = data[pos]; pos += 1
        value = (value << 7) | (d & 0x7F)
    return value, pos

NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def pname(p):
    return f"{NAMES[p%12]}{p//12 - 1}"

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'novemberrain.mid'
    fmt, division, tracks, tempos = parse_midi(path)
    print(f"formato={fmt} pistas={len(tracks)} divisão={division} (ticks por semínima)")
    if tempos:
        print("tempos (bpm):", sorted(set(round(60_000_000/us) for _, us in tempos))[:10])
    for i, t in enumerate(tracks):
        chs = sorted(set(n[0] for n in t['notes']))
        rng = (pname(min(n[1] for n in t['notes'])), pname(max(n[1] for n in t['notes']))) if t['notes'] else ('-','-')
        inst = sorted(t['instruments'])
        print(f"[{i}] '{t['name']}' notas={len(t['notes'])} canais={chs} extenso={rng} inst={inst}")
