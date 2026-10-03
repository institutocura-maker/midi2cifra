#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mapa Musical November Rain — Partes 1, 2 e 3 (Verso 3 + Final)."""

# ============================================================ DADOS
# Convenção: notas uma oitava abaixo da voz do Axl (região confortável MD),
# EXCETO no final, onde a voz já canta na região do dó central (D4–E4) — sem transposição.
# Melodia verificada nota a nota no MIDI ('Axl Rose -Vocals-') + cruzamentos.

P1 = [  # ---------- PARTE 1: VERSO 1 ----------
    dict(chords=[("E7M", 0), ("C#m7", 6)],
         syls=["When", "I", "look", "in-", "to", "your", "eyes"],
         notes=[["G#3"], ["B3"], ["C#4"], ["B3"], ["C#4"], ["D#4"], ["B3", "F#3", "G#3"]],
         peak=5, fingers=["1", "3", "4", "3", "4", "5", "3·1·2"]),
    dict(chords=[("B", 6)],
         syls=["I", "can", "see", "a", "love", "re-", "strained"],
         notes=[["G#3"], ["G#3"], ["D#4"], ["D#4"], ["C#4"], ["D#4"], ["B3→"]],
         peak=2, fingers=["1", "1", "3", "3", "2", "3", "1"]),
    dict(chords=[("E7M", 0), ("C#m7", 5)],
         syls=["But", "dar-", "lin'", "when", "I", "hold", "you"],
         notes=[["B3"], ["G#4"], ["F#4"], ["E4"], ["D#4"], ["D#4"], ["C#4"]],
         peak=1, fingers=["1", "5", "4", "3", "2", "2", "1"]),
    dict(chords=[("B", 6)],
         syls=["Don't", "you", "know", "I", "feel", "the", "same"],
         notes=[["C#4"], ["C#4"], ["E4"], ["D#4"], ["C#4"], ["D#4"], ["B3→"]],
         peak=2, fingers=["1", "1", "3", "2", "1", "2", "1"]),
    dict(chords=[("C#m", 0), ("F#", 4)],
         syls=["'Cause", "no-", "thin'", "lasts", "for-", "e-", "ver"],
         notes=[["D#4"], ["C#4"], ["D#4"], ["D#4"], ["F#4"], ["D#4"], ["D#4→"]],
         peak=4, fingers=["2", "1", "2", "2", "4", "3", "3"]),
    dict(chords=[("B", 6)],
         syls=["And", "we", "both", "know", "hearts", "can", "change"],
         notes=[["C#4"], ["C#4"], ["C#4"], ["E4"], ["D#4"], ["C#4"], ["D#4", "B3→"]],
         peak=3, fingers=["1", "1", "1", "3", "2", "1", "2·1"]),
    dict(chords=[("C#m", 0), ("F#", 6)],
         syls=["And", "it's", "hard", "to", "hold", "a", "can-", "dle"],
         notes=[["C#4"], ["C#4"], ["D#4"], ["C#4"], ["D#4"], ["D#4"], ["F#4"], ["D#4→"]],
         peak=6, fingers=["1", "1", "2", "1", "2", "2", "4", "3"]),
    dict(chords=[("B", 6)],
         syls=["In", "the", "cold", "No-", "vem-", "ber", "rain"],
         notes=[["C#4"], ["C#4"], ["C#4"], ["E4"], ["D#4"], ["C#4"], ["D#4", "B3→"]],
         peak=3, fingers=["1", "1", "1", "3", "2", "1", "2·1"]),
]

P2 = [  # ---------- PARTE 2: VERSO 2 ----------
    dict(chords=[("E7M", 0), ("C#m7", 7)],
         syls=["We've", "been", "through", "this", "such", "a", "long", "long", "time"],
         notes=[["B3"], ["G#4"], ["F#4"], ["E4"], ["D#4"], ["D#4"], ["F#4"], ["D#4"], ["C#4"]],
         peak=1, fingers=["1", "4", "3", "2", "1", "1", "3", "2", "1"]),
    dict(chords=[("B", 5)],
         syls=["Just", "tryin'", "to", "kill", "the", "pain"],
         notes=[["C#4"], ["F#4"], ["D#4"], ["C#4"], ["D#4"], ["B3→"]],
         peak=1, fingers=["2", "5", "3", "2", "3", "1"],
         note="depois do \"pain\" tem um \"oh yeah!\" solto — improviso, não perde tempo com ele"),
    dict(chords=[("E7M", 0), ("C#m7", 11)],
         syls=["But", "lo-", "vers", "al-", "ways", "come", "and", "lo-", "vers", "al-", "ways", "go"],
         notes=[["B3"], ["G#4"], ["F#4"], ["G#4"], ["F#4"], ["G#4"], ["G#4"],
                ["F#4"], ["G#4"], ["F#4"], ["G#4"], ["G#4"]],
         peak=11, fingers=["1", "4", "3", "4", "3", "4", "4", "3", "4", "3", "4", "4"],
         note="no \"go\" o Axl solta um vocalise: F#4–G#4–F#4–G#4–G#4–B4–G#4–F#4–D#4–G#4 "
              "(toca o G#4 segurando e depois brinca com o vai-e-vem G#4↔F#4)"),
    dict(chords=[("B", 0), ("E7M", 6), ("C#m7", 11), ("B", 12)],
         syls=["And", "no", "one's", "real-", "ly", "sure", "who's", "let-", "tin'",
               "go", "to-", "day", "walk-", "ing", "a-", "way"],
         notes=[["F#4"], ["E4"], ["E4"], ["F#4"], ["E4"], ["D#4"],
                ["B3"], ["G#4"], ["F#4"], ["G#4"], ["F#4"], ["G#4"],
                ["F#4"], ["E4"], ["F#4"], ["E4", "D#4"]],
         peak=11, fingers=["4", "2", "2", "4", "2", "1", "1", "4", "3", "4", "3", "4",
                           "4", "2", "4", "2·1"],
         note="o \"today\" e o \"walking away\" são improvisos longos em G#4↔F#4 — segure o G#4 e "
              "faça o vai-e-vem quantos tempos quiser; \"walking away\" desce: F#4–E4–E4–F#4–E4–D#4"),
    dict(chords=[("C#m", 0), ("F#7", 6), ("B", 11)],
         syls=["If", "we", "could", "take", "the", "time", "to", "lay", "it", "on", "the", "line"],
         notes=[["C#4"], ["F#4"], ["C#4"], ["D#4"], ["F#4"], ["D#4"],
                ["C#4"], ["C#4"], ["E4"], ["D#4"], ["C#4"], ["D#4", "B3→"]],
         peak=1, fingers=["2", "5", "2", "3", "5", "3", "2", "2", "4", "3", "2", "3·1"]),
    dict(chords=[("C#m", 0)],
         syls=["I", "could", "rest", "my", "head"],
         notes=[["C#4"], ["D#4"], ["D#4"], ["D#4"], ["D#4→"]],
         peak=None, fingers=["2", "3", "3", "3", "3"]),
    dict(chords=[("F#7", 0), ("B", 6)],
         syls=["Just", "know-", "in'", "that", "you", "were", "mine"],
         notes=[["C#4"], ["C#4"], ["C#4"], ["E4"], ["D#4"], ["C#4"], ["D#4", "B3→"]],
         peak=3, fingers=["2", "2", "2", "4", "3", "2", "3·1"],
         note="emendado vem um \"all mine!\" de improviso por cima da nota presa — opcional"),
    dict(chords=[("B", 0), ("E7M", 4), ("F#", 6)],
         syls=["So", "if", "you", "want", "to", "love", "me"],
         notes=[["B3"], ["C#4"], ["B3"], ["E4"], ["D#4"], ["B3→"], ["C#4", "D#4", "C#4→"]],
         peak=3, fingers=["1", "2", "1", "4", "3", "1", "2·3·2"],
         pre="PREVAMP", note="o \"me\" tem uma voltinha: C#4–D#4–C#4"),
    dict(chords=[],
         syls=["Then", "dar-", "lin'", "don't", "re-", "frain"],
         notes=[["B3"], ["C#4"], ["E4"], ["D#4"], ["B3"], ["B3", "G#3", "G#3", "F#3"]],
         peak=2, fingers=["1", "2", "4", "3", "1", "1·1·1·1"],
         note="\"refrain\" desce escadinha: B3–G#3–G#3–F#3 (a nota final é a raiz do F# do vamp)"),
    dict(chords=[],
         syls=["Or", "I'll", "just", "end", "up", "walk-", "in'"],
         notes=[["F#4"], ["E4"], ["E4"], ["E4"], ["D#4"], ["E4"], ["D#4", "B3→"]],
         peak=0, fingers=["4", "2", "2", "2", "1", "2", "1·1"],
         note="as notas repetidas em E4 são o Axl re-atacando — toque uma vez e deixe soar"),
    dict(chords=[],
         syls=["In", "the", "cold", "No-", "vem-", "ber", "rain"],
         notes=[["C#4"], ["F#4"], ["E4"], ["E4"], ["E4"], ["E4"], ["C#4", "E4", "D#4", "B3→"]],
         peak=1, fingers=["2", "5", "2", "2", "2", "2", "2·4·3·1"],
         note="versão 2 do final: \"rain\" ganha um melisma C#4–E4–D#4–B3 e um eco depois "
              "(B3–G#3–G#3–F#3); sem a resposta do piano — segura e cai DIRETO no refrão"),
]

CH = [  # ---------- PARTE 2: REFRAO ----------
    dict(chords=[("D#m", 0), ("E", 4), ("B/D#", 7)],
         syls=["Do", "you", "need", "some", "time", "on", "your", "own"],
         notes=[["D#4"], ["C#4"], ["C#4"], ["C#4"], ["B3"], ["B3"], ["C#4"], ["D#4", "F#4", "D#4→"]],
         peak=7, fingers=["3", "2", "2", "2", "1", "1", "2", "3·5·3"],
         note="\"own\" tem a voltinha pra cima: D#4–F#4–D#4 (é o grito do refrão)"),
    dict(chords=[("D#m", 0), ("E", 4), ("C#m", 7)],
         syls=["Do", "you", "need", "some", "time", "all", "a-", "lone"],
         notes=[["D#4"], ["C#4"], ["C#4"], ["B3"], ["B3"], ["G#3"], ["D#4"], ["C#4→"]],
         peak=None, fingers=["3", "2", "2", "1", "1", "1", "3", "2"],
         note="o \"all\" mergulha no G#3 e o \"alone\" resolve descendo — a linha \"triste\" do refrão"),
    dict(chords=[("D#m", 0), ("E", 3), ("B/D#", 7)],
         syls=["Ev-", "ry-", "bo-", "dy", "needs", "some", "time", "on", "their", "own"],
         notes=[["D#4"], ["C#4"], ["C#4"], ["B3"], ["B3"], ["C#4"], ["D#4"],
                ["F#4"], ["F#4"], ["D#4→"]],
         peak=7, fingers=["3", "2", "2", "1", "1", "2", "3", "5", "5", "3"]),
    dict(chords=[("D#m", 0), ("E", 3), ("F#", 6)],
         syls=["Don't", "you", "know", "you", "need", "some", "time", "all", "a-", "lone"],
         notes=[["D#4"], ["C#4"], ["C#4"], ["B3"], ["B3"], ["G#3"], ["D#4"],
                ["C#4"], ["C#4"], ["C#4→"]],
         peak=None, fingers=["3", "2", "2", "1", "1", "1", "3", "2", "2", "2"],
         note="termina no F# (dominante) segurado — o refrão NUNCA chega no B (tônica). "
              "É por isso que ele soa como uma pergunta no ar"),
]

P3 = [  # ---------- PARTE 3: VERSO 3 ----------
    dict(chords=[("E7M", 0)],
         syls=["And", "when", "your", "fears", "sub-", "side"],
         notes=[["B3"], ["G#4"], ["F#4"], ["E4"], ["D#4"], ["D#4→"]],
         peak=1, fingers=["1", "4", "3", "2", "1", "1"],
         note="a abertura é a MESMA do \"We've been through this\" (Verso 2) — reciclagem de luxo"),
    dict(chords=[("C#m7", 0), ("B", 5)],
         syls=["And", "sha-", "dows", "still", "re-", "main"],
         notes=[["C#4"], ["C#4"], ["F#4"], ["D#4"], ["C#4"], ["D#4", "B3→"]],
         peak=2, fingers=["2", "2", "5", "3", "2", "3·1"],
         note="vem um \"oh yeah!\" solto no fim — improviso, como no Verso 2"),
    dict(chords=[("E7M", 0), ("C#m7", 5)],
         syls=["I", "know", "that", "you", "can", "love", "me"],
         notes=[["B3"], ["C#4"], ["B3"], ["C#4"], ["D#4"], ["B3"], ["G#3"]],
         peak=4, fingers=["1", "2", "1", "2", "3", "1", "1"],
         note="a frase termina afundando no G#3 — é o respiro antes da próxima"),
    dict(chords=[("B", 6)],
         syls=["When", "there's", "no", "one", "left", "to", "blame"],
         notes=[["G#3"], ["G#3"], ["E4"], ["D#4"], ["C#4"], ["B3"], ["B3→"]],
         peak=2, fingers=["1", "1", "3", "2", "1", "1", "1"],
         note="\"no\" pula pro E4 e desce escadinha até o B3 — cadência assinatura de novo"),
    dict(chords=[("C#m", 0), ("F#7", 6)],
         syls=["So", "ne-", "ver", "mind", "the", "dark-", "ness"],
         notes=[["C#4"], ["D#4"], ["C#4"], ["D#4"], ["F#4"], ["D#4"], ["D#4→"]],
         peak=4, fingers=["2", "3", "2", "3", "5", "3", "3"]),
    dict(chords=[("F#7", 0), ("B", 5)],
         syls=["We", "still", "can", "find", "a", "way"],
         notes=[["C#4"], ["B3"], ["E4"], ["D#4"], ["C#4"], ["D#4", "B3→"]],
         peak=2, fingers=["2", "1", "4", "3", "2", "3·1"],
         note="irmã das frases 4/6/8 da Parte 1, só começando um pouquinho diferente"),
    dict(chords=[("C#m", 0), ("F#7", 6)],
         syls=["'Cause", "no-", "thin'", "lasts", "for-", "e-", "ver"],
         notes=[["D#4"], ["C#4"], ["D#4"], ["D#4"], ["F#4"], ["D#4"], ["D#4→"]],
         peak=4, fingers=["3", "2", "3", "3", "5", "3", "3"],
         note="idêntica à frase 5 da Parte 1 — já sabe de cor!"),
    dict(chords=[("B", 6)],
         syls=["E-", "ven", "cold", "No-", "vem-", "ber", "rain"],
         notes=[["C#4"], ["C#4"], ["C#4"], ["E4"], ["D#4"], ["C#4"], ["D#4", "B3→"]],
         peak=3, fingers=["2", "2", "2", "4", "3", "2", "3·1"],
         note="idêntica à frase 8 da Parte 1; no \"rain\" o Slash assume (3º solo)"),
]

OUT = [  # ---------- PARTE 3: FINAL (já na região real da voz: D4–E4) ----------
    dict(chords=[("Bm", 0)], pre="LOOP",
         syls=["Don't", "ya", "think", "that", "you", "need", "some-bo-dy"],
         notes=[["D4"], ["D4"], ["B3"], ["A3"], ["D4"], ["B3→"], ["B3→"]],
         peak=4, fingers=["3", "3", "1", "1", "3", "1", "1"]),
    dict(chords=[("Bm", 0)],
         syls=["Don't", "ya", "think", "that", "you", "need", "some-one"],
         notes=[["D4"], ["D4"], ["B3"], ["A3"], ["D4"], ["B3→"], ["B3→"]],
         peak=4, fingers=["3", "3", "1", "1", "3", "1", "1"]),
    dict(chords=[("Bm", 0), ("F#", 4)],
         syls=["Ev-", "ry-", "bo-", "dy", "needs", "some-", "bo-", "dy"],
         notes=[["D4"], ["D4"], ["D4"], ["C#4"], ["B3"], ["F#3"], ["C#4"], ["C#4", "B3→"]],
         peak=0, fingers=["3", "3", "3", "2", "1", "1", "2", "2·1"],
         note="o \"some-\" mergulha no F#3 e volta — o balanço da frase"),
    dict(chords=[("E", 0), ("D", 5)],
         syls=["You're", "not", "the", "on-", "ly", "one"],
         notes=[["E4"], ["E4"], ["E4"], ["D4"], ["C#4"], ["F#3", "D4", "D4→"]],
         peak=0, fingers=["4", "4", "4", "3", "2", "1·3·3"],
         note="o E maior por baixo é o \"tempero\" do final — repare como ele puxa o ouvido"),
    dict(chords=[("G", 0), ("A", 5)],
         syls=["You're", "not", "the", "on-", "ly", "one"],
         notes=[["D4"], ["D4"], ["D4"], ["B3"], ["C#4"], ["D4", "C#4", "A3→"]],
         peak=None, fingers=["3", "3", "3", "1", "2", "3·2·1"],
         note="a resposta da anterior, terminando no A3 — e o loop inteiro começa de novo"),
]

FILL = ["F#4", "D#4", "E4", "D#4", "C#4", "B3"]

P1_FILLS = {1: "fill", 3: "fill", 5: "fill", 7: "fill"}
P2_FILLS = {1: "fill", 3: "fill", 4: "fill", 6: "fill", 10: "nofill"}
CH_FILLS = {3: "bridge"}
P3_FILLS = {1: "fill", 3: "fill2", 5: "fill", 7: "solo3"}
OUT_FILLS = {4: "fade"}

VAMP_NOTE = ("daqui até o refrão o piano fica alternando E ↔ F#, um compasso de cada "
             "(pedal de tensão — não mostra na cifra comum, mas é o que o disco toca)")
LOOP_NOTE = ("loop de 5 compassos: Bm | Bm | Bm–F# | E–D | G–A — repete 4× até o fade, "
             "com os solos conversando por cima")
MOLDURA_NOTE = ("a direita trava UMA moldura — B3+D#4+G#4 — batendo nos 4 tempos de cada compasso. "
                "Sobre o baixo E ela vira E7M; sobre o C# vira C#m7(9): a mão não se mexe, só o baixo anda. "
                "Sobre o B, a moldura desce um degrau (F#3+B3+D#4) e o topo passeia (D# D# E E | D# D# C#); "
                "no 2º ciclo, o compasso de E repete a escadinha G#→A#→B4")

# ============================================================ PARTE 0: INTRO
# Fonte: pista 'Axl Rose -Piano-' do MIDI, compassos 1-15 (tema) e 16-23 (groove);
# fanfarra = pista 'Reed Section' (c21-24). Registro REAL do disco — é a própria
# parte do piano. Na linha do meio vão os TEMPOS (1 e 2 e 3 e 4 e), não a letra.
INTRO = [
    dict(label="Compasso 1 — a abertura", chords=[("E", 0)],
         syls=["1", "2", "3–4"], notes=[["·"], ["·"], ["D#5", "E5→"]],
         fingers=["", "", "4–5"], peak=2,
         note="A graça D#5 é rapidinha — um mergulhinho antes do salto; o E5 segura 2 tempos. "
              "Esquerda: E grave desde o tempo 1 (E1+E2 se o piano chegar lá; E2 sozinho já serve)."),
    dict(label="Compasso 2 — a corrida", chords=[("E", 0)],
         syls=["1", "2", "e", "3", "e", "4", "e"],
         notes=[["B3+E4+G#4"], ["E4"], ["F#4"], ["G#4"], ["A#4"], ["·"], ["B4"]],
         fingers=["1·3·5", "1", "2", "3", "4", "", "5"], peak=6,
         note="Escala de Si maior correndo de E4 até o B4 — os fills dos versos DESCem essa "
              "mesma escala; a intro SOBE. Esquerda: E2+E3, o compasso inteiro."),
    dict(label="Compasso 3 — o sobe-e-desce", chords=[("B/D#", 0)],
         syls=["1", "2", "3", "e", "4", "e"],
         notes=[["B3+D#4+G#4"], ["D#4", "F#4", "G#4", "A#4"], ["B4"], ["A#4"], ["G#4"], ["F#4"]],
         fingers=["1·2·4", "1·2·3·4", "5", "4", "3", "2"], peak=2,
         note="Mesmo gesto, com o baixo um degrau abaixo (D#): sobe até o B4, dá uma olhada lá "
              "em cima… e desce. Primeira aparição do B/D# — o acorde que flutua no refrão!"),
    dict(label="Compasso 4 — o pedido", chords=[("C#m", 0)],
         syls=["1", "2", "e", "3", "e", "4", "e"],
         notes=[["C#4+E4+G#4"], ["E4"], ["F#4"], ["G#4"], ["F#4"], ["·"], ["E4", "D#4"]],
         fingers=["1·2·4", "2", "3", "4", "3", "", "2–1"],
         note="Trava o C#4 com o polegar e deixa os outros dedos conversarem por cima "
              "(E4 F#4 G#4 F#4). No fim, o pickup E4–D#4 já puxa o próximo acorde. "
              "Esquerda: C#2 (re-ataca no tempo 4)."),
    dict(label="Compasso 5 — o balanço", chords=[("B", 0)],
         syls=["1", "e", "2", "e", "3", "e", "4", "e"],
         notes=[["B3+D#4"], ["F#4→"], ["B3+D#4"], ["B3+E4"], ["B3+F#4"], ["B3+E4"],
                ["B3+D#4"], ["B3+E4"]],
         fingers=["1·3", "5", "1·3", "1·4", "1·5", "1·4", "1·3", "1·4"], peak=1,
         note="O B3 fica de moldura embaixo e o topo balança D#–E–F#–E–D#–E — o vai-e-vem "
              "dos versos, agora em acorde. Esquerda: B1+B2 o compasso inteiro."),
    dict(label="Compasso 6 — o trampolim", chords=[("E", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["B3+E4+G#4"], ["B3+E4+G#4"], ["B3+E4+A#4"], ["B3+E4+B4"]],
         fingers=["1·3·5", "1·3·5", "1·3·5", "1·3·5"], peak=3,
         note="O acorde de E bate em todos os tempos (toc-toc-toc-toc) e só o dedinho do topo "
              "anda: G#→A#→B — a escadinha do trampolim de novo, agora em acorde. "
              "Esquerda: E2 pulsando (1, e do 2, e do 3, e do 4)."),
    dict(label="Compasso 7 — a descida", chords=[("C#m", 0)],
         syls=["1", "2", "3", "e", "4", "e"],
         notes=[["·"], ["C#4", "D#4", "E4", "F#4"], ["G#4"], ["F#4"], ["E4"], ["D#4"]],
         fingers=["", "1·2·3·4", "5", "4", "3", "2"], peak=2,
         note="A corrida rápida: sobe C#4→F#4 num fôlego só e desce G#4→D#4 com calma. "
              "Respira — é mais fácil do que parece. Esquerda: C#2 o compasso inteiro."),
    dict(label="Compasso 8 — o grito", chords=[("B", 0)],
         syls=["1", "e", "2", "e", "3", "e", "4", "e"],
         notes=[["B3+D#4"], ["F#4→"], ["B4"], ["F#4"], ["·"], ["D#4"], ["F#4"], ["C#4→"]],
         fingers=["1·3", "5", "5", "4", "", "3", "4", "2"], peak=2,
         note="O B3 segue preso embaixo; a graça D#4 cai no F#4 pontuado… e o B4 no tempo 2 é "
              "o grito da primeira metade. Depois escorrega: D#4 F#4 C#4. Esquerda: B pulsando."),
    dict(label="Compasso 9 — o sossego", chords=[("B", 0)],
         syls=["1", "e", "2", "3", "4"],
         notes=[["·"], ["D#4"], ["B3"], ["C#4"], ["D#4"]],
         fingers=["", "3", "1", "2", "3"],
         note="A resposta, mais calada: D#4… e as terças subindo B3→C#4→D#4, "
              "com o baixo pulsando em colcheias."),
    dict(label="Compasso 10 — de novo! (variação)", chords=[("E", 0)],
         syls=["1", "2", "3", "e", "4", "e"],
         notes=[["B3+E4+G#4"], ["E4", "F#4", "G#4", "A#4"], ["B4"], ["A#4"], ["G#4"], ["A#4"]],
         fingers=["1·3·5", "1·2·3·4", "5", "4", "3", "4"], peak=2,
         note="O tema inteiro volta — e a corrida muda de humor: o B4 chega mais cedo "
              "(tempo 3) e a volta termina subindo G#→A#, preparando a variação que vem."),
    dict(label="Compasso 11 — terças de mãos dadas", chords=[("B/D#", 0)],
         syls=["1", "2", "e", "3", "e", "4", "e"],
         notes=[["B3+F#4"], ["D#4+A#4"], ["G#4+D#4"], ["F#4"], ["E4"], ["D#4"], ["C#4"]],
         note="Variação do sobe-e-desce: duas terças descendo juntas (D#+A#, depois G#+D#) "
              "e a linha escorrega até o C#4. Esquerda: D#2."),
    dict(label="Compasso 12 — o pedido (de novo)", chords=[("C#m", 0)],
         syls=["1", "2", "e", "3", "e", "4", "e"],
         notes=[["C#4+E4+G#4"], ["E4"], ["F#4"], ["G#4"], ["F#4"], ["·"], ["E4", "D#4"]],
         fingers=["1·2·4", "2", "3", "4", "3", "", "2–1"],
         note="Cópia fiel do compasso 4 — presente! Esquerda: C#2."),
    dict(label="Compasso 13 — o rolê", chords=[("B", 0)],
         syls=["1", "e", "2", "e", "3", "e", "4"],
         notes=[["B3+D#4"], ["F#4"], ["B3", "D#4", "F#4", "B4"], ["B3+D#4"], ["·"],
                ["B3+F#4"], ["B3+C#4"]],
         fingers=["1·3", "4", "1·2·3·5", "1·3", "", "1·5", "1·2"], peak=2,
         note="O momento de bravura: arrasta o acorde de B de baixo pra cima e coroa com o "
              "B4 — o último suspiro alto do tema. Esquerda: B."),
    dict(label="Compasso 14 — o balanço final", chords=[("B", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["B3+D#4"], ["B3+E4"], ["B3+C#4"], ["B3+D#4"]],
         fingers=["1·3", "1·4", "1·2", "1·3"],
         note="As terças balançando mais uma vez (D#–E–C#–D#), baixo pulsando — "
              "a calma antes da porta abrir."),
    dict(label="Compasso 15 — TÁ-DÃM! entra a banda", chords=[("B", 0)],
         syls=["(compasso inteiro)"],
         notes=[["B1+B2+F#3+B3+D#4→"]], peak=0,
         note="O acorde de B das profundezas (B1) até o D#4 — SEGURA os 4 tempos. "
              "A bateria chega junto (o fill dela entra no tempo 3). É a porta que abre a banda."),
]

GROOVE = [
    dict(label="A caminhada do baixo (2 ciclos de 4 compassos)", pre="MOLDURA",
         chords=[("E7M", 0), ("C#m7", 1), ("B", 2), ("B", 3),
                 ("E7M", 4), ("C#m7", 5), ("B", 6), ("B", 7)],
         syls=["c.1", "c.2", "c.3", "c.4", "c.1", "c.2", "c.3", "c.4"],
         notes=[["E2"], ["C#2"], ["B2"], ["B2"], ["E2"], ["C#2"], ["B2"], ["B2"]],
         note="Um baixo por compasso — e cada um é puxado meio-tempo antes (o D#2 anuncia o "
              "C#2; o C#2 anuncia o B2). A direita fica parada na moldura (veja a dica) "
              "e a bateria marca o tempo."),
    dict(label="A fanfarra dos sopros (o anúncio do verso)",
         chords=[("C#m7", 0), ("C#m7", 1), ("B", 2), ("B", 3), ("B", 4), ("B", 5)],
         syls=["ta ta ta", "ta!", "TÁ (c.22)", "··", "TÁ (c.23)", "→ verso"],
         notes=[["C#5", "C#5", "C#5"], ["D#5", "F#5"], ["D#5→"], ["D#5", "C#5"],
                ["B4→"], ["F#4", "G#4→"]],
         peak=4,
         note="Os sopros chegam pra anunciar a voz: três ta no C#5, sobem pro D#5 e F#5 e "
              "coroam no D#5 longo; a resposta é o B4 longo. O G#4 final é literalmente a nota "
              "em que o Axl entra — no seu mapa, o G#3 do \"When\". Toque junto se quiser "
              "brilhar, ou deixe pro disco e prepare a mão pro verso."),
]
INTRO_FILLS = {}
GROOVE_FILLS = {}

# ============================================================ PONTE + SOLO 1 (c76–92)
# Transparência: a pista vocal do MIDI fica MUDA aqui (c77–92) — a melodia cantada
# não existe em fonte confiável. A cama de acordes foi conferida em 4 fontes
# independentes (UG ver 2, Scribd, Gitagram, Khmerchords): por linha, D#m → E →
# B/D# (L1/L3), C#m (L2) e F# seco (L4) — a mesma viagem do refrão.
# O solo 1 abaixo é nota a nota da pista '-Slash -Lead and rythem-' (essência:
# repetições viram notas presas, ornamentos resumidos).
PONTE = [
    dict(label="Linha 1 — a confissão", chords=[("D#m", 0), ("E", 4), ("B/D#", 8)],
         syls=["I", "know", "it's", "hard", "to", "keep", "an", "o-", "pen", "heart"],
         notes=[["D#2"], ["·"], ["·"], ["·"], ["E2"], ["·"], ["·"], ["·"], ["D#2"], ["·"]],
         note="A mesma viagem do refrão (D#m → E → B/D#), só que sussurrada. Cama completa "
              "na esquerda: D#2+F#3+A#3 → E2+G#3+B3 → D#2+F#3+B3 (os mesmos formatos do refrão!)"),
    dict(label="Linha 2 — o medo", chords=[("D#m", 0), ("E", 3), ("C#m", 6)],
         syls=["When", "e-", "ven", "friends", "seem", "out", "to", "harm", "you"],
         notes=[["D#2"], ["·"], ["·"], ["E2"], ["·"], ["·"], ["C#2"], ["·"], ["·"]],
         note="A 2ª linha mergulha no C#m — igual à 2ª linha do refrão (a linha \"triste\")"),
    dict(label="Linha 3 — a esperança", chords=[("D#m", 0), ("E", 3), ("B/D#", 6)],
         syls=["But", "if", "you", "could", "heal", "a", "bro-", "ken", "heart"],
         notes=[["D#2"], ["·"], ["·"], ["E2"], ["·"], ["D#2"], ["·"], ["·"], ["·"]],
         note="Irmã da linha 1 — no disco o Slash já vai respondendo por cima (o solo está "
              "chegando…)"),
    dict(label="Linha 4 — a pergunta no ar", chords=[("D#m", 0), ("E", 2), ("F#", 4)],
         syls=["Would-", "n't", "time", "be", "out", "to", "charm", "you"],
         notes=[["D#2"], ["·"], ["E2"], ["·"], ["F#2"], ["·"], ["·"], ["·"]],
         note="Termina em F# SECO (a dominante) — a mesma pergunta no ar do refrão. "
              "É daqui que o 1º solo do Slash decola"),
]
PONTE_FILLS = {}

# ============================================================ GUIA DE MONTAGEM
# A música inteira, de ponta a ponta. Compassos = os do nosso MIDI.
GUIDE = [
    ("🌧️ Intro A — tema do piano", "abre no E5 (a nota mais famosa)",
     "E | B/D# | C#m | B (a escadinha) + E | C#m | B | B — tudo 2×", "🌧️ Intro (tema)", "c1–15"),
    ("🌩️ Intro B — a banda entra", "o acorde grande de B e o groove",
     "E7M | C#m7 | B | B ×2 + fanfarra dos sopros", "🌩️ Intro (banda)", "c16–24"),
    ("Verso 1", "\"When I look into your eyes\" (entra no G#3)",
     "E7M | C#m7 | B — e na 2ª metade C#m | F#7 | B", "Parte 1", "c24–43"),
    ("Verso 2", "\"We've been through this…\" (entra no B3)",
     "igual ao Verso 1 + vamp E↔F# no fim (\"so if you want to love me\")", "Parte 2 — Verso 2", "c44–67"),
    ("Refrão 1", "\"Do you need some time…\" (entra no D#4)",
     "D#m → E → B/D# por linha (cifra simples: E → F#)", "Parte 2 — Refrão", "c68–76"),
    ("🌉 Ponte", "\"I know it's hard…\" (sussurrado)",
     "D#m → E → B/D# / C#m / B/D# / F# seco", "Ponte", "c77–84*"),
    ("🎸 Solo 1", "o Slash responde a ponte",
     "cama: E | C#m | B (com o baixo passeando: B/D#, B/F#)", "Solo 1 (transcrito!)", "c77–92*"),
    ("Refrão 2", "\"Sometimes I need some time…\" (entra no B3)",
     "igual ao refrão (mesmo molde, abertura diferente)", "Parte 2 — Refrão + dica", "c93–100"),
    ("🎸 Solo 2", "a escada de lançamento e o grito longo",
     "cama: F# | F# | E | C#m | B | B/D# ×2", "Solo 2 (transcrito!)", "c100–109"),
    ("Verso 3", "\"And when your fears subside…\" (entra no B3)",
     "igual ao Verso 1 (é um greatest hits!)", "Parte 3 — Verso 3", "c110–123"),
    ("🎸 Solo 3", "o gigante — reconheça o compasso de silêncio TOTAL e o groove G–A",
     "B | F#/A# | G#m | F# | E | F# ×2 → silêncio → G | A | B → clímax em Bm (C#6!)",
     "Solo 3 (transcrito!)", "c122–151"),
    ("🌟 Final", "\"Don't ya think that you need somebody\" (D4, já em Ré!)",
     "Bm | Bm | Bm–F# | E–D | G–A ×4 até o fade", "Parte 3 — Final", "c150–169"),
]
GUIDE_NOTE = ("* no nosso MIDI a ponte cantada não existe (a pista vocal fica muda) e o solo 1 "
              "cobre os 16 compassos; no disco, a ponte ocupa ~8 compassos e o solo entra depois")

def guide_text():
    out = ["[🗺️ Guia de montagem — a música inteira, de ponta a ponta]",
           "(169 compassos · ~9 minutos · tudo já está no seu mapa)", ""]
    for i, (nome, como, ac, mapa, comp) in enumerate(GUIDE, 1):
        out.append(f"{i:>2}. {nome}  ·  {comp}")
        out.append(f"     entra: {como}")
        out.append(f"     acordes: {ac}")
        out.append(f"     no mapa: {mapa}")
        out.append("")
    out.append(f"({GUIDE_NOTE})")
    return "\n".join(out)

def guide_table_html():
    rows = "".join(
        f'<tr><td>{i}</td><td><b>{n}</b></td><td>{como}</td><td><code>{ac}</code></td>'
        f'<td>{mp}</td><td>{comp}</td></tr>'
        for i, (n, como, ac, mp, comp) in enumerate(GUIDE, 1))
    return (f'<table class="lh"><tr><th>#</th><th>Seção</th><th>Como reconhece</th>'
            f'<th>Acordes</th><th>No mapa</th><th>Comp.</th></tr>{rows}</table>'
            f'<p class="small" style="margin-top:8px">{GUIDE_NOTE}.</p>')

SOLO1 = [
    dict(label="Compasso 77 — o oi (E)", chords=[("E", 0)],
         syls=["1", "2", "3", "4", "e"],
         notes=[["G#4→"], ["G#4", "F#4", "G#4"], ["B4", "G#4→"], ["G#4", "F#4"], ["E4"]], peak=2,
         note="A abertura é o vai-e-vem G#↔F# (as duas teclas pretas vizinhas — o mesmo par "
              "do \"lovers always come and go\"!), com o B4 espiando por cima"),
    dict(label="Compasso 78 — a conversa (C#m)", chords=[("C#m", 0)],
         syls=["1", "2", "3", "4", "e"],
         notes=[["G#4", "F#4", "G#4→"], ["G#4", "F#4"], ["G#4", "B4", "G#4"], ["G#4", "F#4"],
                ["D#4", "E4"]],
         note="A mesma conversa sobre o C#m — e no fim escorrega pro D#4–E4"),
    dict(label="Compasso 79 — a primeira resposta (B)", chords=[("B", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["D#4→"], ["B4→"], ["·"], ["E4", "D#4", "E4"]], peak=1,
         note="A resposta: D#4 preso (o Slash \"senta\" a frase) e o B4 cantado em cima"),
    dict(label="Compasso 80 — a escadinha (B/F#)", chords=[("B/F#", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["D#4→"], ["C#4", "B3"], ["C#4", "D#4", "F#4", "C#4"], ["C#4", "B3"]],
         note="A escadinha do acorde de B subindo (C#–D#–F#) e caindo de volta no B3"),
    dict(label="Compasso 81 — de novo! (E)", chords=[("E", 0)],
         syls=["1", "2", "3", "4", "e"],
         notes=[["G#4→"], ["G#4", "F#4"], ["G#4", "B4", "G#4"], ["G#4", "F#4"], ["E4"]],
         note="Cópia do compasso 77 — o Slash repete a frase inteira (e você também pode!)"),
    dict(label="Compasso 82 — a conversa sobe (C#m)", chords=[("C#m", 0)],
         syls=["1", "2", "3", "4", "e"],
         notes=[["G#4", "F#4", "G#4→"], ["G#4", "F#4"], ["G#4", "B4"], ["C#5→"], ["B4"]], peak=3,
         note="…mas o final agora sobe um degrau a mais: C#5! Repetir a frase um tom acima "
              "é o truque favorito do Slash (e de todo bom solista)"),
    dict(label="Compasso 83 — O GRITO (B)", chords=[("B", 0)],
         syls=["1", "3", "4", "e"],
         notes=[["D#5→"], ["D#5", "C#5"], ["B4", "C#5", "B4"], ["G#4"]], peak=0,
         note="O grito: D#5 comprido — a nota que abre a segunda metade do solo"),
    dict(label="Compasso 84 — a coroa (B/D#)", chords=[("B/D#", 0)],
         syls=["1", "2", "3", "4", "e"],
         notes=[["B4→"], ["B4→"], ["E5", "D#5", "B4", "E5"], ["D#5", "B4"], ["F#5"]], peak=4,
         note="A volta do grito: B4 preso, os saltos E5–D#5… e o F#5 no fim — o primeiro "
              "teto novo do mapa"),
    dict(label="Compasso 85 — o canto (C#m)", chords=[("C#m", 0)],
         syls=["1", "3", "4", "e"],
         notes=[["E5→"], ["E5", "C#5", "D#5"], ["E5→"], ["D#5", "E5", "D#5"]], peak=0,
         note="O canto: E5 comprido (a nota mais cantada do solo) com o roteiro C#–D# em volta"),
    dict(label="Compasso 86 — subindo pro teto (F#)", chords=[("F#", 0)],
         syls=["1", "2", "3", "4", "e"],
         notes=[["C#5→"], ["C#5", "D#5"], ["E5", "F#5→"], ["F#5→"], ["E5", "D#5"]], peak=2,
         note="A escada C#5→D#5→E5→F#5 em cima do acorde de F# — e fica lá em cima"),
    dict(label="Compasso 87 — O TETO (B/D#)", chords=[("B/D#", 0)],
         syls=["1", "2", "4"],
         notes=[["E5", "D#5→"], ["B5→"], ["A#5→"]], peak=1,
         note="O TETO DO SOLO: B5! A nota mais aguda de tudo que o seu mapa já viu. "
              "Depois encosta no A#5 pra começar a viagem de volta"),
    dict(label="Compasso 88 — a grande escada (B/D#)", chords=[("B/D#", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["A#5", "G#5→"], ["F#5", "E5→"], ["D#5→"], ["E5", "D#5", "C#5→"]],
         note="A GRANDE ESCADA: desce a escala de Si maior do teto até o chão "
              "(A#→G#→F#→E→D#→C#), cada degrau repetido — o mesmo trampolim da intro, "
              "agora gigante e pra baixo"),
    dict(label="Compasso 89 — o lamento (C#m)", chords=[("C#m", 0)],
         syls=["1", "3", "4", "e"],
         notes=[["E5→"], ["D#5", "E5", "D#5"], ["C#5", "B4"], ["D#5", "B4"]], peak=0,
         note="O lamento: E5 de novo, e a frase chora descendo"),
    dict(label="Compasso 90 — as terças em queda (F#)", chords=[("F#", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["C#5", "B4", "C#5→"], ["A#4", "B4", "A#4→"], ["G#4", "F#4", "A#4", "F#4"],
                ["G#4", "E4", "F#4", "E4"]],
         note="As terças em queda: C#–B, A#–G#… a escada em pares, caindo em direção ao chão"),
    dict(label="Compasso 91 — a aterrissagem (B/D#)", chords=[("B/D#", 0)],
         syls=["1", "2", "3", "4", "e"],
         notes=[["D#4→"], ["D#4", "F#4", "E4", "D#4"], ["B4→"], ["E4", "F#4", "E4"], ["B4→"]],
         note="A aterrissagem: o solo começou no D#4 e VOLTA pro D#4 — volta pra casa. "
              "O B4 comprido prepara a entrega"),
    dict(label="Compasso 92 — a entrega (B/D#)", chords=[("B/D#", 0)],
         syls=["2", "3", "e", "4", "e"],
         notes=[["E4", "F#4", "E4", "D#4"], ["D#5→"], ["B4"], ["C#5"], ["B4"]], peak=1,
         note="A entrega: D#5–B4–C#5–B4 joga a bola pro refrão 2 — \"Sometimes I need some "
              "time…\", que você já tem!"),
]
SOLO1_FILLS = {}

# ============================================================ SOLO 2 (c100–109)
# Nota a nota da pista do Slash. Vem logo depois do refrão 2 ("Sometimes I
# need…", que termina segurando o F#). Cama: F# F# | E | C#m | B | B/D# | E |
# C#m | B | B/D# — e no c.110 entra o Verso 3. O momento famoso: B5 por mais
# de 4 tempos (c104), o "bend chorado" do disco.
SOLO2 = [
    dict(label="Compasso 100 — a escada de lançamento, 1º degrau (F#)", chords=[("F#", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["C#4→"], ["D#4→"], ["E4→"], ["F#4→"]],
         note="Uma nota por tempo, subindo a escala de Si maior. O F# na esquerda é o rabo do "
              "refrão 2 (a pergunta no ar) — e a resposta do Slash é subir"),
    dict(label="Compasso 101 — …2º degrau (F#)", chords=[("F#", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["G#4→"], ["A#4→"], ["B4→"], ["C#5→"]],
         note="Degrau por degrau até o C#5 — dois compassos, oito notas, uma escada inteira. "
              "E o próximo compasso salta direto pro E5!"),
    dict(label="Compasso 102 — o salto (E)", chords=[("E", 0)],
         syls=["1", "4", "e"],
         notes=[["E5→"], ["G#5"], ["B5"]], peak=0,
         note="O E5 cantado por 2 tempos, e a subida relâmpago G#5→B5: em dois compassos "
              "o Slash subiu dois andares"),
    dict(label="Compasso 103 — as sacudidas (C#m)", chords=[("C#m", 0)],
         syls=["1", "3", "4"],
         notes=[["F#5→"], ["F#5", "G#5"], ["G#5", "B5", "E5"]], peak=2,
         note="F#5 de novo no tempo 1, e as sacudidas: G#5… B5… caindo no E5"),
    dict(label="Compasso 104 — O GRITO LONGO (B)", chords=[("B", 0)],
         syls=["1", "2", "e", "3"],
         notes=[["D#5→"], ["·"], ["B5"], ["B5→"]], peak=3,
         note="A NOTA DO DISCO: B5 segurado por mais de 4 tempos (na guitarra é um bend "
              "gigante que chora — no piano, segue o pedal e deixa cantar)"),
    dict(label="Compasso 105 — a volta começa (B/D#)", chords=[("B/D#", 0)],
         syls=["3", "e", "4", "e"],
         notes=[["·"], ["E5→"], ["·"], ["D#5"]],
         note="O B5 do compasso passado ainda está soando por cima (por isso os primeiros "
              "tempos parecem vazios) — e a voz desce: E5… D#5…"),
    dict(label="Compasso 106 — a corrida (E)", chords=[("E", 0)],
         syls=["1", "3", "4"],
         notes=[["E5→"], ["E5", "C#5", "D#5"], ["E5", "F#5", "G#5", "E5"]], peak=0,
         note="O lamento E5 de novo, e no fim a mão dispara: E–F#–G# em 16 avos "
              "(a escadinha da intro, agora em velocidade)"),
    dict(label="Compasso 107 — a roseta (C#m)", chords=[("C#m", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["F#5", "D#5", "E5", "F#5", "D#5", "E5"], ["D#5", "C#5", "D#5", "C#5"],
                ["B4", "C#5", "B4", "G#4"], ["C#5", "B4", "G#4", "B4"]],
         note="O bordado: 16 avos escorregando do F#5 até o B4. Parece difícil, mas é a "
              "escala de Si maior enfeitada — devagar, uma nota por vez, a mão aprende sozinha"),
    dict(label="Compasso 108 — o motor (B)", chords=[("B", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["F#5", "B4", "B4"], ["B4", "G#4", "B4"], ["F#5", "B4", "B4"],
                ["B4", "G#4", "B4"]],
         note="O motor: o F#5 volta nos tempos 1 e 3 e o B4 martela em volta, com o G#4 "
              "de passagem — hipnótico"),
    dict(label="Compasso 109 — a aterrissagem (B/D#)", chords=[("B/D#", 0)],
         syls=["1", "2", "3", "4", "e"],
         notes=[["G#5", "F#5"], ["E5", "D#5"], ["D#5", "C#5", "D#5"], ["D#5", "F#5"],
                ["C#5→"]], peak=0,
         note="G#5–F#5 caindo, o roteiro D#–C# acha o chão, e o C#5 segurado é a porta pro "
              "Verso 3 — \"And when your fears subside…\", que você já tem"),
]
SOLO2_FILLS = {}

# ============================================================ SOLO 3 (c122–151)
# O gigante: ~30 compassos. Fase 1 (c124–131): cama B | F#/A# | G#m | F# | E | F#
# ×2 — sem lead (a guitarra só marca acordes; a escadinha desce nos graves). Fase 2
# (c132–133): último eco de Si + UM COMPASSO DE SILÊNCIO TOTAL (nada toca no MIDI).
# Fase 3 (c134–141): o piano assume o groove G | A | B — a modulação (e o tempo
# acelera de 80 pra 105 bpm exatamente no c134). Fase 4 (c142–149): clímax sobre a
# harmonia do FINAL comprimida (Bm | F# | E–D | G–A) — lead: B5, A#5, C#6 (A NOTA
# MAIS AGUDA DA MÚSICA!), flutter F#–G–F#–E, uníssono B+D — repetido 2×. Fase 5
# (c150–151): o motor F#–G–F#–E / C#–D–C#–B em 32 avos, que se dissolve no final
# (os vocais "Don't ya think…" entram em c150 POR CIMA — o material continua
# rodando, com o C#6 voltando em c158 e c163, até o fade).
SOLO3 = [
    dict(label="A resposta — o grito da porta (c. 122–123)",
         chords=[("C#m", 0), ("F#7", 2)],
         syls=["3", "4", "1", "2", "3", "4", "e"],
         notes=[["D#5", "C#5", "D#5"], ["F#5", "D#5"], ["C#5"], ["C#5", "C#5"],
                ["E5", "D#5"], ["C#5", "D#5"], ["B4→"]], peak=1,
         note="A última palavra é do Slash: depois do \"…November rain\" ele responde subindo "
              "ao F#5 e descendo chorando até o B4 — que fica segurado no ar, esperando o solo "
              "começar. (Transparência: no nosso MIDI esses gritinhos moram na pista do vocal — "
              "é o fill que responde à voz; no disco é a guitarra.)"),
    dict(label="A cama clássica — a escadinha nos graves (c. 124–127)",
         chords=[("B", 0), ("F#/A#", 1), ("G#m", 2), ("F#", 3), ("E", 4), ("F#", 5)],
         syls=["B", "A#", "G#", "F#", "E", "F#"],
         notes=[["B2"], ["A#2"], ["G#2"], ["F#2"], ["E2"], ["F#2"]],
         note="A linha do meio é a ESCADINHA, e a linha de baixo é o que você toca: "
              "B → A# → G# → F# → E, degrau por degrau da escala de Si DESCENDO — a mesma "
              "escadinha da intro (E→D#→C#→B), agora no porão. Um acorde por degrau "
              "(B, F#/A#, G#m, F# duram meio compasso; E e F# duram um compasso cada). "
              "A guitarra só respira acordes aqui — não há lead: é a cama."),
    dict(label="A cama de novo (c. 128–130)",
         chords=[("B", 0), ("F#/A#", 1), ("G#m", 2), ("F#", 3), ("E", 4)],
         syls=["B", "A#", "G#", "F#", "E"],
         notes=[["B2"], ["A#2"], ["G#2"], ["F#2"], ["E2"]],
         note="O mesmo ciclo de novo — reciclagem clássica. Desta vez a volta termina no E… "
              "e o último degrau (F#) vira rampa de lançamento:"),
    dict(label="A subida — a rampa de lançamento (c. 131)",
         chords=[("F#", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["F#2→"], ["·"], ["F#3", "G#3"], ["A#3", "B3"]],
         note="Sobre o F# na esquerda, a guitarra sobe a escada em 8 avos: F# → G# → A# → B — "
              "a MESMA escala de Si maior das corridas da intro, agora subindo degrau a degrau "
              "até sumir no B. Algo está para acontecer…"),
    dict(label="O mergulho — o último eco e o silêncio (c. 132–133)",
         chords=[("B", 0)],
         syls=["c. 132", "c. 133"],
         notes=[["B2→"], ["·"]],
         note="O último acorde do mundo de Si maior, redondo e comprido (oitavas B1+B2 no "
              "piano)… e depois UM COMPASSO DE SILÊNCIO ABSOLUTO — neste trecho do MIDI não "
              "toca NADA, nem a bateria. A música inteira prende a respiração. O que vem "
              "depois é outro mundo."),
    dict(label="O NOVO MUNDO — o groove G | A | B (c. 134–141)",
         chords=[("B", 0), ("G→A", 1), ("B", 2), ("G→A", 3), ("B", 4), ("G→A", 5),
                 ("B", 6), ("G→A", 7)],
         syls=["c. 134", "c. 135", "c. 136", "c. 137", "c. 138", "c. 139", "c. 140", "c. 141"],
         notes=[["B2"], ["G2", "A2"], ["B2"], ["G2", "A2"], ["B2"], ["G2", "A2"],
                ["B2"], ["G2", "A2"]],
         note="O piano ASSUME a música: compassos de B alternando com G→A, quatro voltas — "
              "é o groove do FINAL (\"Don't ya think…\"), chegando uns 20 compassos antes da "
              "hora! No piano: oitavas B1+B2 com a moldura F#3+B3 e o passinho F#–A–F#–B no "
              "3º tempo; no G, oitavas + B3+D4; no A, oitavas + a dupla A3–C#4. O G NATURAL "
              "é a senha: o G# do mundo de Si morreu — bem-vindos ao mundo do final. E olha "
              "o detalhe: a música ACELERA de 80 pra 105 bpm exatamente aqui (c. 134)."),
    dict(label="O clímax — o lançamento (c. 142)",
         chords=[("Bm", 0), ("F#", 2)],
         syls=["1", "2", "3", "4"],
         notes=[["B5→"], ["·"], ["A#5→"], ["B5"]], peak=0,
         note="A lead decola sobre a harmonia do FINAL comprimida (Bm | F#, meio compasso "
              "cada): B5 segurado dois tempos, A#5 de resposta e o B5 de novo no rabinho — "
              "tudo lá em cima, na região que era do teto dos solos 1 e 2."),
    dict(label="O clímax — A NOTA DO DISCO: C#6! (c. 143)",
         chords=[("E", 0), ("D", 2)],
         syls=["1", "2", "3", "4"],
         notes=[["C#6→"], ["B5", "A#5"], ["B5", "F#5"], ["D5", "F#5"]], peak=0,
         note="A NOTA MAIS AGUDA DA MÚSICA INTEIRA no nosso MIDI: C#6 — um degrau acima do "
              "B5 (o teto dos solos 1 e 2), duas oitavas acima do dó central. No disco é um "
              "bend alucinante da guitarra; no piano, se doer a mão, toque uma oitava abaixo "
              "— o desenho é o que importa. Depois desce em escadinha: B5 → A#5 → B5 → F#5 → "
              "D5 → F#5."),
    dict(label="O clímax — o flutter e a resposta (c. 144)",
         chords=[("G", 0), ("A", 2)],
         syls=["1", "2", "3", "4"],
         notes=[["G5→"], ["F#5", "G5", "F#5", "E5"], ["F#5→"], ["·"]], peak=2,
         note="Sobre o G: G5 gritado. No meio, o tremer rápido F#–G–F#–E (quatro notinhas em "
              "disparada — comece com uma dupla por tempo e vá acelerando). E sobre o A: F#5 "
              "comprido — a nota-resposta que fica cantando."),
    dict(label="O uníssono gigante (c. 145–146)",
         chords=[("Bm", 0)],
         syls=["c. 145", "c. 146"],
         notes=[["B3+D5→"], ["D5"]], peak=0,
         note="Toda a guitarra vira UM instrumento só: B (grave) + D (agudo) martelados "
              "juntos por DOIS compassos — o acorde-gigante antes do arrepio final. É o Bm "
              "deitado no teclado: B2 na esquerda, D5 na direita, e força."),
    dict(label="O clímax, de novo — o lançamento (c. 147)",
         chords=[("Bm", 0), ("F#", 2)],
         syls=["1", "2", "3", "4"],
         notes=[["B5→"], ["·"], ["A#5→"], ["B5"]], peak=0,
         note="Cópia de c. 142, nota por nota — o Slash repete o grito inteiro (e você também "
              "pode: já sabe onde cada nota mora)."),
    dict(label="O clímax, de novo — C#6! (c. 148)",
         chords=[("E", 0), ("D", 2)],
         syls=["1", "2", "3", "4"],
         notes=[["C#6→"], ["B5", "A#5"], ["B5", "F#5"], ["D5", "F#5"]], peak=0,
         note="E lá vem a nota mais aguda da música DE NOVO — mesma escadinha descendo. "
              "Repetir a frase inteira é o truque favorito do Slash (lembra do Solo 1, "
              "c. 77 → 81?)."),
    dict(label="O clímax, de novo — o flutter (c. 149)",
         chords=[("G", 0), ("A", 2)],
         syls=["1", "2", "3", "4"],
         notes=[["G5→"], ["F#5", "G5", "F#5", "E5"], ["F#5→"], ["·"]], peak=2,
         note="Cópia de c. 144 — G5, o tremer, e o F#5 comprido de novo. A segunda volta é "
              "idêntica à primeira: aprendeu uma, ganhou duas."),
    dict(label="O motor eterno — o solo se dissolve no final (c. 150–151)",
         chords=[("Bm", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["F#5", "G5", "F#5", "E5", "F#5", "G5", "F#5", "E5"],
                ["C#5", "D5", "C#5", "B4", "C#5", "D5", "C#5", "B4"],
                ["F#5", "G5", "F#5", "E5", "F#5", "G5", "F#5", "E5"],
                ["C#5", "D5", "C#5", "B4", "C#5", "D5", "C#5", "B4"]],
         note="O motor: sobre o pedal de B (B3 grave segurado o tempo todo), quatro notinhas "
              "em disparada — duas voltas de F#–G–F#–E no tempo 1, duas de C#–D–C#–B no "
              "tempo 2, e alterna até o fim. E aqui a mágica: o Axl JÁ ESTÁ cantando "
              "\"Don't ya think…\" — a seção Final do seu mapa entra aqui, POR CIMA do "
              "motor. O solo 3 não termina: ele se dissolve no final e continua rodando até "
              "o fade. No piano: comece com uma volta por tempo e vá dobrando."),
]
SOLO3_FILLS = {13: "outro"}

# ============================================================ TEXTO (chat)
def phrase_lines(p):
    n = len(p["syls"])
    chords_at = {i: c for c, i in p["chords"]}
    note_strs = ["-".join(ns) for ns in p["notes"]]
    widths = [max(len(p["syls"][i]), len(note_strs[i]),
                  len(chords_at.get(i, ""))) + 2 for i in range(n)]
    rc = rs = rn = ""
    for i in range(n):
        rc += chords_at.get(i, "").ljust(widths[i])
        rs += p["syls"][i].ljust(widths[i])
        rn += note_strs[i].ljust(widths[i])
    return rc.rstrip(), rs.rstrip(), rn.rstrip()

def chat_section(title, phrases, fills, first_fill_full=True):
    out = [f"[{title}]", ""]
    shown_fill = not first_fill_full
    for k, p in enumerate(phrases):
        if p.get("pre") == "PREVAMP":
            out.append(f"({VAMP_NOTE})")
            out.append("")
        if p.get("pre") == "LOOP":
            out.append(f"({LOOP_NOTE})")
            out.append("")
        if p.get("pre") == "MOLDURA":
            out.append(f"({MOLDURA_NOTE})")
            out.append("")
        if p.get("label"):
            out.append(f"◆ {p['label']}")
        c, s, n = phrase_lines(p)
        out += [c if c.strip() else "", s, n]
        if p.get("note"):
            out.append(f"     ({p['note']})")
        out.append("")
        if k in fills:
            kind = fills[k]
            if kind == "fill":
                if shown_fill:
                    out.append("↳ (resposta do piano de novo: F#4 · D#4 · E4 · D#4 · C#4 · B3)")
                else:
                    out.append("↳ (piano responde: F#4 · D#4 · E4 · D#4 · C#4 · B3 — notas compridas, descendo)")
                    shown_fill = True
            elif kind == "fill2":
                out.append("↳ (piano responde com uma graça a mais: F#4 · G#4 · F#4 · E4 · D#4 · C#4 · B3)")
            elif kind == "solo3":
                out.append("↳ (sem resposta — o \"rain\" segura e o Slash assume: 3º solo… e a música descola pra Ré maior)")
            elif kind == "bridge":
                out.append("↳ (termina segurando o F#… e entra a ponte \"I know it's hard to keep an open heart\")")
            elif kind == "fade":
                out.append(f"↳ ({LOOP_NOTE})")
            elif kind == "outro":
                out.append("↳ (o motor não para: o Axl já está cantando \"Don't ya think…\" — a "
                           "seção Final do seu mapa entra AQUI, por cima do solo)")
            out.append("")
    return "\n".join(out)

def chat_map():
    parts = [chat_section("Intro — o tema do piano (c. 1–15 · linha do meio = tempos, notas AS DO DISCO)", INTRO, INTRO_FILLS)]
    parts.append(chat_section("Intro — a entrada da banda (c. 16–24 · groove + fanfarra)", GROOVE, GROOVE_FILLS))
    parts.append(chat_section("Primeira Parte — igual à que você já tem", P1, P1_FILLS, first_fill_full=False))
    parts.append(chat_section("Verso 2", P2, P2_FILLS))
    parts.append(chat_section("Refrão", CH, CH_FILLS))
    parts.append(chat_section("Ponte — \"I know it's hard…\" (cama de acordes; linha de baixo = onde o acorde chega)", PONTE, PONTE_FILLS))
    parts.append(chat_section("Solo 1 — a resposta do Slash (c. 77–92 · registro real, essência nota a nota)", SOLO1, SOLO1_FILLS))
    parts.append(chat_section("Solo 2 — o chorão (c. 100–109 · depois do refrão 2, registro real)", SOLO2, SOLO2_FILLS))
    parts.append(chat_section("Verso 3", P3, P3_FILLS))
    parts.append(chat_section("Solo 3 — o gigante (c. 122–151 · a viagem completa: da cama de Si maior à porta do Ré)", SOLO3, SOLO3_FILLS))
    parts.append(chat_section("Final — a música sobe de Si maior pra Ré maior!", OUT, OUT_FILLS))
    parts.append(guide_text())
    return "\n\n".join(parts)

# ============================================================ HTML
def note_cell_html(notes, is_peak):
    parts = []
    for j, nt in enumerate(notes):
        hold = " hold" if nt.endswith("→") else ""
        peak = " peak" if is_peak else ""
        parts.append(f'<span class="nt{peak}{hold}">{nt}</span>')
        if j < len(notes) - 1:
            parts.append('<span class="glue">›</span>')
    return "".join(parts)

def phrase_html(p, label):
    chords_at = {i: c for c, i in p["chords"]}
    cols = []
    for i in range(len(p["syls"])):
        ch = f'<div class="chord">{chords_at[i]}</div>' if i in chords_at else "<div class='chord'></div>"
        fin = p.get("fingers", [""] * len(p["syls"]))[i] if p.get("fingers") else ""
        cols.append(
            f'<div class="cell">{ch}'
            f'<div class="syl">{p["syls"][i]}</div>'
            f'<div class="notes">{note_cell_html(p["notes"][i], i == p.get("peak"))}</div>'
            f'<div class="fin">{fin}</div></div>')
    note = f'<div class="pnote">💡 {p["note"]}</div>' if p.get("note") else ""
    return (f'<div class="card"><div class="plabel">{label}</div>'
            f'<div class="phrase">{"".join(cols)}</div>{note}</div>')

def keyboard_svg():
    W, H, BW, BH = 34, 150, 21, 92
    WHITE, BLACK = ["C", "D", "E", "F", "G", "A", "B"], {"C": "C#", "D": "D#", "F": "F#", "G": "G#", "A": "A#"}
    mel = {"F#3", "G#3", "A3", "B3", "C#4", "D4", "D#4", "E4", "F#4", "G#4", "A#4", "B4",
           "C#5", "D#5", "E5", "F#5", "G#5", "A#5", "B5", "C#6"}
    lh = {"E2", "C#2", "D#2", "F#2", "B2", "D2", "G2", "A2", "A#2", "G#2"}
    x, parts = 0, [f'<svg viewBox="0 0 1000 205" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Teclado guia">']
    for octv in (2, 3, 4, 5):
        for wname in WHITE:
            label = f"{wname}{octv}"
            fill, txt, tcol = "#ffffff", "", "#5a6b7d"
            if label in mel: fill, tcol = "#cfe3f8", "#1d5c9e"; txt = label
            if label in lh:  fill, tcol = "#f9e4c8", "#b06a1a"; txt = label
            parts.append(f'<rect x="{x}" y="0" width="{W}" height="{H}" rx="4" fill="{fill}" stroke="#8d9aa8"/>')
            if txt: parts.append(f'<text x="{x+W/2}" y="{H-34}" text-anchor="middle" font-size="12" font-weight="700" fill="{tcol}">{txt}</text>')
            if label.startswith("C"):
                parts.append(f'<text x="{x+W/2}" y="{H-10}" text-anchor="middle" font-size="11" fill="#7d8b99">{label}</text>')
            if label == "C4":
                parts.append(f'<circle cx="{x+W/2}" cy="{H-52}" r="4" fill="#e67e22"/>')
                parts.append(f'<text x="{x+W/2}" y="{H-58}" text-anchor="middle" font-size="10" font-weight="700" fill="#e67e22">dó central</text>')
            if wname in BLACK:
                bl = f"{BLACK[wname]}{octv}"
                bx = x + W - BW / 2
                bfill, btxt = ("#2f6fb5", bl) if bl in mel else (("#d08a3e", bl) if bl in lh else ("#2b3038", ""))
                parts.append(f'<rect x="{bx}" y="0" width="{BW}" height="{BH}" rx="3" fill="{bfill}" stroke="#14171b"/>')
                if btxt: parts.append(f'<text x="{bx+BW/2}" y="{BH-14}" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">{btxt}</text>')
            x += W
    parts.append(f'<rect x="{x}" y="0" width="{W}" height="{H}" rx="4" fill="#ffffff" stroke="#8d9aa8"/>')
    parts.append(f'<text x="{x+W/2}" y="{H-10}" text-anchor="middle" font-size="11" fill="#7d8b99">C6</text>')
    bx = x + W - BW / 2
    parts.append(f'<rect x="{bx}" y="0" width="{BW}" height="{BH}" rx="3" fill="#2f6fb5" stroke="#14171b"/>')
    parts.append(f'<text x="{bx+BW/2}" y="{BH-14}" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">C#6</text>')
    parts.append("</svg>")
    return "".join(parts)

def fill_html(kind, shown):
    if kind == "fill":
        if shown:
            return '<div class="fill">🎹 <b>Resposta do piano</b> (de novo): <b>F#4 · D#4 · E4 · D#4 · C#4 · B3</b></div>'
        return ('<div class="fill">🎹 <b>Resposta do piano/cordas</b> (enquanto a nota presa ainda soa): '
                '<b>F#4 · D#4 · E4 · D#4 · C#4 · B3</b> — notas compridas, descendo</div>')
    if kind == "fill2":
        return ('<div class="fill">🎹 <b>Resposta do piano, agora com uma graça a mais:</b> '
                '<b>F#4 · G#4 · F#4 · E4 · D#4 · C#4 · B3</b></div>')
    if kind == "solo3":
        return ('<div class="fill">🎸 <b>Sem resposta aqui:</b> o "rain" segura e o Slash assume com o 3º solo — '
                'e a banda descola de Si maior para <b>Ré maior</b>…</div>')
    if kind == "nofill":
        return ('<div class="fill">🚫 <b>Sem resposta aqui:</b> o "rain" segura em cima do vamp E↔F# e a banda '
                'cai <b>direto no refrão</b> — é a entrada mais satisfatória da música</div>')
    if kind == "bridge":
        return ('<div class="fill">🌉 <b>Depois do refrão:</b> o F# segura e entra a ponte '
                '("I know it\'s hard to keep an open heart…") e o 1º solo do Slash</div>')
    if kind == "fade":
        return (f'<div class="fill">🔁 <b>{LOOP_NOTE}.</b> Cada frase cai em cima do seu compasso — '
                'é só deixar rolar até a música se despedir.</div>')
    if kind == "outro":
        return ('<div class="fill">🎤 <b>O motor não para:</b> o Axl já está cantando '
                '<i>"Don\'t ya think…"</i> — a seção <b>Final</b> do mapa entra aqui, '
                'por cima do solo que ainda roda. Os dois mundos se sobrepõem.</div>')
    return ""

def section_html(title, subtitle, phrases, fills, start_num, first_fill_full=True):
    out = [f'<h2>{title}</h2>', f'<p class="small">{subtitle}</p>']
    shown = not first_fill_full
    for k, p in enumerate(phrases):
        if p.get("pre") == "PREVAMP":
            out.append(f'<div class="tip"><h3>🔁 O vamp antes do refrão</h3>{VAMP_NOTE}.</div>')
        if p.get("pre") == "LOOP":
            out.append(f'<div class="tip"><h3>🔁 O loop do final</h3>{LOOP_NOTE}. '
                       'Cada frase cai em cima do seu compasso.</div>')
        if p.get("pre") == "MOLDURA":
            out.append(f'<div class="tip"><h3>🧱 A moldura parada — o truque do groove</h3>'
                       f'{MOLDURA_NOTE}.</div>')
        out.append(phrase_html(p, p.get("label") or f"Frase {start_num + k}"))
        if k in fills:
            out.append(fill_html(fills[k], shown))
            if fills[k] == "fill": shown = True
    return "".join(out)

def build_html():
    css = """
    :root{--ink:#22303e;--blue:#1d6fb8;--peak:#c0392b;--muted:#68788a;--card:#fff;--bg:#eef2f7;--chip:#2c3e50}
    *{box-sizing:border-box}
    body{margin:0;background:var(--bg);color:var(--ink);font-family:'Segoe UI',system-ui,-apple-system,Roboto,Arial,sans-serif;line-height:1.55}
    .wrap{max-width:940px;margin:0 auto;padding:28px 20px 60px}
    header.hero{background:linear-gradient(135deg,#24344a 0%,#3a5a82 60%,#587fae 100%);color:#fff;border-radius:16px;padding:30px 30px 26px;margin-bottom:26px;box-shadow:0 6px 24px rgba(30,50,80,.25)}
    header.hero h1{margin:0 0 4px;font-size:30px;letter-spacing:.5px}
    header.hero .sub{color:#d7e3f2;font-size:15px}
    .badges{margin-top:14px;display:flex;flex-wrap:wrap;gap:8px}
    .badge{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25);padding:4px 12px;border-radius:999px;font-size:13px}
    h2{font-size:20px;margin:34px 0 12px;color:#1d2f4b;border-left:5px solid var(--blue);padding-left:10px}
    .card{background:var(--card);border-radius:14px;padding:18px 20px;box-shadow:0 2px 10px rgba(30,50,80,.08);margin-bottom:14px}
    .nt{font-family:'Cascadia Mono',Consolas,Menlo,monospace;font-weight:700;color:var(--blue);font-size:15px;white-space:nowrap}
    .nt.peak{color:var(--peak)}
    .nt.hold{text-decoration:underline wavy #9fb4c8 2px;text-underline-offset:4px}
    .glue{color:#9aa9b8;margin:0 1px;font-size:12px}
    .phrase{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:flex-start}
    .cell{display:flex;flex-direction:column;gap:2px;min-width:34px}
    .chord{font-weight:800;color:var(--chip);font-size:14.5px;min-height:20px;font-style:italic}
    .syl{font-weight:600;font-size:16px}
    .notes{display:flex;align-items:center;flex-wrap:wrap;gap:1px}
    .fin{font-size:11px;color:#93a3b3;font-family:Consolas,monospace}
    .fill{border:2px dashed #b7c5d4;border-radius:12px;padding:10px 16px;color:var(--muted);font-style:italic;background:#f6f9fc;margin:10px 0 22px}
    .fill b{font-style:normal;font-family:Consolas,monospace;color:#4a6076}
    .plabel{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:1.2px;margin-bottom:6px;font-weight:700}
    .pnote{margin-top:10px;font-size:13.5px;color:#5b6c7d;background:#f4f8fc;border-radius:8px;padding:8px 12px}
    .kbdwrap{overflow-x:auto}
    .kbdwrap svg{min-width:700px;width:100%;height:auto;display:block}
    .kbd-legend{display:flex;gap:18px;flex-wrap:wrap;margin-top:10px;font-size:13.5px;color:var(--muted)}
    .sw{display:inline-block;width:14px;height:14px;border-radius:3px;vertical-align:-2px;margin-right:5px;border:1px solid #99a8b8}
    .tip{background:#fff8ec;border:1px solid #f0dcb8;border-radius:12px;padding:14px 18px;margin:14px 0}
    .tip h3{margin:0 0 6px;font-size:15.5px;color:#8a5d0b}
    table.lh{border-collapse:collapse;width:100%;font-size:14.5px}
    table.lh th,table.lh td{padding:8px 10px;border-bottom:1px solid #e4eaf1;text-align:left}
    table.lh th{background:#f2f6fa;color:#33465a;font-size:13px;text-transform:uppercase;letter-spacing:.6px}
    table.lh td code{background:#eef3f8;padding:2px 7px;border-radius:6px;font-family:Consolas,monospace;font-weight:700;color:var(--blue)}
    .next{display:flex;gap:10px;flex-wrap:wrap;margin-top:8px}
    .next div{background:#e7eef7;border-radius:10px;padding:10px 14px;font-size:14px;flex:1;min-width:200px}
    .small{font-size:13px;color:var(--muted)}
    footer{margin-top:36px;font-size:12.5px;color:#8a99a8;text-align:center}
    @media print{body{background:#fff}.card,.tip{box-shadow:none;border:1px solid #dde5ee}}
    """

    s0a = section_html("🌧️ Intro — o tema do piano (compassos 1–15)",
                       "O começo mais famoso do rock ao piano. Aqui não tem letra: a linha do meio conta os "
                       "<b>tempos</b> (1 e 2 e 3 e 4 e — conte \"um-e-dois-e…\"), e notas com <b>+</b> são "
                       "juntas (<span class=\"nt\">B3+E4+G#4</span> = acorde de uma vez). Nada de transposição: "
                       "são as notas do disco, a própria parte do piano. A receita: o baixo desce a escadinha "
                       "<b>E → D# → C# → B</b> enquanto a direita corre a escala de Si maior.",
                       INTRO, INTRO_FILLS, 1)

    s0b = section_html("🌩️ Intro — a entrada da banda (compassos 16–24)",
                       "Depois do acorde grande, o piano vira base: a direita trava uma moldura e o baixo anda "
                       "(<b>E7M → C#m7 → B → B</b>, dois ciclos). Por cima, os sopros fazem a fanfarra que "
                       "anuncia o verso… e o Axl entra exatamente no verso que você já tem.",
                       GROOVE, GROOVE_FILLS, 1)

    s1 = section_html("🌧️ Parte 1 — o mapa (Verso 1)",
                      "Melodia da voz (mão direita), uma oitava abaixo do Axl. A cifra não mostra ritmo: "
                      "você já conhece a música — <b>cante a frase e encaixe as notas</b>.",
                      P1, P1_FILLS, 1)

    s2v = section_html("🎤 Parte 2 — Verso 2",
                       "Mesma toada da Parte 1, mas o Axl solta mais a voz: tem dois trechos de vocalise "
                       "(\"lovers always… go\" e \"today / walking away\"). No mapa está a essência; o enfeite vem depois.",
                       P2, P2_FILLS, 1)

    s2c = section_html("🙌 Parte 2 — Refrão",
                       "Um molde novo, e ele se repete 4 vezes: <b>D#4 C#4 C#4 C#4 B3 B3 C#4</b> + a palavra final. "
                       "As linhas 1 e 3 (\"own\") sobem pra cima; as linhas 2 e 4 (\"alone\") mergulham no G#3. "
                       "Acordes do disco: <b>D#m → E → B/D#</b> (linhas 1 e 3) e <b>D#m → E → C#m</b> (linha 2)… "
                       "a cifra comum simplifica pra <b>E → F#</b> por linha — funciona, mas o disco é mais rico.",
                       CH, CH_FILLS, 1)

    s2p = section_html("🌉 Ponte — \"I know it's hard to keep an open heart…\"",
                       "A última parte cantada que faltava. <b>Transparência:</b> o nosso MIDI não tem a voz "
                       "nesta seção (a pista vocal fica muda aqui) e não há transcrição confiável da linha "
                       "cantada — então o mapa traz o que dá pra garantir nota a nota: a <b>cama de acordes</b> "
                       "(conferida em 4 fontes independentes) e a letra. O canto do Axl é baixinho, quase "
                       "falado — você conhece a música, cante por cima. E repare: é <b>a mesma viagem "
                       "harmônica do refrão</b> (D#m → E → B/D#…), com a última linha terminando em <b>F# "
                       "seco</b> — a pergunta no ar que o Slash responde com o solo.",
                       PONTE, PONTE_FILLS, 1)

    s2s = section_html("🎸 Solo 1 — a resposta do Slash (compassos 77–92)",
                       "Nota a nota do nosso MIDI, no registro real da guitarra — é a <b>essência</b> do solo "
                       "(repetições rápidas viram notas presas; os enfeites ficam por sua conta). A cama é uma "
                       "volta aos acordes do verso — <b>E → C#m → B</b>, com o baixo passeando (B/D#, B/F#). "
                       "Se quiser, toque tudo uma oitava abaixo: o desenho é o que importa.",
                       SOLO1, SOLO1_FILLS, 1)

    s2s2 = section_html("🎸 Solo 2 — o chorão (depois do refrão 2, compassos 100–109)",
                       "O solo mais emocional do disco, logo depois do refrão 2 (<i>\"Sometimes I "
                       "need some time…\"</i>). O refrão termina segurando o F# (a pergunta no ar) — "
                       "e o Slash responde com uma <b>escada de lançamento</b> inteira. Cama: "
                       "<b>F# → E → C#m → B → B/D#</b> (duas voltas). O momento famoso: um "
                       "<b>B5 segurado por mais de 4 tempos</b> — na guitarra é o bend chorado; "
                       "no piano, pedale e deixe cantar. Registro real, essência nota a nota.",
                       SOLO2, SOLO2_FILLS, 1)

    s3v = section_html("🌅 Parte 3 — Verso 3",
                       "O verso da despedida — e um presente pra quem estudou a Parte 1: quase tudo aqui é "
                       "reciclagem das melodias que você já sabe.",
                       P3, P3_FILLS, 1)

    s2s3 = section_html("🎸 Solo 3 — o gigante (compassos 122–151)",
                        "O solo mais longo da música — 30 compassos — e o único que é uma <b>viagem</b>: "
                        "a cama clássica de Si maior, um mergulho com <b>compasso de silêncio TOTAL</b>, "
                        "o groove <b>G | A</b> que muda o mundo (e a velocidade: <b>80 → 105 bpm</b>!) e o "
                        "clímax com <b>a nota mais aguda de toda a música: C#6</b>. A lead está no registro "
                        "real da guitarra; a linha grave é a cama (baixo). Regra de ouro: se doer a mão, "
                        "uma oitava abaixo — o desenho é o que importa.",
                        SOLO3, SOLO3_FILLS, 1)

    s3o = section_html("🌟 Parte 3 — Final (\"everybody needs somebody\")",
                       "Aqui a música <b>sobe de Si maior para Ré maior</b> (uma 3ª menor acima) — por isso o "
                       "encerramento soa \"iluminado\", como se o sol abrisse depois da chuva. E um detalhe prático: "
                       "a voz já canta na região do dó central (D4–E4), então <b>estas notas são as da gravação, "
                       "sem transposição nenhuma</b>.",
                       OUT, OUT_FILLS, 1)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mapa Musical — November Rain (completo, com os 3 solos)</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">

<header class="hero">
  <h1>🎹 Mapa Musical — November Rain</h1>
  <div class="sub">Guns N' Roses · <i>Use Your Illusion I</i> &nbsp;·&nbsp; O mapa completo — os 3 solos + guia de montagem, do primeiro acorde ao fade</div>
  <div class="badges">
    <span class="badge">Tom: Si maior (final em Ré maior!)</span>
    <span class="badge">Cifras: E7M · C#m7 · B/D# · B · F# · D#m · Bm…</span>
    <span class="badge">Voz 1 oitava abaixo; intro, solos e final no registro real</span>
    <span class="badge">Andamento: lento, livre (~80 bpm)</span>
  </div>
</header>

<h2>📖 Como ler o mapa</h2>
<div class="card">
<ul>
  <li><b>Números = oitavas.</b> <span class="nt">C4</span> é o <b>dó central</b>. <span class="nt">G#3</span> fica logo abaixo dele; <span class="nt">D#4</span> logo acima.</li>
  <li><span class="nt">→</span> <b>nota longa:</b> toca e deixa soar. &nbsp;·&nbsp; <span class="glue">›</span> liga notas da <b>mesma sílaba</b> (melisma).</li>
  <li>Na <b>🌧️ intro</b> não tem letra: a linha do meio são os <b>tempos</b> (1 e 2 e 3 e 4 e — conte "um-e-dois-e…"), e notas com <b>+</b> tocam juntas: <span class="nt">B3+E4+G#4</span> = acorde de uma vez.</li>
  <li>Notas em <span class="nt peak">vermelho</span> = pico da frase (onde a voz abre). Números cinza = dedilhado sugerido (MD) — ajuste ao que for confortável.</li>
  <li><b>Notas repetidas</b> são o Axl re-atacando a mesma nota — toque uma vez e deixe cantar.</li>
  <li><b>Cifra de violão × piano:</b> muita cifra mostra F–Dm–C com \"afine meio tom abaixo\" (os violões da banda). No piano, toque direto <b>E7M, C#m7, B, F#</b> — é o som real do disco.</li>
</ul>
</div>

<h2>🎼 Onde estão as notas (teclado-guia)</h2>
<div class="card kbdwrap">
{keyboard_svg()}
<div class="kbd-legend">
  <span><span class="sw" style="background:#cfe3f8"></span>melodia (mão direita)</span>
  <span><span class="sw" style="background:#f9e4c8"></span>baixos da mão esquerda (E2, C#2, D#2, F#2, B2 + D2, G2, A2 do final + A#2, G#2 da escadinha do Solo 3)</span>
  <span><span class="sw" style="background:#e67e22;border-radius:50%"></span>C4 = dó central</span>
</div>
<p class="small">A Parte 1 inteira mora em 8 teclas (F#3 → G#4). Partes 1–3 juntas: <b>11 teclas</b> —
a Parte 2 acrescentou só a <b>B4</b>, e o final (já em Ré maior) trouxe a <b>A3</b> e a <b>D4</b>.
A intro estica o mapa pra cima: <b>A#4, C#5, D#5, E5 e F#5</b> — o tema abre direto no E5
e a fanfarra dos sopros coroa no F#5. E os solos do Slash vão além: <b>G#5, A#5, B5…</b> e o Solo 3
coroa no <b>C#6</b> — a nota mais aguda da música inteira, o teto absoluto do mapa (no Solo 2,
o B5 ainda é a nota mais longa). Repare como o mapa \"anda\" pra direita
no teclado conforme a música avança. 😉</p>
</div>

{s0a}

<div class="tip">
  <h3>🎹 A intro é o verso "de lado"</h3>
  Olha os acordes do tema: <b>E → B/D# → C#m → B</b> — são os mesmos acordes do verso
  (<b>E, C#m, B</b>), só que com o baixo <b>andando degrau a degrau pela escala</b> (E→D#→C#→B).
  E as corridas? A MESMA escala de Si maior dos fills do piano nos versos — lá ela desce
  (<span class="nt">F#4 D#4 E4 D#4 C#4 B3</span>), aqui ela sobe
  (<span class="nt">E4 F#4 G#4 A#4 B4</span>). Quem sabe a Parte 1 já toca metade da intro de graça.
</div>

<div class="card">
<h3 style="margin:0 0 10px">✈️ Como estudar a intro</h3>
<ol>
  <li><b>A abertura sozinha, até virar músculo:</b> E2 na esquerda, conte 1… 2…, graça D#5 e caí no
      <span class="nt peak">E5</span>, segurando. É o primeiro som que todo mundo reconhece.</li>
  <li><b>A escadinha do baixo:</b> E → D# → C# → B, um compasso cada, com a direita parada num acorde simples.
      Quando a mão esquerda decorar o caminho, adicione as corridas.</li>
  <li><b>As corridas são UMA escala só</b> (Si maior: E4 F#4 G#4 A#4 B4 — dedos 1-2-3-4-5). Devagar, sem pulo:
      a velocidade vem de graça com a repetição.</li>
  <li><b>O groove é o presente:</b> direita parada na moldura, esquerda andando E→C#→B. Deixe a bateria
      imaginária entrar e curta o papel de base.</li>
  <li><b>Monte a sequência inteira</b> (tema → variação → acorde grande → groove 2× → fanfarra → verso)
      num andamento manso, ~60–70 bpm, antes de correr pro tempo do disco.</li>
</ol>
</div>

{s0b}

{s1}

<div class="tip">
  <h3>🔑 O "segredo" da Parte 1 — a cadência assinatura</h3>
  Quase toda frase termina no mesmo desenho: <span class="nt">C#4</span> <span class="nt">D#4</span> <span class="nt hold">B3→</span>.
  E as frases 4, 6 e 8 são irmãs quase idênticas:
  <span class="nt">C#4 C#4 C#4 E4 D#4 C#4 D#4</span> <span class="nt hold">B3→</span>.
</div>

{s2v}

<div class="tip">
  <h3>🎭 Os dois "momentos Axl" do Verso 2</h3>
  <b>1) \"But lovers always come and lovers always go\":</b> a melodia é um vai-e-vem <span class="nt">G#4↔F#4</span>
  (é o par de teclas pretas vizinhas!). No \"go\" ele sobe até o <span class="nt peak">B4</span> e volta — toque o G#4 seguro e improvise o resto.<br>
  <b>2) \"…who's lettin' go today, walking away\":</b> mesmo vai-e-vem, mas o \"today\" e o \"away\" ficam rodando entre G#4 e F#4
  enquanto a banda mantém o vamp. Quando cansar, o \"walking away\" te devolve pro chão: <span class="nt">F#4 E4 E4 F#4 E4</span> <span class="nt hold">D#4→</span>.
</div>

{s2c}

<div class="tip">
  <h3>🧲 Por que o refrão "flutua" (e nunca pousa)</h3>
  Os acordes ficam rodando em <b>D#m → E → B/D# → C#m → F#</b> — repare que <b>nunca chegam no B</b> (a tônica, o "casa" da música).
  Tudo fica suspenso, como uma pergunta no ar. Por isso, quando o verso volta e resolve no B, dá aquela sensação de alívio.
  No piano: comece com a cifra simples (<b>E → F#</b> por linha) e, quando estiver firme, troque pelos acordes reais.
</div>

{s2p}

<div class="tip">
  <h3>🧩 A ordem da seção (pra não se perder)</h3>
  Refrão 1 → <b>ponte</b> (4 linhas, ~2 compassos cada) → <b>solo 1</b> (16 compassos) → refrão 2
  (<i>"Sometimes I need some time…"</i>). Detalhe curioso: no nosso MIDI o transcritor pulou a cama
  da ponte e deixou o solo cobrir os 16 compassos — no disco são ~8 compassos de ponte cantada e
  depois o solo. E os acordes do solo são <b>os do verso de novo</b> (E, C#m, B) — a música inteira
  mora na mesma família.
</div>

{s2s}

<div class="tip">
  <h3>🎸 A arquitetura do solo (o mapa do arco)</h3>
  <b>Conversa</b> (o vai-e-vem G#↔F#, compassos 77–78) → <b>repetição um degrau acima</b> (81–82) →
  <b>o grito</b> (D#5, c. 83) → <b>o canto</b> (E5, c. 85) → <b>O TETO</b> (B5!, c. 87) →
  <b>a grande escada descendo</b> (c. 88) → <b>as terças em queda</b> (c. 90) →
  <b>a aterrissagem</b> (de volta ao D#4 onde começou, c. 91) → <b>a entrega</b> pro refrão 2 (c. 92).
  Sobe, canta no teto e volta pra casa — um arco completo de quase 2 minutos de conversa.
</div>

<div class="tip">
  <h3>🔁 Bônus: o 2º refrão é uma variação</h3>
  Na segunda volta Axl canta <i>"Sometimes I need some time on my own"</i> — mesmo molde, abertura diferente:
  <span class="nt">Some-</span><span class="nt">(B3)</span> <span class="nt">times</span><span class="nt">(C#4)</span>
  <span class="nt">I</span><span class="nt">(B3)</span> <span class="nt">need</span><span class="nt peak">(E4)</span>
  <span class="nt">some</span><span class="nt">(D#4)</span> <span class="nt">time</span><span class="nt hold">(B3→)</span>
  <span class="nt">on</span><span class="nt">(C#4)</span> <span class="nt">my</span><span class="nt">(D#4)</span>
  <span class="nt">own</span><span class="nt hold">(C#4→)</span>.
</div>

{s2s2}

<div class="tip">
  <h3>🎸 Os três irmãos — Solo 1, Solo 2 e Solo 3</h3>
  O Solo 1 <b>conversa</b>: vai-e-vem, repetições, um grito e volta pra casa. O Solo 2 <b>chora</b>:
  sobe uma escada inteira, salta dois andares e segura a nota mais longa da música. O Solo 3 <b>viaja</b>:
  em vez de uma frase, é a música inteira — cama, silêncio, um mundo novo e o teto absoluto
  (<span class="nt peak">C#6</span>!). Os três têm o mesmo DNA: a <b>escala de Si maior</b> nas veias,
  e cada um termina <b>na porta da próxima seção</b>. Aprende um, metade do outro já está na mão.
</div>

{s3v}

<div class="tip">
  <h3>♻️ O Verso 3 é um "greatest hits" da Parte 1</h3>
  <b>"'Cause nothin' lasts forever"</b> e <b>"Even cold November rain"</b> são <i>literalmente</i> as frases 5 e 8 da Parte 1
  (nota por nota). <b>"We still can find a way"</b> é irmã das frases 4/6/8, e a abertura <b>"And when your fears subside"</b>
  recicla o pulo do "We've been through this". Se você domina a Parte 1, o Verso 3 sai quase de graça.
</div>

{s2s3}

<div class="tip">
  <h3>🎸 A arquitetura do gigante — 5 fases e uma porta</h3>
  <b>1) A cama</b> (c. 124–131): <b>B | F#/A# | G#m | F# | E | F#</b> ×2 — a escadinha
  <span class="nt">B2 A#2 G#2 F#2 E2</span> descendo nos graves, um acorde por degrau.<br>
  <b>2) O mergulho</b> (c. 132–133): o último eco de Si maior… e <b>um compasso de silêncio TOTAL</b> —
  neste trecho do MIDI não toca nada, nem bateria.<br>
  <b>3) O novo mundo</b> (c. 134–141): o piano assume o groove <b>G | A | B</b> — o mesmo do final! O
  <b>G natural</b> é a senha do mundo novo, e a música <b>acelera de 80 pra 105 bpm</b> exatamente aqui.<br>
  <b>4) O clímax</b> (c. 142–149): sobre a harmonia do final comprimida (<b>Bm | F# | E–D | G–A</b>),
  a lead grita <span class="nt">B5</span> → <span class="nt">A#5</span> →
  <span class="nt peak">C#6!</span>, flutua <span class="nt">F#5 G5 F#5 E5</span> e martela o uníssono
  <b>B+D</b> — e depois repete TUDO, nota por nota.<br>
  <b>5) O motor</b> (c. 150–151): o trem <span class="nt">F#5 G5 F#5 E5</span> /
  <span class="nt">C#5 D5 C#5 B4</span> que não para mais — enquanto o Axl já canta
  <i>"Don't ya think…"</i> por cima.<br>
  Por isso o Solo 3 é único: os outros <b>voltam pra casa</b> (o 1 pro refrão, o 2 pro Verso 3) —
  este <b>abre uma porta</b> e se dissolve no final, com o mesmo material rodando até o fade.
</div>

{s3o}

<div class="tip">
  <h3>🌟 A modulação do final — o "sol depois da chuva"</h3>
  A música inteira mora em <b>Si maior</b>… e o final sobe pra <b>Ré maior</b> (uma 3ª menor acima) —
  mas não do nada: o Solo 3 já preparou o terreno com o groove <b>G | A</b> e o G natural (desde o
  c. 134!). Quando o final chega, seu ouvido já mora lá.
  É por isso que o encerramento soa iluminado e épico. O groove é um loop de 5 compassos:
  <b>Bm | Bm | Bm–F# | E–D | G–A</b> — o <b>E maior</b> no meio é o tempero (repare como ele \"puxa\" o ouvido),
  e o G–A no fim é a mola que joga tudo de volta pro Bm. Na esquerda: um baixo por acorde
  (<code>B2 · F#2 · E2 · D2 · G2 · A2</code>), oitava 2, bem fraquinho — o brilho fica por conta dos solos.
</div>

<h2>🖐️ Mão esquerda (acompanhamento)</h2>
<div class="card">
<p>Comece simples — só o baixo, bem fraquinho:</p>
<table class="lh">
  <tr><th>Acorde</th><th>Simplezinho (1ª etapa)</th><th>Com corpo (2ª etapa)</th><th>Onde aparece</th></tr>
  <tr><td><b>E7M</b></td><td><code>E2 + E3</code></td><td><code>E2</code> + <code>G#3+Si3+Re#4</code></td><td>versos (o Ré# é a 7ª maior — o som "docinho")</td></tr>
  <tr><td><b>C#m7</b></td><td><code>C#2 + C#3</code></td><td><code>C#2</code> + <code>G#2+C#3+Mi3</code></td><td>versos</td></tr>
  <tr><td><b>F# / F#7</b></td><td><code>F#2 + F#3</code></td><td><code>F#2</code> + <code>La#3+Do#4</code></td><td>"for-E-ver", "If we could take the time", "We still can find a way"</td></tr>
  <tr><td><b>B</b></td><td><code>B2</code> (ou <code>B1+B2</code>)</td><td><code>B2</code> + <code>Fa#3+Si3</code></td><td>fim de frase (cadência) e intro (o acorde grande do c.15)</td></tr>
  <tr><td><b>B/D#</b></td><td><code>D#2</code></td><td><code>D#2</code> + <code>Fa#3+Si3</code></td><td>intro (o 2º degrau da escadinha) e refrão</td></tr>
  <tr><td><b>D#m</b></td><td><code>D#2 + D#3</code></td><td><code>D#2</code> + <code>Fa#3+La#3</code></td><td>refrão e ponte</td></tr>
  <tr><td><b>Final (Ré maior)</b></td><td><code>B2 / F#2 / E2 / D2 / G2 / A2</code></td><td>um por acorde do loop</td><td>o loop Bm | Bm | Bm–F# | E–D | G–A</td></tr>
</table>
<p class="small" style="margin-bottom:0">💡 <b>Upgrade:</b> no refrão, o disco alterna <code>D#m → E → B/D#</code> (ou <code>C#m</code>) dentro de cada linha;
no final do verso 2 ("So if you want to love me…") é um vamp <code>E ↔ F#</code> compasso a compasso até estourar no refrão.
E na intro: o baixo desce a escadinha <code>E → D# → C# → B</code> (tema) e depois pulsa <code>E → C# → B</code> (groove, 2×) —
no groove a direita nem se mexe, fica parada na moldura <code>Si3+Ré#4+Sol#4</code>.</p>
</div>

<h2>✈️ Como estudar a Parte 3</h2>
<div class="card">
<ol>
  <li><b>Comece pelo que é de graça:</b> "'Cause nothin' lasts forever / Even cold November rain" você JÁ sabe
      (frases 5 e 8 da Parte 1, nota por nota). Depois "So never mind the darkness" (mesmo molde) e "We still can find a way".</li>
  <li><b>As duas frases novas:</b> "And when your fears subside" (o pulo B3→G#4 que você já conhece do "We've been…")
      e o par "I know that you can love me / When there's no one left to blame" (o mergulho no G#3 e a subida no "no").</li>
  <li><b>O final é um loop:</b> aprenda as 5 frases, ligue cada uma ao seu acorde do loop
      (<span class="nt">Bm</span>·<span class="nt">Bm</span>·<span class="nt">Bm–F#</span>·<span class="nt">E–D</span>·<span class="nt">G–A</span>)
      e repita 4×. Fica bonito subir uma oitava na última repetição — é o papel das harmonias agudas do disco.</li>
  <li><b>Grave-se</b> tocando junto com o trecho final do disco — o loop é longo, é ótimo pra treitar flow e dinâmica.</li>
</ol>
</div>

<h2>🗺️ Guia de montagem — a música inteira, de ponta a ponta</h2>
<div class="card">
<p><b>169 compassos, ~9 minutos</b> — e você já tem TODAS as notas: é só seguir a fila.
Os números de compasso são os do nosso MIDI (a referência que usamos o projeto inteiro).
A letra entre aspas é a deixa: quando ouvir ela chegando, a seção é aquela.</p>
{guide_table_html()}
</div>

<div class="tip">
  <h3>🎸 E os solos? (como tocar a música inteira sem tocar os solos)</h3>
  Nos solos 1 e 2 a cama é a <b>família do verso</b> (E, C#m, B, F#) — toque como se fosse um verso
  sem letra: baixo nos tempos, moldura na direita, e deixe o disco brilhar por cima. No solo 3, a cama
  é a <b>escadinha nos graves</b> (B → A# → G# → F# → E) e depois o groove <b>G | A</b> — o mesmo do
  final, que você já tem. E agora <b>os três solos estão transcritos no mapa</b>, se um dia quiser
  brilhar você mesmo. Lembre: no disco o piano NUNCA para — ele é a cama o tempo todo.
  Tocar a cama já é tocar a música.
</div>

<div class="tip">
  <h3>🧵 As 6 costuras (é onde todo mundo se perde)</h3>
  <b>1) Refrão 1 → Ponte:</b> o refrão morre no F# suspenso (pergunta no ar) — a ponte responde
  <i>baixinho</i>, descendo pro D#m. É a queda de volume mais dramática da música.<br>
  <b>2) Ponte → Solo 1:</b> a última linha termina em F# SECO — e o Slash decola no vai-e-vem G#↔F#.<br>
  <b>3) Refrão 2 → Solo 2:</b> de novo o F# suspenso — e a resposta é a escada C#4→C#5.<br>
  <b>4) Solo 2 → Verso 3:</b> o solo aterrissa no C#5 e o "And when your fears subside" entra no
  B3 — uma nota de distância.<br>
  <b>5) Verso 3 → Solo 3:</b> o \"Even cold November rain\" segura no B3→, a guitarra responde gritando
  (F#5 → B4)… e depois da cama clássica vem o mergulho: <b>um compasso de silêncio TOTAL</b> — e o
  piano assume o groove G | A (a música acelera pra 105 bpm aqui!).<br>
  <b>6) Solo 3 → Final:</b> quando o motor F#–G–F#–E começar a rodar, prepare a mão: \"Don't ya think…\"
  entra no <span class=\"nt\">D4</span> — a primeira nota da região nova (Ré maior!) — <b>por cima do
  solo, que continua rodando até o fade</b>.
</div>

<div class="card">
<h3 style="margin:0 0 10px">✈️ Roteiro pra primeira rodada inteira</h3>
<ol>
  <li><b>Antes de tudo:</b> ouça o disco com o guia aberto, acompanhando as 12 seções — marque
      onde cada uma entra (a letra é a deixa).</li>
  <li><b>Ensaie só as costuras:</b> a última frase de cada seção + a primeira da seguinte
      (a lista das 6 acima). A mão tropeça aí, não no meio.</li>
  <li><b>Nos solos, toque a cama</b> (ou cante junto — também conta!).</li>
  <li><b>Se perder, NÃO pare:</b> segura o acorde da seção (quase sempre E, C#m ou B) e espera a
      próxima entrada — a música sempre volta pra casa.</li>
  <li><b>Duas ou três rodadas assim, depois grave-se</b> e compare com o disco. Aí é só curtir. 🎹</li>
</ol>
</div>

<div class="tip">
  <h3>🏆 Status do projeto</h3>
  <b>Toda a estrutura da música está mapeada:</b> intro, versos 1–3, refrões (com a variação do 2º),
  ponte (cama + letra), o final em Ré maior — e, de bônus, <b>os TRÊS solos nota a nota</b>, do
  vai-e-vem do Solo 1 ao C#6 do gigante. Sobrou pra um dia, se a curiosidade apertar: só a
  <b>linha cantada da ponte</b> (que não existe no nosso MIDI — precisaria de outra fonte).
</div>

<footer>Mapa conferido nota a nota com a gravação original (MIDI da performance). Versos/refrão na região F#3–B4
(uma oitava abaixo da voz); intro, solos e final no registro real — a intro abre no E5, a fanfarra dos sopros
chega ao F#5, os solos 1 e 2 coroam no B5 e o solo 3 chega ao C#6 (a nota mais aguda da música inteira);
o final mora no D4–E4, já em Ré maior. Ponte: cama de acordes conferida
em 4 fontes (a linha cantada não consta no MIDI).</footer>
</div>
</body>
</html>"""
    return html

# ── saídas: a pasta ../saidas desta música (a fábrica roda de qualquer lugar) ──
from pathlib import Path as _P
SAIDAS = _P(__file__).resolve().parent.parent / "saidas"
SAIDAS.mkdir(exist_ok=True)

if __name__ == "__main__":
    print(chat_map())
    with open(SAIDAS / "mapa-musical-november-rain.html", "w", encoding="utf-8") as f:
        f.write(build_html())
    print("\n[HTML atualizado: mapa-musical-november-rain.html]")
