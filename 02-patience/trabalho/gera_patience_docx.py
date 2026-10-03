#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera mapa-musical-patience.docx a partir dos dados de gera_patience.py
(fonte única de verdade — nenhuma transcrição manual das notas).

Requer:  pip install python-docx pillow
Roda:    python3 02-patience/trabalho/gera_patience_docx.py
Saída:   mapa-musical-patience.docx (A4, editável, uma tabela por frase)

Organização do documento (pensada pro ATRIL e pra anotação à mão):
  • Cada FRASE é uma tabela independente (Acorde / Canto-Conta / Notas)
    — pra encurtar, é só apagar tabelas ou linhas; pra anotar, margens generosas.
  • Seções = "Heading 1" — navega no painel do Word e gera sumário automático.
  • Notas em VERMELHO = o pico da frase (mesma convenção do HTML).
  • Notas em azul = registro real do disco (assobio G5–D6, solo A4–F#6…).
"""
import gera_patience as gp
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------------------------------------------------------------- cores (pergaminho em papel)
INK   = RGBColor(0x33, 0x30, 0x2A)
DARK  = RGBColor(0x5A, 0x46, 0x32)
GOLD  = RGBColor(0x8A, 0x6D, 0x3A)   # rótulos / acordes
MEL   = RGBColor(0x1D, 0x5C, 0x9E)   # melodia (azul do HTML)
LHC   = RGBColor(0xB0, 0x6A, 0x1A)   # a cama (laranja do HTML)
PEAK  = RGBColor(0xC0, 0x39, 0x2B)   # o pico
MUTED = RGBColor(0x85, 0x7A, 0x6C)
NOTE  = RGBColor(0x5A, 0x50, 0x44)
CREAM = "FDF6E9"

# ---------------------------------------------------------------- helpers docx
def shade(p, fill):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), fill)
    pPr.append(shd)


def box(doc, title, text, icon="💡"):
    p1 = doc.add_paragraph()
    p1.paragraph_format.space_before = Pt(8)
    p1.paragraph_format.space_after = Pt(0)
    r = p1.add_run(f"{icon} {title}")
    r.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = GOLD
    shade(p1, CREAM)
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(8)
    r2 = p2.add_run(text)
    r2.font.size = Pt(10)
    r2.font.color.rgb = NOTE
    shade(p2, CREAM)


def sub(doc, text, size=9.5):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(size)
    r.font.color.rgb = NOTE
    p.paragraph_format.space_after = Pt(4)


def cama(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    r1 = p.add_run("🛏️ Cama: ")
    r1.bold = True
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = GOLD
    r2 = p.add_run(text)
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = NOTE


def bullets(doc, items):
    for b in items:
        p = doc.add_paragraph(b, style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        for run in p.runs:
            run.font.size = Pt(10)


def numlist(doc, items):
    for lead, rest in items:
        p = doc.add_paragraph(style="List Number")
        p.paragraph_format.space_after = Pt(4)
        r1 = p.add_run(lead)
        r1.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = INK
        r2 = p.add_run(rest)
        r2.font.size = Pt(10)
        r2.font.color.rgb = NOTE


# ---------------------------------------------------------------- frase → tabela
def add_frase(doc, p, fallback_label):
    label = p.get("label") or fallback_label
    lp = doc.add_paragraph()
    lp.paragraph_format.space_before = Pt(10)
    lp.paragraph_format.space_after = Pt(2)
    lr = lp.add_run("◆ " + label)
    lr.bold = True
    lr.font.size = Pt(9.5)
    lr.font.color.rgb = MUTED

    ncols = len(p["syls"])
    tbl = doc.add_table(rows=3, cols=ncols + 1)
    tbl.style = "Table Grid"
    chords_at = {i: c for c, i in p["chords"]}
    peak = p.get("peak")
    for ri, row in enumerate((
            ["Acorde"] + [chords_at.get(i, "") for i in range(ncols)],
            ["Canto/Conta"] + list(p["syls"]),
            ["Notas"] + ["›".join(ns) for ns in p["notes"]])):
        for ci, val in enumerate(row):
            cell = tbl.cell(ri, ci)
            para = cell.paragraphs[0]
            para.paragraph_format.space_after = Pt(0)
            run = para.add_run(val)
            if ci == 0:
                run.font.size = Pt(8)
                run.font.color.rgb = MUTED
                run.bold = True
            elif ri == 0:                                    # acorde
                run.bold = True
                run.italic = True
                run.font.size = Pt(9.5)
                run.font.color.rgb = GOLD if val else MUTED
            elif ri == 1:                                    # canto/conta
                run.bold = True
                run.font.size = Pt(10.5)
                run.font.color.rgb = INK if val != "·" else MUTED
            else:                                            # notas
                run.font.name = "Consolas"
                run.font.size = Pt(10)
                if val == "·":
                    run.font.color.rgb = MUTED
                    run.font.weight = False
                elif ci - 1 == peak:
                    run.bold = True
                    run.font.color.rgb = PEAK
                else:
                    run.bold = True
                    run.font.color.rgb = MEL
    tbl.autofit = False
    total, first = 6.7, 1.0
    wcol = (total - first) / ncols
    for ri in range(3):
        tbl.cell(ri, 0).width = Inches(first)
        for ci in range(1, ncols + 1):
            tbl.cell(ri, ci).width = Inches(wcol)
    if p.get("note"):
        np_ = doc.add_paragraph()
        np_.paragraph_format.space_before = Pt(2)
        np_.paragraph_format.space_after = Pt(4)
        nr = np_.add_run("💡 " + p["note"])
        nr.italic = True
        nr.font.size = Pt(9.5)
        nr.font.color.rgb = NOTE


def secao(doc, titulo, nota, cama_txt, phrases, fills=None):
    doc.add_heading(titulo, level=1)
    if nota:
        sub(doc, nota)
    if cama_txt:
        cama(doc, cama_txt)
    for k, p in enumerate(phrases):
        add_frase(doc, p, f"Frase {k + 1}")
        if fills and k in fills:
            fp = doc.add_paragraph()
            fp.paragraph_format.space_before = Pt(2)
            fp.paragraph_format.space_after = Pt(6)
            fr = fp.add_run("↳ " + fills[k])
            fr.italic = True
            fr.font.size = Pt(9.5)
            fr.font.color.rgb = MUTED


# ---------------------------------------------------------------- teclado (PIL)
def draw_keyboard(path):
    from PIL import Image, ImageDraw, ImageFont
    mel = gp._all_note_names() - gp.LH_NOTES
    lh = set(gp.LH_NOTES)
    WHITE = ["C", "D", "E", "F", "G", "A", "B"]
    BLACK = {"C": "C#", "D": "D#", "F": "F#", "G": "G#", "A": "A#"}
    W, H, BW, BH, M = 62, 200, 36, 124, 16
    y0 = 86
    # conta as brancas C2..F6
    n_white = sum(1 for o in range(2, 7) for w in WHITE if not (o == 6 and w == "G"))
    IMGW = 2 * M + n_white * W
    img = Image.new("RGB", (IMGW, y0 + H + 74), "#ffffff")
    d = ImageDraw.Draw(img)

    def font(sz, bold=True):
        import os
        pth = ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
               else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
        if os.path.exists(pth):
            return ImageFont.truetype(pth, sz)
        return ImageFont.load_default()

    f_key, f_leg = font(14), font(14)

    def center(cx, cy, txt, f, col):
        bb = d.textbbox((0, 0), txt, font=f)
        d.text((cx - (bb[2] - bb[0]) / 2, cy - (bb[3] - bb[1]) / 2), txt, font=f, fill=col)

    x_pos, x = {}, M
    for octv in range(2, 7):
        for wname in WHITE:
            if octv == 6 and wname == "G":
                break
            label = f"{wname}{octv}"
            if label in mel:
                fill, tcol, txt = "#cfe3f8", "#1d5c9e", label
            elif label in lh:
                fill, tcol, txt = "#f9e4c8", "#b06a1a", label
            else:
                fill, tcol, txt = "#ffffff", None, None
            d.rectangle([x, y0, x + W - 2, y0 + H - 1], fill=fill, outline="#8d9aa8", width=2)
            if txt:
                center(x + (W - 2) / 2, y0 + H - 26, txt, f_key, tcol)
            if wname == "C":
                center(x + (W - 2) / 2, y0 + H - 8, label, font(12, bold=False), "#a5947d")
            if label == "C4":
                cx = x + (W - 2) / 2
                d.ellipse([cx - 7, y0 + 118, cx + 7, y0 + 132], fill="#e67e22")
                center(cx, y0 + 108, "dó central", font(12, bold=False), "#e67e22")
            if wname in BLACK:
                bl = f"{BLACK[wname]}{octv}"
                bx = x + W - BW // 2 - 1
                if bl in mel:
                    bfill, btxt, btcol = "#2f6fb5", bl, "#ffffff"
                elif bl in lh:
                    bfill, btxt, btcol = "#d08a3e", bl, "#241505"
                else:
                    bfill, btxt, btcol = "#2b3038", None, "#fff"
                d.rectangle([bx, y0, bx + BW - 1, y0 + BH - 1], fill=bfill, outline="#14171b", width=2)
                if btxt:
                    center(bx + BW / 2, y0 + BH - 14, btxt, font(11), btcol)
                x_pos[bl] = bx
            x_pos[label] = x
            x += W

    def cx(p):
        return x_pos[p] + ((W - 2) / 2 if p in mel or p in lh or p[0] in "CDEFGAB" and "#" not in p else BW / 2)

    def callout(key, txt, ty, col):
        c = x_pos[key] + (BW / 2 if "#" in key else (W - 2) / 2)
        f = font(14)
        bb = d.textbbox((0, 0), txt, font=f)
        d.line([c, ty + 12, c, y0 - 3], fill=col, width=1)
        d.text((c - (bb[2] - bb[0]) / 2, ty), txt, font=f, fill=col)

    callout("G5", "o assobio abre aqui (G5)", 40, "#1d5c9e")
    callout("G4", "a voz recebe o bastão (G4)", 14, "#1d5c9e")
    callout("F#6", "▲ o teto — F#6 (grito do solo)", 14, "#C0392B")

    ly = y0 + H + 22
    lx = M
    for fill, lab in (("#cfe3f8", "melodia (registro real)"), ("#f9e4c8", "cama (mão esquerda)")):
        d.rectangle([lx, ly, lx + 26, ly + 16], fill=fill, outline="#8d9aa8")
        d.text((lx + 32, ly), lab, font=f_leg, fill="#33465a")
        lx += 32 + d.textlength(lab, font=f_leg) + 22
    d.ellipse([lx + 4, ly + 2, lx + 18, ly + 16], fill="#e67e22")
    d.text((lx + 26, ly), "C4 = dó central", font=f_leg, fill="#33465a")
    img.save(path)


# ---------------------------------------------------------------- montagem
def build():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2)
    sec.top_margin = sec.bottom_margin = Cm(1.8)

    st = doc.styles["Normal"]
    st.font.name = "Segoe UI"
    st.font.size = Pt(11)
    st.font.color.rgb = INK
    h1 = doc.styles["Heading 1"]
    h1.font.name = "Segoe UI"
    h1.font.size = Pt(14)
    h1.font.bold = True
    h1.font.color.rgb = DARK

    # ---------- cabeçalho
    doc.add_heading("🎹 Mapa Musical — Patience", level=0)
    sub(doc, "Guns N' Roses · Lies (1988) — nota a nota, do assobio no G5 ao A5 no ar", 11)
    badges = doc.add_paragraph()
    rb = badges.add_run("150 compassos · 5:56 no disco   ·   60 frases · 9 seções   ·   Tom: Dó maior "
                        "(ponte em Ré maior)   ·   Teto: F#6   ·   Esqueleto: bitmidi 51380")
    rb.font.size = Pt(9)
    rb.font.color.rgb = MUTED

    # ---------- como ler
    doc.add_heading("📖 Como ler o mapa", level=1)
    bullets(doc, [
        "Cada tabela é uma frase. Na linha do meio: a sílaba cantada — ou o TEMPO (1–8), nas "
        "seções instrumentais. Embaixo: a nota, em REGISTRO REAL (as notas do disco).",
        "→ nota comprida (toca e deixa soar) · › notas ligadas no mesmo tempo · · silêncio (na "
        "ponte: a nota anterior segue valendo) · + notas juntas (guitarras em pares).",
        "Notas em VERMELHO = o pico da frase. A linha \u201cAcorde\u201d marca onde a cama muda.",
        "O assobio mora no G5–D6. Quer \u201ccantar\u201d junto no piano? Uma oitava abaixo "
        "(G4–D5) — o desenho é o que importa.",
        "A mão esquerda mora na tabela \u201cMão esquerda\u201d, no fim do mapa — quem aprende a "
        "intro já sabe acompanhar quase a música toda.",
    ])
    box(doc, "Transparência da afinação",
        "A cifra da Ultimate Guitar diz \u201cviolões meio tom abaixo\u201d — o disco pode soar em "
        "Si enquanto este mapa (e o MIDI) fala Dó. Se acontecer ao tocar junto da gravação, "
        "transporte tudo meio tom: o desenho não muda um milímetro — é a vantagem do mapa.")

    # ---------- teclado
    doc.add_heading("🎼 Onde estão as notas (teclado-guia)", level=1)
    try:
        draw_keyboard(SAIDAS / "teclado-pat.png")
        doc.add_picture(str(SAIDAS / "teclado-pat.png"), width=Inches(6.7))
        doc.paragraphs[-1].alignment = 1
    except Exception as e:
        p = doc.add_paragraph(f"(Teclado-guia indisponível nesta geração: {e})")
        p.runs[0].font.color.rgb = MUTED
    sub(doc, "Azul = melodia (assobio, voz, falsete, solo, respostas — registro real). Laranja = a "
             "cama da mão esquerda (C2 · G2 · A2 · D2 · E2 · F3). O ponto laranja é o dó central. "
             "Do G4 da entrada da voz ao F#6 do grito do solo — é o território inteiro da música.")

    doc.paragraphs[-1].add_run().add_break(WD_BREAK.PAGE)

    # ---------- seções
    secao(doc, "🎵 INTRO — o assobio (c. 2–25 · registro real G5–D6)",
          gp.INTRO_NOTA, gp.CAMA_INTRO, gp.INTRO, gp.INTRO_FILLS)
    box(doc, "A intro em uma frase",
        "O assobio conta a história toda antes da letra: convite (C), tema (G), tensão (A7), "
        "pouso (D), pico D6, calma, bordado… e entrega a bola pra voz num G4 — a nota exata em "
        "que o Axl entra no \u201cShed a tear\u201d. Doze frases, quatro acordes, um pico e uma "
        "oitava de descida.")

    secao(doc, "🎤 VERSO 1 — \u201cShed a tear…\u201d (c. 26–41)",
          gp.VERSO_1_NOTA, gp.CAMA_INTRO, gp.VERSO_1, gp.VERSO_1_FILLS)

    secao(doc, "🎤 REFRAO 1 — \u201cSaid, woman…\u201d (c. 42–57)",
          gp.REFRAO_1_NOTA, gp.CAMA_REFRAO, gp.REFRAO_1, gp.REFRAO_1_FILLS)

    secao(doc, "🌬️ ECO — o falsete (c. 57–63 e 95–101 · toca 2×)",
          gp.ECO_NOTA,
          "só o colchão de D das guitarras (D2 na esquerda conta a história).",
          gp.ECO, gp.ECO_FILLS)

    doc.add_heading("♻️ VERSO 2 — de graça (c. 64–79)", level=1)
    box(doc, "O Verso 2 é o Verso 1, nota por nota",
        "\u201cI sit here on the stairs…\u201d usa o mapa do Verso 1 nota por nota — verificado "
        "compasso a compasso no MIDI (64 notas idênticas em altura, tempo e duração). Um mapa, "
        "dois versos: volte à seção VERSO 1 e cante as palavras novas.")

    secao(doc, "🎤 REFRAO 2 — a variação (c. 80–101 · mesma música, palavras novas)",
          gp.REFRAO_2_NOTA, gp.CAMA_REFRAO, gp.REFRAO_2, gp.REFRAO_2_FILLS)

    secao(doc, "🎸 SOLO — a guitarra canta o refrão (c. 102–121 · teto F#6)",
          gp.SOLO_NOTA, gp.CAMA_SOLO, gp.SOLO, gp.SOLO_FILLS)

    secao(doc, "🛬 INTERLÚDIO — a aterrissagem (c. 122–128)",
          gp.INTERLUDIO_NOTA,
          "D (c. 122–125) · G (c. 126) · D (c. 127–128) — o D2 seguro conta a história.",
          gp.INTERLUDIO, gp.INTERLUDIO_FILLS)

    secao(doc, "🌉 PONTE — em Ré maior: as ruas (c. 129–147)",
          gp.PONTE_NOTA, gp.CAMA_PONTE, gp.PONTE, gp.PONTE_FILLS)

    secao(doc, "🕯️ FINAL — o adeus (c. 148–150)",
          gp.FINAL_NOTA, "D (D2) — e a 5ª no ar.", gp.FINAL, gp.FINAL_FILLS)

    box(doc, "O disco em uma frase",
        "A música é um convite que termina suspenso: abre com um assobio no G5 e acaba com um "
        "A5 no ar. Entre os dois: uma voz que recebe a bola exatamente onde o assobio deixou, um "
        "refrão que mora uma oitava acima, um falsete que responde no andar do assobio, um solo "
        "que canta o refrão e grita no F#6 a palavra que a voz não aguenta, e uma ponte que muda "
        "de mundo pra Ré — com a única nuvem menor da história (o Dm7 do \u201coh, I need "
        "you\u201d) aparecendo nos últimos segundos. Tudo com quatro moldes e um tempero (o A7).")

    box(doc, "A música mora em 4 moldes",
        "1) A roda do verso (C C G G A7 A7 D D) — verso, e o esqueleto de tudo.  2) A roda do "
        "refrão (C G C Em C G D) — o A7 vira Em: o tempero vira melancolia.  3) O campo do D — o "
        "eco, o solo 2ª metade, o interlúdio, os sinos, o final: tudo D.  4) As ruas de Ré "
        "(D ↔ G, com a nuvem Dm7 → G7) — a ponte. Quem aprende os 4 moldes toca a música "
        "inteira de ponta a ponta.")

    # ---------- mão esquerda
    doc.add_heading("🖐️ Mão esquerda (a cama)", level=1)
    p = doc.add_paragraph("Comece simples — só o baixo, bem fraquinho, um por acorde:")
    p.runs[0].font.size = Pt(10)
    LH_ROWS = [
        ("C", "C2", "C2 + C4-E4-G4", "a casa — intro, verso, refrão"),
        ("G", "G2", "G2 + G4-B4", "o outro pé — verso, refrão, ponte, interlúdio"),
        ("A7", "A2", "A2 + C#4 (+G4)", "o tempero — verso e 2ª metade do solo"),
        ("D", "D2", "D2 + D4-F#4", "o pouso — intro, refrão, solo, ponte, final"),
        ("Em", "E2", "E2 + G4-B4-E5", "a melancolia — refrão"),
        ("Dm7", "D2", "D2 + F3-A3-C4", "a nuvem — só na ponte (\u201cOh, I need you\u201d)"),
        ("G7", "G2", "G2 + F4-B4", "o ámén de blues — final da ponte"),
    ]
    lt = doc.add_table(rows=len(LH_ROWS) + 1, cols=4)
    lt.style = "Table Grid"
    lw = [Inches(0.7), Inches(0.7), Inches(1.9), Inches(3.4)]
    for ci, h in enumerate(("Acorde", "Baixo", "Com corpo (2ª etapa)", "Onde mora")):
        cell = lt.cell(0, ci)
        cell.width = lw[ci]
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = GOLD
    for ri, row in enumerate(LH_ROWS, 1):
        for ci, val in enumerate(row):
            cell = lt.cell(ri, ci)
            cell.width = lw[ci]
            run = cell.paragraphs[0].add_run(val)
            run.font.size = Pt(9.5)
            if ci == 0:
                run.bold = True
                run.font.color.rgb = GOLD
            elif ci == 1:
                run.font.name = "Consolas"
                run.font.color.rgb = LHC
    box(doc, "Quem aprende a intro já sabe quase tudo",
        "A cama do verso/refrão é a mesma da intro. Na ponte, a mão esquerda descansa em "
        "D2/A2 (o Ré maior novo).")

    # ---------- costuras
    doc.add_heading("🧵 As 7 costuras — onde tudo se encaixa", level=1)
    numlist(doc, [
        ("Intro → Verso 1: ", "o assobio desce até o G4 (c. 23) e a voz recebe NA MESMA NOTA "
         "(c. 26) — a passagem de bastão combinada."),
        ("Verso → Refrão: ", "a voz termina no D4 e o refrão abre no C5 — muda de bairro: uma "
         "oitava acima da tônica."),
        ("Refrão → Eco: ", "o refrão morre no A4… e o falsete responde uma oitava acima (A5) — "
         "o registro do assobio."),
        ("Refrão 2 → Solo: ", "o grito \u201cwe won't fake it!\u201d e os licks de F#6 "
         "despacham — e o solo abre CANTANDO o refrão, uma oitava acima."),
        ("Solo → Interlúdio: ", "o F#5 fica no ar… e a cadência B4-A4 · F4-F#4 aterrissa em D."),
        ("Interlúdio → Ponte: ", "os sinos D6+A5 → F#6+D6 anunciam: a ponte vai ser em Ré maior."),
        ("Ponte → Final: ", "a última nota cantada é um D4 de 4 tempos… o eco E5-D5… e o A5 no "
         "ar. O convite fica suspenso."),
    ])

    # ---------- como estudar
    doc.add_heading("✈️ Como estudar", level=1)
    numlist(doc, [
        ("A cama primeiro: ", "4 baixos (C2 G2 A2 D2) cobrem a maior parte da música — toque "
         "eles com o disco até virar músculo."),
        ("O assobio: ", "12 frases, registro G5–D6. Quer \u201ccantar\u201d junto? Uma oitava "
         "abaixo (G4–D5) — o desenho é o que importa."),
        ("O verso: ", "6 frases e 2 reciclagens de graça (L4–6 = L1–3; Verso 2 = Verso 1)."),
        ("O refrão: ", "morar no C5. A variação do 2º refrão só troca palavras — cante junto."),
        ("O solo: ", "quem sabe o refrão já sabe a 1ª metade. O resto é licks em colcheias."),
        ("A ponte: ", "o esqueleto D-E-F#-G + a nuvem Dm7. Poucas notas, muito teatro."),
        ("Costure por último ", "(a lista das 7 acima) e grave-se tocando com o disco. 🎹"),
    ])

    # ---------- guia de montagem
    doc.add_heading("🗺️ Guia de montagem — a música inteira, de ponta a ponta", level=1)
    sub(doc, "150 compassos no MIDI (a transcrição é condensada: 5:00 contra 5:56 do disco — os "
             "números de compasso são a referência do projeto). A letra entre aspas é a deixa.")
    gt = doc.add_table(rows=len(gp.GUIDE) + 1, cols=6)
    gt.style = "Table Grid"
    gw = [Inches(0.3), Inches(1.35), Inches(1.9), Inches(1.5), Inches(0.95), Inches(0.7)]
    for ci, h in enumerate(("#", "Seção", "Como reconhece", "Acordes", "No mapa", "Comp.")):
        cell = gt.cell(0, ci)
        cell.width = gw[ci]
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = GOLD
    for ri, (n, como, ac, mp, comp) in enumerate(gp.GUIDE, 1):
        for ci, val in enumerate((str(ri), n, como, ac, mp, comp)):
            cell = gt.cell(ri, ci)
            cell.width = gw[ci]
            run = cell.paragraphs[0].add_run(val)
            run.font.size = Pt(8.5)
            if ci == 1:
                run.bold = True

    box(doc, "Status do projeto",
        "Toda a música está mapeada: intro, versos (o 2º de graça), refrões (com a variação), o "
        "eco, o solo, o interlúdio, a ponte em Ré e o final — 60 frases nota a nota. "
        "Transparências registradas no caminho: a afinação (meio tom), o dropout das guitarras "
        "(c. 54–55 e 92–93), o esqueleto da ponte, o grito \u201cwe won't fake it\u201d (letra "
        "sem nota — não se inventa nota), o eco morando numa pista separada e a condensação do "
        "MIDI. Nada ficou pendente.")

    # ---------- anotações
    doc.add_heading("✍️ Anotações", level=1)
    sub(doc, "dedos, voicings, lembranças — o espaço é seu")
    for _ in range(8):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(14)
        r = p.add_run("‍" + "＿" * 38)
        r.font.color.rgb = MUTED
        r.font.size = Pt(10)

    # ---------- rodapé
    foot = doc.add_paragraph()
    foot.paragraph_format.space_before = Pt(16)
    fr = foot.add_run(
        "Mapa conferido nota a nota com a transcrição MIDI (bitmidi.com/uploads/51380.mid), "
        "triangulada com Ultimate Guitar (ver 1 e 3), Cifra Club e 3 fontes de letra (letras.com, "
        "Shazam, lyrics.com). Registros reais: assobio G5–D6 · voz D4–D5 · falsete G5–A5 · solo "
        "A4–F#6 · respostas D5–E6. Tom: Dó maior, ponte em Ré maior. Teto: F#6 (c. 109–110, o "
        "grito do solo; c. 128, a cortina dos sinos).  ·  Regenera: python3 02-patience/trabalho/gera_patience_docx.py "
        "— os dados moram em gera_patience.py, a fonte única de verdade.")
    fr.font.size = Pt(8)
    fr.font.color.rgb = MUTED

    doc.core_properties.title = "Mapa Musical — Patience (Guns N' Roses)"
    doc.core_properties.author = "Fábrica gera_patience.py + gera_patience_docx.py"
    doc.save(SAIDAS / "mapa-musical-patience.docx")
    return doc


# ── saídas: a pasta ../saidas desta música (a fábrica roda de qualquer lugar) ──
from pathlib import Path as _P
SAIDAS = _P(__file__).resolve().parent.parent / "saidas"
SAIDAS.mkdir(exist_ok=True)

if __name__ == "__main__":
    doc = build()
    d2 = Document(SAIDAS / "mapa-musical-patience.docx")
    n_h1 = sum(1 for p in d2.paragraphs if p.style.name == "Heading 1")
    n_tbl = len(d2.tables)
    n_frases = sum(len(v) for v in (gp.INTRO, gp.VERSO_1, gp.REFRAO_1, gp.ECO, gp.REFRAO_2,
                                    gp.SOLO, gp.INTERLUDIO, gp.PONTE, gp.FINAL))
    print("═" * 74)
    print("DOCX: mapa-musical-patience.docx")
    print(f"  H1: {n_h1} · tabelas: {n_tbl} (frases {n_frases} + cama + guia)")
    ok = n_tbl == n_frases + 2 and len(d2.inline_shapes) == 1
    print(f"  [{'✓' if ok else '✗'}] estrutura esperada")
    raise SystemExit(0 if ok else 1)
