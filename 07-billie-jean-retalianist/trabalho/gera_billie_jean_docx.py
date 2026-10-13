#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gera_billie_jean_docx.py — fábrica PoC 7 (DOCX)
Gera ../saidas/mapa-musical-billie-jean.docx — a versão imprimível do mapa,
no padrão da casa (PoCs 4–6). Consome os mesmos dados do gera_billie_jean.py
(notas.json + fatos validados) e o teclado-billie.png.
"""
import json
import sys
from collections import Counter
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gera_billie_jean import (AQUI, SAIDAS, BPM, EDITORIAL, LETRAS_SIS, RIFF,
                              RIFF_ROTULO, TOM, DURACAO_Q,
                              acha_riffs, carrega, nm, secoes, stats,
                              cama_por_secao)

OURO = RGBColor(0xB8, 0x86, 0x0B)
CINZA = RGBColor(0x59, 0x59, 0x59)
ESCURO = RGBColor(0x1A, 0x1A, 0x1A)


def par(doc, txt='', bold=False, size=11, cor=ESCURO, center=False, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if txt:
        r = p.add_run(txt)
        r.bold = bold
        r.font.size = Pt(size)
        r.font.color.rgb = cor
    return p


def h1(doc, txt):
    par(doc, txt, bold=True, size=20, cor=OURO, space_after=2)


def h2(doc, txt):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(txt)
    r.bold = True
    r.font.size = Pt(14)
    r.font.color.rgb = OURO
    return p


def tabela(doc, cabecas, linhas, larguras=None):
    t = doc.add_table(rows=1, cols=len(cabecas))
    t.style = 'Light Grid Accent 1'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, c in enumerate(cabecas):
        cell = t.rows[0].cells[i]
        cell.text = c
        for r in cell.paragraphs[0].runs:
            r.bold = True
    for linha in linhas:
        cel = t.add_row().cells
        for i, v in enumerate(linha):
            cel[i].text = str(v)
            for r in cel[i].paragraphs[0].runs:
                r.font.size = Pt(10)
    if larguras:
        for row in t.rows:
            for i, w in enumerate(larguras):
                row.cells[i].width = Inches(w)
    return t


def main():
    SAIDAS.mkdir(exist_ok=True)
    evs, restos, rel = carrega()
    secs = secoes(rel)
    riffs = acha_riffs(evs)
    geral, por_mao, raros = stats(evs, riffs)
    cama = cama_por_secao(evs, secs)
    dur = lambda a, b: sum(4.0 if m not in raros['um_tempo'] else 1.0
                           for m in range(a, b + 1)) * DURACAO_Q

    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    # ── cabeçalho ──
    h1(doc, 'Billie Jean — o mapa musical')
    par(doc, 'Michael Jackson (1982) · versão lírica de piano de Romain Olivieri '
             '“Retalianist” (2013) · Prova de Conceito nº 7', cor=CINZA, center=True,
        space_after=2)
    par(doc, 'extração nota-a-nota do PDF oficial do arranjador · validada de ouvido '
             'contra o vídeo · 13/10/2026', cor=CINZA, center=True, space_after=10)

    # ── a ideia ──
    h2(doc, 'A ideia em 1 minuto')
    par(doc, 'O arranjador pegou o groove mais famoso do pop e o desacelerou à metade: '
             'o disco corre a ~115 bpm, aqui são ♩=75 — andamento de canção de '
             'madrugada. E fez uma mudança de papel genial: o riff que no disco é do '
             'baixo vira matéria-prima de tudo — primeiro é melodia na mão direita, '
             'depois emigra pra mão esquerda, no fim vira refrão inteiro.')
    par(doc, f'Tom: {TOM} (o mesmo do disco) · {rel["n_compassos"]} compassos · '
             f'{geral["n_notas"]} notas · extensão {nm(geral["ext"][0])}–'
             f'{nm(geral["ext"][1])} · 6:00 tocada reta.', bold=True)

    # ── a assinatura ──
    h2(doc, 'A assinatura — o riff')
    par(doc, RIFF_ROTULO, bold=True, size=13, cor=OURO, center=True)
    par(doc, 'Oito colcheias, quatro notas — Fá#, Dó#, Mi e Si: a escala de Fá#m '
             'cabendo numa mão. No disco, isso é o baixo; aqui é a primeira coisa que '
             'você ouve — e a semente de onde a melodia inteira vai nascer.')
    par(doc, 'Treino: o arquivo a-assinatura.mid traz o compasso 1 em loop (4 voltas '
             'da cama Fá#m → Mi → Ré → Si).', cor=CINZA)

    # ── teclado ──
    h2(doc, 'O teclado-guia — onde a peça mora')
    if (SAIDAS / 'teclado-billie.png').exists():
        doc.add_picture(str(SAIDAS / 'teclado-billie.png'), width=Inches(6.7))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    par(doc, 'As três moradas: Fá#4 (×186), Dó#4 (×167) e Fá#3 (×134) — tônica e '
             'quinta de Fá#m em dois andares. Mão direita '
             f'{nm(por_mao["D"]["ext"][0])}–{nm(por_mao["D"]["ext"][1])}; mão esquerda '
             f'{nm(por_mao["E"]["ext"][0])}–{nm(por_mao["E"]["ext"][1])}.', cor=CINZA)

    # ── a rua do riff ──
    h2(doc, f'A rua da assinatura — as {len(riffs)} aparições do riff')
    por_mao_riff = {mao: [r['m'] for r in riffs if r['mao'] == mao] for mao in 'DE'}

    def grupos(ms):
        out, a, b = [], None, None
        for m in ms:
            if a is None:
                a = b = m
            elif m == b + 1:
                b = m
            else:
                out.append((a, b))
                a = b = m
        if a is not None:
            out.append((a, b))
        return out

    linhas = []
    for rot, mao_n in (('mão direita (agudo)', 'D'), ('mão esquerda (grave)', 'E')):
        gs = ', '.join(f'c{a}' if a == b else f'c{a}–{b}' for a, b in grupos(por_mao_riff[mao_n]))
        linhas.append([rot, len(por_mao_riff[mao_n]), gs])
    tabela(doc, ['quem toca', 'nº de vezes', 'compassos'],
           linhas, larguras=[1.6, 0.9, 4.2])
    par(doc, 'A leitura: o riff nasce no agudo (INTRO), emigra pro grave na seção A, '
             'volta ao agudo como relâmpago na seção C, ronca no porão na seção D — e '
             'na seção F explode: 12 vezes seguidas (c77–91), o coração do refrão do '
             'arranjador.', cor=CINZA)

    # ── a cama ──
    h2(doc, 'A cama — o carrossel Fá# · Mi · Ré')
    par(doc, 'Quase toda a harmonia gira num carrossel de três acordes que você '
             'conhece do disco: Fá#m → Mi → Ré (com o Si fazendo a virada). '
             '“Fá#5” = quinta aberta, sem a terça — o som redondo que o arranjador '
             'prefere no fundo.')
    linhas = []
    for rot, a, b in secs:
        cont5, _raizes = cama[rot]
        txt = (', '.join(f'{c} ×{n}' for c, n in cont5) if cont5
               else '— (esquerda em notas curtas)')
        linhas.append([f'{rot} (c{a}–{b})', txt])
    tabela(doc, ['seção', 'acordes da mão esquerda'], linhas, larguras=[1.3, 5.4])

    # ── a jornada ──
    h2(doc, 'A jornada — seção a seção')
    for rot, a, b in secs:
        titulo, texto = EDITORIAL[rot]
        ps = [p for e in evs if a <= e['m'] <= b for p in e['pitches']]
        ext_s = f'{nm(min(ps))}–{nm(max(ps))}' if ps else '—'
        top = Counter(nm(p) for p in ps).most_common(3)
        n_riff = len([r for r in riffs if a <= r['m'] <= b])
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        r = p.add_run(f'{rot} — {titulo}')
        r.bold = True
        r.font.size = Pt(12)
        p2 = doc.add_paragraph()
        r2 = p2.add_run(f'c{a}–{b} · {dur(a, b):.0f} s · extensão {ext_s} · '
                        f'moradas: {", ".join(f"{t} ×{n}" for t, n in top)}'
                        + (f' · riff ×{n_riff}' if n_riff else ''))
        r2.italic = True
        r2.font.size = Pt(9)
        r2.font.color.rgb = CINZA
        par(doc, texto)

    # ── momentos raros ──
    h2(doc, 'Os momentos raros — o que procurar de ouvido')
    tabela(doc, ['momento', 'onde', 'o que você ouve'], [
        ['o único Fá natural + Mi♯', 'c23',
         'a cor “fora” da peça: Fá natural contra a sensível Mi♯ — instante de '
         'clima de filme'],
        ['a família Mi♯', 'c12 · c23 · c33 · c50 · c62',
         'a sensível da Fá#m harmônica espalhada pela peça — o tempero clássico '
         'do tom menor'],
        ['o porão', 'Sol#1 em c52', 'a nota mais grave da peça, no fundo da seção D'],
        ['o teto', 'Fá#5 em c105',
         'a nota mais aguda, na despedida — a direita abre o leque no fim'],
        ['as fusas em oitonas', 'c93–99',
         'pares velozes em duas oitavas — a única “vertigem” da peça, na ponte'],
        ['os compassos de 1 tempo', 'c14 e c39',
         'a música pisa no freio: um compasso inteiro dura um só tempo — viradas '
         'de cenário'],
        ['as respirações', 'c14–15 · c39 · c92',
         'as duas mãos param juntas antes da barra — fôlego antes das grandes '
         'viradas'],
    ], larguras=[1.7, 1.5, 3.5])

    # ── as mãos ──
    h2(doc, 'O diálogo das mãos')
    for mao, rot in (('D', 'A mão direita'), ('E', 'A mão esquerda')):
        pm = por_mao[mao]
        par(doc, f'{rot} — {pm["n"]} notas, moradias '
                 f'{", ".join(f"{t} ×{n}" for t, n in pm["top"])}.')
    par(doc, 'O diálogo é a dramaturgia da peça: a direita começa cantando o riff; na '
             'seção A o riff desce pro porão da esquerda enquanto a direita vira voz; '
             'na seção F eles se juntam — o riff no alto, o carrossel embaixo — e a '
             'peça vira, por 15 compassos, a si mesma em câmera dupla.')

    # ── guia de montagem ──
    h2(doc, 'Guia de montagem — a ordem de estudar')
    for txt in [
        '1. A assinatura primeiro. Estude o riff sozinho (quatro notas!) e com '
        'a-assinatura.mid — 4 voltas do compasso 1 com a cama.',
        '2. A cama. estudo-esquerda-55.mid: acompanhe o carrossel Fá#m–Mi–Ré–Si da '
        'INTRO — o mesmo desenho do disco, só devagar.',
        '3. A cantiga. estudo-direita-55.mid: a melodia da seção A nasce do riff — '
        'você já sabe metade dela.',
        '4. Juntas, devagar. estudo-juntas-55.mid até sentir o diálogo; depois 65 e '
        '75 (o andamento escrito).',
        '5. As vitrines. Pontos de prova de ouvido: a emigração do riff (c16), o '
        'porão (c52), a campeã (c77–91), as fusas (c93–99) e o teto (c105).',
    ]:
        par(doc, txt)

    # ── transparência ──
    h2(doc, 'Transparência da fábrica')
    for txt in [
        '• Fonte da verdade: o PDF oficial do arranjador (Finale 2012/Maestro, 6 '
        'páginas), dissecado nota-a-nota por leitura vetorial: 1690 notas; 87% dos '
        'compassos fechando exato no 4/4 (o resto são pausas de respiração reais e '
        '±meia-colcheia de ambiguidade).',
        '• Contraprova: transcrição IA do vídeo do Retalianist — mesmas notas mais '
        'tocadas (Fá#4, Dó#4, Lá3, Mi4), mesmo tom.',
        '• Validação final: a sonda MIDI (a partitura tocada reta) foi ouvida e '
        'confirmada nota a nota contra o vídeo pelo juiz final (13/10/2026).',
        '• Arquivos: mapa-musical-billie-jean.html · este DOCX · teclado-billie.png · '
        'a-assinatura.mid + 9 MIDIs de estudo (esquerda/direita/juntas a 55, 65 e 75).',
    ]:
        par(doc, txt, size=10, cor=CINZA)

    doc.save(SAIDAS / 'mapa-musical-billie-jean.docx')
    print('✓ mapa-musical-billie-jean.docx gerado em', SAIDAS)
    return SAIDAS / 'mapa-musical-billie-jean.docx'


if __name__ == '__main__':
    main()
