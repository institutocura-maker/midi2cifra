#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAPA MUSICAL — PATIENCE (Guns N' Roses, "GN'R Lies", 1988)
Fonte única de verdade: patience.mid (bitmidi.com/uploads/51380.mid)

Tom: DÓ MAIOR (corpo principal sem sustenidos; temperos: C# do A7, F# do D/ponte)
Grade: 150 compassos, 4/4, 120 bpm no MIDI (disco soa mais largo, ~5:56)
Registro: o assobio está no registro REAL (G5–D6), como a intro do November Rain.

Estrutura (reconhecimento, compassos do MIDI):
  c1      contagem sussurrada (vazia no MIDI)
  c2–25   INTRO — assobio (C G A7 D ×2, 2 compassos cada + C G C Em C G D D)
  c26–41  VERSO 1 (6 linhas — "Shed a tear…" + "Was a time…")
  c42–57  REFRAO 1 ("Said, woman…" + "Said, sugar…")
  c58–63  eco "patience…" (vocalise agudo)
  c64–79  VERSO 2 ("I sit here on the stairs…")
  c80–101 REFRAO 2 (variação + "We won't fake it…") + ecos
  c102–121 SOLO do Slash (20 compassos, família do Ré; teto F#6)
  c122–128 interlúdio
  c129–147 PONTE cantada EM RÉ MAIOR ("I've been walking the streets…")
          — harmonias (pista 'axl2') só a partir do c137 ("need you")
  c148–150 o último "patience…" se despede

API das frases (irmã do gera_mapa.py):
  dict(label, chords=[(acorde, idx)], syls, notes=[[..]], peak, note)
  "→" = nota longa · "·" = silêncio · "›" liga notas do mesmo tempo
"""

# ============================================================ INTRO — O ASSOBIO (c. 2–25)
# Cada frase = 2 compassos = 8 tempos (+ "e" quando tem anacruse).
# Cama: C | G | A7 | D ×2 (2 compassos cada) + C | G | C | Em | C | G | D | D.
INTRO = [
    dict(label="O convite — violões sozinhos (c. 2–3)", chords=[("C", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8", "e"],
         notes=[["·"], ["·"], ["·"], ["·"], ["·"], ["·"], ["·"], ["·"], ["G5"]],
         note="Dois compassos só de violão (a cama de C arpejada). No piano: C2 na esquerda, "
              "C4-E4-G4 de leve na direita. O assobio chega DE FININHO, no contratempo do último "
              "tempo: um G5 plantado — a 5ª do acorde, a nota mais neutra possível. "
              "Quem chega assim, quer ser ouvido."),
    dict(label="O tema canta (c. 4–5)", chords=[("G", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["B5→"], ["·"], ["·"], ["A5", "G5→"], ["·"], ["·"], ["A5"], ["B5→"]], peak=0,
         note="O tema: B5 segurado por 3 tempos — a 3ª do G. O assobio canta a harmonia: "
              "cada frase pousa numa nota do acorde de baixo."),
    dict(label="O tempero aparece (c. 6–7)", chords=[("A7", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["A5"], ["G5", "E5"], ["E5→"], ["·"], ["·"], ["·"],
                ["B5", "A5"], ["G5", "A5"]],
         note="O A7 entra (o tempero da música). Repare: o C# mora na CAMA, não no assobio — "
              "que só usa A, G e E. Sabedoria de melodista: deixa o acorde fazer o drama."),
    dict(label="O pouso (c. 8–9)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["A5→"], ["·"], ["·"], ["F#5"], ["E5"], ["D5→"], ["·"], ["·"]],
         note="O pouso no D: F#5 (a 3ª do acorde) e a escadinha E5→D5. O formato do assobio: "
              "segura, responde, desce. É a gramática de todas as frases."),
    dict(label="A resposta — e o PICO: D6! (c. 10–11)", chords=[("C", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["·"], ["G5"], ["G5", "A5"], ["·"], ["B5"], ["D6", "B5"],
                ["B5", "A5"], ["G5"]], peak=5,
         note="A resposta repete o convite… e coroa no D6 — o pico do assobio inteiro! Sobre o "
              "C, o D é a 9ª: a nota 'brilhante'. Um degrau acima do B5 da abertura — repetir a "
              "frase um pouco mais alto, o truque favorito do Slash (lembra do Solo 1, c. 77→81?)."),
    dict(label="A volta mansa (c. 12–13)", chords=[("G", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["·"], ["B5", "A5"], ["B5"], ["A5", "G5"], ["G5→"], ["·"], ["·"], ["·"]],
         note="A calma depois do pico: G5 comprido sobre o G — a tônica em pessoa. Respira. "
              "(Aqui o transcritor emagreceu as guitarras — figurações agudas respondendo; "
              "a cama da cifra segue: G.)"),
    dict(label="O bordado (c. 14–15)", chords=[("A7", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["·"], ["A5", "G5"], ["A5", "G5"], ["E5", "A5"],
                ["A5", "G5", "E5", "A5"], ["A5→"], ["·"], ["B5→"]],
         note="O bordado: pares de notas no contratempo (A-G, A-G, E-A…). Quase uma fala — "
              "o assobio conversando. Termina subindo pro B5: prepara o pouso."),
    dict(label="O pouso de novo (c. 16–17)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["F#5→"], ["·"], ["·"], ["E5", "D5"], ["D5→"], ["·"], ["·"], ["·"]],
         note="Irmão do pouso (c. 8–9): mesma curva, agora começando no F#5 e caindo pro D5 "
              "comprido. Reciclagem de novo! (Na guitarra há um deslize cromático D#-E-F# "
              "anunciando o D — enfeite, não se preocupe com ele.)"),
    dict(label="A terceira frase — a última volta (c. 18–19)", chords=[("C", 0), ("G", 4)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["·"], ["·"], ["G5", "A5", "G5"], ["B5"], ["A5", "G5→"], ["·"], ["G5"], ["·"]],
         note="Material novo — a última volta antes da entrega. E repare: continua morando nas "
              "mesmas notas (G, A, B, E). O vocabulário é pequeno; as frases é que mudam."),
    dict(label="O segundo pico: C6! (c. 20–21)", chords=[("C", 0), ("Em", 4)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["·"], ["C6", "B5"], ["A5"], ["G5", "E5"], ["E5"], ["G5", "G5"],
                ["A5", "G5"], ["E5"]], peak=1,
         note="O segundo pico: C6 — a oitava da tônica, em cima do acorde de C! A coroa do "
              "assobio. E dali cai em escadinha B5-A5-G5-E5… pra começar a despedida."),
    dict(label="A descida — a mão pra voz (c. 22–23)", chords=[("C", 0), ("G", 4)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["·"], ["C5"], ["E5", "G5"], ["E5"], ["E5"], ["D5"], ["G4"], ["G5"]], peak=6,
         note="A descida pra região da VOZ: o assobio afunda uma oitava até o G4 — exatamente "
              "a nota em que o Axl vai entrar. A passagem de bastão está ensaiada."),
    dict(label="A entrega (c. 24–25)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["F#5→"], ["·"], ["G5→"], ["·"], ["A5→"], ["·"], ["·"], ["·"]], peak=4,
         note="A última nota fica no ar: A5 (a 5ª do D) por três tempos… e quem responde é a "
              "VOZ: \"Shed a tear\" — no G4, c. 26. É a porta do Verso 1."),
]
INTRO_FILLS = {}

INTRO_NOTA = ("Assobio no REGISTRO REAL (G5–D6), as notas do disco — igual à intro do November "
              "Rain. Cada frase = 2 compassos = 8 tempos; \"·\" = tempo de violão; \"›\" liga "
              "notas do mesmo tempo. Quer acompanhar cantando? Toque o assobio uma oitava abaixo "
              "(G4–D5) — o desenho é o que importa.")
CAMA_INTRO = ("Cama (mão esquerda, um baixo por acorde): C → C2 · G → G2 · A7 → A2 (o C# do "
              "tempero fica por conta da direita, se quiser) · D → D2. A direita pode ficar "
              "parada no acorde batido de leve — os violões do disco arpejam, mas a moldura "
              "estática já soa a música.")

# ============================================================ VERSO 1 — "Shed a tear…" (c. 26–41)
# A voz entra no G4 (c. 26, tempo 2) — a nota exata em que o assobio desceu (c. 23).
# Grade: 2 voltas de 8 compassos (C C | G G | A7 A7 | D D); L4–L6 repetem L1–L3.
# Cama idêntica à da intro. Compassos 33 e 41: respiração (só as guitarras).
VERSO_1 = [
    dict(label="L1 · “Shed a tear 'cause I'm missing you” (c. 26–27, em C)", chords=[("C", 0)],
         syls=["Shed", "a", "tear", "'cause", "I'm", "miss-", "ing", "you"],
         notes=[["G4"], ["G4"], ["G4"], ["G4"], ["G4"], ["A4"], ["A4"], ["B4", "G4", "G4"]],
         peak=7,
         note="A voz entra NO G4 — a nota exata que o assobio deixou no ar (c. 23): passagem de "
              "bastão combinada. E olha a simetria: o assobio começou no G5 (a 5ª, neutra); a voz "
              "começa no G4, a 5ª de novo, uma oitava abaixo. Cinco tempos quase falado — e só no "
              "“you” sobe ao B4, a 7ª maior do C: a nota da saudade."),
    dict(label="L2 · “I'm still alright to smile” (c. 28–29, em G)", chords=[("G", 0)],
         syls=["I'm", "still", "a-", "lright", "to", "smi-", "ile"],
         notes=[["D4"], ["B4"], ["B4"], ["B4"], ["A4"], ["G4"], ["G4", "G4→"]], peak=1,
         note="O “I'm” é pick-up: entra no D4, meia batida antes, e SALTA uma 6ª pro B4 — a 3ª do "
              "G, de novo a nota do acorde. O “smi-ile” partido em dois é o jeitinho íntimo do "
              "Axl: mesma nota (G4), duas sílabas."),
    dict(label="L3 · “Girl, I think about you every day now” (c. 30–32, A7 → D)",
         chords=[("A7", 0), ("D", 9)],
         syls=["Girl", "I", "think", "a-", "bout", "you", "ev-", "ery", "day", "now"],
         notes=[["A4"], ["A4"], ["A4"], ["A4"], ["B4"], ["B4"], ["A4"], ["A4"], ["A4"],
                ["A4", "F#4", "F#4", "E4", "D4→"]], peak=4,
         note="A frase mais longa (10 sílabas sem respirar): quase tudo em A4, a tônica do A7, "
              "esperando. O “bout” toca o teto B4 — a 9ª do A7, a mesma nota “brilhante” do pico "
              "do assobio (D6 sobre o C, c. 10)! E o “now” desaba em cascata: A4-F#4-F#4-E4-D4, "
              "antecipando o D que chega debaixo — a escadinha do pouso (c. 8–9), agora cantada. "
              "Depois, 1 compasso de respiração (c. 33)."),
    dict(label="L4 · “Was a time when I wasn't su-ure” (c. 34–35, em C)", chords=[("C", 0)],
         syls=["Was", "a", "time", "when", "I", "was-", "n't", "su-", "ure"],
         notes=[["G4"], ["G4"], ["G4"], ["G4"], ["G4"], ["A4"], ["A4"], ["B4", "G4"],
                ["G4", "A4", "G4"]], peak=7,
         note="Reciclagem pura: a melodia do “Shed a tear” de novo, quase nota por nota — até o "
              "desenho do “you” voltou no “su-ure”. Só mudam as palavras. O verso inteiro é "
              "2 voltas da mesma música."),
    dict(label="L5 · “But you set my mind at ease” (c. 36–37, em G)", chords=[("G", 0)],
         syls=["But", "you", "set", "my", "mind", "at", "ease"],
         notes=[["B4"], ["B4"], ["B4"], ["A4"], ["G4"], ["G4"], ["G4→"]], peak=0,
         note="Irmã do “I'm still alright” (c. 28–29), agora sem o pulo do pick-up: começa direto "
              "no B4 e desce a escada B-A-G. E o “ease” segura o G4 por 2 tempos — a tônica. O "
              "alívio da letra mora na nota mais estável que existe."),
    dict(label="L6 · “There is no doubt you're in my heart now” (c. 38–40, A7 → D)",
         chords=[("A7", 0), ("D", 8)],
         syls=["There", "is", "no", "doubt", "you're", "in", "my", "heart", "now"],
         notes=[["A3"], ["A4"], ["A4"], ["B4"], ["B4"], ["A4"], ["A4"], ["A4"],
                ["A4", "F#4", "F#4", "E4", "D4→"]], peak=3,
         note="O “There” entra numa oitava abaixo (A3 — na transcrição, quase falado: o momento "
              "mais íntimo do verso) e o final é o mesmo “now” em cascata do “day now”, caindo "
              "pro D4. Teto do verso: B4 no “doubt” (a 9ª do A7 de novo). A voz mora entre D4 e "
              "B4; o assobio, uma oitava acima. Depois, respiração (c. 41)."),
]
VERSO_1_FILLS = {}

VERSO_1_NOTA = ("A voz entra no G4 que o assobio deixou no ar — a passagem de bastão combinada. "
                "Cada linha = 1 acorde da cama (C → G → A7 → D), 2 voltas de 8 compassos, e as "
                "linhas 4–6 repetem a melodia das 1–3 quase nota por nota. Depois de L3 e L6, um "
                "compasso de respiração (c. 33 e 41). Bônus: o Verso 2 (c. 64–79, “I sit here on "
                "the stairs…”) usa este MESMO mapa, nota por nota — um mapa, dois versos.")

# ============================================================ REFRAO 1 — "Said, woman…" (c. 42–57)
# A voz sobe ao C5 (oitava da tônica) e mora lá. Harmonia: C | G | C | Em | C | G | D —
# o A7 do verso vira Em. Program change da pista: assobio (inst 78) até c. 26 t2;
# daí em diante é VOZ (inst 54) — inclusive o eco em falsete (c. 57–62).
# Transparência: nos c. 54–55 a transcrição das guitarras silencia (dropout) —
# segue a cifra e o paralelo com a 1ª metade: C (c. 54), G (c. 55).
REFRAO_1 = [
    dict(label="R1 · “Said, woman, take it slow” (c. 42–43, C → G)",
         chords=[("C", 0), ("G", 4)],
         syls=["Said,", "wo-", "man,", "take", "it", "slo-", "ow"],
         notes=[["C5"], ["C5"], ["C5"], ["D5"], ["G4"], ["G4"],
                ["G4", "G4", "G4", "E4"]], peak=3,
         note="O refrão abre um degrau acima: “Said” já chega no C5 — a oitava da tônica, o novo "
              "teto (o verso morava abaixo do B4). O “take” toca o D5 e a linha escorrega pelo G "
              "até o E4 — a porta do Em que vem aí."),
    dict(label="R2 · “It'll work itself out fine” (c. 44–45, C → Em)",
         chords=[("C", 0), ("Em", 6)],
         syls=["It-", "'ll", "work", "it-", "self", "out", "fine"],
         notes=[["C5"], ["C5"], ["C5"], ["C5"], ["B4"], ["E4"], ["E4"]], peak=0,
         note="Quatro C5 seguidos — o refrão não sobe mais que o verso: ele MORA mais alto. O "
              "“out” entra antecipado no contratempo e o “fine” cai no tempo forte exatamente "
              "junto com o Em chegando — e termina no E4, a raiz do acorde: conforto."),
    dict(label="R3 · “All we need is just a little patience” (c. 46–49, C → G → D)",
         chords=[("C", 0), ("G", 5), ("D", 9)],
         syls=["All", "we", "need", "is", "just", "a", "lit-", "tle", "pa-", "tience"],
         notes=[["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["B4"], ["A4"], ["G4"],
                ["G4", "B4", "B4", "A4→"]], peak=2,
         note="Seis C5 martelados — “all we need is just a” inteiro na mesma nota. Aí desce a "
              "escadinha B-A-G… e a palavra “patience” é a única que GANHA movimento (G-B-B-A): "
              "a palavra-chave da música é a única que dança. Termina no A4, a 5ª do D — e é "
              "desse fio que o eco vai subir (c. 58). Depois, 1 compasso de guitarra (c. 49)."),
    dict(label="R4 · “Said, sugar, make it slow” (c. 50–51, C → G)",
         chords=[("C", 0), ("G", 4)],
         syls=["Said,", "su-", "gar,", "make", "it", "slo-", "ow"],
         notes=[["C5"], ["C5"], ["C5"], ["D5"], ["G4"], ["G4"],
                ["G4", "G4", "G4", "E4"]], peak=3,
         note="Mesma melodia, só troca a palavra: “woman” vira “sugar” — a letra fala com duas "
              "pessoas, a música não muda um centímetro. (A transcrição tensiona o “slow” de um "
              "jeitinho diferente na repetição — mesmo lick, mesma graça.)"),
    dict(label="R5 · “And we'll come together fine” (c. 52–53, C → Em)",
         chords=[("C", 0), ("Em", 6)],
         syls=["And", "we'll", "come", "to-", "geth-", "er", "fine"],
         notes=[["C5"], ["C5"], ["C5"], ["C5"], ["B4"], ["E4"], ["E4"]], peak=0,
         note="De novo a melodia do “It'll work itself out fine”, nota por nota — reciclagem "
              "dupla. E “come together” no mesmo C5 das duas vozes do diálogo: a letra pede "
              "união, a música obedece — todo mundo na mesma nota."),
    dict(label="R6 · “All we need is just a little patience” (c. 54–57, C → G → D)",
         chords=[("C", 0), ("G", 6), ("D", 9)],
         syls=["All", "we", "need", "is", "just", "a", "lit-", "tle", "pa-", "tience"],
         notes=[["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["B4"], ["A4"],
                ["G4", "G4", "B4", "B4", "A4→"]], peak=2,
         note="A segunda volta sobe um degrau: o “a little” agora mora em C5-B4-A4 (antes era "
              "B4-A4-G4) — repetir a frase mais alta, o MESMO truque do assobio (convite → "
              "resposta no pico, c. 10)! E o “patience” estica o melisma mais ainda, terminando "
              "no A4 de novo: o fio pro eco. (Nos c. 54–55 a transcrição das guitarras silencia "
              "— a cifra e o paralelo seguram C e G; nos c. 56–57 elas voltam num colchão "
              "comprido de D.)"),
]
REFRAO_1_FILLS = {}

REFRAO_1_NOTA = ("O refrão abre os pulmões: a voz sobe ao C5 — a oitava da tônica — e passa a "
                 "MORAR lá (o teto do verso era B4). A roda harmônica gira C | G | C | Em | "
                 "C | G | D: o A7 do verso vira Em — o tempero vira melancolia — e o D, a "
                 "chegada, fica reservado pra palavra “patience”. As linhas 4–6 repetem as 1–3 "
                 "nota por nota (“woman” → “sugar”), com o “little patience” final um degrau "
                 "mais alto que o primeiro.")

# ============================================================ ECO — o falsete (c. 57–63; repete idêntico em c. 95–101)
# Voz em falsete (inst 54 — não é o assobio), registro G5–A5: o refrão virado do avesso.
# Cama: só o colchão de D das guitarras (notas de 3–4 tempos nos c. 56–57 e 94–95).
ECO = [
    dict(label="E1 · O eco chega (c. 57–58, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8", "e"],
         notes=[["·"], ["·"], ["·", "G5→"], ["·"], ["G5→"], ["·"], ["·"], ["·"], ["A5"]],
         note="O refrão termina no A4 — e quem responde é a própria voz do Axl em FALSETE, uma "
              "oitava acima (a pista confirma: segue no instrumento “voz”, não assobio). Dois "
              "G5 — o primeiro entra no contratempo do tempo 3 — e um A5 de fininho no fim do "
              "c. 58. O registro é o do assobio; quem aprendeu a intro já sabe o caminho."),
    dict(label="E2 · O eco sobe (c. 59–60, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["A5", "A5→"], ["·"], ["·"], ["·"], ["·"], ["·"], ["D5→"], ["·"]],
         note="O A5 se dobra (tempo 1 e contratempo) e segura um tempo e meio… aí, no tempo 3 "
              "do c. 60, cai o D5: a tônica do acorde — o eco resolvendo em casa. (Por baixo, "
              "um aceno de A7 — o C# de sempre — passa no fim do c. 59.)"),
    dict(label="E3 · O eco se despede (c. 61–62, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["D5→"], ["·"], ["D5", "B4", "B4"], ["·"], ["B4"], ["A4→"], ["·"], ["·"]],
         note="A assinatura: D5 preso de novo e a tercina D5-B4-B4 (três notas iguais de 2/3 de "
              "tempo na transcrição) descendo pro B4… e o A4 — a MESMA nota em que o refrão "
              "terminou. Eco e refrão acabam em casa juntos. (No c. 63 só as guitarras: licks "
              "agudos espiando o F#6 que o solo vai usar.)"),
]
ECO_FILLS = {}

ECO_NOTA = ("Depois do refrão, a voz do Axl responde em falsete — o “eco” — subindo ao registro "
            "onde o assobio morava (G5–A5). Embaixo, só o colchão de D das guitarras. É o refrão "
            "do avesso: mesma tônica, uma oitava acima, sem letra. Toca DUAS vezes: após o "
            "Refrão 1 (c. 57–63) e após o Refrão 2 (c. 95–101) — idêntico, nota por nota.")

# ============================================================ REFRAO 2 — a variação (c. 80–101)
# Melodia: cópia EXATA do Refrão 1 (c. 80–94 = c. 42–56, verificado nota por nota no dump;
# eco c. 95–100 = cópia de E1–E3). O que muda são as PALAVRAS — letra da variação confirmada
# em 3 fontes (letras.com, Shazam, lyrics.com). O grito "we won't fake it" NÃO está no MIDI
# (transcrição comprimida) → entra como fill com a letra, SEM nota inventada (regra do NR).
# Cama: idêntica à do Refrão 1 (C G C Em C G D); c. 93 = dropout das guitarras (como c. 55).
REFRAO_2 = [
    dict(label="R7 · “Said, woman, take it slow” (c. 80–81, C → G)",
         chords=[("C", 0), ("G", 4)],
         syls=["Said,", "wo-", "man,", "take", "it", "slo-", "ow"],
         notes=[["C5"], ["C5"], ["C5"], ["D5"], ["G4"], ["G4"],
                ["G4", "G4", "G4", "E4"]], peak=3,
         note="Mesma música do começo ao fim: a voz não muda UMA nota em relação ao Refrão 1 "
              "(verificado compasso a compasso no MIDI). O que muda é o que se DIZ — o refrão "
              "agora é uma conversa que já evoluiu."),
    dict(label="R8 · “And things will be just fine” (c. 82–83, C → Em)",
         chords=[("C", 0), ("Em", 5)],
         syls=["And", "things", "will", "be", "just", "fine"],
         notes=[["C5"], ["C5"], ["C5"], ["C5"], ["B4"], ["E4", "E4"]], peak=0,
         note="“It'll work itself out fine” (vai SE RESOLVER sozinho) vira “things will be just "
              "fine” (está ficando bem): do futuro para o presente. Uma sílaba a menos — o "
              "“fine” engole sozinho as duas notas que antes eram de “out fine”."),
    dict(label="R9 · “You and I'll just use a little patience” (c. 84–87, C → G → D)",
         chords=[("C", 0), ("G", 5), ("D", 9)],
         syls=["You", "and", "I'll", "just", "use", "a", "lit-", "tle", "pa-", "tience"],
         notes=[["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["B4"], ["A4"], ["G4"],
                ["G4", "B4", "B4", "A4→"]], peak=2,
         note="A grande mudança é de PRONOME: “all we need is just…” vira “YOU AND I'LL just "
              "use…” — do pedido coletivo pro pacto a dois. Mesmas notas, mesma escadinha — só "
              "que agora a palavra “patience” pertence a alguém. Depois, 1 compasso de "
              "respiração (c. 87)."),
    dict(label="R10 · “Said, sugar, take the time” (c. 88–89, C → G)",
         chords=[("C", 0), ("G", 4)],
         syls=["Said,", "su-", "gar,", "take", "the", "time"],
         notes=[["C5"], ["C5"], ["C5"], ["D5"], ["G4"],
                ["G4", "G4", "G4", "G4", "E4"]], peak=3,
         note="“Make it slow” vira “take the time”: o conselho da primeira vez (“vai devagar”) "
              "virou instrução de uso (“toma o tempo”). E o “time” estica o mesmo melisma do "
              "“slow” — 5 notas numa sílaba só."),
    dict(label="R11 · “'Cause the lights are shining bright” (c. 90–91, C → Em)",
         chords=[("C", 0), ("Em", 6)],
         syls=["'Cause", "the", "lights", "are", "shin-", "ing", "bright"],
         notes=[["C5"], ["C5"], ["C5"], ["C5"], ["B4"], ["E4"], ["E4"]], peak=0,
         note="“And we'll come together fine” vira “'cause the lights are shining bright”: da "
              "promessa pra o cenário — a cena iluminada em vez do combinado. A mesma escada "
              "C5-C5-C5-C5-B4-E4-E4, palavra por palavra."),
    dict(label="R12 · “You and I've got what it takes to make it” (c. 92–94, C → G → D)",
         chords=[("C", 0), ("G", 6), ("D", 9)],
         syls=["You", "and", "I've", "got", "what", "it", "takes", "to", "make", "it"],
         notes=[["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["C5"], ["B4"], ["A4"],
                ["G4", "G4", "B4", "B4", "A4→"]], peak=2,
         note="A frase mais confiante da música: “you and I'VE GOT WHAT IT TAKES” — sete C5 "
              "martelados de certeza. E o “make it” cai no mesmo melisma do “patience”: fazer "
              "é a nova palavra-chave. (Nos c. 92–93 o dropout das guitarras de novo — a cifra "
              "e o paralelo seguram C e G, como no Refrão 1.)"),
]
REFRAO_2_FILLS = {5: "E logo o GRITO do disco: “We won't fake it! / I'll never break it! / "
                     "'Cause I can't take it!” (c. 94–95, em cima do colchão de D). O MIDI não "
                     "transcreve as notas dele — é ritmo quase falado — e o mapa não inventa "
                     "nota: fica a letra, do jeito que o disco grita. Depois disso, o eco de "
                     "falsete repete (c. 95–101 = E1–E3 idêntico) e as guitarras despacham pro "
                     "solo com licks de F#6 (c. 101)."}

REFRAO_2_NOTA = ("O Refrão 2 é o Refrão 1 com as palavras trocadas — a transcrição copia a "
                 "melodia nota por nota (c. 80–94 = c. 42–56, verificado). Mas a letra evolui: "
                 "o pedido coletivo (“all we need”) vira pacto a dois (“you and I”), a promessa "
                 "vira cena (“lights shining bright”), a certeza chega (“what it takes to make "
                 "it”) — e explode o grito “we won't fake it”. A música parada, a letra "
                 "correndo: quem muda aqui é o texto, não a melodia. (Letra da variação "
                 "conferida em 3 fontes; o grito não está no MIDI — entra como letra, sem "
                 "nota inventada.)")

CAMA_REFRAO = ("Cama do refrão: C → C2 · G → G2 · Em → E2 (o único acorde novo — na direita, "
               "G4-B4-E5) · D → D2. Os baixos da intro servem o refrão inteiro; só o Em é "
               "estreante.")

# ============================================================ SOLO — a guitarra canta o refrão (c. 102–121)
# 20 compassos sem voz. Pista 'Izzy' vazia aqui (a cama não foi transcrita) — os acordes
# indicados são IMPLÍCITOS, lidos nas notas do próprio solo: C6=tônica do C, B5=3ª do G,
# E6=raiz do Em, F#6=3ª do D → 1ª metade = a roda do refrão (C G C Em C G D);
# 2ª metade = o fim da roda do verso (G → A7 → D). Teto da música: F#6 (c. 109–110).
# Licks da 2ª metade em colcheias (D-E-G no campo do G; A-G-E no campo do A7).
SOLO = [
    dict(label="S1 · O solo canta: “Said, woman…” (c. 102–103, C implícito)", chords=[("C", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["·"], ["·"], ["·"], ["C6", "B5"], ["C6→"], ["·"], ["C6", "D6"],
                ["C6", "B5"]],
         note="O solo abre CANTANDO o refrão, uma oitava acima da voz: o pickup C6-B5 no tempo 4 "
              "e a tônica C6 segurada 2 tempos — o “Said” da guitarra. Quem aprendeu o refrão "
              "já sabe cantar este solo nota por nota."),
    dict(label="S2 · “…take it slow…” (c. 104–105, G → C)", chords=[("G", 0), ("C", 4)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["B5→"], ["·"], ["G5"], ["C6", "B5"], ["C6→"], ["·"], ["C6", "D6"],
                ["B5", "E6"]],
         note="O “take it slow” da guitarra: B5 comprido — a 3ª do G, a mesma nota do “you” do "
              "verso! E o pickup C-B no fim do compasso: o vício de linguagem do solo inteiro, "
              "toda frase termina preparando a próxima."),
    dict(label="S3 · “…it'll work itself out fine” (c. 106–107, Em → C)",
         chords=[("Em", 0), ("C", 4)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["E6→"], ["·"], ["·"], ["C6", "B5"], ["C6→"], ["·"], ["C6", "D6"],
                ["C6", "B5"]],
         note="O “fine” do refrão, versão guitarra: E6 por TRÊS tempos — a raiz do Em, a nota "
              "mais longa do solo até aqui. O refrão terminava cada frase na raiz do acorde; "
              "a guitarra obedece à mesma gramática."),
    dict(label="S4 · A escalada do “patience” (c. 108–109, G → D)",
         chords=[("G", 0), ("D", 4)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["B5", "A5"], ["G5"], ["G5"], ["G5", "E6"], ["E6", "D6"], ["D6"], ["D6→"],
                ["·", "F#6"]],
         note="A escadinha B-A-G do “lit-tle pa-”… e aí E6-D6 — a 9ª e a tônica do D, as notas "
              "“brilhantes” de novo — até o F#6 entrar NO CONTRATEMPO do último tempo: o grito "
              "chegando por baixo da mesa."),
    dict(label="S5 · O PICO: F#6! (c. 110, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["F#6", "E6"], ["D6", "E6"], ["D6"], ["·"]], peak=0,
         note="O teto da música inteira: F#6 — a 3ª do D, uma oitava e uma 6ª acima do A4 em "
              "que a voz terminava o “patience”. A guitarra grita a palavra que a voz não "
              "aguenta. E desce devagar: F#-E-D-E-D — o grito virando fala."),
    dict(label="S6 · A resposta, uma oitava abaixo (c. 111–112, em G)", chords=[("G", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["D5", "D5"], ["E5", "G5"], ["D5", "D5"], ["C5", "D5"], ["A4", "A4"],
                ["B4", "D5"], ["A4", "A4"], ["G4"]],
         note="A segunda metade do solo desce uma oitava e conversa: licks em colcheias no "
              "campo do G (D-E-G). Frase alta no pico, resposta baixa embaixo — o solo "
              "dialogando consigo mesmo."),
    dict(label="S7 · De novo — e sobe (c. 113–114, G → A7)",
         chords=[("G", 0), ("A7", 4)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["D5", "D5"], ["E5", "G5"], ["D5", "D5"], ["C5", "D5"], ["E5", "G5"],
                ["A5", "A5", "G5"], ["E5"], ["G5", "A5"]],
         note="A mesma frase de novo, nota por nota — e aí a subida: E-G-A até o A5, mudando "
              "pro campo do A7 (o tempero!). Repetir a frase e SUBIR: o truque da casa "
              "inteira — o assobio fez (c. 10), o refrão 2 fez, agora o solo."),
    dict(label="S8 · O martelar do A7 (c. 115–116, em A7)", chords=[("A7", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["A5", "A5"], ["A5", "G5"], ["A5", "E5"], ["G5", "A5"], ["A5", "G5"],
                ["A5", "E5"], ["G5", "A5"], ["G5", "B5"]],
         note="O martelar: A-G-E-E-G-A — a espinha do A7 (tônica, 7ª, 5ª) socada em colcheias, "
              "subindo e descendo. Sem letra pra cantar, a guitarra começou a CONTAR. E o B5 "
              "no fim arma o pouso."),
    dict(label="S9 · O pouso alto (c. 117–118, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["B5", "A5"], ["A5→"], ["·"], ["·"], ["A5→"], ["·"], ["·"], ["·"]],
         note="O pouso: B5-A5 e o A5 segurado ~5 tempos (c. 117–118) — a 5ª do D. Depois do "
              "grito, a nota mais comprida do solo inteiro é uma nota QUIETA."),
    dict(label="S10 · A descida e o deslize F-F# (c. 119–120, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["E5"], ["D5→"], ["·"], ["B4", "A4"], ["F4", "F#4"], ["A4", "D4"], ["D4→"],
                ["·", "F#5"]],
         note="A descida pra casa: E5-D5… B4-A4, e o walk cromático F4-F#4-A4-D4 — o deslize "
              "que anuncia o D, primo do D#-E-F# da intro (c. 16). A música inteira usa o "
              "mesmo truque de aproximação."),
    dict(label="S11 · O F#5 no ar (c. 121, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["F#5"], ["F#5→"], ["·"], ["·"]],
         note="O solo acaba com o F#5 no ar — 4 tempos de 3ª do D, a pergunta suspensa. Quem "
              "responde é a ponte, logo ali, e ela vai morar justamente em Ré maior."),
]
SOLO_FILLS = {7: "Lembrete do contrato: o MIDI é a versão condensada do disco (5:00 contra "
                 "5:56). Onde o disco enche os trechos de runs, a transcrição traz o "
                 "esqueleto — e o esqueleto é o que está aqui, nota a nota."}

SOLO_NOTA = ("20 compassos sem voz — e a primeira surpresa: a guitarra ABRE o solo cantando o "
             "refrão (“Said, woman, take it slow…”), uma oitava acima da voz, quase nota por "
             "nota — até o “fine” virar um E6 comprido. Aí a escalada: F#6, o teto da música "
             "inteira. A segunda metade desce uma oitava e conversa (frase alta / resposta "
             "baixa), martela o A7 e pousa no D, com o F#5 final no ar — a porta da ponte. "
             "Transparência: a transcrição traz SÓ a guitarra do solo (a cama não foi escrita; "
             "os acordes indicados são implícitos, lidos nas notas do próprio solo) — 1ª "
             "metade = a roda do refrão, 2ª metade = o fim da roda do verso (G → A7 → D).")

CAMA_SOLO = ("Cama do solo (a transcrição não traz — sugestão na mão esquerda): 1ª metade = a "
             "roda do refrão C | G | C | Em | C | G | D (os baixos de sempre: C2 G2 E2 A2 "
             "D2); 2ª metade = G | A7 | D — o fim da roda do verso.")

# ============================================================ INTERLÚDIO — a aterrissagem (c. 122–128)
# 7 compassos de guitarra entre o solo e a ponte. Convenção nova: "+" = notas JUNTAS
# (dyads — as guitarras tocam em pares aqui; "›" continua = nota após nota).
# A pista 'Izzy' volta a tocar aqui (hiatus durante o solo).
INTERLUDIO = [
    dict(label="I1 · A cadência de novo (c. 122–123, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["B4", "A4"], ["F4", "F#4"], ["C5+D4→"], ["·", "F#5"], ["F#5", "F#5→"],
                ["·"], ["E5", "F#5"], ["·", "D5"]],
         note="A figura da descida do solo repete quase igual (c. 119–120): B-A e o deslize "
              "F-F#, caindo no D. A música se ajeita na mesa antes de falar."),
    dict(label="I2 · Os arpejos de D (c. 124–125, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["D5", "A4"], ["·", "G4"], ["G4", "D5+A4→"], ["·"], ["F#5+D5"],
                ["F#5+D5"], ["F#5+D5"], ["F#5+D5", "B4+G4"]],
         note="Violões em arpejo de Ré (D-F#-A), mansos — e o ritmo pontuado (curto-longo) dos "
              "pares F#5+D5, que atravessa a música toda. O B4+G4 no fim é o salto pro G."),
    dict(label="I3 · A aceleração (c. 126, em G)", chords=[("G", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["D5+G4", "D5+G4", "D5+G4"], ["D5+G4", "D5+G4", "G5+D5"],
                ["G5+D5", "G5+D5", "G5+D5"], ["G5+D5", "G5+D5", "G5+D5", "G5+D5"]],
         note="Em G: os pares G4+D5 aceleram de colcheias a semicolcheias e sobem até o G5 — o "
              "coração batendo mais rápido. Um compasso inteiro de rolagem: a respiração "
              "segura antes da ponte."),
    dict(label="I4 · Os sinos de Ré (c. 127–128, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["D6+A5→"], ["·"], ["·"], ["·"], ["F#6+D6→"], ["·"], ["·"], ["·"]],
         note="O AVISO: Ré maior aberto em oitavas altas — D+A, depois F#+D — 8 tempos de "
              "sino dizendo “a ponte vai ser aqui, e vai ser em Ré”. E é o F#6 de novo, o teto "
              "do solo, agora servindo de cortina."),
]
INTERLUDIO_FILLS = {}

INTERLUDIO_NOTA = ("7 compassos só de guitarra entre o solo e a ponte — a aterrissagem. "
                   "Convenção nova desta seção: “+” = notas JUNTAS (as guitarras tocam em "
                   "pares; “›” continua sendo nota após nota). A pista 'Izzy' volta a tocar "
                   "aqui, depois do hiatus do solo.")

# ============================================================ PONTE — em Ré maior: as ruas (c. 129–147)
# A modulação prometida: o corpo em Dó, a ponte em RÉ. Harmonia que CAMINHA: D ↔ G,
# até parar em D no "need you", escurecer (Dm7 — F4 na voz, C5 nas guitarras: a única
# cor menor da música inteira) e cair no G7 → D final.
# Transparência: a transcrição esqueletiza a voz aqui (~8 notas por linha — as notas
# longas seguram as palavras que o disco enfeita; "·" = a nota anterior segue valendo).
# As respostas "(a little patience, yeah)" moram na pista 'axl2' (a partir do c. 137).
PONTE = [
    dict(label="L1 · “I've been walking the streets at night” (c. 129–131, em D)",
         chords=[("D", 0)],
         syls=["I've", "been", "walk-", "ing", "the", "streets", "at", "night"],
         notes=[["D4"], ["B3"], ["F#4"], ["E4"], ["D4→"], ["G4"], ["G4"], ["F#4", "D4"]],
         note="A ponte abre em RÉ MAIOR — a mudança de mundo (o mesmo gesto do final do "
              "November Rain). E a voz entra em miniatura: pickup D4-B3, sobe F#-E-D… a ponte "
              "inteira vai morar nesse quarteto de notas (D-E-F#-G)."),
    dict(label="L2 · “Just trying to get it right” (c. 131–133, D → G)",
         chords=[("D", 0), ("G", 2)],
         syls=["Just", "try-", "ing", "to", "get", "it", "right"],
         notes=[["G4"], ["A4"], ["F#4"], ["E4"], ["D4→"], ["D4"], ["B3", "D4", "B3→"]],
         note="A moldura clássica: “walking” em D, “trying” em G — a harmonia CAMINHA, "
              "D ↔ G, um pé em cada calçada. As ruas da letra, traduzidas em acordes."),
    dict(label="L3 · “It's hard to see with so many around” (c. 133–134, em D)",
         chords=[("D", 0)],
         syls=["It's", "hard", "to", "see", "with", "so", "man-", "y", "a-", "round"],
         notes=[["F#4"], ["D4"], ["F#4→"], ["·"], ["·"], ["D4→"], ["D4"], ["B3"], ["D4"],
                ["B3→"]],
         note="O “see” esticado: F#4 por 2 tempos — a 3ª do D, a nota do pedido (a mesma do "
              "“you” do verso). E a multidão amontoada em poucas notas: D4-B3-D4-B3, gente "
              "empilhada."),
    dict(label="L4 · “You know I don't like being stuck in the crowd” (c. 135–137, D → G)",
         chords=[("D", 0), ("G", 5)],
         syls=["You", "know", "I", "don't", "like", "be-", "ing", "stuck", "in", "the",
               "crowd"],
         notes=[["F#4"], ["D4"], ["F#4→"], ["·"], ["·"], ["D4→"], ["D4"], ["D4"], ["F#4"],
                ["·"], ["F#4", "D4"]],
         note="De novo o par D→G — a terceira ida e volta. E o “crowd” termina no par F#4-D4 "
              "(3ª e tônica): a multidão não resolve, só aterrissa."),
    dict(label="L5 · “And the streets don't change but maybe the names” (c. 137–139, D → G)",
         chords=[("D", 0), ("G", 2)],
         syls=["And", "the", "streets", "don't", "change", "but", "may-", "be", "the",
               "names"],
         notes=[["F#4→"], ["·"], ["D4→"], ["G4"], ["G4"], ["F#4"], ["·"], ["·"], ["·"],
                ["F#4", "D4"]],
         note="A mesma moldura de novo — e a letra confessa por que: “the streets don't "
              "CHANGE”. A música também não muda de ideia; muda só o nome das ruas (e dos "
              "acordes, D↔G). O lado honesto da letra."),
    dict(label="L6 · “I ain't got time for the game” (c. 139–140, em D)",
         chords=[("D", 0)],
         syls=["I", "ain't", "got", "time", "for", "the", "game"],
         notes=[["F#4→"], ["·"], ["D4→"], ["·"], ["D4"], ["F#4"], ["E4", "D4", "F#4"]],
         note="O “game” ganha o melisma mais falado da ponte: E4-D4-F#4, rápido, quase um "
              "deboche — “I ain't got TIME for the game”. A voz fala, não canta."),
    dict(label="L7 · “'Cause I need you” (c. 141–142, em D)", chords=[("D", 0)],
         syls=["'Cause", "I", "need", "you"],
         notes=[["F#4"], ["D4"], ["F#4→"], ["D4→", "G4", "G4", "G4", "G4"]],
         note="O coro da ponte: “'cause I NEED you” — a 3ª (F#4) segurada 2 tempos no “need”, "
              "como todo pedido desta música. E o “you” sobe pra 4 G4s: a resposta mora "
              "acima, sempre."),
    dict(label="L8 · “But I need you” (c. 143–144, em D)", chords=[("D", 0)],
         syls=["But", "I", "need", "you"],
         notes=[["F#4"], ["D4"], ["F#4→"], ["D4→", "F#4", "D4", "F#4", "D4", "F4"]],
         note="Repete o “need you” — e o “you” termina em F4: F NATURAL. A primeira sombra: "
              "Ré maior ganha um F e escurece. O que vem aí é a única nuvem da música "
              "inteira."),
    dict(label="L9 · “Oh, I need you” (c. 145–146, Dm7 → G7)",
         chords=[("Dm7", 0), ("G7", 3)],
         syls=["Oh", "I", "need", "you"],
         notes=[["F4"], ["D4"], ["A4", "A4", "A4", "A4→"], ["G4", "F4", "D4"]], peak=2,
         note="A única cor MENOR da música inteira: Dm7 — as guitarras em A-C-D, a voz no F4. "
              "“Oh, I NEED you”: 4 A4s martelados no “need” (a teimosia dos C5 do refrão, "
              "agora em menor!) e o “you” desce G-F-D… em cima do G7. O momento mais escuro "
              "do disco, num mapa até aqui todo maior."),
    dict(label="L10 · “All this time” (c. 146–147, G7 → D)",
         chords=[("G7", 0), ("D", 2)],
         syls=["All", "this", "time"],
         notes=[["B3"], ["D4", "D4"], ["B3", "D4", "D4→"]],
         note="“All this time” — B3-D4… e a última nota cantada da música: D4 por QUATRO "
              "tempos (c. 147). G7 → D, o ámén de blues. A voz termina na tônica, no chão — "
              "depois de 5 minutos e 56 segundos de espera."),
]
PONTE_FILLS = {
    4: "A partir daqui (c. 137) entra a pista 'axl2': as respostas “(a little patience, "
       "yeah)” — suspiros B5-A5-F#5 por cima da voz. No disco elas espreitam desde o “just "
       "trying to get it right”; na transcrição, chegam aqui. Pergunta embaixo, “patience” "
       "em cima: o disco inteiro em miniatura.",
    8: "E a resposta atinge o TETO: D6→ e um E6 (c. 145) — EXATAMENTE o registro do pico do "
       "assobio (c. 10 e c. 20). O “patience” cantado mora na mesma altura do “patience” "
       "assobiado. Depois desce A#5-A5-G5 e cai em casa.",
}

PONTE_NOTA = ("A ponte inteira mora em RÉ MAIOR — a modulação que o final do solo anunciou "
              "(o F#5 no ar). E a harmonia CAMINHA: D ↔ G, pra frente e pra trás — as ruas da "
              "letra em acordes — até parar em D no “need you”, escurecer no Dm7 (única cor "
              "menor da música) e cair no G7 → D. Transparência: a transcrição esqueletiza a "
              "voz aqui (~8 notas por linha; “·” = a nota anterior segue valendo) e as "
              "respostas “(patience, yeah)” moram numa pista separada, a partir do c. 137.")

CAMA_PONTE = ("Cama da ponte: D → D2 (a mão esquerda descansa em D2/A2 — o Ré maior novo) · "
              "G → G2 · Dm7 → D2 + F3 na direita (a nuvem) · G7 → G2 (com F4, se quiser o "
              "suor) · D final → D2. A roda D↔G é o passeio: um baixo por compasso já conta "
              "a história.")

# ============================================================ FINAL — o adeus (c. 148–150)
FINAL = [
    dict(label="F1 · O último eco (c. 148, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4"],
         notes=[["E5", "D5→"], ["·"], ["·"], ["·"]],
         note="A última frase da música é um suspiro de resposta (pista 'axl2'): E5 caindo "
              "pra D5 — a 9ª voltando pra tônica, o “patience” final agora só eco."),
    dict(label="F2 · O acorde no ar (c. 149–150, em D)", chords=[("D", 0)],
         syls=["1", "2", "3", "4", "5", "6", "7", "8"],
         notes=[["D5→"], ["·"], ["·"], ["·"], ["A5"], ["·"], ["·"], ["·"]],
         note="O mapa acaba como começou: um acorde de D e uma 5ª no ar — no comecinho era o "
              "assobio no G5 sobre o C; agora é o A5 sobre o D (com um último aceno de G, o "
              "suspenso de sempre, c. 149). A música inteira é um convite que termina "
              "suspenso."),
]
FINAL_FILLS = {}

FINAL_NOTA = ("Três compassos de despedida: o eco, o acorde e a 5ª flutuando. Fim — "
              "150 compassos, exatamente onde a transcrição disse que acabava.")

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


def chat_section(title, phrases, fills=None, first_line=None):
    out = [f"[{title}]", ""]
    if first_line:
        out += [first_line, ""]
    for k, p in enumerate(phrases):
        if p.get("label"):
            out.append(f"◆ {p['label']}")
        c, s, n = phrase_lines(p)
        out += [c if c.strip() else "", s, n]
        if p.get("note"):
            out.append(f"     ({p['note']})")
        out.append("")
        if fills and k in fills:
            out.append(f"↳ ({fills[k]})")
            out.append("")
    return "\n".join(out)


def chat_pat():
    parts = [chat_section("INTRO — o assobio (c. 2–25 · registro real G5–D6, notas do disco)",
                          INTRO, INTRO_FILLS, first_line=INTRO_NOTA),
             chat_section("VERSO 1 — “Shed a tear…” (c. 26–41 · a voz entra no G4 que o assobio deixou no ar)",
                          VERSO_1, VERSO_1_FILLS, first_line=VERSO_1_NOTA),
             f"({CAMA_INTRO})",
             chat_section("REFRAO 1 — “Said, woman…” (c. 42–57 · a voz sobe ao C5 e passa a morar lá)",
                          REFRAO_1, REFRAO_1_FILLS, first_line=REFRAO_1_NOTA),
             f"({CAMA_REFRAO})",
             chat_section("ECO — o falsete (c. 57–63 e 95–101 · toca 2×, no registro do assobio)",
                          ECO, ECO_FILLS, first_line=ECO_NOTA),
             chat_section("REFRAO 2 — a variação (c. 80–101 · mesma música, palavras novas)",
                          REFRAO_2, REFRAO_2_FILLS, first_line=REFRAO_2_NOTA),
             chat_section("SOLO — a guitarra canta o refrão (c. 102–121 · registro real, teto F#6)",
                          SOLO, SOLO_FILLS, first_line=SOLO_NOTA),
             f"({CAMA_SOLO})",
             chat_section("INTERLÚDIO — a aterrissagem (c. 122–128)",
                          INTERLUDIO, INTERLUDIO_FILLS, first_line=INTERLUDIO_NOTA),
             chat_section("PONTE — em Ré maior: as ruas (c. 129–147)",
                          PONTE, PONTE_FILLS, first_line=PONTE_NOTA),
             f"({CAMA_PONTE})",
             chat_section("FINAL — o adeus (c. 148–150)",
                          FINAL, FINAL_FILLS, first_line=FINAL_NOTA)]
    return "\n\n".join(parts)


# ============================================================ HTML
import re as _re

LH_NOTES = {"C2", "G2", "A2", "D2", "E2", "F3"}  # a cama (mão esquerda)

def _all_note_names():
    names = set()
    for phrases in (INTRO, VERSO_1, REFRAO_1, ECO, REFRAO_2, SOLO, INTERLUDIO, PONTE, FINAL):
        for p in phrases:
            for slot in p["notes"]:
                for nt in slot:
                    for tok in nt.replace("→", "").split("+"):
                        if _re.match(r"^[A-G]#?\d$", tok):
                            names.add(tok)
    return names


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
        cols.append(
            f'<div class="cell"><div class="chord">{chords_at.get(i, "")}</div>'
            f'<div class="syl">{p["syls"][i]}</div>'
            f'<div class="notes">{note_cell_html(p["notes"][i], i == p.get("peak"))}</div></div>')
    note = f'<div class="pnote">💡 {p["note"]}</div>' if p.get("note") else ""
    return (f'<div class="card"><div class="plabel">{label}</div>'
            f'<div class="phrase">{"".join(cols)}</div>{note}</div>')


def section_html(title, subtitle, cama, phrases, fills):
    out = [f'<h2>{title}</h2>', f'<p class="small">{subtitle}</p>',
           f'<p class="small cama">🛏️ <b>Cama:</b> {cama}</p>']
    for k, p in enumerate(phrases):
        out.append(phrase_html(p, p.get("label") or f"Frase {k + 1}"))
        if fills and k in fills:
            out.append(f'<div class="fill">↳ {fills[k]}</div>')
    return "".join(out)


def keyboard_svg():
    names = _all_note_names()
    lh = LH_NOTES
    mel = names - lh
    W, H, BW, BH = 30, 150, 18, 92
    WHITE = ["C", "D", "E", "F", "G", "A", "B"]
    BLACK = {"C": "C#", "D": "D#", "F": "F#", "G": "G#", "A": "A#"}
    x, parts = 0, []
    for octv in range(2, 7):
        for wname in WHITE:
            if octv == 6 and wname == "G":
                break
            label = f"{wname}{octv}"
            fill, txt, tcol = "#ffffff", "", "#8a7a68"
            if label in mel:
                fill, tcol, txt = "#cfe3f8", "#1d5c9e", label
            if label in lh:
                fill, tcol, txt = "#f9e4c8", "#b06a1a", label
            parts.append(f'<rect x="{x}" y="0" width="{W}" height="{H}" rx="3" fill="{fill}" stroke="#b8a88f"/>')
            if txt:
                parts.append(f'<text x="{x + W / 2}" y="{H - 32}" text-anchor="middle" font-size="11" '
                             f'font-weight="700" fill="{tcol}">{txt}</text>')
            if label.startswith("C"):
                parts.append(f'<text x="{x + W / 2}" y="{H - 10}" text-anchor="middle" font-size="10" '
                             f'fill="#a5947d">{label}</text>')
            if label == "C4":
                parts.append(f'<circle cx="{x + W / 2}" cy="{H - 50}" r="4" fill="#e67e22"/>')
                parts.append(f'<text x="{x + W / 2}" y="{H - 56}" text-anchor="middle" font-size="9" '
                             f'font-weight="700" fill="#e67e22">dó central</text>')
            if wname in BLACK:
                bl = f"{BLACK[wname]}{octv}"
                bx = x + W - BW / 2
                if bl in mel:
                    bfill, btxt = "#2f6fb5", bl
                elif bl in lh:
                    bfill, btxt = "#d08a3e", bl
                else:
                    bfill, btxt = "#3a332b", ""
                parts.append(f'<rect x="{bx}" y="0" width="{BW}" height="{BH}" rx="2" fill="{bfill}" stroke="#211c15"/>')
                if btxt:
                    parts.append(f'<text x="{bx + BW / 2}" y="{BH - 12}" text-anchor="middle" font-size="9" '
                                 f'font-weight="700" fill="#fff">{btxt}</text>')
            x += W
    width = x + 2
    return (f'<svg viewBox="0 0 {width} 205" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="Teclado guia do Patience">' + "".join(parts) + "</svg>")


GUIDE = [
    ("🎵 Intro — o assobio", "assobio no G5, pickup no “e” do tempo 8 (c. 2)",
     "C G A7 D ×2 + C G C Em C G D D", "INTRO", "c. 2–25"),
    ("Verso 1", "“Shed a tear…” — a voz recebe no G4 que o assobio deixou",
     "C C G G A7 A7 D D ×2", "VERSO 1", "c. 26–41"),
    ("Refrão 1", "“Said, woman…” — a voz sobe ao C5 e mora lá",
     "C G C Em C G D", "REFRAO 1", "c. 42–57"),
    ("Eco", "falsete no G5, contratempo do tempo 3", "D (colchão)", "ECO", "c. 57–63"),
    ("Verso 2", "“I sit here on the stairs…” — MESMO mapa do Verso 1",
     "igual ao Verso 1", "VERSO 1 (de novo)", "c. 64–79"),
    ("Refrão 2", "mesma música, palavras novas + “We won't fake it!”",
     "igual ao Refrão 1", "REFRAO 2", "c. 80–101"),
    ("Eco (2ª vez)", "idêntico ao primeiro", "D", "ECO (de novo)", "c. 95–101"),
    ("🎸 Solo", "a guitarra canta o refrão, uma oitava acima",
     "roda do refrão → G A7 D", "SOLO", "c. 102–121"),
    ("Interlúdio", "cadência B-A/F-F# + arpejos + sinos de Ré", "D · G · D", "INTERLÚDIO", "c. 122–128"),
    ("🌉 Ponte", "“I've been walking the streets…” — em Ré maior",
     "D ↔ G · D · Dm7 · G7→D", "PONTE", "c. 129–147"),
    ("Final", "eco E5-D5… e o A5 no ar", "D", "FINAL", "c. 148–150"),
]


def guide_table_html():
    rows = "".join(
        f'<tr><td>{i}</td><td><b>{n}</b></td><td>{como}</td><td><code>{ac}</code></td>'
        f'<td>{mp}</td><td>{comp}</td></tr>'
        for i, (n, como, ac, mp, comp) in enumerate(GUIDE, 1))
    return (f'<table class="lh"><tr><th>#</th><th>Seção</th><th>Como reconhece</th>'
            f'<th>Acordes</th><th>No mapa</th><th>Comp.</th></tr>{rows}</table>')


def build_html():
    css = """
:root{--ink:#2e2620;--acc:#b06a1a;--peak:#c0392b;--muted:#8a7a68;--card:#fffdf8;--bg:#f4ede0;--chip:#3c2f24;--line:#e7dcc6}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'Segoe UI',system-ui,-apple-system,'Helvetica Neue',sans-serif;line-height:1.5}
.wrap{max-width:1080px;margin:0 auto;padding:30px 18px 60px}
header h1{margin:0;font-size:34px;letter-spacing:.5px}
header h1 span{color:var(--acc)}
header .sub{color:var(--muted);font-size:16px;margin:6px 0 14px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:8px}
.chips span{background:var(--chip);color:#f8f2e4;border-radius:999px;padding:4px 12px;font-size:12.5px;font-weight:600}
h2{font-size:24px;margin:38px 0 4px;padding-bottom:6px;border-bottom:3px solid var(--acc)}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:12px 0;box-shadow:0 1px 5px rgba(70,45,10,.07)}
.plabel{font-weight:800;color:var(--acc);font-size:15px;margin-bottom:10px}
.phrase{display:flex;flex-wrap:wrap;gap:7px;align-items:stretch}
.cell{min-width:46px;flex:0 0 auto;text-align:center;padding:6px 7px 9px;border-radius:9px;background:#faf5ea;border:1px solid #f0e6d0}
.chord{font-weight:800;font-size:12.5px;color:#f8f2e4;background:var(--chip);border-radius:6px;padding:1px 7px;display:inline-block}
.chord:empty{display:none}
.syl{font-size:13px;color:var(--muted);margin:5px 0 3px;min-height:17px;overflow-wrap:anywhere}
.notes{font-size:14.5px;font-weight:700;white-space:nowrap}
.nt.hold{color:#8a5a12}
.nt.peak{color:var(--peak)}
.glue{color:#c3b39a;margin:0 1px;font-weight:400}
.pnote{margin-top:10px;font-size:13.5px;color:#5c4f3e;border-top:1px dashed var(--line);padding-top:8px}
.fill{background:#fbf3df;border:1px solid #eed9ac;border-radius:10px;padding:9px 13px;margin:10px 0;font-size:13.5px}
.tip{background:#fbf3df;border:1px solid #eed9ac;border-radius:14px;padding:14px 18px;margin:16px 0;font-size:14.5px}
.tip h3{margin:0 0 8px;color:var(--acc);font-size:16px}
.small{color:var(--muted);font-size:13.5px}
.cama{margin-top:2px}
table.lh{border-collapse:collapse;width:100%;font-size:13.5px;margin:8px 0}
table.lh th{background:var(--chip);color:#f8f2e4;text-align:left;padding:6px 9px}
table.lh td{border-bottom:1px solid var(--line);padding:6px 9px;vertical-align:top}
code{background:#f1e8d4;padding:1px 5px;border-radius:5px;font-size:12.5px}
footer{margin-top:36px;color:var(--muted);font-size:12.5px;border-top:1px solid var(--line);padding-top:14px}
svg{width:100%;height:auto;display:block}
"""

    s_intro = section_html("🎵 INTRO — o assobio (c. 2–25 · registro real G5–D6)",
                           INTRO_NOTA, CAMA_INTRO, INTRO, INTRO_FILLS)
    s_v1 = section_html("🎤 VERSO 1 — “Shed a tear…” (c. 26–41)",
                        VERSO_1_NOTA, CAMA_INTRO, VERSO_1, VERSO_1_FILLS)
    s_r1 = section_html("REFRAO 1 — “Said, woman…” (c. 42–57)",
                        REFRAO_1_NOTA, CAMA_REFRAO, REFRAO_1, REFRAO_1_FILLS)
    s_eco = section_html("🌬️ ECO — o falsete (c. 57–63 e 95–101 · toca 2×)",
                         ECO_NOTA, "só o colchão de D das guitarras (D2 na esquerda conta a história).",
                         ECO, ECO_FILLS)
    s_r2 = section_html("REFRAO 2 — a variação (c. 80–101 · mesma música, palavras novas)",
                        REFRAO_2_NOTA, CAMA_REFRAO, REFRAO_2, REFRAO_2_FILLS)
    s_solo = section_html("🎸 SOLO — a guitarra canta o refrão (c. 102–121 · teto F#6)",
                          SOLO_NOTA, CAMA_SOLO, SOLO, SOLO_FILLS)
    s_int = section_html("🛬 INTERLÚDIO — a aterrissagem (c. 122–128)",
                         INTERLUDIO_NOTA, "D (c. 122–125) · G (c. 126) · D (c. 127–128) — o D2 seguro conta a história.",
                         INTERLUDIO, INTERLUDIO_FILLS)
    s_ponte = section_html("🌉 PONTE — em Ré maior: as ruas (c. 129–147)",
                           PONTE_NOTA, CAMA_PONTE, PONTE, PONTE_FILLS)
    s_final = section_html("🕯️ FINAL — o adeus (c. 148–150)",
                           FINAL_NOTA, "D (D2) — e a 5ª no ar.", FINAL, FINAL_FILLS)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Patience — Guns N' Roses · O Mapa Musical</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">

<header>
<h1>Patience <span>· Guns N' Roses</span></h1>
<p class="sub">O mapa musical — nota a nota, do assobio no G5 ao A5 no ar</p>
<div class="chips">
<span>150 compassos · 5:56 no disco</span><span>60 frases · 9 seções</span>
<span>tom: Dó maior (ponte em Ré)</span><span>teto: F#6</span><span>MIDI: bitmidi 51380</span>
</div>
</header>

<div class="card">
<p><b>Como ler:</b> cada cartão é uma frase. Em cima, a sílaba (ou o tempo, nas seções
instrumentais); embaixo, a nota — <b>registro real, as notas do disco</b>. Os símbolos:
<span class="nt hold">→</span> nota comprida · <span class="glue">›</span> notas ligadas no mesmo
tempo · <span class="nt">·</span> silêncio (na ponte: a nota anterior segue valendo) ·
<b>+</b> notas juntas (guitarras em pares) · <span class="nt peak">vermelho</span> = o pico.
O chip escuro acima da palavra é o acorde da cama. A mão esquerda mora na tabela
“Mão esquerda”, lá embaixo.</p>
<p class="small" style="margin-bottom:0">🎚️ <b>Transparência da afinação:</b> a cifra da UG diz
“violões meio tom abaixo” — o disco pode soar em Si enquanto este mapa (e o MIDI) fala Dó.
Se acontecer ao tocar junto da gravação, transporte tudo meio tom: <i>o desenho não muda um
milímetro</i> — é a vantagem do mapa.</p>
</div>

<h2>🖐️ O teclado do Patience</h2>
<div class="card">
{keyboard_svg()}
<p class="small" style="margin-bottom:0">Azul = melodia (assobio, voz, falsete, solo, respostas —
registro real). Laranja = a cama da mão esquerda (C2 · G2 · A2 · D2 · E2 · F3). O ponto laranja é
o dó central. Do G4 da entrada da voz ao F#6 do grito do solo — é o território inteiro da música.</p>
</div>

{s_intro}

<div class="tip">
<h3>🎁 A intro em uma frase</h3>
O assobio conta a história toda antes da letra: convite (C), tema (G), tensão (A7), pouso (D),
pico <span class="nt peak">D6</span>, calma, bordado… e entrega a bola pra voz num
<span class="nt">G4</span> — a nota exata em que o Axl entra no “Shed a tear”.
<b>Doze frases, quatro acordes, um pico e uma oitava de descida.</b>
</div>

{s_v1}

{s_r1}

{s_eco}

<div class="tip">
<h3>♻️ O Verso 2 é de graça (c. 64–79)</h3>
“I sit here on the stairs…” usa o mapa do <b>Verso 1 nota por nota</b> — verificado compasso a
compasso no MIDI (64 notas idênticas em altura, tempo e duração). Um mapa, dois versos.
Depois vem o Refrão 2 — mesma música, palavras novas.
</div>

{s_r2}

{s_solo}

{s_int}

{s_ponte}

{s_final}

<div class="tip">
<h3>🎁 O disco em uma frase</h3>
A música é um convite que termina suspenso: abre com um assobio no <span class="nt">G5</span> e
acaba com um <span class="nt">A5</span> no ar. Entre os dois: uma voz que recebe a bola exatamente
onde o assobio deixou, um refrão que mora uma oitava acima, um falsete que responde no andar do
assobio, um solo que <b>canta o refrão e grita no <span class="nt peak">F#6</span></b> a palavra
que a voz não aguenta, e uma ponte que muda de mundo pra Ré — com a <b>única nuvem menor</b> da
história (o Dm7 do “oh, I need you”) aparecendo nos últimos segundos. Tudo com
<b>quatro moldes e um tempero</b> (o A7).
</div>

<div class="tip">
<h3>♻️ A música mora em 4 moldes</h3>
<b>1) A roda do verso</b> (C C G G A7 A7 D D) — verso, e o esqueleto de tudo.<br>
<b>2) A roda do refrão</b> (C G C Em C G D) — o A7 vira Em: o tempero vira melancolia.<br>
<b>3) O campo do D</b> — o eco, o solo 2ª metade, o interlúdio, os sinos, o final: tudo D.<br>
<b>4) As ruas de Ré</b> (D ↔ G, com a nuvem Dm7 → G7) — a ponte.<br>
Quem aprende os 4 moldes toca a música inteira de ponta a ponta.
</div>

<h2>🖐️ Mão esquerda (a cama)</h2>
<div class="card">
<p>Comece simples — só o baixo, bem fraquinho, um por acorde:</p>
<table class="lh">
<tr><th>Acorde</th><th>Baixo</th><th>Com corpo (2ª etapa)</th><th>Onde mora</th></tr>
<tr><td><b>C</b></td><td><code>C2</code></td><td><code>C2</code> + <code>C4-E4-G4</code></td><td>a casa — intro, verso, refrão</td></tr>
<tr><td><b>G</b></td><td><code>G2</code></td><td><code>G2</code> + <code>G4-B4</code></td><td>o outro pé — verso, refrão, ponte, interlúdio</td></tr>
<tr><td><b>A7</b></td><td><code>A2</code></td><td><code>A2</code> + <code>C#4</code> (+<code>G4</code>)</td><td>o tempero — verso e 2ª metade do solo</td></tr>
<tr><td><b>D</b></td><td><code>D2</code></td><td><code>D2</code> + <code>D4-F#4</code></td><td>o pouso — intro, refrão, solo, ponte, final</td></tr>
<tr><td><b>Em</b></td><td><code>E2</code></td><td><code>E2</code> + <code>G4-B4-E5</code></td><td>a melancolia — refrão</td></tr>
<tr><td><b>Dm7</b></td><td><code>D2</code></td><td><code>D2</code> + <code>F3-A3-C4</code></td><td>a nuvem — só na ponte (“Oh, I need you”)</td></tr>
<tr><td><b>G7</b></td><td><code>G2</code></td><td><code>G2</code> + <code>F4-B4</code></td><td>o ámén de blues — final da ponte</td></tr>
</table>
<p class="small" style="margin-bottom:0">💡 A cama do verso/refrão é <b>a mesma da intro</b> — quem
aprende a intro já sabe acompanhar quase a música toda. Na ponte, a mão esquerda descansa em
<code>D2/A2</code> (o Ré maior novo).</p>
</div>

<div class="tip">
<h3>🧵 As 7 costuras (é onde tudo se encaixa)</h3>
<b>1) Intro → Verso 1:</b> o assobio desce até o <span class="nt">G4</span> (c. 23) e a voz
recebe <b>na mesma nota</b> (c. 26) — a passagem de bastão combinada.<br>
<b>2) Verso → Refrão:</b> a voz termina no <span class="nt">D4</span> e o refrão abre no
<span class="nt">C5</span> — muda de bairro: uma oitava acima da tônica.<br>
<b>3) Refrão → Eco:</b> o refrão morre no <span class="nt">A4</span>… e o falsete responde uma
oitava acima (<span class="nt">A5</span>) — o registro do assobio.<br>
<b>4) Refrão 2 → Solo:</b> o grito “we won't fake it!” e os licks de F#6 despacham — e o solo
abre <b>cantando o refrão</b>, uma oitava acima.<br>
<b>5) Solo → Interlúdio:</b> o <span class="nt">F#5</span> fica no ar… e a cadência
<span class="nt">B4-A4 · F4-F#4</span> aterrissa em D.<br>
<b>6) Interlúdio → Ponte:</b> os sinos <span class="nt">D6+A5</span> → <span class="nt">F#6+D6</span>
anunciam: <b>a ponte vai ser em Ré maior</b>.<br>
<b>7) Ponte → Final:</b> a última nota cantada é um <span class="nt">D4</span> de 4 tempos… o eco
<span class="nt">E5-D5</span>… e o <span class="nt">A5</span> no ar. O convite fica suspenso.
</div>

<h2>✈️ Como estudar</h2>
<div class="card">
<ol>
<li><b>A cama primeiro:</b> 4 baixos (<code>C2 G2 A2 D2</code>) cobrem a maior parte da música —
toque eles com o disco até virar músculo.</li>
<li><b>O assobio:</b> 12 frases, registro G5–D6. Quer “cantar” junto? Uma oitava abaixo
(G4–D5) — o desenho é o que importa.</li>
<li><b>O verso:</b> 6 frases e 2 reciclagens de graça (L4–6 = L1–3; Verso 2 = Verso 1).</li>
<li><b>O refrão:</b> morar no C5. A variação do 2º refrão só troca palavras — cante junto.</li>
<li><b>O solo:</b> quem sabe o refrão já sabe a 1ª metade. O resto é licks em colcheias.</li>
<li><b>A ponte:</b> o esqueleto D-E-F#-G + a nuvem Dm7. Poucas notas, muito teatro.</li>
<li><b>Costure por último</b> (a lista das 7 acima) e <b>grave-se</b> tocando com o disco. 🎹</li>
</ol>
</div>

<h2>🗺️ Guia de montagem — a música inteira, de ponta a ponta</h2>
<div class="card">
<p><b>150 compassos no MIDI</b> (a transcrição é condensada: 5:00 contra 5:56 do disco — os
números de compasso são a referência do projeto). A letra entre aspas é a deixa.</p>
{guide_table_html()}
</div>

<div class="tip">
<h3>🏆 Status do projeto</h3>
<b>Toda a música está mapeada:</b> intro, versos (o 2º de graça), refrões (com a variação), o eco,
o solo, o interlúdio, a ponte em Ré e o final — <b>60 frases nota a nota</b>.
Transparências registradas no caminho: a afinação (meio tom), o dropout das guitarras
(c. 54–55 e 92–93), o esqueleto da ponte, o grito “we won't fake it” (letra sem nota — não se
inventa nota), o eco morando numa pista separada e a condensação do MIDI.
<b>Nada ficou pendente.</b>
</div>

<footer>Mapa conferido nota a nota com a transcrição MIDI (bitmidi.com/uploads/51380.mid), triangulada
com Ultimate Guitar (ver 1 e 3), Cifra Club e 3 fontes de letra (letras.com, Shazam, lyrics.com).
Registros reais: assobio G5–D6 · voz D4–D5 · falsete G5–A5 · solo A4–F#6 · respostas D5–E6.
Tom: Dó maior, ponte em Ré maior. Teto: F#6 (c. 109–110, o grito do solo; c. 128, a cortina dos sinos).
Versão de chat e dados: <code>gera_patience.py</code> — a fonte única de verdade.</footer>

</div>
</body>
</html>"""
    return html


# ── saídas: a pasta ../saidas desta música (a fábrica roda de qualquer lugar) ──
from pathlib import Path as _P
SAIDAS = _P(__file__).resolve().parent.parent / "saidas"
SAIDAS.mkdir(exist_ok=True)

if __name__ == "__main__":
    print(chat_pat())
    with open(SAIDAS / "mapa-musical-patience.html", "w", encoding="utf-8") as f:
        f.write(build_html())
    print("\n[HTML gerado: mapa-musical-patience.html]")
    print("[gera_patience.py — Patience · MAPA COMPLETO + HTML]")
