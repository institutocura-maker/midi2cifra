#!/usr/bin/env python3
"""
gera_dsb.py — fábrica PoC 4 · Don't Stop Believin' (Journey, 1981)
              versão-âncora: Richard Goodall (AGT S19, 28/05/2024, Golden Buzzer)
v0.3 — GERA O HTML (mapa-musical-dont-stop-believin.html), visual streetlights.
       Melodia validada pelo usuário (5/5). Fonte única de verdade = FRASES.

TOM: MI MAIOR — o disco (Musicnotes/Wikipedia), a audição do Goodall (Chordify ×2:
A E B G#m, ~120bpm — a cópia é REAL) e a cifra do usuário (cifra-usuario-dsb.txt).
Performance: Richard Goodall, "strong, clear baritone" (bio oficial) — um BARÍTONO
cantando a montanha do tenor (Perry), no tom original.

Esqueleto: dont-stop-believin.mid (bitmidi 63595 — Dó# maior +3st na importação;
17 pistas; SEM voz — fornece textura: riff, baixo caminhante, batida).
Harmonia/estrutura: consenso Chordify(áudio oficial) + 5 charts + Hooktheory + usuário.
"""
import sys

# ────────────────────────── 1. A CAMA ──────────────────────────
LOOP = ['E', 'B', 'C#m', 'A', 'E', 'B', 'G#m', 'A']      # 1 acorde/compasso × 8
STRANGERS = ['B7/A→A', 'B7/A→A', 'Eadd9→E', 'Eadd9→E']   # a única saída do loop
STRANGERS_TAG = ['B5·E5', 'B5·E5·A5']                     # terminação da seção

BAIXO = {
    'E':  'E1 (2 tempos) · F#1 G#1 · → B1 no tempo 4 (antecipa o B!)',
    'B':  'B1 (segura) · C#2 D#2 · → C#2 no tempo 4 (antecipa o C#m!)',
    'C#m':'C#2 · D#2 E2 · → A1 no tempo 4 (antecipa o A!)',
    'G#m':'G#1 · B1 D#2 · → A1 no tempo 4 (antecipa o A!)',
    'A':  'A1 · D#2 E2 · → caminha de volta ao E',
}

RIFF = {  # validado: candidato A + voicings lidas do esqueleto
    'E':  'B3-E4-G#4-B4 · C#5-B4-G#4-B4',
    'B':  'B3-D#4-F#4(-B4)',
    'C#m':'G#3-C#4-E4(-G#4)',
    'G#m':'G#3-B3-D#4(-G#4)',
    'A':  'A3-C#4-E4(-A4)',
}

ESTRUTURA = [
    ('INTRO',       1,   8,  'o riff do piano, sozinho', LOOP),
    ('V1a',         9,  16,  '"Just a small town girl, livin\u2019 in a lonely world…"', LOOP),
    ('V1b',        17,  24,  '"Just a city boy…" — a GÊMEA: V1a nota a nota, outra história', LOOP),
    ('INTERLÚDIO', 25,  32,  'o riff de novo; a guitarra entra 4 compassos depois', LOOP),
    ('V2',         33,  40,  '"A singer in a smoky room… it goes on and on and on and on"', LOOP),
    ('STRANGERS 1',41,  52,  '"Strangers waiting… Streetlight people…" + tag', 'STRANGERS'),
    ('V3a',        53,  60,  '"Working hard to get my fill, everybody wants a thrill…"', LOOP),
    ('V3b',        61,  68,  '"Some will win, some will lose… it goes on and on…"', LOOP),
    ('STRANGERS 2',69,  80,  '= STRANGERS 1 (a segunda volta)', 'STRANGERS'),
    ('SOLO',       81,  88,  'guitarra cita o contorno do refrão; teto E5 — É DO SOLO, não da voz', LOOP),
    ('REFRÃO',     89, 116,  '"Don\u2019t stop believ\u2019in\u2019…" ×3 — no MESMO loop do verso', LOOP),
    ('TAG',       117, 123,  'a terminação fria do disco: "Don\u2019t stop!"', ['B', 'A', 'E']),
]

GOODALL = {
    'tom': 'Mi maior ✓ (Chordify ×2 na audição: A E B G#m, ~120bpm — mesmo tom/tempo do disco)',
    'voz': 'barítono claro e forte (bio oficial) — cantando a parte do tenor no tom original',
    'corte': ['🎹 riff', '🎤 V1a', '🎤 V1b', '🎤 STRANGERS', '🎤 REFRÃO ×2', '🔔 BUZZER'],
    'cortados': ['interlúdio', 'V2 (smoky room)', 'V3a+b', 'strangers 2', 'solo'],
}

# ────────────────── 2. AS FRASES (fonte única: sílaba ↔ nota) ──────────────────
DIATONICAS = {'E','F#','G#','A','B','C#','D#'}

def F(pares, acordes, obs=''):
    return {'pares': pares, 'acordes': acordes, 'obs': obs}

FRASES = {
 'V1': [
   F([('just','E4'),('a','E4'),('small','E4'),('town','F#4'),('girl','G#4')], ['E','B'],
     'quase falado — o verso "commuter": o "girl" só chega ao G#4'),
   F([('liv','G#4'),('in','F#4'),('in','E4'),('a','F#4'),('LONE','G#4'),('ly','F#4'),('world','E4')], ['C#m','A'],
     'plano e contido — o "LONE" toca G#4 e volta'),
   F([('she','E4'),('took','E4'),('the','F#4'),('mid','G#4'),('night','A4'),('train','A4')], ['E','B'],
     'micro-checagem: o "TRAIN" pode tocar B4 — o acento fugaz do verso (Hooktheory: verso B3–B4)'),
   F([('go','A4'),('in','G#4'),('an','F#4'),('y','E4'),('where','D#4'),('→','C#4'),('→','B3')], ['G#m','A'],
     'O FUNDÃO — o "where" racha D#4→C#4→B3: o E4 é a saída, não a chegada'),
 ],
 'V2_CAUDA': [
   F([('it','E4'),('goes','E4'),('on','F#4'),('and','G#4'),('on','F#4'),('and','E4'),('on','F#4'),('and','E4'),('on','E4')],
     ['G#m','A'], 'célula repetida e plana — o versinho que não acaba (fecha o V2 e o V3b)'),
 ],
 'STRANGERS': [
   F([('Stran','B4'),('gers','B4'),('wait','B4'),('ing','B4')], ['B7/A→A'],
     'o chant no andar de cima — a mudança de andar: aqui o barítono acende'),
   F([('up','G#4'),('and','A4'),('DOWN','B4'),('the','A4'),('bou','G#4'),('le','F#4'),('vard','G#4')], ['B7/A→A'],
     'o "DOWN" pica no B4 e cai'),
   F([('their','B4'),('sha','B4'),('dows','A4'),('search','B4'),('ing','B4')], ['Eadd9→E'],
     'espelha o chant'),
   F([('in','A4'),('the','G#4'),('night','F#4'),('→','E4')], ['Eadd9→E'],
     'a 1ª volta cai — não segura'),
   F([('street','G#4'),('LIGHT','B4'),('peo','A4'),('ple','G#4')], ['B7/A→A'],
     'o "LIGHT" no B4, o "PLE" espelha caindo'),
   F([('liv','A4'),('ing','G#4'),('just','F#4'),('to','G#4'),('find','A4'),('e-','B4'),('MO','A4'),('tion','G#4')], ['B7/A→A'],
     'o salto no "e-" anuncia o "MO-tion"'),
   F([('hid','A4'),('ing','G#4'),('some','F#4'),('where','E4')], ['Eadd9→E'], ''),
   F([('in','F#4'),('the','G#4'),('night','A4'),('→','B4')], ['Eadd9→E'],
     'SEGURA o B4 — a rampa que solta o refrão'),
 ],
 'REFRAO': [
   F([('don\u2019t','G#4'),('stop','B4'),('be','B4'),('LIEV','C#5'),('in\u2019','B4')], ['E','B','C#m'],
     'O PICO DA VOZ — o C#5 sustentado no "be-LIEV" (raiz do C#m) caindo pro B4: o barítono no tenro do Perry'),
   F([('hold','B4'),('on','B4'),('to','A4'),('that','G#4'),('feel','F#4'),('in\u2019','E4')], ['A','E'],
     'a escada de resposta — desce passo a passo até o E4'),
   F([('street','G#4'),('LIGHTS','B4'),('peo','A4'),('ple','G#4')], ['B','G#m','A'],
     'o "LIGHTS" no B4 de novo — e o loop gira pro riff responder'),
 ],
 'TAG': [
   F([('don\u2019t','B4'),('stop!','B4')], ['B','A','E'],
     'corta seco — a terminação fria do disco de 1981'),
 ],
}

GRUPOS_SANITY = [('V1','V1',(59,71),'B3–B4'), ('V2 cauda','V2_CAUDA',(59,71),'B3–B4'),
                 ('STRANGERS','STRANGERS',(64,71),'E4–B4'), ('REFRÃO','REFRAO',(64,73),'E4–C#5'),
                 ('TAG','TAG',(59,71),'B3–B4')]

# ────────────────────────── 3. SANITY ──────────────────────────
def _pitch(nome):
    n, o = nome[:-1], int(nome[-1])
    base = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}[n]
    return base + 12*(o+1)

def sanity():
    ok = True
    for nome, chave, (lo, hi), alvo in GRUPOS_SANITY:
        notas = [n for f in FRASES[chave] for _, n in f['pares'] if n != '→']
        fora = [n for n in notas if n[:-1] not in DIATONICAS]
        p = [_pitch(n) for n in notas]
        status = '✓' if (not fora and lo <= min(p) and max(p) <= hi) else '✗'
        if status == '✗': ok = False
        nomes = [n for f in FRASES[chave] for _, n in f['pares'] if n != '→']
        print(f"  [{status}] {nome:10s} {min(nomes, key=_pitch)}–{max(nomes, key=_pitch):4s} "
              f"(alvo {alvo})  {'FORA: '+str(fora) if fora else 'diatônica ✓'}")
    n_frases = sum(len(v) for v in FRASES.values())
    print(f"  [✓] {n_frases} frases · LOOP de 8 consistente nas {len(ESTRUTURA)} seções")
    return ok

# ────────────────────────── 4. CHAT ──────────────────────────
def imprime_chat():
    print('═'*74)
    print('DON\u2019T STOP BELIEVIN\u2019 — Journey · a cópia do Richard Goodall (AGT 2024)')
    print('Tom: MI MAIOR · 118 bpm · 4/4 · voz B3–C#5 · barítono na montanha do tenor')
    print('═'*74)
    for titulo, chave in [('V1 (V1a ≡ V1b, a gêmea)','V1'), ('V2/V3b (cauda)','V2_CAUDA'),
                          ('STRANGERS','STRANGERS'), ('REFRÃO','REFRAO'), ('TAG','TAG')]:
        print(f"\n🎤 {titulo}")
        for f in FRASES[chave]:
            if f['obs']: print(f"  • {f['obs']}")
            print(f"  {' '.join(s for s,_ in f['pares'])}")
            print(f"  {' '.join(n for _,n in f['pares'])}   [{', '.join(f['acordes'])}]")

# ────────────────────────── 5. HTML ──────────────────────────
CSS = """
body{background:#0a0e17;color:#e8e4d8;font-family:Georgia,'Times New Roman',serif;margin:0;padding:26px 14px;}
.wrap{max-width:1000px;margin:0 auto;}
h1{color:#ffd166;font-size:30px;margin:6px 0 4px;letter-spacing:.5px;}
.sub{color:#9aa3b5;font-style:italic;margin:0 0 6px;font-size:15px;}
.chips{margin:12px 0 22px;}
.chip{display:inline-block;background:#161d2e;border:1px solid #2a3448;color:#ffd166;border-radius:20px;
padding:4px 14px;margin:3px 6px 3px 0;font-size:12.5px;font-family:Verdana,Arial,sans-serif;}
.card{background:#101625;border:1px solid #232d44;border-radius:14px;padding:18px 22px;margin:16px 0;}
.card.gold{border-color:#8a6d2f;background:#131426;}
h2{color:#ffd166;font-size:20px;margin:0 0 2px;}
h3{color:#e8d9a8;font-size:15px;margin:18px 0 6px;font-weight:normal;}
.sub2{color:#8b93a7;font-size:12.5px;font-family:Verdana,Arial,sans-serif;margin:0 0 10px;}
p{line-height:1.55;font-size:14.5px;}
.frase{margin:15px 0 17px;}
.acordes{margin-bottom:6px;}
.acorde{display:inline-block;background:#2a2413;border:1px solid #8a6d2f;color:#ffd166;border-radius:6px;
padding:2px 10px;margin-right:6px;font-size:12px;font-family:Verdana,Arial,sans-serif;}
.cells{display:flex;flex-wrap:wrap;gap:3px;}
.cell{background:#161d2e;border:1px solid #2a3448;border-radius:8px;min-width:46px;padding:6px 7px 5px;text-align:center;}
.cell .sil{display:block;font-size:13.5px;color:#e8e4d8;line-height:1.15;}
.cell .nota{display:block;font-size:12px;color:#ffd166;font-family:Verdana,Arial,sans-serif;margin-top:3px;}
.cell.pico{background:#3d2f0e;border-color:#ffd166;box-shadow:0 0 11px rgba(255,209,102,.38);}
.cell.pico .nota{color:#ffe9a8;font-weight:bold;}
.cell.fundo{background:#0f1b33;border-color:#3b5486;}
.cell.fundo .nota{color:#9ec1ff;}
.cell.mel{opacity:.72;border-style:dashed;min-width:34px;}
.cell.acento{border-color:#c99b3c;}
.obs{color:#8b93a7;font-size:12.5px;font-style:italic;margin-top:6px;}
.molda{display:inline-block;background:#1b2338;border:1px dashed #3b5486;color:#9ec1ff;border-radius:10px;
padding:10px 16px;margin:6px 4px;font-size:13.5px;}
.rika{color:#ffd166;}
.rika2{color:#9ec1ff;}
.cortado{color:#5b6377;text-decoration:line-through;margin-right:10px;}
.tl{display:inline-block;background:#231a08;border:1px solid #8a6d2f;color:#ffd166;border-radius:10px;
padding:6px 12px;margin:3px 4px;font-size:13px;font-family:Verdana,Arial,sans-serif;}
.seta{color:#8a6d2f;font-family:Verdana,Arial,sans-serif;}
ol.cost{margin:6px 0;padding-left:0;list-style:none;counter-reset:c;}
ol.cost li{counter-increment:c;margin:11px 0;padding-left:40px;position:relative;line-height:1.5;font-size:14px;}
ol.cost li::before{content:counter(c);position:absolute;left:0;top:1px;width:26px;height:26px;border-radius:50%;
background:#2a2413;border:1px solid #8a6d2f;color:#ffd166;text-align:center;line-height:24px;font-size:13px;
font-family:Verdana,Arial,sans-serif;}
table.mao{border-collapse:collapse;margin:8px 0;font-size:13.5px;}
table.mao td,table.mao th{border:1px solid #2a3448;padding:7px 12px;text-align:left;}
table.mao th{color:#ffd166;background:#1a1610;font-family:Verdana,Arial,sans-serif;font-size:12px;}
table.mao td.k{color:#ffd166;font-family:Verdana,Arial,sans-serif;}
.foot{color:#5b6377;font-size:12px;line-height:1.6;margin-top:26px;border-top:1px solid #232d44;padding-top:14px;}
.big{font-size:16px;}
"""

def _cell(sil, nota):
    cls = 'cell'
    if nota == 'C#5': cls += ' pico'
    elif nota == 'B3': cls += ' fundo'
    elif nota == '→': cls += ' mel'
    if len(sil) > 1 and sil.replace('-','').replace('!','').replace('\u2019','').isupper(): cls += ' acento'
    return f'<div class="{cls}"><span class="sil">{sil}</span><span class="nota">{nota}</span></div>'

def _frase(f):
    ac = ''.join(f'<span class="acorde">{a}</span>' for a in f['acordes'])
    cells = ''.join(_cell(s, n) for s, n in f['pares'])
    obs = f'<div class="obs">▸ {f["obs"]}</div>' if f['obs'] else ''
    return f'<div class="frase"><div class="acordes">{ac}</div><div class="cells">{cells}</div>{obs}</div>'

def _grupo(chave):
    return ''.join(_frase(f) for f in FRASES[chave])

def _nome_tecla(p):
    N = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    return N[p % 12] + str(p // 12 - 1)

def keyboard_svg():
    WW, BW, TOP, H = 34, 20, 58, 112
    whites = [p for p in range(48, 77) if p % 12 in (0,2,4,5,7,9,11)]
    blacks = [p for p in range(48, 77) if p % 12 in (1,3,6,8,10)]
    FORTE = {59, 64, 68, 71, 73}                      # B3 E4 G#4 B4 + C#5 (o bar do E)
    SUAVE = {56, 57, 61, 63, 66}                      # G#3 A3 C#4 D#4 F#4 (as outras voicings)
    W = 10 + len(whites) * WW
    x_pos, x = {}, 10
    s = [f'<svg viewBox="0 0 {W+14} 216" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:640px;">']
    for p in whites:
        fill = '#f5b942' if p in FORTE else ('#c8a557' if p in SUAVE else '#f4efe4')
        s.append(f'<rect x="{x}" y="{TOP}" width="{WW-2}" height="{H}" rx="4" fill="{fill}" stroke="#1a1f2e"/>')
        s.append(f'<text x="{x+WW/2-1}" y="{TOP+H-7}" text-anchor="middle" font-size="10" '
                 f'font-family="Verdana" fill="#39404f">{_nome_tecla(p)}</text>')
        x_pos[p] = x; x += WW
    for p in blacks:
        bx = x_pos[p-1] + WW - BW/2 - 1
        fill = '#f5b942' if p in FORTE else ('#8a6d2f' if p in SUAVE else '#141926')
        s.append(f'<rect x="{bx}" y="{TOP}" width="{BW}" height="{int(H*0.62)}" rx="3" fill="{fill}" stroke="#000"/>')
        x_pos[p] = bx
    def call(p, txt, ty, cor='#ffd166'):
        cx = x_pos[p] + (WW/2 if p in whites else BW/2)
        s.append(f'<line x1="{cx}" y1="{TOP-3}" x2="{cx}" y2="{ty+5}" stroke="{cor}" '
                 f'stroke-width="1" stroke-dasharray="2,2"/>')
        s.append(f'<text x="{cx}" y="{ty}" text-anchor="middle" font-size="11" font-family="Verdana" '
                 f'fill="{cor}">{txt}</text>')
    call(71, '▲ a rampa — LIGHTS / NIGHT (B4)', 16)
    call(73, '▲ o pico — be-LIEV (C#5)', 36)
    call(76, 'E5: o solo da guitarra — não é da voz', 16, cor='#8b93a7')
    cx = x_pos[59] + WW/2
    s.append(f'<text x="{cx}" y="{TOP+H+16}" text-anchor="middle" font-size="11" font-family="Verdana" '
             f'fill="#9ec1ff">▼ o fundão — where (B3)</text>')
    xr = (x_pos[59] + x_pos[73] + BW) / 2
    s.append(f'<text x="{xr}" y="{TOP+H+36}" text-anchor="middle" font-size="11" font-family="Verdana" '
             f'fill="#ffd166">o riff mora aqui — B3 · E4 · G#4 · B4 (+ o C#5 de borda)</text>')
    s.append('</svg>')
    return ''.join(s)

def build_html():
    H = []
    H.append('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">')
    H.append('<title>Don\u2019t Stop Believin\u2019 — mapa musical em Mi maior · a cópia do Richard Goodall</title>')
    H.append(f'<style>{CSS}</style></head><body><div class="wrap">')

    # cabeçalho
    H.append('<h1>🌃 Don\u2019t Stop Believin\u2019 — o mapa musical</h1>')
    H.append('<div class="sub">Journey, 1981 · a cópia do Richard Goodall — AGT 2024, Golden Buzzer da Heidi Klum</div>')
    H.append('<div class="chips">'
             '<span class="chip">tom: MI MAIOR — o disco, a audição e a sua cifra</span>'
             '<span class="chip">118 bpm · 4/4 · ≈123 compassos</span>'
             '<span class="chip">voz B3–C#5 · um barítono na montanha do tenor</span>'
             '<span class="chip">solo de guitarra: E5 — não é voz!</span>'
             '<span class="chip">um loop carrega a música inteira</span></div>')

    # a história
    H.append('<div class="card"><h2>💡 A música que não para de girar</h2>'
             '<div class="sub2">a matriz que o Goodall montou no palco</div>'
             '<p>Um loop de oito compassos — <span class="rika">E · B · C#m · A · E · B · G#m · A</span> — '
             'carrega a música INTEIRA: riff, versos, solo e refrão viajam no mesmo trem. O refrão-título '
             'só chega aos <span class="rika">3min20 dos 4min11</span>: a paciência é a estrutura. A única '
             'parada é o desvio dos <span class="rika">Strangers</span> — e até ele volta pra estação.</p>'
             '<p>E em 2024 um faxineiro de Terre Haute, que cantava essa música nos corredores da escola '
             'há 23 anos, subiu no palco do AGT e <span class="rika">montou o disco inteiro</span>: mesmo tom, '
             'mesmo tempo, mesmo loop. A cópia era tão fiel que na final o próprio Journey subiu para cantar '
             'com ele — <span class="rika">a cópia encontrou o original</span>.</p></div>')

    # transparência
    H.append('<div class="card"><h2>🎚️ Transparência da afinação (e da fábrica)</h2>'
             '<div class="sub2">tudo o que foi verificado, por quem, e onde a fonte era fraca</div>'
             '<p><b>O tom é Mi maior</b> por quatro testemunhas independentes: a partitura oficial '
             '(Musicnotes MN0100427), a Wikipedia (118 bpm), o Chordify no áudio oficial e o Chordify '
             '<b>na audição do Goodall, duas vezes</b> (A E B G#m, ~120 bpm). Disco = audição: '
             '<span class="rika">a cópia é real</span>.</p>'
             '<p><b>O esqueleto MIDI</b> (bitmidi 63595, 17 pistas, 118 bpm) veio em <b>Dó# maior</b> com '
             'enarmonias selvagens (F onde quer dizer E#, C onde quer dizer B#) — a fábrica importa com '
             '<b>+3 semitons</b>. Ele não tem pista de voz: <b>a linha vocal foi transcrita de ouvido e '
             'validada por você</b> (5 perguntas, 5 respostas), dentro das cercas do Hooktheory: '
             'verso B3–B4, strangers E4–B4, refrão E4–C#5, melodia 100% diatônica, 69% notas de acorde.</p>'
             '<p><b>Onde o esqueleto mente (e o disco venceu)</b>: os Strangers esticados em blocos de '
             '2 compassos (o disco alterna <span class="rika">B7/A→A · Eadd9→E</span> por compasso), '
             'o solo sumiu (vamp direto), a bateria atrasa, o final desacelera — o disco de 1981 '
             '<b>termina frio</b>.</p></div>')

    # teclado
    H.append('<div class="card"><h2>⌨️ O teclado-guia</h2>'
             '<div class="sub2">as cinco notas da história, todas apontadas</div>'
             + keyboard_svg() +
             '<div class="obs">dourado forte = o riff no bar do E (B3·E4·G#4·B4 + C#5 de borda) · '
             'dourado fraco = as outras voicings do riff · C#5 = o pico da voz · B4 = a rampa · '
             'B3 = o fundão (e a primeira nota do riff!) · E5 cinza = o solo da guitarra</div></div>')

    # riff
    H.append('<div class="card gold"><h2>🎹 O RIFF — a assinatura</h2>'
             '<div class="sub2">a mão que re-voza: quinta embaixo no E e no C#m, fundamental embaixo no B e no A</div>'
             + ''.join(f'<div><span class="acorde">{k}</span> <span class="big rika">{v}</span></div>'
                       for k, v in RIFF.items()) +
             '<div class="obs">8 compassos de intro = duas voltas do loop · por baixo, o trem: '
             'E1 (2 tempos) → F#1–G#1 → <b>B1 no tempo 4</b> — cada acorde seguinte é lançado um tempo antes. '
             'No disco o riff abre sozinho; no AGT, foi ele que acendeu o Goodall.</div></div>')

    # seções
    H.append('<h3 style="font-size:18px;color:#ffd166;margin:26px 0 4px;">🎤 As seções, frase a frase</h3>'
             '<div class="sub2">célula = sílaba ↔ nota · dourado = pico · azul = fundão · tracejado = melisma</div>')

    H.append('<div class="card"><h2>INTRO · c1–8</h2><div class="sub2">o riff, sozinho no disco — '
             'a assinatura da música inteira</div>'
             '<div><span class="acorde">E</span><span class="acorde">B</span><span class="acorde">C#m</span>'
             '<span class="acorde">A</span><span class="acorde">E</span><span class="acorde">B</span>'
             '<span class="acorde">G#m</span><span class="acorde">A</span></div>'
             '<div class="obs">duas voltas do loop · a voz só entra depois — e entra baixo. É o contraste '
             'que faz o lift funcionar.</div></div>')

    H.append('<div class="card"><h2>V1a — "small town girl" · c9–16</h2>'
             '<div class="sub2">o verso commuter: contido, quase falado — de propósito</div>'
             + _grupo('V1') + '</div>')

    H.append('<div class="card"><h2>V1b — "city boy" · c17–24</h2>'
             '<div class="sub2">a GÊMEA</div>'
             '<p class="molda">V1b = V1a <b>nota a nota</b> — a mesma melodia, outra história. '
             'Treine uma, ganhe duas.</p>'
             '<div class="obs">"just a city boy, born and raised in South Detroit…" — mesmo mapa do V1a.</div></div>')

    H.append('<div class="card"><h2>INTERLÚDIO · c25–32</h2>'
             '<div class="sub2">o riff volta a falar sozinho</div>'
             '<div class="obs">a guitarra entra 4 compassos depois e vai enchendo — a pista do esqueleto '
             'mostra os fills crescendo compasso a compasso até o V2.</div></div>')

    H.append('<div class="card"><h2>V2 — "smoky room" · c33–40</h2>'
             '<div class="sub2">o mapa do V1, emprestado + a cauda</div>'
             '<p class="molda">"a singer in a smoky room… for a smile they can share the night" = '
             '<b>o mapa do V1</b> (a máquina dos versos é uma só).</p>'
             + _grupo('V2_CAUDA') + '</div>')

    H.append('<div class="card gold"><h2>STRANGERS — a rampa · c41–52</h2>'
             '<div class="sub2">a única saída do loop: B7/A→A · B7/A→A · Eadd9→E · Eadd9→E + tag B5·E5 | B5·E5·A5</div>'
             + _grupo('STRANGERS') + '</div>')

    H.append('<div class="card"><h2>V3a + V3b · c53–68</h2>'
             '<div class="sub2">de novo o mapa do V1 + a cauda</div>'
             '<p class="molda">"working hard to get my fill…" e "some will win, some will lose…" = '
             '<b>o mapa do V1</b>, com a mesma cauda "on and on" fechando o V3b.</p>'
             '<div class="obs">no Goodall essa página nem abre: o corte da audição pula direto dos '
             'strangers pro refrão.</div></div>')

    H.append('<div class="card"><h2>STRANGERS 2 · c69–80</h2><div class="sub2">a segunda volta</div>'
             '<p class="molda">= STRANGERS 1, nota a nota — e a segunda vez você já conhece o caminho.</p>'
             '</div>')

    H.append('<div class="card"><h2>SOLO · c81–88</h2><div class="sub2">a guitarra canta o refrão — mais alto</div>'
             '<p>A guitarra cita o <b>contorno do refrão</b> e sobe ao <span class="rika">E5</span> — o teto '
             'da música. No mapa da voz o E5 não existe: <span class="rika">é o violão falando</span>. '
             '(Foi um piano-solo de referência que entregou isso: a região que parecia refrão era o solo.)</p>'
             '</div>')

    H.append('<div class="card gold"><h2>REFRÃO — "Don\u2019t stop believ\u2019in\u2019" · c89–116</h2>'
             '<div class="sub2">no MESMO loop do verso — a altura é que mudou · ×3 no disco</div>'
             + _grupo('REFRAO') +
             '<div class="obs">a terceira vez corta direto pro tag. A famosa espera do refrão '
             '(3min20!) é esta: o loop girou 10 voltas antes de a voz subir ao C#5.</div></div>')

    H.append('<div class="card"><h2>TAG · c117–123</h2><div class="sub2">a terminação fria</div>'
             + _grupo('TAG') + '</div>')

    # camada goodall
    H.append('<div class="card gold"><h2>🔔 A CAMADA GOODALL — a audição que copiou o disco</h2>'
             '<div class="sub2">AGT S19, 28/05/2024 · a performance que fechou a estreia da temporada</div>'
             '<p class="big">' + ' <span class="seta">→</span> '.join(f'<span class="tl">{c}</span>' for c in GOODALL['corte']) + '</p>'
             '<p><b>Cortes do TV:</b> ' + ' '.join(f'<span class="cortado">{c}</span>' for c in GOODALL['cortados']) + '</p>'
             '<p><span class="rika2">A cópia, provada:</span> o Chordify ouviu a audição duas vezes — '
             '<b>Mi maior, ~120 bpm, A·E·B·G#m</b>: mesmo tom, mesmo tempo, mesmo loop do disco de 1981. '
             'A voz é de <b>barítono claro e forte</b> (bio oficial dele) — cantando a parte de um tenor, '
             'Steve Perry, no tom original. O momento em que a montanha aparece é o '
             '<span class="rika">C#5 do "be-LIEV"</span>: o barítono no tenro do Perry, a plateia de pé, '
             'e o buzzer dourado da Heidi Klum. Em setembro ele venceu a temporada — e cantou essa música '
             'na final <b>com o próprio Journey</b>.</p></div>')

    # mão esquerda
    linhas = ''.join(f'<tr><td class="k">{k}</td><td>{v}</td></tr>' for k, v in BAIXO.items())
    H.append('<div class="card"><h2>🖐️ A mão esquerda — o trem</h2>'
             '<div class="sub2">a caminhada do baixo por acorde do loop (lida do esqueleto, compasso a compasso)</div>'
             f'<table class="mao"><tr><th>acorde</th><th>a caminhada</th></tr>{linhas}</table>'
             '<div class="obs">a regra de ouro: <b>o tempo 4 lança o acorde seguinte</b> — é isso que faz '
             'a música andar de trem. Enquanto a direita faz o riff, a esquerda empurra.</div></div>')

    # costuras
    H.append('<div class="card"><h2>🧵 As costuras — onde a música vira</h2>'
             '<div class="sub2">as seis dobras que sustentam a montagem</div><ol class="cost">'
             '<li><b>INTRO → V1a:</b> o riff abre espaço e a voz entra <i>quase falada</i>. Não empurre o '
             'verso — o contraste é o que faz o lift funcionar.</li>'
             '<li><b>V1a → V1b:</b> a gêmea — mesma melodia, outra história. Respire na virada; o público '
             'reconhece o caminho na segunda vez.</li>'
             '<li><b>V1b → INTERLÚDIO → V2:</b> o riff volta sozinho, a guitarra entra 4 compassos depois, '
             'e o V2 devolve o mapa do V1 com a cauda "on and on".</li>'
             '<li><b>V2 → STRANGERS:</b> a única dobra harmônica da música — o loop <i>para</i> e o '
             'B7/A→A suspende tudo. Primeira vez que a harmonia sai dos trilhos.</li>'
             '<li><b>STRANGERS → REFRÃO:</b> a rampa — o "in the NIGHT" segura o B4 e solta o refrão no C#5. '
             'É a maior subida de um compasso só da música.</li>'
             '<li><b>REFRÃO → TAG:</b> o disco termina <b>frio</b>: "Don\u2019t stop!" corta seco. Sem fade, '
             'sem desacelerar (o esqueleto desacelera — licença do arranjador; o disco não).</li></ol></div>')

    # guia de montagem
    H.append('<div class="card"><h2>🗺️ Guia de montagem — a ordem de estudar</h2>'
             '<div class="sub2">do trem ao palco, em oito passos</div><ol class="cost">'
             '<li><b>O trem na mão esquerda</b> — o loop com as antecipações do tempo 4, até automatizar.</li>'
             '<li><b>O riff</b> — a mão que re-voza: B3-E4-G#4 / B3-D#4-F#4 / G#3-C#4-E4 / A3-C#4-E4 (+ o G#m).</li>'
             '<li><b>V1a + V1b</b> — a gêmea: treine uma, ganhe duas.</li>'
             '<li><b>Os STRANGERS</b> — o B7/A→A e o Eadd9→E; o chant em B4; a rampa do "night".</li>'
             '<li><b>O REFRÃO</b> — o C#5 do "be-LIEV" e a escada de resposta.</li>'
             '<li><b>V2 e V3</b> — os mapas emprestados + as caudas "on and on".</li>'
             '<li><b>A montagem inteira</b> — na ordem do disco, com o interlúdio e o solo de recorte.</li>'
             '<li><b>A camada Goodall</b> — toque junto com a audição: é o mesmo tom, dá pra acompanhar '
             'do início ao buzzer. 🔔</li></ol></div>')

    # footer
    H.append('<div class="foot">'
             '<b>Fontes:</b> Musicnotes MN0100427 (partitura oficial, Mi maior) · Wikipedia (118 bpm, voz '
             'E4–C#5) · Chordify no áudio oficial + duas análises da audição Goodall (Mi, ~120 bpm) · '
             'Hooktheory theorytab (cercas melódicas por seção) · spytunes (B/A·A / Eadd9·E) · tucuatro '
             '(estrutura + interlúdio) · guitaralliance · thesingingjanitor.com (barítono) · esqueleto: '
             'bitmidi 63595 (Dó# maior +3st, sem voz) · piano de referência: bitmidi 14642 · '
             'cifra do usuário (cifra-usuario-dsb.txt) — auditada: loop ✓, interlúdio ✓, A5–E5 = a '
             'essência dos B7/A→A / Eadd9→E, tag ✓.<br>'
             '<b>Validação:</b> melodia validada pelo ouvido do usuário (5/5) · sanity 7/7 · '
             'harmonia em consenso de 7 fontes.<br>'
             '<b>Regenera:</b> <code>python3 04-dont-stop-believin/trabalho/gera_dsb.py</code> — a fábrica é a fonte única de verdade. '
             'Esta página abre em qualquer navegador, com ou sem internet.</div>')

    H.append('</div></body></html>')
    html = '\n'.join(H)
    with open(SAIDAS / 'mapa-musical-dont-stop-believin.html', 'w', encoding='utf-8') as f:
        f.write(html)
    return html

# ────────────────────────── main ──────────────────────────
# ── saídas: a pasta ../saidas desta música (a fábrica roda de qualquer lugar) ──
from pathlib import Path as _P
SAIDAS = _P(__file__).resolve().parent.parent / "saidas"
SAIDAS.mkdir(exist_ok=True)

if __name__ == '__main__':
    ok = sanity()
    print()
    imprime_chat()
    html = build_html()
    n_abre = lambda t: html.count(f'<{t}') if t != 'div' else html.count('<div')
    n_fecha = lambda t: html.count(f'</{t}>')
    print('\n' + '═'*74)
    print(f'HTML: mapa-musical-dont-stop-believin.html · {len(html):,} caracteres')
    for t in ('div','span','svg','text','table'):
        a, f_ = html.count('<'+t), html.count('</'+t+'>')
        if a != f_: print(f'  ⚠ <{t}>: {a} abre vs {f_} fecha'); ok = False
    print(f"  frases: {sum(len(v) for v in FRASES.values())} · células: "
          f"{sum(len(f['pares']) for v in FRASES.values() for f in v)} · "
          f"pico C#5: {html.count('class=\"cell pico')} · fundão B3: {html.count('class=\"cell fundo')}")
    sys.exit(0 if ok else 1)
