#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera mapa-musical-dont-stop-believin.docx a partir dos dados de gera_dsb.py
(fonte única de verdade — nenhuma transcrição manual das notas).

Requer:  pip install python-docx pillow
Roda:    python3 04-dont-stop-believin/trabalho/gera_dsb_docx.py
Saída:   mapa-musical-dont-stop-believin.docx (A4, editável, uma tabela por frase)

Organização do documento (pensada pro ATRIL e pra anotação à mão):
  • Cada FRASE é uma tabela independente (Acorde / Sílaba / Nota)
    — pra encurtar, é só apagar tabelas ou linhas; pra anotar, margens generosas.
  • Seções musicais = "Heading 2" sob "As seções, frase a frase" — navega no
    painel do Word e gera sumário automático.
  • Notas em VERMELHO = o pico da voz (C#5, "be-LIEV"); em AZUL = o fundão (B3);
    cinza tracejado (→) = melisma. Mesma convenção do HTML.
  • Identidade streetlights em dourado — mas fundo branco: imprime barato.
"""
import gera_dsb as gd
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------------------------------------------------------------- cores (streetlights em papel)
INK   = RGBColor(0x22, 0x30, 0x3E)   # texto principal
DARK  = RGBColor(0x4A, 0x37, 0x0A)   # títulos (bronze escuro)
GOLD  = RGBColor(0x8A, 0x6D, 0x2F)   # rótulos / acordes (dourado de sódio)
GOLDT = RGBColor(0x9A, 0x64, 0x0C)   # notas normais
PEAK  = RGBColor(0xC0, 0x39, 0x2B)   # o pico C#5
BLUE  = RGBColor(0x1D, 0x5F, 0xA8)   # o fundão B3
MUTED = RGBColor(0x68, 0x78, 0x8A)   # rótulos pequenos
NOTE  = RGBColor(0x4A, 0x5A, 0x6B)   # observações

CREAM = "FFF8EC"   # caixa-dica (luz de sódio em papel)
GOLDB = "FFF3D6"   # caixa Goodall

# ---------------------------------------------------------------- helpers docx
def shade(p, fill):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), fill)
    pPr.append(shd)


def box(doc, title, text, fill=CREAM, icon="💡", tcol=GOLD):
    p1 = doc.add_paragraph()
    p1.paragraph_format.space_before = Pt(8)
    p1.paragraph_format.space_after = Pt(0)
    r = p1.add_run(f"{icon} {title}")
    r.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = tcol
    shade(p1, fill)
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(8)
    r2 = p2.add_run(text)
    r2.font.size = Pt(10)
    r2.font.color.rgb = NOTE
    shade(p2, fill)
    return p2


def sub(doc, text, size=10):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(size)
    r.font.color.rgb = NOTE
    p.paragraph_format.space_after = Pt(4)
    return p


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
def add_frase(doc, f, label):
    lp = doc.add_paragraph()
    lp.paragraph_format.space_before = Pt(10)
    lp.paragraph_format.space_after = Pt(2)
    lr = lp.add_run("◆ " + label)
    lr.bold = True
    lr.font.size = Pt(9.5)
    lr.font.color.rgb = MUTED

    pares = f["pares"]
    ncols = len(pares)
    tbl = doc.add_table(rows=3, cols=ncols + 1)
    tbl.style = "Table Grid"

    # linha 1 — acordes da frase (célula unida)
    tbl.cell(0, 0).paragraphs[0].add_run("Acorde")
    uni = tbl.cell(0, 1).merge(tbl.cell(0, ncols))
    ru = uni.paragraphs[0].add_run("  ·  ".join(f["acordes"]))
    ru.bold = True
    ru.italic = True
    ru.font.size = Pt(10.5)
    ru.font.color.rgb = GOLD

    for ci, (sil, nota) in enumerate(pares, start=1):
        # linha 2 — a sílaba cantada
        cs = tbl.cell(1, ci).paragraphs[0]
        cs.paragraph_format.space_after = Pt(0)
        rs = cs.add_run(sil)
        rs.font.size = Pt(11)
        rs.font.color.rgb = INK
        if len(sil) > 1 and sil.replace("-", "").replace("!", "").replace("\u2019", "").isupper():
            rs.bold = True                       # a sílaba em cima = o acento
        elif sil == "→":
            rs.italic = True
            rs.font.color.rgb = MUTED
        else:
            rs.bold = True
        # linha 3 — a nota
        cn = tbl.cell(2, ci).paragraphs[0]
        cn.paragraph_format.space_after = Pt(0)
        rn = cn.add_run(nota)
        rn.font.name = "Consolas"
        rn.font.size = Pt(10.5)
        if nota == "C#5":                        # O PICO
            rn.bold = True
            rn.font.color.rgb = PEAK
        elif nota == "B3":                       # o fundão
            rn.bold = True
            rn.font.color.rgb = BLUE
        elif nota == "→":                        # melisma (a sílaba continua)
            rn.italic = True
            rn.font.color.rgb = MUTED
        else:
            rn.bold = True
            rn.font.color.rgb = GOLDT

    # rótulos da 1ª coluna
    for ri, rot in enumerate(("Acorde", "Sílaba", "Nota")):
        if ri == 0:
            continue
        c0 = tbl.cell(ri, 0).paragraphs[0]
        c0.paragraph_format.space_after = Pt(0)
        r0 = c0.add_run(rot)
        r0.bold = True
        r0.font.size = Pt(8)
        r0.font.color.rgb = MUTED
    c0 = tbl.cell(0, 0).paragraphs[0]
    r0 = c0.add_run(" ")
    r0.font.size = Pt(8)

    # larguras
    tbl.autofit = False
    total, first = 6.7, 0.95
    wcol = (total - first) / ncols
    for ri in range(3):
        tbl.cell(ri, 0).width = Inches(first)
        if ri == 0:
            uni.width = Inches(total - first)
        else:
            for ci in range(1, ncols + 1):
                tbl.cell(ri, ci).width = Inches(wcol)

    if f["obs"]:
        np_ = doc.add_paragraph()
        np_.paragraph_format.space_before = Pt(2)
        np_.paragraph_format.space_after = Pt(4)
        nr = np_.add_run("💡 " + f["obs"])
        nr.italic = True
        nr.font.size = Pt(9.5)
        nr.font.color.rgb = NOTE


def grupo(doc, chave):
    for k, f in enumerate(gd.FRASES[chave], 1):
        add_frase(doc, f, f"Frase {k}")


# ---------------------------------------------------------------- teclado (PIL)
def draw_keyboard(path):
    from PIL import Image, ImageDraw, ImageFont
    FORTE = {59, 64, 68, 71, 73}                 # B3 E4 G#4 B4 + C#5 (o bar do E)
    SUAVE = {56, 57, 61, 63, 66}                 # G#3 A3 C#4 D#4 F#4 (outras voicings)
    SOLO  = {76}                                 # E5 — da guitarra, não da voz

    W, H, BW, BH, M = 62, 200, 36, 124, 16
    whites = [p for p in range(48, 77) if p % 12 in (0, 2, 4, 5, 7, 9, 11)]
    blacks = [p for p in range(48, 76) if p % 12 in (1, 3, 6, 8, 10)]
    y0 = 86
    IMGW = 2 * M + len(whites) * W
    img = Image.new("RGB", (IMGW, y0 + H + 74), "#ffffff")
    d = ImageDraw.Draw(img)

    def font(sz, bold=True):
        import os
        p = ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
             else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
        return ImageFont.load_default()

    f_key, f_leg = font(14), font(14)
    N = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    nome = lambda p: N[p % 12] + str(p // 12 - 1)

    def center(cx, cy, txt, f, col):
        bb = d.textbbox((0, 0), txt, font=f)
        d.text((cx - (bb[2] - bb[0]) / 2, cy - (bb[3] - bb[1]) / 2), txt, font=f, fill=col)

    x_pos = {}
    x = M
    for p in whites:                              # brancas
        if p in FORTE:   fill, tcol, lab = "#F5B942", "#4a3a10", nome(p)
        elif p in SUAVE: fill, tcol, lab = "#E8CE8A", "#4a3a10", nome(p)
        elif p in SOLO:  fill, tcol, lab = "#CFCFCF", "#3a3f4a", nome(p)
        else:            fill, tcol, lab = "#F7F3E8", None, None
        d.rectangle([x, y0, x + W - 2, y0 + H - 1], fill=fill, outline="#8d9aa8", width=2)
        if lab:
            center(x + (W - 2) / 2, y0 + H - 26, lab, f_key, tcol)
        if p == 60:                               # C4 = dó central
            cx = x + (W - 2) / 2
            d.ellipse([cx - 7, y0 + 118, cx + 7, y0 + 132], fill="#e67e22")
            center(cx, y0 + 108, "dó central", font(12, bold=False), "#e67e22")
        x_pos[p] = x
        x += W
    for p in blacks:                              # pretas
        bx = x_pos[p - 1] + W - BW // 2 - 1
        if p in FORTE:   fill, tcol, lab = "#F5B942", "#4a3a10", nome(p)
        elif p in SUAVE: fill, tcol, lab = "#B08A2E", "#ffffff", nome(p)
        else:            fill, tcol, lab = "#23262E", None, None
        d.rectangle([bx, y0, bx + BW - 1, y0 + BH - 1], fill=fill, outline="#14171b", width=2)
        if lab:
            center(bx + BW / 2, y0 + BH - 14, lab, font(11), tcol)
        x_pos[p] = bx

    def cx(p):
        return x_pos[p] + ((W - 2) / 2 if p in whites else BW / 2)

    def callout(p, txt, ty, col, align="mid"):
        f = font(14)
        bb = d.textbbox((0, 0), txt, font=f)
        tw = bb[2] - bb[0]
        c = cx(p)
        tx = c - tw / 2
        if align == "right":
            tx = IMGW - M - tw
        d.line([c, ty + 12, c, y0 - 3], fill=col, width=1)
        d.text((tx, ty), txt, font=f, fill=col)

    callout(59, "▼ o fundão — B3 (\u201cwhere\u201d)", 14, "#1D5FA8")
    callout(73, "▲ o PICO — be-LIEV (C#5)", 40, "#C0392B")
    callout(71, "▲ a rampa — LIGHTS / NIGHT (B4)", 66, "#8A6D2F")
    callout(76, "E5 = solo da guitarra — não é voz", 14, "#6a6f7a", align="right")

    # o bracket do riff (embaixo, B3 → C#5)
    yb = y0 + H + 12
    d.line([cx(59), yb, cx(73) + BW, yb], fill="#8A6D2F", width=2)
    d.line([cx(59), yb - 6, cx(59), yb + 6], fill="#8A6D2F", width=2)
    d.line([cx(73) + BW, yb - 6, cx(73) + BW, yb + 6], fill="#8A6D2F", width=2)
    center((cx(59) + cx(73) + BW) / 2, yb + 20, "o riff mora aqui — B3 · E4 · G#4 · B4 (+ o C#5 de borda)",
           font(14), "#8A6D2F")

    # legenda
    ly = y0 + H + 48
    x = M
    for fill, lab in (("#F5B942", "riff no bar do E"), ("#E8CE8A", "voicings do riff"),
                      ("#CFCFCF", "solo — não é voz")):
        d.rectangle([x, ly, x + 26, ly + 16], fill=fill, outline="#8d9aa8")
        d.text((x + 32, ly), lab, font=f_leg, fill="#33465a")
        x += 32 + d.textlength(lab, font=f_leg) + 22
    d.ellipse([x + 4, ly + 2, x + 18, ly + 16], fill="#e67e22")
    d.text((x + 26, ly), "C4 = dó central", font=f_leg, fill="#33465a")
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
    h2 = doc.styles["Heading 2"]
    h2.font.name = "Segoe UI"
    h2.font.size = Pt(12.5)
    h2.font.bold = True
    h2.font.color.rgb = GOLD

    # ---------- cabeçalho
    doc.add_heading("🎹 Mapa Musical — Don\u2019t Stop Believin\u2019", level=0)
    sub(doc, "Journey, 1981 · a cópia do Richard Goodall — AGT 2024, Golden Buzzer da Heidi Klum", 11)
    badges = doc.add_paragraph()
    rb = badges.add_run("Tom: MI MAIOR — o disco, a audição e a sua cifra   ·   118 bpm · 4/4 · ≈123 "
                        "compassos   ·   Voz: B3–C#5 (um barítono na montanha do tenor)   ·   E5 é do "
                        "solo de guitarra — não é voz   ·   Um loop carrega a música inteira")
    rb.font.size = Pt(9)
    rb.font.color.rgb = MUTED

    # ---------- a história
    doc.add_heading("💡 A música que não para de girar", level=1)
    for txt in (
        "Um loop de oito compassos — E · B · C#m · A · E · B · G#m · A — carrega a música INTEIRA: "
        "riff, versos, solo e refrão viajam no mesmo trem. O refrão-título só chega aos 3min20 dos "
        "4min11: a paciência é a estrutura. A única parada é o desvio dos Strangers — e até ele "
        "volta pra estação.",
        "E em 2024 um faxineiro de Terre Haute, que cantava essa música nos corredores da escola há "
        "23 anos, subiu no palco do AGT e montou o disco inteiro: mesmo tom, mesmo tempo, mesmo "
        "loop. A cópia era tão fiel que na final o próprio Journey subiu para cantar com ele — "
        "a cópia encontrou o original.",
    ):
        p = doc.add_paragraph(txt)
        p.paragraph_format.space_after = Pt(6)

    # ---------- transparência
    box(doc, "Transparência da afinação (e da fábrica)",
        "O tom é Mi maior por quatro testemunhas independentes: partitura oficial (Musicnotes "
        "MN0100427), Wikipedia (118 bpm), Chordify no áudio oficial e o Chordify na audição do "
        "Goodall — duas vezes (A·E·B·G#m, ~120 bpm): a cópia é real. O esqueleto MIDI (bitmidi "
        "63595) veio em Dó# maior (+3 semitons na importação) e NÃO tem pista de voz: a linha "
        "vocal foi transcrita de ouvido, validada por você (5 perguntas, 5 respostas), dentro das "
        "cercas do Hooktheory — verso B3–B4, strangers E4–B4, refrão E4–C#5, melodia 100% "
        "diatônica. Onde o esqueleto mente (e o disco venceu): strangers esticados em blocos de 2 "
        "compassos, solo sumido, bateria que atrasa, final que desacelera — o disco de 1981 "
        "termina frio. 🟡 Micro-checagens pendentes: o possível B4 fugaz no \u201cTRAIN\u201d e as "
        "caudas \u201con and on\u201d.")

    # ---------- como ler
    doc.add_heading("📖 Como ler o mapa", level=1)
    bullets(doc, [
        "Números = oitavas; C4 é o dó central. A voz mora entre o B3 (o fundão) e o C#5 (o pico).",
        "Célula = sílaba ↔ nota. MAIÚSCULAS = a sílaba em cima (o acento). → na nota = a sílaba "
        "continua soando (melisma) — é a mesma sílaba viajando.",
        "Notas em VERMELHO = o pico da voz (C#5, o \u201cbe-LIEV\u201d); em AZUL = o fundão (B3, "
        "o \u201cwhere\u201d — que é também a primeira nota do riff).",
        "A cama da mão esquerda é o LOOP E·B·C#m·A·E·B·G#m·A — um acorde por compasso, 8 "
        "compassos, a música inteira. Strangers = o desvio B7/A→A · Eadd9→E.",
        "O E5 é do solo de guitarra — o teto da música, mas não da voz: não force até lá.",
        "A audição do Goodall está NO MESMO TOM (Mi maior, ~120 bpm): dá pra tocar junto, do "
        "riff ao buzzer. 🔔",
    ])

    # ---------- teclado
    doc.add_heading("⌨️ Onde estão as notas (teclado-guia)", level=1)
    try:
        draw_keyboard(SAIDAS / "teclado-dsb.png")
        doc.add_picture(str(SAIDAS / "teclado-dsb.png"), width=Inches(6.7))
        doc.paragraphs[-1].alignment = 1
    except Exception as e:
        p = doc.add_paragraph(f"(Teclado-guia indisponível nesta geração: {e})")
        p.runs[0].font.color.rgb = MUTED
    sub(doc, "Dourado forte = o riff no bar do E (B3·E4·G#4·B4 + o C#5 de borda) · dourado suave = as "
             "outras voicings do riff · C#5 = o pico da voz · B4 = a rampa · B3 = o fundão · E5 "
             "cinza = o solo da guitarra. A música inteira mora em 11 teclas.")

    doc.paragraphs[-1].add_run().add_break(WD_BREAK.PAGE)

    # ---------- o riff
    doc.add_heading("🎹 O RIFF — a assinatura", level=1)
    sub(doc, "a mão que re-voza: quinta embaixo no E e no C#m, fundamental embaixo no B e no A")
    rt = doc.add_table(rows=len(gd.RIFF) + 1, cols=2)
    rt.style = "Table Grid"
    for ci, h in enumerate(("Acorde", "A mão direita (voicing)")):
        cell = rt.cell(0, ci)
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = GOLD
    for ri, (k, v) in enumerate(gd.RIFF.items(), 1):
        for ci, val in enumerate((k, v)):
            cell = rt.cell(ri, ci)
            run = cell.paragraphs[0].add_run(val)
            run.font.size = Pt(10.5)
            run.bold = True
            if ci == 0:
                run.font.color.rgb = GOLD
            else:
                run.font.name = "Consolas"
    rt.cell(0, 0).width = Inches(1.1)
    rt.cell(0, 1).width = Inches(5.6)
    for ri in range(1, len(gd.RIFF) + 1):
        rt.cell(ri, 0).width = Inches(1.1)
        rt.cell(ri, 1).width = Inches(5.6)
    box(doc, "Embaixo do riff, o trem",
        "8 compassos de intro = duas voltas do loop. Por baixo, o baixo: E1 (2 tempos) → F#1–G#1 "
        "→ B1 NO TEMPO 4 — cada acorde seguinte é lançado um tempo antes (veja a mão esquerda, "
        "no fim do mapa). No disco o riff abre sozinho; no AGT, foi ele que acendeu o Goodall.")

    # ---------- as seções
    doc.add_heading("🎤 As seções, frase a frase", level=1)
    sub(doc, "célula = sílaba ↔ nota · VERMELHO = pico (C#5) · AZUL = fundão (B3) · → = melisma · "
             "MAIÚSCULAS = o acento")

    doc.add_heading("INTRO · c1–8", level=2)
    sub(doc, "o riff do piano, sozinho — a assinatura da música inteira")
    box(doc, "Duas voltas do loop",
        "E · B · C#m · A · E · B · G#m · A. A voz só entra depois — e entra baixo. É o contraste "
        "que faz o lift funcionar: não empurre o verso.")

    doc.add_heading("V1a — \u201csmall town girl\u201d · c9–16", level=2)
    sub(doc, "o verso commuter: contido, quase falado — de propósito")
    grupo(doc, "V1")

    doc.add_heading("V1b — \u201ccity boy\u201d · c17–24", level=2)
    sub(doc, "a GÊMEA")
    box(doc, "V1b = V1a, nota a nota",
        "A mesma melodia, outra história — \u201cJust a city boy, born and raised in South "
        "Detroit…\u201d Treine uma, ganhe duas. Respire na virada: o público reconhece o caminho "
        "na segunda vez.")

    doc.add_heading("INTERLÚDIO · c25–32", level=2)
    sub(doc, "o riff volta a falar sozinho")
    box(doc, "A guitarra vai enchendo",
        "Ela entra 4 compassos depois e cresce compasso a compasso (a pista do esqueleto mostra "
        "os fills subindo) até o V2 chegar.")

    doc.add_heading("V2 — \u201csmoky room\u201d · c33–40", level=2)
    sub(doc, "o mapa do V1, emprestado + a cauda")
    box(doc, "A máquina dos versos é uma só",
        "\u201cA singer in a smoky room… a smell of wine and cheap perfume\u201d e \u201cfor a "
        "smile they can share the night\u201d = o MAPA DO V1, nota a nota. Abaixo, só a cauda nova:")
    grupo(doc, "V2_CAUDA")

    doc.add_heading("STRANGERS — a rampa · c41–52", level=2)
    sub(doc, "a única saída do loop: B7/A→A · B7/A→A · Eadd9→E · Eadd9→E  (+ a tag B5·E5 | "
             "B5·E5·A5 fechando)")
    grupo(doc, "STRANGERS")
    box(doc, "A harmonia sai dos trilhos",
        "O loop PARA — primeira e única vez — e o B7/A suspende tudo (o A grave embaixo do B7 é "
        "o cheiro desuspenso no ar). A tag B5·E5 | B5·E5·A5 é a terminação da seção: no teclado, "
        "duas oitavas de punho (essência da sua cifra A5–E5).")

    doc.add_heading("V3a + V3b · c53–68", level=2)
    sub(doc, "de novo o mapa do V1 + a cauda")
    box(doc, "Mais duas voltas da máquina",
        "\u201cWorking hard to get my fill, everybody wants a thrill…\u201d (V3a) e \u201cSome "
        "will win, some will lose…\u201d (V3b) = o MAPA DO V1, com a mesma cauda \u201con and "
        "on\u201d fechando o V3b. No Goodall essa página nem abre: o corte da audição pula direto "
        "dos strangers pro refrão.")

    doc.add_heading("STRANGERS 2 · c69–80", level=2)
    sub(doc, "a segunda volta")
    box(doc, "STRANGERS 2 = STRANGERS 1, nota a nota",
        "E a segunda vez você já conhece o caminho: o chant em B4, o \u201cDOWN\u201d que pica, a "
        "rampa do \u201cin the NIGHT\u201d segurando o B4…")

    doc.add_heading("SOLO · c81–88", level=2)
    sub(doc, "a guitarra canta o refrão — mais alto")
    box(doc, "O E5 é do violão",
        "A guitarra cita o CONTORNO do refrão e sobe ao E5 — o teto da música. No mapa da voz o "
        "E5 não existe: é o violão falando. (Foi um piano-solo de referência que entregou isso: a "
        "região que parecia refrão era o solo.) A cama continua sendo o loop — acompanhe com a "
        "mão esquerda e a guitarra por cima.")

    doc.add_heading("REFRÃO — \u201cDon\u2019t stop believ\u2019in\u2019\u201d · c89–116", level=2)
    sub(doc, "no MESMO loop do verso — a altura é que mudou · ×3 no disco")
    grupo(doc, "REFRAO")
    box(doc, "A famosa espera",
        "O refrão só chega aos 3min20 dos 4min11: o loop girou 10 voltas antes de a voz subir ao "
        "C#5. A terceira vez corta direto pro tag — sem pausa, sem fade.")

    doc.add_heading("TAG · c117–123", level=2)
    sub(doc, "a terminação fria")
    grupo(doc, "TAG")

    doc.paragraphs[-1].add_run().add_break(WD_BREAK.PAGE)

    # ---------- camada goodall
    doc.add_heading("🔔 A camada Goodall — a audição que copiou o disco", level=1)
    sub(doc, "AGT S19, 28/05/2024 · a performance que fechou a estreia da temporada")
    tl = doc.add_paragraph()
    tl.paragraph_format.space_after = Pt(4)
    for i, c in enumerate(gd.GOODALL["corte"]):
        if i:
            s = tl.add_run("  →  ")
            s.bold = True
            s.font.color.rgb = GOLD
        r = tl.add_run(c)
        r.bold = True
        r.font.size = Pt(11)
        r.font.color.rgb = INK
    pc = doc.add_paragraph()
    rc = pc.add_run("Cortes do TV: ")
    rc.bold = True
    rc.font.size = Pt(10)
    rc.font.color.rgb = INK
    for i, c in enumerate(gd.GOODALL["cortados"]):
        if i:
            sep = pc.add_run(" · ")
            sep.font.color.rgb = MUTED
        rs = pc.add_run(c)
        rs.font.strike = True
        rs.italic = True
        rs.font.size = Pt(10)
        rs.font.color.rgb = MUTED
    box(doc, "A cópia, provada",
        "O Chordify ouviu a audição duas vezes — Mi maior, ~120 bpm, A·E·B·G#m: mesmo tom, mesmo "
        "tempo, mesmo loop do disco de 1981. A voz é de barítono claro e forte (a bio oficial "
        "dele) — cantando a parte de um tenor, Steve Perry, no tom original. O momento em que a "
        "montanha aparece é o C#5 do \u201cbe-LIEV\u201d: o barítono no tenro do Perry, a plateia "
        "de pé, e o buzzer dourado da Heidi Klum. Em setembro ele venceu a temporada — e cantou "
        "essa música na final com o próprio Journey.", fill=GOLDB, icon="🔔")

    # ---------- mão esquerda
    doc.add_heading("🖐️ A mão esquerda — o trem", level=1)
    sub(doc, "a caminhada do baixo por acorde do loop (lida do esqueleto, compasso a compasso)")
    lt = doc.add_table(rows=len(gd.BAIXO) + 1, cols=2)
    lt.style = "Table Grid"
    for ci, h in enumerate(("Acorde", "A caminhada")):
        run = lt.cell(0, ci).paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = GOLD
    for ri, (k, v) in enumerate(gd.BAIXO.items(), 1):
        c0, c1 = lt.cell(ri, 0), lt.cell(ri, 1)
        r0 = c0.paragraphs[0].add_run(k)
        r0.bold = True
        r0.font.size = Pt(10)
        r0.font.color.rgb = GOLD
        r1 = c1.paragraphs[0].add_run(v)
        r1.font.size = Pt(10)
        r1.font.name = "Consolas"
        c0.width = Inches(0.9)
        c1.width = Inches(5.8)
    box(doc, "A regra de ouro",
        "O tempo 4 lança o acorde seguinte — é isso que faz a música andar de trem. Enquanto a "
        "direita faz o riff, a esquerda empurra. Nos Strangers, o baixo para junto: A sustentado "
        "sob o B7/A, e o Eadd9 resolving no E.")

    # ---------- costuras
    doc.add_heading("🧵 As costuras — onde a música vira", level=1)
    numlist(doc, [
        ("INTRO → V1a: ", "o riff abre espaço e a voz entra quase falada. Não empurre o verso — "
         "o contraste é o que faz o lift funcionar."),
        ("V1a → V1b: ", "a gêmea — mesma melodia, outra história. Respire na virada; o público "
         "reconhece o caminho na segunda vez."),
        ("V1b → INTERLÚDIO → V2: ", "o riff volta sozinho, a guitarra entra 4 compassos depois, "
         "e o V2 devolve o mapa do V1 com a cauda \u201con and on\u201d."),
        ("V2 → STRANGERS: ", "a única dobra harmônica da música — o loop para e o B7/A→A "
         "suspende tudo. Primeira vez que a harmonia sai dos trilhos."),
        ("STRANGERS → REFRÃO: ", "a rampa — o \u201cin the NIGHT\u201d segura o B4 e solta o "
         "refrão no C#5. É a maior subida de um compasso só da música."),
        ("REFRÃO → TAG: ", "o disco termina frio: \u201cDon\u2019t stop!\u201d corta seco. Sem "
         "fade, sem desacelerar (o esqueleto desacelera — licença do arranjador; o disco não)."),
    ])

    # ---------- guia de montagem
    doc.add_heading("🗺️ Guia de montagem — a música inteira, de ponta a ponta", level=1)
    sub(doc, "≈123 compassos, ~4min11 · os números de compasso são os do consenso das fontes · a "
             "letra entre aspas é a deixa: ouviu a deixa, é aquela seção")
    cama_txt = lambda cama: ("loop E·B·C#m·A·E·B·G#m·A" if cama == gd.LOOP else
                             "B7/A→A ×2 · Eadd9→E ×2 + tag" if cama == gd.STRANGERS else
                             " · ".join(cama))
    gt = doc.add_table(rows=len(gd.ESTRUTURA) + 1, cols=5)
    gt.style = "Table Grid"
    gw = [Inches(1.15), Inches(0.8), Inches(2.95), Inches(1.8)]
    for ci, h in enumerate(("#", "Comp.", "A deixa", "A cama")):
        cell = gt.cell(0, ci)
        cell.width = gw[ci]
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = GOLD
    for ri, (nome, ini, fim, deixa, cama) in enumerate(gd.ESTRUTURA, 1):
        vals = (nome, f"c{ini}–{fim}", deixa, cama_txt(cama))
        for ci, val in enumerate(vals):
            cell = gt.cell(ri, ci)
            cell.width = gw[ci]
            run = cell.paragraphs[0].add_run(val)
            run.font.size = Pt(8.5)
            if ci == 0:
                run.bold = True

    doc.add_heading("A ordem de estudar — do trem ao palco, em oito passos", level=2)
    numlist(doc, [
        ("O trem na mão esquerda — ", "o loop com as antecipações do tempo 4, até automatizar."),
        ("O riff — ", "a mão que re-voza: B3-E4-G#4 / B3-D#4-F#4 / G#3-C#4-E4 / A3-C#4-E4 "
         "(+ o G#m)."),
        ("V1a + V1b — ", "a gêmea: treine uma, ganhe duas."),
        ("Os STRANGERS — ", "o B7/A→A e o Eadd9→E; o chant em B4; a rampa do \u201cnight\u201d."),
        ("O REFRÃO — ", "o C#5 do \u201cbe-LIEV\u201d e a escada de resposta."),
        ("V2 e V3 — ", "os mapas emprestados + as caudas \u201con and on\u201d."),
        ("A montagem inteira — ", "na ordem do disco, com o interlúdio e o solo de recorte."),
        ("A camada Goodall — ", "toque junto com a audição: é o mesmo tom, dá pra acompanhar do "
         "início ao buzzer. 🔔"),
    ])

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
        "Fontes: Musicnotes MN0100427 (partitura oficial, Mi maior) · Wikipedia (118 bpm) · "
        "Chordify no áudio oficial + ×2 na audição Goodall (Mi, ~120 bpm) · Hooktheory (cercas "
        "melódicas) · spytunes · tucuatro · thesingingjanitor.com (barítono) · esqueleto: bitmidi "
        "63595 (Dó# maior, +3st, sem voz) · piano de referência: bitmidi 14642 · cifra do usuário "
        "(cifra-usuario-dsb.txt) — auditada e aprovada.  ·  Validação: melodia validada pelo "
        "ouvido do usuário (5/5) · sanity 7/7 · harmonia em consenso de 7 fontes.  ·  Regenera: "
        "python3 04-dont-stop-believin/trabalho/gera_dsb_docx.py — os dados moram em gera_dsb.py, a fonte única de verdade.")
    fr.font.size = Pt(8)
    fr.font.color.rgb = MUTED

    doc.core_properties.title = "Mapa Musical — Don't Stop Believin' (Mi maior · versão Richard Goodall)"
    doc.core_properties.author = "Fábrica gera_dsb.py + gera_dsb_docx.py"
    doc.save(SAIDAS / "mapa-musical-dont-stop-believin.docx")
    return doc


# ── saídas: a pasta ../saidas desta música (a fábrica roda de qualquer lugar) ──
from pathlib import Path as _P
SAIDAS = _P(__file__).resolve().parent.parent / "saidas"
SAIDAS.mkdir(exist_ok=True)

if __name__ == "__main__":
    doc = build()
    # sanity do próprio DOCX: reabre e confere
    d2 = Document(SAIDAS / "mapa-musical-dont-stop-believin.docx")
    n_h1 = sum(1 for p in d2.paragraphs if p.style.name == "Heading 1")
    n_h2 = sum(1 for p in d2.paragraphs if p.style.name == "Heading 2")
    n_tbl = len(d2.tables)
    n_frases = sum(len(v) for v in gd.FRASES.values())
    print("═" * 74)
    print(f"DOCX: mapa-musical-dont-stop-believin.docx")
    print(f"  H1: {n_h1} · H2 (seções): {n_h2} · tabelas: {n_tbl} "
          f"(frases {n_frases} + riff + trem + guia)")
    ok = n_tbl == n_frases + 3 and n_h1 == 10 and n_h2 == 12 and len(d2.inline_shapes) == 1
    print(f"  [{'✓' if ok else '✗'}] estrutura esperada")
    raise SystemExit(0 if ok else 1)
