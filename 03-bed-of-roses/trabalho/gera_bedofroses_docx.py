#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera mapa-musical-bed-of-roses.docx a partir dos dados de gera_bedofroses.py
(fonte única de verdade — nenhuma transcrição manual das notas).

Requer:  pip install python-docx pillow
Roda:    python3 03-bed-of-roses/trabalho/gera_bedofroses_docx.py
Saída:   mapa-musical-bed-of-roses.docx (A4, editável, uma tabela por frase)

Organização do documento (pensada pro ATRIL e pra anotação à mão):
  • Cada FRASE é uma tabela independente em GRADE DE TEMPOS do 12/8:
    linhas Acorde / Tempo / Sílaba / Nota; cada tempo grande = células
    mescladas no cabeçalho, com até 3 tercinas lado a lado; coluna "e" =
    anacruze. Pra encurtar, é só apagar tabelas ou linhas.
  • Seções = "Heading 1" — navega no painel do Word e gera sumário automático.
  • Notas em VERMELHO = o pico da frase (mesma convenção do HTML).
  • TOM: FÁ MAIOR (o disco, a partitura oficial e o single 2019 do Matthias).
    A gêmea meio tom acima (Fá#) existe em HTML; a fábrica transpõe num comando.
"""
import gera_bedofroses as gb
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------------------------------------------------------------- cores (veludo vermelho em papel)
INK   = RGBColor(0x33, 0x27, 0x2B)
DARK  = RGBColor(0x6B, 0x24, 0x34)   # títulos (vinho)
ROSE  = RGBColor(0xA8, 0x3A, 0x52)   # notas (rosa)
GOLD  = RGBColor(0x8A, 0x6D, 0x2F)   # acordes / rótulos (dourado)
LHC   = RGBColor(0xB0, 0x7F, 0x2E)   # a cama
PEAK  = RGBColor(0xC0, 0x39, 0x2B)   # o pico (vermelho da casa)
MUTED = RGBColor(0x8A, 0x7A, 0x80)
NOTE  = RGBColor(0x5A, 0x4A, 0x50)
CREAM = "FCEFEF"

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
    r.font.color.rgb = DARK
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


# ---------------------------------------------------------------- frase (grade 12/8) → tabela
def add_frase(doc, p, fallback_label):
    label = p.get("label") or fallback_label
    lp = doc.add_paragraph()
    lp.paragraph_format.space_before = Pt(10)
    lp.paragraph_format.space_after = Pt(2)
    lr = lp.add_run("◆ " + label)
    lr.bold = True
    lr.font.size = Pt(9.5)
    lr.font.color.rgb = MUTED

    beats = p["beats"]
    anac = p.get("anac")
    peak = p.get("peak")
    chords_at = {i: c for c, i in p["chords"]}          # i = tempo (1-based)

    grupos = []                                          # (chave, [(sílaba, nota), …])
    if anac:
        grupos.append(("e", [anac]))
    for bi, b in enumerate(beats, 1):
        grupos.append((bi, b if b else [("·", "·")]))

    ncols = sum(len(pares) for _, pares in grupos)
    tbl = doc.add_table(rows=4, cols=ncols + 1)
    tbl.style = "Table Grid"

    c0 = 1
    for chave, pares in grupos:
        span = len(pares)
        last = c0 + span - 1
        if span > 1:
            cell_ch = tbl.cell(0, c0).merge(tbl.cell(0, last))
            cell_tp = tbl.cell(1, c0).merge(tbl.cell(1, last))
        else:
            cell_ch = tbl.cell(0, c0)
            cell_tp = tbl.cell(1, c0)
        ch = "" if chave == "e" else chords_at.get(chave, "")
        rch = cell_ch.paragraphs[0].add_run(ch)
        rch.bold = True
        rch.italic = True
        rch.font.size = Pt(9.5)
        rch.font.color.rgb = GOLD if ch else MUTED
        cell_ch.paragraphs[0].paragraph_format.space_after = Pt(0)
        rtp = cell_tp.paragraphs[0].add_run(str(chave))
        rtp.bold = True
        rtp.font.size = Pt(8)
        rtp.font.color.rgb = MUTED
        rtp.italic = chave == "e"
        cell_tp.paragraphs[0].paragraph_format.space_after = Pt(0)
        for pi, (sy, no) in enumerate(pares):
            is_peak = bool(peak) and chave != "e" and (chave, pi) == peak
            cs = tbl.cell(2, c0 + pi).paragraphs[0]
            cs.paragraph_format.space_after = Pt(0)
            rs = cs.add_run(sy)
            rs.font.size = Pt(10 if ncols <= 10 else 9.5)
            if sy == "·":
                rs.font.color.rgb = MUTED
            else:
                rs.bold = True
                rs.font.color.rgb = INK if not is_peak else PEAK
            cn = tbl.cell(3, c0 + pi).paragraphs[0]
            cn.paragraph_format.space_after = Pt(0)
            rn = cn.add_run(no)
            rn.font.name = "Consolas"
            rn.font.size = Pt(10 if ncols <= 10 else 9)
            if no == "·":
                rn.italic = True
                rn.font.color.rgb = MUTED
            elif is_peak:
                rn.bold = True
                rn.font.color.rgb = PEAK
            else:
                rn.bold = True
                rn.font.color.rgb = ROSE
        c0 += span

    for ri, rot in enumerate(("Acorde", "Tempo", "Sílaba", "Nota")):
        c0c = tbl.cell(ri, 0).paragraphs[0]
        c0c.paragraph_format.space_after = Pt(0)
        r0 = c0c.add_run(rot)
        r0.bold = True
        r0.font.size = Pt(8)
        r0.font.color.rgb = MUTED

    tbl.autofit = False
    total, first = 6.7, 0.85
    wcol = (total - first) / ncols
    for ri in range(4):
        tbl.cell(ri, 0).width = Inches(first)
    c0 = 1
    for chave, pares in grupos:
        span = len(pares)
        for ri in range(4):
            if span > 1 and ri in (0, 1):
                tbl.cell(ri, c0).width = Inches(wcol * span)
            else:
                for k in range(span):
                    tbl.cell(ri, c0 + k).width = Inches(wcol)
        c0 += span

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
    GEO = {"Bb": "A#", "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#"}
    geo = lambda n: GEO.get(n[:-1], n[:-1]) + n[-1]
    mel_orig = gb._all_note_names() - gb.LH_NOTES
    lh_orig = set(gb.LH_NOTES)
    disp = {geo(n): n for n in mel_orig}          # nome exibido (soletração em Fá)
    disp.update({geo(n): n for n in lh_orig})     # a cama vence
    mel = {geo(n) for n in mel_orig}
    lh = {geo(n) for n in lh_orig}
    WHITE = ["C", "D", "E", "F", "G", "A", "B"]
    BLACK = {"C": "C#", "D": "D#", "F": "F#", "G": "G#", "A": "A#"}
    W, H, BW, BH, M = 62, 200, 36, 124, 16
    y0 = 86
    n_white = 7 * 4                                     # C2..B5
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
    for octv in range(2, 6):
        for wname in WHITE:
            label = f"{wname}{octv}"
            if label in lh:
                fill, tcol, txt = "#F3E3C2", "#8a6d2f", disp.get(label, label)
            elif label in mel:
                fill, tcol, txt = "#F2C7D2", "#A83A52", disp.get(label, label)
            else:
                fill, tcol, txt = "#ffffff", None, None
            d.rectangle([x, y0, x + W - 2, y0 + H - 1], fill=fill, outline="#8d9aa8", width=2)
            if txt:
                center(x + (W - 2) / 2, y0 + H - 26, txt, f_key, tcol)
            if wname == "C":
                center(x + (W - 2) / 2, y0 + H - 8, label, font(12, bold=False), "#a58a80")
            if label == "C4":
                cx = x + (W - 2) / 2
                d.ellipse([cx - 7, y0 + 118, cx + 7, y0 + 132], fill="#d8a84e")
                center(cx, y0 + 108, "dó central", font(12, bold=False), "#b07f2e")
            if wname in BLACK:
                bl = f"{BLACK[wname]}{octv}"
                bx = x + W - BW // 2 - 1
                if bl in lh:
                    bfill, btxt, btcol = "#B07F2E", disp.get(bl, bl), "#241505"
                elif bl in mel:
                    bfill, btxt, btcol = "#C2425E", disp.get(bl, bl), "#ffffff"
                else:
                    bfill, btxt, btcol = "#2b2528", None, "#fff"
                d.rectangle([bx, y0, bx + BW - 1, y0 + BH - 1], fill=bfill, outline="#14171b", width=2)
                if btxt:
                    center(bx + BW / 2, y0 + BH - 14, btxt, font(11), btcol)
                x_pos[bl] = bx
            x_pos[label] = x
            x += W

    def callout(key, txt, ty, col):
        c = x_pos[key] + (BW / 2 if "#" in key else (W - 2) / 2)
        f = font(14)
        bb = d.textbbox((0, 0), txt, font=f)
        d.line([c, ty + 12, c, y0 - 3], fill=col, width=1)
        d.text((c - (bb[2] - bb[0]) / 2, ty), txt, font=f, fill=col)

    callout("F5", "o gancho — F5", 40, "#A83A52")
    callout("D5", "a rosa — D5 (a terça do Bb)", 14, "#8a6d2f")
    callout(geo("Bb5"), "▲ o teto — Bb5 (\u201cCLOSE\u201d)", 14, "#C0392B")

    ly = y0 + H + 22
    lx = M
    for fill, lab in (("#F2C7D2", "melodia (F4–Bb5)"), ("#F3E3C2", "cama (mão esquerda)")):
        d.rectangle([lx, ly, lx + 26, ly + 16], fill=fill, outline="#8d9aa8")
        d.text((lx + 32, ly), lab, font=f_leg, fill="#4a3a40")
        lx += 32 + d.textlength(lab, font=f_leg) + 22
    d.ellipse([lx + 4, ly + 2, lx + 18, ly + 16], fill="#d8a84e")
    d.text((lx + 26, ly), "C4 = dó central", font=f_leg, fill="#4a3a40")
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
    doc.add_heading("🌹 Mapa Musical — Bed of Roses", level=0)
    sub(doc, "Bon Jovi · versão Matthias Nebel — The Voice of Germany, 18/10/2018 · nota a nota, "
             "do rocking Bb↔F à rosa segurada no bis", 11)
    badges = doc.add_paragraph()
    rb = badges.add_run("3min09 + Zugabe   ·   25 frases · 7 seções   ·   Tom: FÁ MAIOR (esqueleto "
                        "−1st)   ·   Grade: 12/8 lento   ·   Teto: Bb5 no \u201cCLOSE\u201d   ·   "
                        "Esqueleto: MIDI do original, bitmidi 19001")
    rb.font.size = Pt(9)
    rb.font.color.rgb = MUTED

    # ---------- como ler
    doc.add_heading("📖 Como ler o mapa", level=1)
    bullets(doc, [
        "Cada tabela é uma frase em GRADE DE TEMPOS do 12/8: as colunas são agrupadas por tempo "
        "grande (1, 2, 3, 4), com até 3 tercinas lado a lado dentro de cada tempo.",
        "A linha \u201cAcorde\u201d marca o acorde que entra naquele tempo; a coluna \u201ce\u201d "
        "é o anacruze (a sílaba que entra antes do tempo 1).",
        "→ nota comprida, que segue soando enquanto a frase anda · › notas ligadas na mesma "
        "sílaba · · silêncio (a nota anterior segue se tinha →).",
        "Sílabas novas sobre uma nota com → = CAVALGAM a nota segurada (re-articulam na mesma "
        "altura).",
        "Notas em VERMELHO = o pico da frase (o teto Bb5 do \u201cCLOSE\u201d, o F5 do gancho…).",
        "A numeração de compassos é a do esqueleto MIDI — no corte de TV as contagens variam, a "
        "estrutura relativa é idêntica.",
    ])
    box(doc, "Transparência da afinação",
        "O esqueleto (MIDI do original) foi gravado 1 semitom acima do disco (Fá# maior); o mapa "
        "já chega transposto −1st para FÁ MAIOR — o tom do disco (partitura oficial: \u201cOriginal "
        "Published Key: F Major\u201d) e do single 2019 do Matthias. Se ao tocar com o clipe soar "
        "1 semitom deslocado, a fábrica transpõe o mapa inteiro num comando: o desenho não muda "
        "um milímetro. A gêmea meio tom acima (Fá#, o tom nativo do esqueleto) já existe em HTML: "
        "mapa-musical-bed-of-roses-fasustenido.html.")

    box(doc, "Como este mapa foi feito (a Prova de Conceito nº 3)",
        "Um ao vivo de TV, sem MIDI próprio — o problema mais duro da série. Três pilares: "
        "esqueleto = MIDI do original do Bon Jovi (transposto −1st); estrutura = o transcript "
        "oficial do corte de TV (o que sobreviveu aos 3min09 — sem o V3 \u201cso far away\u201d, "
        "bridge ou solo); tom = triangulação de 4 fontes (Musicnotes, Chordify ×2, GuitarTuna). E "
        "a ferramenta nova do bis: o transcript como detector de ad-lib — cada palavra que o ASR "
        "engoliu caiu em cima de um melisma real do esqueleto (zonas A, B e C). Três vezes a "
        "fábrica corrigiu o palpite com dados: o pico do V2 (\u201cthat I long\u201d), o teto no "
        "\u201cCLOSE\u201d (não no \u201cGHOST\u201d) e o plano do bis inteiro (reciclagem → o "
        "refrão já decorado do esqueleto, c. 44–49).", icon="🎭")

    # ---------- teclado
    doc.add_heading("🎼 Onde estão as notas (teclado-guia)", level=1)
    try:
        draw_keyboard(SAIDAS / "teclado-bor.png")
        doc.add_picture(str(SAIDAS / "teclado-bor.png"), width=Inches(6.7))
        doc.paragraphs[-1].alignment = 1
    except Exception as e:
        p = doc.add_paragraph(f"(Teclado-guia indisponível nesta geração: {e})")
        p.runs[0].font.color.rgb = MUTED
    sub(doc, "Rosa = melodia e figuras do mapa (do F4 do \u201cown\u201d ao Bb5 do teto). Dourado "
             "= a cama da mão esquerda (a escada Bb2·C2·D2·E2·F2 + os corpos da moldura da intro). "
             "O ponto dourado é o dó central. E os três apontamentos: o gancho F5, a rosa D5 (a "
             "terça do Bb — a nota-cor do rocking) e o teto Bb5.")

    doc.paragraphs[-1].add_run().add_break(WD_BREAK.PAGE)

    # ---------- seções
    secao(doc, "🎹 INTRO — o rocking (esqueleto c. 3–10 · no clipe: encurtado, sob a conversa "
               "dos coaches)",
          gb.INTRO_NOTA,
          "Bb6 (Bb3+D4+F4) ↔ Fadd9 (A3+C4+F4) — o par que moldura a música inteira.",
          gb.INTRO, gb.INTRO_FILLS)

    secao(doc, "🎤 VERSO 1 — \u201cSittin' here wasted…\u201d (esqueleto c. 11–19 · 5 frases · "
               "71 sílabas)",
          gb.V1_NOTA, gb.CAMA_V1, gb.V1, gb.V1_FILLS)

    secao(doc, "🎤 VERSO 2 — \u201cWith an ironclad fist…\u201d (esqueleto c. 20–26 · 5 frases · "
               "63 sílabas · o chão abre)",
          gb.V2_NOTA, gb.CAMA_V2, gb.V2, gb.V2_FILLS)

    secao(doc, "🕯️ REFRAO 1 — \u201cI wanna lay you down…\u201d (esqueleto c. 27–29 · a meia-voz "
               "antes da tempestade)",
          gb.CH1_NOTA, gb.CAMA_CH1, gb.CH1, gb.CH1_FILLS)

    secao(doc, "🛫 LIFT — a RAMPA do corte de TV (reprise das frases do V2 · a banda sobe)",
          gb.LIFT_NOTA,
          "a cama do V2 (F/A → Bb → F — o chão aberto): a rampa sobe por cima dela.",
          gb.LIFT, gb.LIFT_FILLS)

    secao(doc, "⛈️ REFRAO 2 — o refrão inteiro, a tempestade (esqueleto c. 27–33 · 4 linhas · "
               "o teto Bb5)",
          gb.CH2_NOTA, gb.CAMA_CH2, gb.CH2, gb.CH2_FILLS)

    box(doc, "A assinatura da música: \u201ca nota não se mexe — só muda de função\u201d",
        "Quatro execuções da mesma jogada, uma por seção — a altura permanece, o acorde embaixo "
        "troca de cor:  1) V1: o F5 do \u201cvot-ka's\u201d — a nota segue enquanto a cama "
        "escurece.  2) V2: o F5 do \u201cthat I\u201d — de novo: mesma altura, nova função.  "
        "3) REFRAO 1: o F5 do \u201cof\u201d — chega como 4ª suspensa sobre o C/E e só vira nota "
        "do acorde (3ª) quando o Dm chega.  4) O TETO: o Bb5 do \u201cCLOSE\u201d chega como 7ª "
        "sobre o C/E e vira FUNDAMENTAL quando o Bb chega — a assinatura no seu mais alto nível. "
        "E no bis, a jogada comprimida: o Bb5 já chega fundamental (o baixo em F: Bb/F).",
        icon="🔑")

    secao(doc, "🌹 ZUGABE — o BIS que fecha os 3min09 (refrão decorado c. 44–49 + final c. 87–91 "
               "· zonas de ad-lib + o tag \u201cLAY YOU DOWN\u201d)",
          gb.ZUGABE_NOTA, gb.CAMA_ZUGABE, gb.ZUGABE, gb.ZUGABE_FILLS)

    box(doc, "O clipe em uma frase",
        "A moldura é o rocking Bb↔F da intro; a voz entra no Bb4, promete no F5 (\u201cin a bed "
        "of RO-ses\u201d), a TV inventa uma rampa por cima dos versos, a banda explode no refrão "
        "com o teto Bb5 no \u201cCLOSE\u201d — e o bis devolve tudo decorado: o gancho vira 8 F5, "
        "o \u201cHO\u201d vira corrida, a música segura a rosa (D5, a terça do Bb) e o último "
        "\u201cdown\u201d afunda até o F4 — a mesma nota onde o primeiro \u201cdown\u201d "
        "resolveu. Começa e termina nos mesmos dois acordes.")

    box(doc, "Reciclagens da casa (por que o mapa é menor que a música)",
        "LIFT = as frases do V2 com papel novo (alavanca, não clímax). REFRAO 2, linhas 1-2 = o "
        "mapa da meia-voz, nota por nota. ZUGABE, linhas 1-2 = o refrão decorado do esqueleto.",
        icon="♻️")

    # ---------- mão esquerda
    doc.add_heading("🖐️ Mão esquerda (a cama)", level=1)
    p = doc.add_paragraph("Comece simples — só o baixo, um por acorde, bem fraquinho:")
    p.runs[0].font.size = Pt(10)
    LH_ROWS = [
        ("Bb", "Bb2", "+ Bb3+D4+F4 (o Bb6 da intro)", "a casa — intro, versos, refrão, final"),
        ("F/A", "A2", "+ F3", "a 3ª no baixo — verso 1"),
        ("Fsus2", "F2", "+ G3", "a névoa — verso 1"),
        ("F", "F2", "+ A3+C4+F4 (o Fadd9)", "a tônica — versos, refrão, final"),
        ("C", "C2", "—", "o degrau da escada — refrão"),
        ("C/E", "E2", "+ C3+G3 na direita", "o escurecimento — refrão (\u201cin a bed…\u201d)"),
        ("Dm", "D2", "—", "a sombra — refrão"),
        ("Bb/F", "F2", "+ Bb2", "o bis — o teto já chega fundamental"),
    ]
    lt = doc.add_table(rows=len(LH_ROWS) + 1, cols=4)
    lt.style = "Table Grid"
    lw = [Inches(0.7), Inches(0.7), Inches(2.2), Inches(3.1)]
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
    box(doc, "A escada do refrão",
        "SOBE Bb2→C2→F2 (\u201cI wanna lay you DOWN\u201d — a palavra resolve na tônica), "
        "escurece E2→D2, DESCE C2→Bb2→F2 (\u201cfor tonight…\u201d). E a moldura de sempre: os "
        "dois acordes da intro balançando — o refrão é a intro com letra.")

    # ---------- costuras
    doc.add_heading("🧵 As 7 costuras — onde tudo se encaixa", level=1)
    numlist(doc, [
        ("Intro → V1: ", "a escadinha do piano entrega a voz exatamente no Bb4 (c. 11)."),
        ("V1 → V2: ", "o chão abre — o baixo sai das inversões (F/A) e mora na fundamental (F2)."),
        ("V2 → Refrão 1: ", "o refrão entra A MEIA-VOZ — a promessa antes da tempestade."),
        ("Refrão 1 → Lift: ", "a meia-voz vira rampa — e o [cheering] do transcript estoura no "
         "\u201cthat I long\u201d."),
        ("Lift → Refrão 2: ", "o monólito C5 do \u201cnails\u201d termina exatamente onde o "
         "\u201cOH\u201d do teto vai saltar — o trampolim está no lugar."),
        ("Refrão 2 → Zugabe: ", "no esqueleto viria o V3 \u201cso far away\u201d (c. 34) — o "
         "corte de TV troca pelo aplauso… e o bis volta ao refrão."),
        ("O fim: ", "a rosa D5→ segurada quase um compasso… e o tag \u201cLAY YOU DOWN\u201d "
         "afunda até o F4 — a mesma nota onde o primeiro \u201cdown\u201d resolveu. O círculo "
         "fecha."),
    ])

    # ---------- como estudar
    doc.add_heading("✈️ Como estudar", level=1)
    numlist(doc, [
        ("A moldura primeiro: ", "Bb↔F rocking — quem aprende a intro já sabe o balanço do "
         "refrão e o final (os mesmos dois acordes abrem e fecham a música)."),
        ("O gancho: ", "os F5 do \u201cin a bed of RO-ses\u201d — a nota da música. No bis ela "
         "vira oito."),
        ("A escada na esquerda: ", "sobe Bb2→C2→F2, desce C2→Bb2→F2 — um compasso de cada, até "
         "virar músculo."),
        ("Os versos: ", "71 + 63 sílabas — cante com o transcript do clipe (é o teste de "
         "sincronia)."),
        ("O teto: ", "Bb5 no \u201cCLOSE\u201d — o A5 cavalgado antes é o trampolim; não gaste "
         "tudo no \u201cGHOST\u201d."),
        ("O bis: ", "as zonas A/B/C — onde o ASR engole palavra, você põe melisma (a corrida "
         "A5›G5›F5›A5 já está no mapa)."),
        ("Costure por último ", "(a lista das 7 acima) e grave-se tocando com o clipe. 🎹"),
    ])

    # ---------- guia de montagem
    doc.add_heading("🗺️ Guia de montagem — o clipe inteiro, de ponta a ponta", level=1)
    sub(doc, "3min09 de clipe sobre 91 compassos de esqueleto. A numeração é a do MIDI do "
             "original — o corte de TV encurta a intro e pula do refrão direto ao aplauso; a "
             "estrutura relativa frase-a-frase é idêntica. A letra entre aspas é a deixa.")
    gt = doc.add_table(rows=len(gb.GUIDE_BOR) + 1, cols=6)
    gt.style = "Table Grid"
    gw = [Inches(0.3), Inches(1.15), Inches(2.15), Inches(1.6), Inches(0.65), Inches(0.85)]
    for ci, h in enumerate(("#", "Seção", "Como reconhece", "Acordes", "No mapa",
                            "Comp. (esq.)")):
        cell = gt.cell(0, ci)
        cell.width = gw[ci]
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = GOLD
    for ri, (n, como, ac, mp, comp) in enumerate(gb.GUIDE_BOR, 1):
        for ci, val in enumerate((str(ri), n, como, ac, mp, comp)):
            cell = gt.cell(ri, ci)
            cell.width = gw[ci]
            run = cell.paragraphs[0].add_run(val)
            run.font.size = Pt(8.5)
            if ci == 1:
                run.bold = True

    box(doc, "Status do projeto",
        "Toda a audição está mapeada: intro, os dois versos, o refrão a meia-voz, a rampa de TV, "
        "o refrão da banda com o teto e o bis com as zonas de ad-lib — 25 frases nota a nota. "
        "Transparências registradas no caminho: a transposição −1st, a meia-voz engolindo o "
        "\u201cI wanna\u201d, as duas leituras do \u201cGHO-O-OST\u201d (as mesmas notas), a "
        "rampa do LIFT (invenção do corte de TV) e o salto c. 44→c. 87 do bis. Nada ficou "
        "pendente.", icon="🏆")

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
        "Mapa conferido nota a nota com o esqueleto MIDI do original (bitmidi.com/uploads/19001, "
        "Fá# maior, −1st = Fá), triangulado com a partitura oficial Musicnotes (\u201cOriginal "
        "Published Key: F Major\u201d), Chordify ×2 e GuitarTuna; estrutura = transcript oficial "
        "do corte de TV (The Voice of Germany, 18/10/2018); single 2019 do Matthias Nebel "
        "(Spotify/YouTube) no mesmo tom. A gêmea meio tom acima (Fá#, o tom nativo do esqueleto): "
        "mapa-musical-bed-of-roses-fasustenido.html.  ·  Regenera: python3 "
        "gera_bedofroses_docx.py — os dados moram em gera_bedofroses.py, a fonte única de "
        "verdade.")
    fr.font.size = Pt(8)
    fr.font.color.rgb = MUTED

    doc.core_properties.title = "Mapa Musical — Bed of Roses (Bon Jovi · versão Matthias Nebel)"
    doc.core_properties.author = "Fábrica gera_bedofroses.py + gera_bedofroses_docx.py"
    doc.save(SAIDAS / "mapa-musical-bed-of-roses.docx")
    return doc


# ── saídas: a pasta ../saidas desta música (a fábrica roda de qualquer lugar) ──
from pathlib import Path as _P
SAIDAS = _P(__file__).resolve().parent.parent / "saidas"
SAIDAS.mkdir(exist_ok=True)

if __name__ == "__main__":
    doc = build()
    d2 = Document(SAIDAS / "mapa-musical-bed-of-roses.docx")
    n_h1 = sum(1 for p in d2.paragraphs if p.style.name == "Heading 1")
    n_tbl = len(d2.tables)
    n_frases = sum(len(v) for v in (gb.INTRO, gb.V1, gb.V2, gb.CH1, gb.LIFT, gb.CH2, gb.ZUGABE))
    print("═" * 74)
    print("DOCX: mapa-musical-bed-of-roses.docx")
    print(f"  H1: {n_h1} · tabelas: {n_tbl} (frases {n_frases} + cama + guia)")
    ok = n_tbl == n_frases + 2 and len(d2.inline_shapes) == 1
    print(f"  [{'✓' if ok else '✗'}] estrutura esperada")
    raise SystemExit(0 if ok else 1)
