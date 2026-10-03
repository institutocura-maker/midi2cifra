#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAPA MUSICAL — BED OF ROSES (Bon Jovi, "Keep the Faith", 1992)
VERSÃO: Matthias Nebel — The Voice of Germany 2018, blind audition (3min09 + Zugabe)

ESQUELETO (fonte única de notas): bed-of-roses.mid — bitmidi.com/uploads/19001
  MIDI do original, format 1, 9 pistas, 60 bpm, 91 compassos — gravado 1 semitom
  ACIMA do disco (F#). TRANSPOSTO −1st → FÁ MAIOR:
    · disco = F (Musicnotes "Original Published Key: F Major", voz Bb3–Bb5;
      Chordify por áudio no clipe oficial: Bb–F–Dm–C)
    · single oficial 2019 do Matthias = F (Chordify por áudio: Bb–F–Dm–C)
    · cruzamento: pico do MIDI B5 −1st = Bb5 = teto vocal da partitura oficial ✓
  TRANSPARÊNCIA: se ao tocar com o clipe soar 1 semitom deslocado, transpõe-se
  o mapa inteiro num comando (a estrutura é idêntica).

ESTRUTURA = corte de TV (transcript oficial do clipe TVOG, 18/10/2018):
  INTRO piano → V1 (5 frases) → V2 (5) → REFRAO 1 (2 linhas, meia-voz) →
  LIFT-reprise ("About all of the things…") → REFRAO 2 (4 linhas, banda,
  pico Bb5 no "CLOSE") → ZUGABE/bis (refrão decorado + a rosa segurada +
  o tag grave "LAY YOU DOWN").
  Sem os versos "so far away"/"hotel bar"/"mistress" — corte de TV.

Numeração de compassos = a do ESQUELETO (MIDI do original). No corte de TV as
contagens absolutas variam; a estrutura relativa frase-a-frase é idêntica.

GRADE: 12/8 lento (tercina ≈ 180/min no MIDI; disco ≈ 167 — Chordify).
  Cada TEMPO do grid = 1 tempo grande = 3 colcheias-tercinas.
CONVENÇÕES (herdadas do Patience/NR + novas p/ o 12/8):
  "→"        = nota longa, que segue soando enquanto a frase anda (os monólitos de
               5+ tercinas e os ganchos/picos esticados)
  "›"        = liga notas na mesma sílaba (melisma) ou no mesmo tempo
  "·"        = silêncio (a nota anterior segue se tinha "→")
  sílaba·nota= um par no mesmo tempo (até 3 pares = as 3 tercinas)
  F4→ repetido com sílabas novas = as sílabas CAVALGAM a nota segurada
                (no disco/clip as palavras re-articulam sobre a mesma altura)
  ▲          = o pico da frase
"""

# ============================================================ INTRO — O ROCKING (c. 3–10)
# No esqueleto: 8 compassos, o par Bb6 ↔ Fadd9 alternando (cada acorde = 1 compasso,
# entrando na última tercina do compasso anterior); do 3º par em diante o piano decora
# com arpejos e sobe a escadinha que entrega a voz no c11. No clipe: encurtado,
# sob a conversa dos coaches ("that's their song, eh?").
INTRO = [
    dict(label="I1 — A figura-mãe: Bb6 (1 compasso · c. 3, 5, 7, 9)",
         chords=[("Bb6", 1)],
         beats=[[("1", "G5"), ("2", "F5"), ("3", "D5")],
                [("1", "G5"), ("2", "F5"), ("3", "D5")],
                [("1", "G5"), ("2", "F5"), ("3", "D5")],
                [("1", "G5"), ("2", "F5"), ("3", "D5")]],
         note="Mão esquerda: Bb3+D4+F4 segurando o compasso inteiro. Direita: a tercina "
              "G5-F5-D5, uma volta por tempo grande. Esse rocking é o DNA da música inteira."),
    dict(label="I2 — O outro lado: Fadd9 (1 compasso · entra na última tercina do anterior)",
         chords=[("Fadd9", 1)],
         beats=[[("1", "G5"), ("2", "F5"), ("3", "C5")],
                [("1", "G5"), ("2", "F5"), ("3", "C5")],
                [("1", "G5"), ("2", "F5"), ("3", "C5")],
                [("1", "G5"), ("2", "F5"), ("3", "C5")]],
         note="Mão esquerda: A3+C4+F4 (o Fá com a 3ª no baixo). A célula G5-F5 NUNCA muda — "
              "só a terceira nota troca de cor: D5 sobre o Bb (a terça — a rosa) e C5 sobre "
              "o F (a quinta — o espinho). O G5 comum aos dois é a cola: 6ª do Bb, 9ª do F."),
]
INTRO_FILLS = {}
INTRO_NOTA = ("No esqueleto o piano + guitarra limpa + pads tocam 8 compassos (4 pares); no "
              "clipe é mais curto e a voz entra quase de cara. Contagem: '1-la-le 2-la-le "
              "3-la-le 4-la-le' — valsa cansada. Do 3º par em diante o piano decora (arpejos "
              "Bb3-D4-F4-Bb4) e no fim sobe a escadinha que entrega a voz no Bb4 (c. 11).")

# ============================================================ VERSO 1 — "Sittin' here wasted…" (c. 11–19)
# 5 frases, 71 sílabas. A voz entra no Bb4 (c11 t1). Harmonia: Bb ↔ F/A alternando
# (o baixo desliza Bb→A, meio tom — o motor do verso); Bb chega no t3 do "bottle" (c15);
# cadência Fsus2 → F no fim (c18–19). Bateria acorda no c15 t2 ("'cause a BOT-tle");
# baixo só no fim do V1 (G2-F2, pousa Bb1 abrindo o V2).
V1 = [
    dict(label="V1·1 — “Sittin' here wasted and wounded at this old piano” (c. 11–12 · Bb → F/A)",
         chords=[("Bb", 1), ("F/A", 4)],
         beats=[[("sit", "Bb4"), ("ting", "A4"), ("here", "G4")],
                [("wast", "Bb4"), ("ed", "A4"), ("and", "G4")],
                [("wound", "Bb4"), ("ed", "Bb4")],
                [("at", "A4"), ("this", "G4")],
                [("old", "G4"), ("pi", "A4→")],
                [("·", "·")],
                [("·", "·")],
                [("a", "G4"), ("no", "A4")]],
         note="O pêndulo do verso: Bb4-A4-G4 duas vezes (raiz → 7ª maior → 6ª do Bb). "
              "“Wound-ed” crava Bb4; “at this old” desce à vizinha; e “PI” segura A4 "
              "por 9+ tercinas (a 3ª do F/A — nota de descanso), com o ornamento "
              "“a-no” G4→A4 no rabinho do compasso. 14 sílabas, 14 notas."),
    dict(label="V1·2 — “Tryin' hard to capture the moment, this mornin', I don't know” (c. 13–15 · Bb → F/A)",
         chords=[("Bb", 1), ("F/A", 4)],
         beats=[[("try", "Bb4"), ("in", "Bb4"), ("hard", "Bb4")],
                [("to", "A4"), ("cap", "G4"), ("ture", "Bb4")],
                [("the", "Bb4"), ("mo", "Bb4")],
                [("ment", "A4"), ("this", "G4")],
                [("mor", "F4")],
                [("nin'", "C4→")],
                [("·", "·")],
                [("I", "C5"), ("don't", "C5")],
                [("know", "C5")]],
         note="Mesmo pêndulo, nova palavra. Aí acontece o mergulho: “mor-NIN'” desce ao "
              "C4 — o fundo do poço do verso inteiro — e segura 6 tercinas. E do fundo, "
              "“I don't know” SALTA UMA OITAVA EXATA: C4 → C5. O primeiro grito, ainda "
              "contido. (“know” já mora no compasso do 'bottle' — a frase invade a "
              "seguinte; a costura é no contratempo, sem costura aparente.)"),
    dict(label="V1·3 — “'Cause a bottle of vodka's still lodged in my head” (c. 15–16 · F/A → Bb → F/A) — O PICO",
         chords=[("F/A", 1), ("Bb", 3), ("F/A", 5)],
         beats=[[("cause", "C5"), ("a", "C5"), ("bot", "C5")],
                [("tle", "C5"), ("of", "F5")],
                [("vot", "F5"), ("ka's", "D5")],
                [("still", "D5")],
                [("lodged", "D5"), ("in", "C5")],
                [("my", "C5"), ("head", "A4")]],
         peak=(3, 0),
         note="O pico do V1: F5 em “of-VOT”. Sabedoria de melodista: o F mora nos DOIS "
              "acordes — raiz do F/A, 5ª do Bb — por isso o clímax atravessa a troca "
              "indiferente. A BATERIA acorda exatamente aqui (c15 t2, na palavra "
              "“bottle”) — o primeiro batimento do coração da música. E “head” pousa "
              "em A4: uníssono com o baixo (o A do F/A). 12 sílabas, 12 notas."),
    dict(label="V1·4 — “And some blonde gave me nightmares, I think that she's still in my bed” (c. 16–17 · F/A → Bb)",
         chords=[("F/A", 1), ("Bb", 2)],
         anac=("and", "C5"),
         beats=[[("some", "D5"), ("blonde", "C5")],
                [("gave", "C5"), ("me", "Bb4"), ("night", "A4")],
                [("mares", "F4"), ("I", "F4→")],
                [("think", "F4→"), ("that", "F4→"), ("she's", "F4→")],
                [("still", "F4→"), ("in", "F4→"), ("my", "F4→")],
                [("bed", "F4")]],
         note="A confissão. “Night-mares” desce A4→F4 e a linha inteira “I think that "
              "she's still in my bed” mora num F4 MONÓLITO de 8 tercinas (a 5ª do Bb) — "
              "quase falado, sem melodrama: a acusação é o texto. TRANSPARÊNCIA: o MIDI "
              "segura UMA nota; no disco/clipe as palavras re-articulam sobre essa "
              "altura (as sílabas com F4→ cavalgam). O “bed” final re-ataca com uma "
              "graça antes dele."),
    dict(label="V1·5 — “As I dream about movies they won't make of me when I'm dead” (c. 18–19 · Fsus2 → F)",
         chords=[("Fsus2", 1), ("F", 5)],
         beats=[[("as", "Bb4"), ("I", "Bb4"), ("dream", "Bb4")],
                [("a", "Bb4"), ("bout", "Bb4"), ("mo", "Bb4")],
                [("vies", "Bb4"), ("they", "Bb4"), ("won't", "Bb4")],
                [("make", "Bb4"), ("of", "A4"), ("me", "G4")],
                [("when", "F4→"), ("I'm", "F4→"), ("dead", "F4→")]],
         note="O motor: DOZE sílabas seguidas no Bb4 — hipnose pura, o verso mais "
              "teatral do disco (Jon quase fala em cima). Harmonia: a célula da intro "
              "VERTICALIZADA — o pad segura F-G-C = Fsus2, o rocking G5-F5-C5 virou "
              "acorde. “When I'm dead” resolve no F (a tônica!) e o “dead” segura "
              "9+ tercinas — a nota mais longa do V1. A escadinha G4-A4-Bb4 no fim "
              "(c19 t4) é a PONTE: entrega o V2 (“With an ironclad…”)."),
]
V1_FILLS = {}
V1_NOTA = ("5 frases, 9 compassos do esqueleto. Camada a camada: piano + pads (e guitarra "
           "limpa no rocking) → bateria acorda no “bottle” (c15) → baixo só no último "
           "compasso (G2-F2, pousando Bb1). No palco TVOG: piano + voz até a banda entrar — "
           "o transcript confirma a mesma dramaturgia. Numeração = esqueleto (MIDI do "
           "original); no corte de TV as contagens absolutas variam, a estrutura não.")

CAMA_V1 = ("Cama (mão esquerda): Bb → Bb2 · F/A → A2 (+F3 se der) · Fsus2 → F2+G3 · F → F2. "
           "O segredo do cheiro da música: o baixo desliza Bb→A — MEIO TOM — a cada troca. "
           "A direita pode ficar na tercina do rocking (G5-F5-D5 / G5-F5-C5) o verso inteiro; "
           "a cama estática já soa a música.")

# ============================================================ VERSO 2 — "With an ironclad fist…" (c. 20–26)
# 5 frases, 63 sílabas — o V1 reencarnado com o chão aberto: baixo na FUNDAMENTAL
# (F1, não mais A2 do F/A), bateria em marcha. A gramática repete de propósito:
# motor Bb4 → mergulho no C4 ("talk") + salto de oitava → pico F5 no "that I long"
# atravessando a chegada do Bb no t3 (c24: baixo A1→Bb1) → confissão num F4 só.
V2 = [
    dict(label="V2·1 — “With an ironclad fist, I wake up and French kiss the mornin'” (c. 20–21 · Bb → F)",
         chords=[("Bb", 1), ("F", 5)],
         beats=[[("with", "Bb4"), ("an", "Bb4"), ("iron", "Bb4")],
                [("clad", "A4"), ("fist", "G4")],
                [("I", "Bb4"), ("wake", "Bb4"), ("up", "Bb4")],
                [("and", "Bb4"), ("french", "A4"), ("kiss", "G4"), ("the", "G4")],
                [("mor", "A4→")],
                [("·", "·")],
                [("·", "·")],
                [("ning", "G4›A4")]],
         note="O V1·1 reencarnado — e com o veneno: onde o V1 balançava o pêndulo "
              "(Bb-A-G), o V2 MARTela o motor (Bb-Bb-Bb) antes de cair. E “mor-NIN'” é "
              "gêmeo de “pi-A-no”: mesmo A4 comprido (8+ tercinas) com o mesmo ornamento "
              "G4›A4 no rabinho (c21 ≡ c12, compasso a compasso). A diferença: embaixo, "
              "o baixo acordou — F na fundamental, chão aberto."),
    dict(label="V2·2 — “While some marchin' band keeps its own beat in my head while we're talkin'” (c. 21–23 · F → Bb → F)",
         chords=[("Bb", 1), ("F", 5)],
         anac=("while", "Bb4"),
         beats=[[("some", "Bb4"), ("march", "Bb4"), ("in'", "Bb4")],
                [("band", "A4"), ("keeps", "G4"), ("its", "Bb4")],
                [("own", "Bb4"), ("beat", "Bb4"), ("in", "Bb4")],
                [("my", "A4"), ("head", "G4"), ("while", "G4")],
                [("we're", "F4")],
                [("talk", "C4→")],
                [("·", "·")],
                [("in'", "C5")]],
         note="A banda de marcha em pessoa: doze sílabas em tercinas certinhas no "
              "Bb4-A4-G4 — a marcha É o rocking da intro cantado. E o mergulho gêmeo do "
              "V1: “we're TALK” desce ao mesmo C4 do poço (5,5 tercinas, c23 ≡ c14) e "
              "“in'” SALTA a oitava exata C4→C5. Mesma porta, mesma chave — só aberta "
              "com mais força."),
    dict(label="V2·3 — “About all of the things that I long to believe” (c. 23–25 · F/A → Bb → F) — O PICO",
         chords=[("F/A", 1), ("Bb", 3), ("F", 5)],
         anac=("a", "C5"),
         beats=[[("bout", "C5"), ("all", "C5"), ("of", "C5")],
                [("the", "C5"), ("things", "C5"), ("that", "F5")],
                [("I", "F5→"), ("long", "D5")],
                [("to", "D5→"), ("be", "C5")],
                [("lieve", "D5")]],
         peak=(3, 0),
         note="O PICO — e a fábrica CORRIGE o palpite do mestre: o F5 não cai no "
              "“believe”; cai no “THAT I LONG” (F5 + F5→), atravessando a MESMA chegada "
              "do Bb no tempo 3 do V1·3 (“vot-ka's”) — o baixo anda A1→Bb1 debaixo, "
              "escutável. Antes do pulo, sete C5s de fila indiana (“in'-a-bout-all-of-"
              "the-things”), a mesma escada do “know-'cause-a-bot-tle”. E o “be-LIEVE” "
              "chega RECLINADO: C5→D5, quase conversa. Reciclagem de elite."),
    dict(label="V2·4 — “About love, the truth, what you mean to me” (c. 25–26 · F → Bb)",
         chords=[("F", 1), ("Bb", 5)],
         anac=("a", "C5"),
         beats=[[("bout", "C5")],
                [("love", "D5"), ("the", "C5")],
                [("truth", "C5")],
                [("what", "C5"), ("you", "Bb4"), ("mean", "A4")],
                [("to", "F4"), ("me", "F4→")]],
         note="“LOVE” ganha o D5 — o único escape da frase — e “the TRUTH” repica no "
              "C5. Aí a música para de cantar e começa a confessar: “me”, a última "
              "palavra, segura o F4 por 9 tercinas com o Bb chegando embaixo (F = 5ª). "
              "A nota não termina: ela VIRA a linha seguinte."),
    dict(label="V2·5 — “And the truth is, baby, you're all that I need” (c. 26 · Bb) — A LINHA DAS CADEIRAS",
         chords=[("Bb", 1)],
         beats=[[("and", "F4→"), ("the", "F4→"), ("truth", "F4→")],
                [("is", "F4→"), ("ba", "F4→"), ("by", "F4→")],
                [("you're", "F4→"), ("all", "F4→"), ("that", "F4→")],
                [("I", "F4→"), ("need", "F4")]],
         note="A linha inteira CAVALGA o mesmo F4 do “me” — o MIDI segura UMA nota de "
              "9 tercinas; no disco e no clipe as palavras re-articulam sobre a altura "
              "(sílabas com F4→ = cavalgam). Gêmea da confissão do V1 (“I think that "
              "she's still in my bed” — também F4 sobre Bb): nas duas vezes o drama é "
              "o TEXTO, a nota é uma só. E é AQUI que o transcript do clipe registra o "
              "[cheering]: a linha que virou as 4 cadeiras é uma nota só. O baixo já "
              "sussurra F1→G1 no fim — a escada para o refrão."),
]
V2_FILLS = {}
V2_NOTA = ("5 frases, 7 compassos (c20–26) — o V1 comprimido com o chão aberto: baixo na "
           "fundamental (no V1 era F/A com A no baixo; agora F1), bateria em marcha. A "
           "gramática repete DE PROPÓSITO: motor → mergulho no C4 + salto de oitava → pico "
           "F5 atravessando a chegada do Bb no t3 → confissão num F4 só. O teto continua "
           "F5 — quem estoura o Bb5 é o refrão que vem aí.")

CAMA_V2 = ("Cama (mão esquerda): Bb → Bb2 · F → F2 (na FUNDAMENTAL agora — o baixo acordou "
           "no fim do V1) · F/A → A2 (só no compasso do pico, c24) · Bb → Bb2. Detalhe de "
           "mestre: no compasso do pico o baixo anda A1→Bb1 (t1→t3) — a chegada do Bb é "
           "ESCU-TÁ-VEL; e nos dois últimos tempos de c26 ele sobe F1→G1, entregando o "
           "refrão de mão beijada.")

# ============================================================ REFRAO 1 — a meia-voz (c. 27–29)
# No corte de TV: 2 linhas a MEIA-VOZ sobre o piano, antes da rampa. As linhas 3-4
# do refrão completo ("Oh I wanna be…") ficam para o REFRAO 2 — no TV ele não as
# canta aqui: vai do "bed of nails" direto à RAMPA (LIFT).
# Cama: Bb → C → F ("I wanna lay you DOWN") → C/E → Dm ("in a bed OOOF…") →
#       C → Bb → F ("for tonight…"). Linha 2: a voz canta as TERÇAS da descida.
CH1 = [
    dict(label="CH1·1 — “I wanna lay you down in a bed of roses” (c. 27–28 · Bb → C → F → C/E → Dm)",
         chords=[("Bb", 1), ("C", 2), ("F", 3), ("C/E", 5), ("Dm", 7)],
         beats=[[("I", "Bb4"), ("wan", "Bb4"), ("na", "Bb4")],
                [("lay", "Bb4"), ("you", "A4"), ("down", "G4›F4→")],
                [("·", "·")],
                [("·", "·")],
                [("·", "·")],
                [("in", "F5"), ("a", "F5"), ("bed", "F5")],
                [("of", "F5→")],
                [("ro", "F5"), ("ses", "F5")]],
         peak=(7, 0),
         note="O gancho inteiro numa nota só: SEIS F5. E olha o teatro: a palavra “down” "
              "PINTA o sentido (G4›F4→ — cai e segue caindo por 2 tempos), passando pela "
              "9ª (o G fantasma da intro morando aqui!) antes de resolver na tônica F. "
              "Respiração — e o SALTO DE OITAVA F4→F5 no “in a bed”. O F5 do “of” fica "
              "SUSPENSO como 4ª sobre o C/E e só vira nota do acorde (3ª) quando o Dm "
              "chega: a nota não se mexe, só muda de função — a ASSINATURA da música, "
              "agora pela 3ª vez (vot-ka's, that I, of). TRANSPARÊNCIAS: no clipe a "
              "meia-voz engole o “I wanna” (o ASR do transcript não o captura) — o "
              "esqueleto mantém; e se o seu ouvido quiser segurar o “RO” em vez do “of”, "
              "a altura é a mesma F5 — o desenho não muda."),
    dict(label="CH1·2 — “For tonight, I sleep on a bed of nails” (c. 29 · C → Bb → F)",
         chords=[("C", 1), ("Bb", 2), ("F", 3)],
         beats=[[("for", "E5"), ("to", "E5")],
                [("night", "D5"), ("I", "D5")],
                [("sleep", "D5")],
                [("on", "C5→")],
                [("a", "C5→"), ("bed", "C5→"), ("of", "C5→")],
                [("nails", "C5")]],
         peak=(1, 0),
         note="A voz canta as TERÇAS da descida: E5 sobre o C, D5 sobre o Bb — e pousa "
              "na 5ª (C5) sobre o F. A linha E5→D5→C5 É a escada harmônica cantada uma "
              "oitava acima do baixo (C2→Bb1→F1). E “on a bed of nails” afunda num C5 "
              "monólito de 7 tercinas — a cama de pregos literalmente afundando no fim "
              "da linha (no disco as palavras re-articulam; as sílabas com C5→ "
              "cavalgam)."),
]
CH1_FILLS = {}
CH1_NOTA = ("No corte de TV, o primeiro refrão é A MEIA-VOZ — “I wanna lay you down…” quase "
            "sussurrado sobre o piano, a promessa antes da tempestade. No esqueleto são 2 "
            "frases (c27–29); as linhas 3-4 do refrão completo (“Oh I wanna be just as "
            "close…”) o TV guarda para o REFRAO 2 — daqui ele vai direto à RAMPA (LIFT).")

CAMA_CH1 = ("Cama (mão esquerda): Bb → Bb2 · C → C2 · F → F2 · C/E → E2 (+C3+G3 na direita) · "
            "Dm → D2 · C → C2 · Bb → Bb2 · F → F2. A escada do refrão: SOBE Bb→C→F (“I wanna "
            "lay you DOWN” — a palavra resolve na tônica), escurece em C/E→Dm (“in a bed "
            "OOOF…”), e DESCE C→Bb→F (“for tonight…”). E a moldura de sempre continua "
            "valendo: a tercina do rocking (G5-F5-D5 sobre Bb / G5-F5-C5 sobre F) — o "
            "refrão é a intro com letra.")

# ============================================================ LIFT — a RAMPA do corte de TV
# Jogada de arranjista da TV: em vez de repetir o refrão, ele REPRISA as frases-rampa
# do V2 com a banda subindo. O esqueleto (o original) NÃO tem essa reprise — o mapa
# usa as frases do V2 como leitura (mesma melodia, mesma cama). Reciclagem da casa,
# como o V2 do Patience que usou o mapa do V1.
LIFT = [
    dict(V2[2], label="LIFT·1 — “About all of the things that I long to believe” (a RAMPA · mapa = V2·3, a mesma música)",
         note="A mesma rampa do V2·3 — mas a FUNÇÃO mudou: aqui o pico F5 do “that I "
              "long” não é clímax, é ALAVANCA. A banda sobe por baixo e o [cheering "
              "and screaming] do transcript estoura bem aqui (“…that I long / to "
              "believe about…”). Reciclagem da casa: mesma música, novo papel — como "
              "o V2 do Patience usou o mapa do V1."),
    dict(V2[3], label="LIFT·2 — “About love, the truth, what you mean to me” (a RAMPA · mapa = V2·4)",
         note="Se a rampa seguir até aqui, é o mapa do V2·4: o “me” segurando o F4 — "
              "que agora vira o TRAMPOLIM de onde o refrão grande salta. "
              "TRANSPARÊNCIA: o transcript corta em “to believe about…” — a rampa do "
              "clipe pode parar no “believe/about love”; os dois mapas estão prontos."),
]
LIFT_FILLS = {}
LIFT_NOTA = ("Invenção do arranjo de TV (não existe no disco): depois do refrão a meia-voz, "
             "Matthias reprise as frases-rampa do V2 e a banda sobe até o grito — a "
             "plateia explode no meio (transcript: [cheering and screaming]) e o refrão "
             "grande entra por cima. No esqueleto, o equivalente harmônico é a mesma "
             "cama do V2 (F/A→Bb→F) com o pico F5 no mesmo lugar de sempre.")

# ============================================================ REFRAO 2 — a tempestade (c. 27–33)
# O refrão inteiro de 4 linhas, banda completa — a recompensa da rampa. Linhas 1-2 =
# o MESMO mapa da meia-voz (reciclagem da casa); linhas 3-4 = o voo novo, com o
# TETO DO MAPA: Bb5 no "CLOSE" (a fábrica corrigiu o palpite do mestre: NÃO é no
# "GHOST" — o "ghost" re-ataca no F5 depois do A5 segurado).
CH2 = [
    dict(CH1[0], label="CH2·1 — “I wanna lay you down in a bed of roses” (c. 27–28 · o mapa de CH1·1, agora com a banda inteira)",
         note="O mesmo mapa da meia-voz, nota por nota — a diferença não está no mapa: "
              "está na BANDA. A meia-voz vira grito de peito; mantenha o desenho (ele é "
              "a espinha) e deixe a banda carregar o resto. No transcript do clipe, só "
              "um pedaço sobrevive ao burburinho: “in a bed of roses” entre [cheering "
              "and music] e [applause]."),
    dict(CH1[1], label="CH2·2 — “For tonight, I sleep on a bed of nails” (c. 29 · o mapa de CH1·2, banda inteira)",
         note="A escada de terças E5-D5-C5, agora com bateria e baixo descendo junto. E "
              "repare na costura sem emenda: o C5 monólito do “nails” termina exatamente "
              "no compasso em que o “OH” do teto vai saltar — o trampolim está no lugar."),
    dict(label="CH2·3 — “Oh, I wanna be just as close as the Holy Ghost is” (c. 30–31 · F → C → Dm → C/E → Bb → F) — O TETO DO MAPA",
         chords=[("F", 1), ("C", 2), ("Dm", 3), ("C/E", 5), ("Bb", 6), ("F", 7)],
         beats=[[("·", "·")],
                [("oh", "F5"), ("I", "F5"), ("wan", "F5→")],
                [("·", "·")],
                [("na", "F5"), ("be", "F5"), ("just", "G5")],
                [("as", "G5"), ("close", "Bb5")],
                [("as", "Bb5")],
                [("the", "A5→"), ("ho", "A5→"), ("ly", "A5→")],
                [("ghost", "F5"), ("is", "F5→")]],
         peak=(5, 1),
         note="O TETO DO MAPA: Bb5 — e a fábrica CORRIGE o mestre pela 2ª vez: o pico "
              "cai no “CLOSE”, não no “GHOST” (como eu apostei!). A mecânica prometida "
              "se confirma e no mais alto nível: o Bb5 chega SUSPENSO — 7ª sobre o C/E "
              "— e vira FUNDAMENTAL quando o Bb chega no tempo seguinte. A assinatura "
              "da música (a nota não se mexe, só muda de função) executada no teto. O "
              "“GHOST” re-ataca no F5 depois do A5 de 4 tercinas (“as the HO-ly” "
              "cavalga) — no disco Jon estica o “GHO-O-OST” sobre esse A5→F5; as duas "
              "leituras cabem nas mesmas notas. E o platô de abertura: “oh-I-WAN” com "
              "F5 seguro de quase 4 tercinas — a nota do gancho virou pedal."),
    dict(label="CH2·4 — “And lay you down on a bed of roses” (c. 32–33 · F → Bb → F → Bb)",
         chords=[("F", 1), ("Bb", 3), ("F", 5), ("Bb", 7)],
         beats=[[("and", "A5→")],
                [("lay", "G5"), ("you", "F5")],
                [("down", "F5→")],
                [("on", "D5"), ("a", "D5")],
                [("bed", "D5")],
                [("of", "C5→")],
                [("ro", "F5→")],
                [("ses", "D5›D5›D5")]],
         peak=(1, 0),
         note="A última linha começa no GRITO: “AND” = A5 (a 2ª nota mais aguda do "
              "mapa, um grau abaixo do teto) segurada por um tempo inteiro sobre o F. "
              "E o word-painting se INVERTE: no REFRAO 1 o “down” afundava (G4›F4→); "
              "agora ele PLANAA no F5 de quase 4 tercinas. “On a bed” martela D5s (a "
              "cor de F6 de novo — a 6ª que já coloriu o “sleep”), e o final inverte o "
              "gancho: desta vez quem segura é o “RO” (F5 de 4+ tercinas!) com o “ses” "
              "ornando em D5s. A harmonia fecha o arco: F↔Bb — os DOIS acordes da "
              "intro, balançando pela última vez. (No esqueleto, esses D5s entregam o "
              "verso “so far away”; o corte de TV os transforma em entrega do aplauso "
              "e do bis.)"),
]
CH2_FILLS = {}
CH2_NOTA = ("O refrão inteiro de 4 linhas — a TEMPESTADE depois da rampa: banda completa, "
            "plateia em pé, e o transcript só consegue captar um pedaço entre [cheering "
            "and music] e [applause]. Linhas 1-2 = o mapa da meia-voz (reciclagem da "
            "casa); linhas 3-4 = o voo novo, com o TETO: Bb5 no “CLOSE”. Depois vem o "
            "aplauso — e o bis.")

CAMA_CH2 = ("Cama (mão esquerda): as linhas 1-3 usam a escada do REFRAO 1 (Bb2·C2·F2·E2·D2·C2·"
            "Bb2·F2); a linha 4 balança F2·Bb2·F2·Bb2 — os dois acordes da intro fechando o "
            "arco. Detalhe do baixo em c32: ele anda F-C-F-G-A → Bb — a escadinha que anuncia "
            "a chegada por baixo do “down” planando.")

# ============================================================ ZUGABE — o BIS (fecha os 3min09)
# O aplauso não o deixa sair ([applause] no transcript) — e ele volta: o refrão
# de novo, DECORADO. E aqui o esqueleto entrega de graça: o refrão 2 do original
# (c44–49) JÁ vem com os ad-libs NOTADOS — o gancho de 8 F5s, a corrida do “HO”
# (A5›G5›F5›A5 entre os dois A5 segurados) — e o final (c87–91) traz a última
# declaração, a ROSA segurada (D5 = a terça do Bb, a nota-cor do rocking da
# intro) e o tag grave “LAY YOU DOWN”. O transcript vira DETECTOR de ad-lib:
# onde o ASR engole palavra, o esqueleto tem melisma. A numeração salta
# (c44 → c87) de propósito: cada nota é do esqueleto, na casa onde o original
# a canta.
ZUGABE = [
    dict(label="Z1 — “I wanna lay you down in a bed of roses” (c. 44–45 · o gancho da meia-voz, agora ESTICADO — o bis já abre decorando)",
         chords=[("Bb", 1), ("C", 2), ("F", 3), ("C/E", 5), ("Dm", 6)],
         beats=[[("I", "Bb4"), ("wan", "Bb4"), ("na", "Bb4")],
                [("lay", "Bb4"), ("you", "A4"), ("down", "G4")],
                [("own", "F4→")],
                [("·", "·")],
                [("in", "F5"), ("a", "F5"), ("be", "F5")],
                [("ed", "F5"), ("of", "F5")],
                [("ro", "F5"), ("o", "F5"), ("ses", "F5")]],
         peak=(5, 0),
         note="O mesmo gancho e a mesma escada (Bb→C→F) da meia-voz — mas o "
              "esqueleto do refrão 2 já vem decorado: o “down” estica a resolução "
              "(o F4 segurado por 2 tempos: “dow-own”) e o “in a bed of roses” "
              "re-articula OITO F5s — a meia-voz usava seis (“in a be-ed of "
              "ro-o-ses”). É a zona A do detector: o ASR do transcript entrega "
              "“I want to lay you down in a bed” e engole o “of roses” — onde a "
              "palavra vira melisma, o detector desiste."),
    dict(label="Z2 — “For tonight, I sleep on a bed of nails” (c. 46 · a escada de terças, uma tercina mais apertada)",
         chords=[("C", 1), ("Bb", 2), ("F", 3)],
         beats=[[("for", "E5"), ("to", "E5")],
                [("night", "D5"), ("I", "D5"), ("sleep", "D5")],
                [("on", "C5→"), ("a", "C5→"), ("bed", "C5→")],
                [("of", "C5→"), ("nails", "C5→")]],
         peak=(1, 0),
         note="A escada E5-D5-C5 de sempre — só que uma tercina mais apertada: no "
              "bis o “sleep” emenda direto no monólito (“night-I-sleep” num tempo "
              "só) e “on a bed of nails” cavalga o C5 segurado até o fim, sem "
              "soltar. Detalhe do detector: o ASR ouve “I sleep”, sem o “I’ll” do "
              "disco — ou a gramática solta no bis, ou o “I’ll” se perdeu no "
              "estica do “tonight”: as duas leituras cabem no mesmo desenho."),
    dict(label="Z3 — “I wanna be just as close as the Holy Ghost is” (c. 47–49 · O TETO DECORADO — a zona de ad-lib PRINCIPAL do bis)",
         chords=[("F/C", 1), ("Dm", 2), ("C/E", 4), ("Bb/F", 5), ("F", 6)],
         beats=[[("oh", "F5"), ("I", "F5"), ("wan", "F5→")],
                [("na", "F5→")],
                [("be", "F5"), ("just", "F5"), ("as", "G5›G5")],
                [("·", "·")],
                [("close", "Bb5"), ("as", "Bb5")],
                [("the", "A5→")],
                [("HO", "A5›G5›F5›A5")],
                [("ly", "A5→")],
                [("ghost", "G5"), ("is", "F5→")]],
         peak=(5, 0),
         note="O TETO de novo — Bb5 no “CLOSE” — e agora COM A CORRIDA NOTADA: na "
              "meia-voz os três A5 do “the-ho-ly” cavalgavam numa altura só; no "
              "refrão decorado do esqueleto, o “HO” DESCE E VOLTA (A5›G5›F5›A5) "
              "entre os dois A5 segurados (3.8 e 3.9 tercinas!), e o “ghost” sobe "
              "ao G5 antes do “is” F5 (que segue soando quando o Bb chega — a "
              "assinatura de novo). É ESSE melisma que o ASR engole: “I want to "
              "lay you just as cold as this”. E a harmonia conta outra história: "
              "no bis o Bb5 JÁ CHEGA fundamental (o baixo em F: Bb/F) — na "
              "meia-voz ele pendia como 7ª sobre o C/E e virava fundamental um "
              "tempo depois. A assinatura comprimida na chegada."),
    dict(label="Z4 — “I wanna lay you down in a bed…” (c. 87–89 · a ÚLTIMA declaração — o “of roses” vira a ROSA segurada)",
         chords=[("Bb", 1), ("F", 2), ("Bb", 4), ("F", 5), ("Dm", 6), ("C", 7), ("Bb/F", 8)],
         beats=[[("I", "D5"), ("wan", "D5")],
                [("na", "D5"), ("lay", "C5→")],
                [("you", "F5→")],
                [("down", "D5"), ("in", "D5"), ("a", "D5")],
                [("bed", "C5→")],
                [("of", "F5→")],
                [("ro", "E5→")],
                [("ses", "D5→")],
                [("·", "·")]],
         peak=(3, 0),
         note="A última declaração — montada do FINAL do original (c87–89): o "
              "balanço F↔Bb (os dois acordes da intro!) embalando “I wanna lay "
              "you down in a”, e o rabo desce F5-E5-D5… e o “ses” SEGURA: D5 por "
              "quase um compasso. O D5 sobre o Bb é A TERÇA — a nota-cor que a "
              "intro chamava de “a rosa” (o D5 do rocking!). A música termina "
              "segurando a ROSA do título. É a zona C: o ASR ouve até “in a bed” "
              "e o rabo melismado some. TRANSPARÊNCIA: no original os rabos "
              "repetem “in a bed of roses” duas vezes (c87–88) antes da segurada "
              "— o mapa mostra a versão comprimida do bis; se o seu bis quiser "
              "repetir, os rabos estão prontos. E se a 4ª linha for a linha 4 "
              "clássica (o berro “AND”=A5), o mapa do CH2·4 continua pronto."),
    dict(label="Z5 — o TAG: “(and) LAY YOU DOWN” (c. 90–91 · GRAVE, afundando — a última frase do mapa)",
         chords=[("Bb/F", 1), ("F", 3)],
         beats=[[("lay", "Bb4"), ("you", "A4")],
                [("DOWN", "G4"), ("·", "·"), ("own", "G4")],
                [("own", "F4→")],
                [("·", "·")]],
         anac=("and", "F4"),
         peak=(1, 0),
         note="A última frase do mapa — e ela DESCE: o “and” em anacruze (F4), "
              "“LAY”(Bb4) “you”(A4), e o “DOWN” afunda em três notas — G4, G4 de "
              "novo, e o F4 FINAL segurado (8.5 tercinas, a nota mais longa da "
              "seção). O word-painting dos três “down” completa o arco: no "
              "REFRAO 1 ele afundou (G4›F4→), no REFRAO 2 planou (F5→) — o do "
              "bis POUSA NO FUNDO: F4, a MESMA nota onde o primeiro “down” da "
              "meia-voz resolveu. O círculo fecha onde abriu. E a harmonia é a "
              "moldura inteira: o Bb/F abre, o F final fica (o acorde final do "
              "original segura ~3 compassos). TRANSPARÊNCIA: se no clip o grito "
              "do tag subir (o A5 do “AND” ou o G5-F5 da linha 4), a cama é a "
              "mesma — os mapas estão prontos."),
]
ZUGABE_FILLS = {
    0: "ZONA DE AD-LIB A — o “down” esticado (F4→ por 2 tempos) + os OITO F5 do "
       "“in a be-ed of ro-o-ses”: é aqui que o detector do transcript engole o "
       "“of roses”. Notado no esqueleto (c44–45) — não é invenção do bis.",
    2: "ZONA DE AD-LIB B — a principal: o “HO” do “Holy Ghost” vira a CORRIDA "
       "A5›G5›F5›A5 entre os dois A5 segurados, e o “ghost” sobe ao G5. O ASR "
       "ouve “just as cold as this”: os melismas engolem “as the Holy Ghost "
       "is” inteiro. As notas da corrida vêm do esqueleto (c48) — dados, não "
       "palpite.",
    3: "ZONA DE AD-LIB C — o rabo da última declaração: “of-ro-ses” descendo "
       "F5-E5-D5 e a ROSA (D5, a terça do Bb) segurada por quase um compasso. "
       "O ASR para no “in a bed”.",
}
ZUGABE_NOTA = ("O aplauso não o deixa sair — [applause] no transcript — e ele volta: "
               "o refrão de novo, agora DECORADO. E o esqueleto entrega de graça: o "
               "refrão 2 do original (c44–49) já vem com os ad-libs notados, e o "
               "final (c87–91) traz a última declaração, a rosa segurada e o tag "
               "grave. O transcript vira DETECTOR: onde o ASR engole palavra, o "
               "esqueleto tem melisma. No meio, ficou fora do corte de TV: os "
               "versos “so far away”/“hotel bar” (c34–43, c51–57), o solo (c58–72, "
               "a segunda metade rondando os DOIS acordes da intro) e o refrão "
               "final dobrado (c73–82). O bis comprime tudo: refrão decorado + "
               "final. A numeração salta (c44 → c87) de propósito — cada nota é do "
               "esqueleto, na casa onde o original a canta.")

CAMA_ZUGABE = ("Cama (mão esquerda): linhas 1-2 = a escada de sempre (Bb2·C2·F2 / "
               "C2·Bb2·F2); linha 3 = F2·D2·E2·Bb2·F2 com o baixo passeando nas "
               "inversões (F/C, Bb/F); a última declaração = o BALANÇO da intro "
               "(Bb↔F, duas vezes) e a cadência final Dm2→C2→Bb/F (a rosa D5 em "
               "cima, o baixo F segurado por ~3 compassos)→F. O mapa termina na "
               "moldura onde começou: os DOIS acordes do rocking.")

# ============================================================ TEXTO (chat)
def phrase_lines(p):
    """Renderiza uma frase em 4 linhas: acordes · tempos · sílabas · notas."""
    beats = p["beats"]
    anac = p.get("anac")
    chords_at = {i: c for c, i in p["chords"]}          # i = tempo (1-based)
    peak = p.get("peak")                                 # (tempo 1-based, índice do par)

    def mark(bi, pi, note):
        return note + ("▲" if (bi, pi) == peak else "")

    cols = []  # (rótulo, pares, larguras por par, largura total do tempo)
    if anac:
        pw = [max(len(anac[0]), len(anac[1])) + 1]
        cols.append(("e", [anac], pw, max(sum(pw), 3)))
    for bi, b in enumerate(beats, start=1):
        pairs = b if b else [("·", "·")]
        pw = [max(len(s), len(mark(bi, pi, n))) + 1
              for pi, (s, n) in enumerate(pairs)]
        w = max(sum(pw), len(str(bi)) + 2, len(chords_at.get(bi, "")) + 2)
        cols.append((str(bi), pairs, pw, w))

    r_chord = r_beat = r_syl = r_note = ""
    offset = 1 if anac else 0
    for ci, (label, pairs, pw, w) in enumerate(cols):
        bi = ci - offset + 1
        if anac and ci == 0:
            r_chord += "".ljust(w)
        else:
            r_chord += chords_at.get(bi, "").ljust(w)
        r_beat += label.ljust(w)
        s = n = ""
        for pi, (sy, no) in enumerate(pairs):
            s += sy.ljust(pw[pi])
            n += mark(bi, pi, no).ljust(pw[pi])
        r_syl += s.ljust(w)
        r_note += n.ljust(w)
    return (r_chord.rstrip(), r_beat.rstrip(), r_syl.rstrip(), r_note.rstrip())


def chat_section(title, phrases, fills=None, first_line=None):
    out = [f"[{title}]", ""]
    if first_line:
        out += [first_line, ""]
    for k, p in enumerate(phrases):
        if p.get("label"):
            out.append(f"◆ {p['label']}")
        c, b, s, n = phrase_lines(p)
        out += [x for x in (c, b, s, n) if x.strip()]
        if p.get("note"):
            out.append(f"     ({p['note']})")
        out.append("")
        if fills and k in fills:
            out.append(f"↳ ({fills[k]})")
            out.append("")
    return "\n".join(out)


def sanity():
    """Confere: sílabas == notas por frase; picos dentro do grid."""
    for name, sec in (("INTRO", INTRO), ("V1", V1), ("V2", V2), ("CH1", CH1),
                      ("LIFT", LIFT), ("CH2", CH2), ("ZUGABE", ZUGABE)):
        for k, p in enumerate(sec):
            beats = p["beats"]
            nsyl = sum(1 for b in beats for s, _ in b if s != "·")
            nnot = sum(1 for b in beats for _, n in b if n != "·")
            a = p.get("anac")
            if a:
                nsyl += 1 if a[0] != "·" else 0
                nnot += 1 if a[1] != "·" else 0
            ok = "OK " if nsyl == nnot else "ATENÇÃO"
            peak = p.get("peak")
            pok = ""
            if peak:
                bi, pi = peak
                lst = beats[bi - 1]
                pok = f" | pico={lst[pi][1].rstrip('→')}" if pi < len(lst) else " | PICO FORA DO GRID!"
            print(f"  {name}[{k+1}] sílabas={nsyl} notas={nnot} {ok}{pok}")


def chat_bor():
    parts = [chat_section("INTRO — o rocking (esqueleto c. 3–10 · no clipe: encurtado, sob a conversa dos coaches)",
                          INTRO, INTRO_FILLS, first_line=INTRO_NOTA),
             chat_section("VERSO 1 — “Sittin' here wasted…” (esqueleto c. 11–19 · 5 frases · 71 sílabas)",
                          V1, V1_FILLS, first_line=V1_NOTA),
             f"({CAMA_V1})",
             chat_section("VERSO 2 — “With an ironclad fist…” (esqueleto c. 20–26 · 5 frases · 63 sílabas · o chão abre)",
                          V2, V2_FILLS, first_line=V2_NOTA),
             f"({CAMA_V2})",
             chat_section("REFRAO 1 — “I wanna lay you down…” (esqueleto c. 27–29 · no corte de TV: a meia-voz antes da tempestade)",
                          CH1, CH1_FILLS, first_line=CH1_NOTA),
             f"({CAMA_CH1})",
             chat_section("LIFT — a RAMPA do corte de TV (reprise das frases do V2 · a banda sobe)",
                          LIFT, LIFT_FILLS, first_line=LIFT_NOTA),
             chat_section("REFRAO 2 — o refrão inteiro, a tempestade (esqueleto c. 27–33 · 4 linhas · o teto Bb5)",
                          CH2, CH2_FILLS, first_line=CH2_NOTA),
             f"({CAMA_CH2})",
             chat_section("ZUGABE — o BIS que fecha os 3min09 (o refrão DECORADO do esqueleto c. 44–49 + o final c. 87–91 · zonas de ad-lib + o tag “LAY YOU DOWN”)",
                          ZUGABE, ZUGABE_FILLS, first_line=ZUGABE_NOTA),
             f"({CAMA_ZUGABE})",
             "\n(MAPA COMPLETO — 25 frases verdes em 7 seções ✅. Falta a última entrega da PoC 3: o HTML — mapa-musical-bed-of-roses.html 🌹)"]
    return "\n\n".join(parts)


# ============================================================ HTML (veludo vermelho 🌹)
import re as _re

LH_NOTES = {"Bb2", "A2", "C2", "D2", "E2", "F2", "G3", "A3", "Bb3", "C4", "D4", "F4"}


def _all_note_names():
    names = set()
    for phrases in (INTRO, V1, V2, CH1, LIFT, CH2, ZUGABE):
        for p in phrases:
            for b in p["beats"]:
                for _, nt in b:
                    for tok in nt.replace("→", "").split("›"):
                        if _re.match(r"^[A-G][#b]?\d$", tok):
                            names.add(tok)
            a = p.get("anac")
            if a:
                for tok in a[1].replace("→", "").split("›"):
                    if _re.match(r"^[A-G][#b]?\d$", tok):
                        names.add(tok)
    return names


def note_run_html(nt, is_peak):
    if nt == "·":
        return '<span class="nt rest">·</span>'
    out = []
    toks = nt.split("›")
    for j, t in enumerate(toks):
        hold = " hold" if t.endswith("→") else ""
        peak = " peak" if is_peak else ""
        out.append(f'<span class="nt{peak}{hold}">{t}</span>')
        if j < len(toks) - 1:
            out.append('<span class="glue">›</span>')
    if is_peak:
        out.append('<span class="pmark">▲</span>')
    return "".join(out)


def phrase_html(p, label):
    chords_at = {i: c for c, i in p["chords"]}          # i = tempo (1-based)
    peak = p.get("peak")                                 # (tempo, índice do par)
    cells = []
    anac = p.get("anac")
    if anac:
        cells.append('<div class="tcell anac"><div class="chord"></div><div class="tnum">e</div>'
                     f'<div class="pairs"><div class="pair"><div class="syl">{anac[0]}</div>'
                     f'<div class="notes">{note_run_html(anac[1], False)}</div></div></div></div>')
    for bi, b in enumerate(p["beats"], start=1):
        pairs = b if b else [("·", "·")]
        inner = []
        for pi, (sy, nt) in enumerate(pairs):
            is_peak = (bi, pi) == peak
            syl_cls = "syl rest" if sy == "·" else "syl"
            inner.append(f'<div class="pair"><div class="{syl_cls}">{sy}</div>'
                         f'<div class="notes">{note_run_html(nt, is_peak)}</div></div>')
        cells.append(f'<div class="tcell"><div class="chord">{chords_at.get(bi, "")}</div>'
                     f'<div class="tnum">{bi}</div><div class="pairs">{"".join(inner)}</div></div>')
    note = f'<div class="pnote">💡 {p["note"]}</div>' if p.get("note") else ""
    return (f'<div class="card"><div class="plabel">{label}</div>'
            f'<div class="phrase">{"".join(cells)}</div>{note}</div>')


def section_html(title, subtitle, cama, phrases, fills):
    out = [f'<h2>{title}</h2>', f'<p class="small">{subtitle}</p>',
           f'<p class="small cama">🛏️ <b>Cama:</b> {cama}</p>']
    for k, p in enumerate(phrases):
        out.append(phrase_html(p, p.get("label") or f"Frase {k + 1}"))
        if fills and k in fills:
            out.append(f'<div class="fill">✨ {fills[k]}</div>')
    return "".join(out)


def _geo(n):
    """Posição geométrica da tecla (na grafia de Fá#, o Mi# mora na tecla branca de Fá)."""
    return "F" + n[2:] if n.startswith("E#") else n


def keyboard_svg(altura=0):
    names = _all_note_names()
    if altura == 1:
        mel = {_t_nome(n) for n in names - LH_NOTES}
        lh = {_t_nome(n) for n in LH_NOTES}
        BLACK = {"C": "C#", "D": "D#", "F": "F#", "G": "G#", "A": "A#"}
        CALLOUTS = {"B5": ("▲ teto", "#ff7b93"), "F#5": ("o gancho", "#ff7b93"),
                    "D#5": ("a rosa", "#d8a84e")}
    else:
        mel = names - LH_NOTES
        lh = set(LH_NOTES)
        BLACK = {"C": "C#", "D": "D#", "F": "F#", "G": "G#", "A": "Bb"}
        CALLOUTS = {"Bb5": ("▲ teto", "#ff7b93"), "F5": ("o gancho", "#ff7b93"),
                    "D5": ("a rosa", "#d8a84e")}
    disp = {**{_geo(n): n for n in mel}, **{_geo(n): n for n in lh}}  # a cama vence
    mel = {_geo(n) for n in mel}
    lh = {_geo(n) for n in lh}
    Y0, W, H, BW, BH = 36, 30, 150, 18, 92
    WHITE = ["C", "D", "E", "F", "G", "A", "B"]
    x, parts, pos = 0, [], {}
    for octv in range(2, 6):
        for wname in WHITE:
            label = f"{wname}{octv}"
            fill, txt, tcol = "#f3e7d6", "", "#b99a8e"
            if label in mel:
                fill, tcol, txt = "#d4526e", "#ffffff", disp.get(label, label)
            if label in lh:
                fill, tcol, txt = "#d8a84e", "#3a2410", disp.get(label, label)
            parts.append(f'<rect x="{x}" y="{Y0}" width="{W}" height="{H}" rx="3" fill="{fill}" stroke="#7a5a52"/>')
            pos[label] = x + W / 2
            if txt:
                parts.append(f'<text x="{x + W / 2}" y="{Y0 + 118}" text-anchor="middle" font-size="11" '
                             f'font-weight="700" fill="{tcol}">{txt}</text>')
            if label.startswith("C"):
                parts.append(f'<text x="{x + W / 2}" y="{Y0 + 140}" text-anchor="middle" font-size="10" '
                             f'fill="#a58a80">{label}</text>')
            if label == "C4":
                parts.append(f'<circle cx="{x + W / 2}" cy="{Y0 + 100}" r="4" fill="#d8a84e"/>')
                parts.append(f'<text x="{x + W / 2}" y="{Y0 + 94}" text-anchor="middle" font-size="9" '
                             f'font-weight="700" fill="#d8a84e">dó central</text>')
            if wname in BLACK:
                bl = f"{BLACK[wname]}{octv}"
                bx = x + W - BW / 2
                if bl in mel:
                    bfill, btxt, btcol = "#c2425e", bl, "#ffffff"
                elif bl in lh:
                    bfill, btxt, btcol = "#b07f2e", bl, "#241505"
                else:
                    bfill, btxt, btcol = "#26141b", "", "#fff"
                parts.append(f'<rect x="{bx}" y="{Y0}" width="{BW}" height="{BH}" rx="2" fill="{bfill}" stroke="#140a0e"/>')
                pos[bl] = bx + BW / 2
                if btxt:
                    parts.append(f'<text x="{bx + BW / 2}" y="{Y0 + 80}" text-anchor="middle" font-size="9" '
                                 f'font-weight="700" fill="{btcol}">{btxt}</text>')
            x += W
    for label, (txt, col) in CALLOUTS.items():
        if label in pos:
            cx = pos[label]
            parts.append(f'<line x1="{cx}" y1="23" x2="{cx}" y2="{Y0 - 3}" stroke="{col}" stroke-width="1.5"/>')
            parts.append(f'<text x="{cx}" y="17" text-anchor="middle" font-size="9.5" '
                         f'font-weight="700" fill="{col}">{txt}</text>')
    width = x + 2
    return (f'<svg viewBox="0 0 {width} {Y0 + H + 8}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="Teclado guia do Bed of Roses">' + "".join(parts) + "</svg>")


GUIDE_BOR = [
    ("🎹 Intro", "o rocking no piano — no clipe, encurtado sob a conversa dos coaches",
     "Bb6 ↔ Fadd9", "INTRO", "c. 3–10"),
    ("Verso 1", "“Sittin' here wasted…” — a voz entra no Bb4", "Bb · F/A · Fsus2 · F", "V1", "c. 11–19"),
    ("Verso 2", "“With an ironclad fist…” — o chão abre: baixo na fundamental", "Bb · F", "V2", "c. 20–26"),
    ("🕯️ Refrão 1", "a MEIA-VOZ — “I wanna lay you down…”", "Bb→C→F · C/E→Dm · C→Bb→F", "CH1", "c. 27–29"),
    ("🛫 Lift", "a RAMPA de TV — “about all of the things…” + [cheering]", "cama do V2 (F/A→Bb→F)", "LIFT", "corte de TV"),
    ("⛈️ Refrão 2", "a tempestade — banda inteira, teto Bb5 no “CLOSE”", "escada do refrão + F↔Bb", "CH2", "c. 27–33"),
    ("🌹 Zugabe", "o BIS — refrão decorado + o tag “LAY YOU DOWN”", "refrão + Dm→C→Bb/F→F", "ZUGABE", "c. 44–49 + 87–91"),
]


def guide_table_html():
    rows = "".join(
        f'<tr><td>{i}</td><td><b>{n}</b></td><td>{como}</td><td><code>{ac}</code></td>'
        f'<td>{mp}</td><td>{comp}</td></tr>'
        for i, (n, como, ac, mp, comp) in enumerate(GUIDE_BOR, 1))
    return (f'<table class="lh"><tr><th>#</th><th>Seção</th><th>Como reconhece</th>'
            f'<th>Acordes</th><th>No mapa</th><th>Comp. (esqueleto)</th></tr>{rows}</table>')


def _corpo_fa():
    css = """
:root{--ink:#f5e9dc;--acc:#d8a84e;--peak:#ff7b93;--muted:#c9a89e;--card:#43141e;--bg:#2a0a11;--chip:#61121f;--line:#63222e;--cellbg:#571a26}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(ellipse at 50% -12%, #521527 0%, #2a0a11 55%, #1c060c 100%);color:var(--ink);font-family:'Segoe UI',system-ui,-apple-system,'Helvetica Neue',sans-serif;line-height:1.5}
.wrap{max-width:1120px;margin:0 auto;padding:30px 18px 60px}
header h1{margin:0;font-size:34px;letter-spacing:.5px}
header h1 span{color:var(--acc)}
header .sub{color:var(--muted);font-size:16px;margin:6px 0 14px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:8px}
.chips span{background:var(--chip);color:#f8e9d8;border:1px solid #8a2a3a;border-radius:999px;padding:4px 12px;font-size:12.5px;font-weight:600}
h2{font-size:24px;margin:38px 0 4px;padding-bottom:6px;border-bottom:3px solid var(--acc);color:#fdf3e7}
.card{background:linear-gradient(180deg,#481624,#3b101b);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:12px 0;box-shadow:0 3px 12px rgba(0,0,0,.35)}
.plabel{font-weight:800;color:var(--acc);font-size:15px;margin-bottom:10px}
.phrase{display:flex;flex-wrap:wrap;gap:7px;align-items:stretch}
.tcell{min-width:58px;flex:0 0 auto;text-align:center;padding:5px 6px 8px;border-radius:9px;background:var(--cellbg);border:1px solid #6f2533}
.tcell.anac{border-style:dashed;background:#4a1622}
.chord{font-weight:800;font-size:12.5px;color:#ffe9c9;background:var(--chip);border:1px solid #8a2a3a;border-radius:6px;padding:1px 7px;display:inline-block;min-height:20px}
.chord:empty{display:none}
.tnum{font-size:10.5px;color:var(--muted);margin:4px 0 3px;font-weight:700}
.pairs{display:flex;gap:5px;justify-content:center}
.pair{min-width:30px}
.syl{font-size:12.5px;color:#f0dcc9;margin:2px 0;min-height:16px;overflow-wrap:anywhere}
.syl.rest{color:#8a6a63}
.notes{font-size:13.5px;font-weight:700;white-space:nowrap}
.nt{color:#fff}
.nt.hold{color:var(--acc)}
.nt.peak{color:var(--peak)}
.nt.rest{color:#8a6a63;font-weight:400}
.pmark{color:var(--peak);font-size:10px}
.glue{color:#a97e74;margin:0 1px;font-weight:400}
.pnote{margin-top:10px;font-size:13.5px;color:#e6d2c4;border-top:1px dashed var(--line);padding-top:8px}
.fill{background:rgba(216,168,78,.07);border:1px solid var(--acc);border-radius:10px;padding:9px 13px;margin:10px 0;font-size:13.5px;color:#f3e3c8}
.tip{background:linear-gradient(180deg,#471a29,#3a1220);border:1px solid #7a2c3a;border-left:4px solid var(--acc);border-radius:14px;padding:14px 18px;margin:16px 0;font-size:14.5px}
.tip h3{margin:0 0 8px;color:var(--acc);font-size:16px}
.small{color:var(--muted);font-size:13.5px}
.cama{margin-top:2px}
table.lh{border-collapse:collapse;width:100%;font-size:13.5px;margin:8px 0}
table.lh th{background:var(--chip);color:#ffe9c9;text-align:left;padding:6px 9px}
table.lh td{border-bottom:1px solid var(--line);padding:6px 9px;vertical-align:top}
code{background:#5d1a28;color:#ffd9a0;padding:1px 5px;border-radius:5px;font-size:12.5px}
footer{margin-top:36px;color:var(--muted);font-size:12.5px;border-top:1px solid var(--line);padding-top:14px}
svg{width:100%;height:auto;display:block}
"""

    s_intro = section_html("🎹 INTRO — o rocking (esqueleto c. 3–10 · no clipe: encurtado, sob a conversa dos coaches)",
                           INTRO_NOTA,
                           "Bb6 (Bb3+D4+F4) ↔ Fadd9 (A3+C4+F4) — o par que moldura a música inteira.",
                           INTRO, INTRO_FILLS)
    s_v1 = section_html("🎤 VERSO 1 — “Sittin' here wasted…” (esqueleto c. 11–19 · 5 frases · 71 sílabas)",
                        V1_NOTA, CAMA_V1, V1, V1_FILLS)
    s_v2 = section_html("🎤 VERSO 2 — “With an ironclad fist…” (esqueleto c. 20–26 · 5 frases · 63 sílabas · o chão abre)",
                        V2_NOTA, CAMA_V2, V2, V2_FILLS)
    s_ch1 = section_html("🕯️ REFRAO 1 — “I wanna lay you down…” (esqueleto c. 27–29 · a meia-voz antes da tempestade)",
                         CH1_NOTA, CAMA_CH1, CH1, CH1_FILLS)
    s_lift = section_html("🛫 LIFT — a RAMPA do corte de TV (reprise das frases do V2 · a banda sobe)",
                          LIFT_NOTA,
                          "a cama do V2 (F/A → Bb → F — o chão aberto): a rampa sobe por cima dela.",
                          LIFT, LIFT_FILLS)
    s_ch2 = section_html("⛈️ REFRAO 2 — o refrão inteiro, a tempestade (esqueleto c. 27–33 · 4 linhas · o teto Bb5)",
                         CH2_NOTA, CAMA_CH2, CH2, CH2_FILLS)
    s_zugabe = section_html("🌹 ZUGABE — o BIS que fecha os 3min09 (refrão decorado c. 44–49 + final c. 87–91 · zonas de ad-lib + o tag “LAY YOU DOWN”)",
                            ZUGABE_NOTA, CAMA_ZUGABE, ZUGABE, ZUGABE_FILLS)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bed of Roses — Bon Jovi · versão Matthias Nebel · O Mapa Musical</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">

<header>
<h1>Bed of Roses 🌹 <span>· Bon Jovi — versão Matthias Nebel</span></h1>
<p class="sub">O mapa musical — nota a nota, do rocking Bb↔F à rosa segurada no bis</p>
<div class="chips">
<span>The Voice of Germany · 18/10/2018 · 3min09 + Zugabe</span><span>25 frases · 7 seções</span>
<span>tom: Fá maior (esqueleto −1st)</span><span>grade: 12/8 lento</span>
<span>teto: Bb5 no “CLOSE”</span><span>MIDI: bitmidi 19001</span>
</div>
</header>

<div class="card">
<p><b>Como ler:</b> cada cartão é uma frase; cada célula é <b>1 tempo grande do 12/8</b> (com até
3 tercinas dentro, lado a lado). O chip escuro no topo da célula = o acorde que entra naquele
tempo; o número miúdo acima dele = o tempo. Os símbolos:
<span class="nt hold">→</span> nota comprida, que segue soando enquanto a frase anda ·
<span class="glue">›</span> notas ligadas na mesma sílaba · <span class="nt">·</span> silêncio
(a nota anterior segue se tinha <span class="nt hold">→</span>) · sílabas novas sobre uma nota com
<span class="nt hold">→</span> = <b>cavalgam</b> a nota segurada (re-articulam na mesma altura) ·
<span class="nt peak">rosa</span> = o pico da frase · célula tracejada “e” = anacruze.
A numeração de compassos é a do esqueleto MIDI — no corte de TV as contagens variam, a estrutura
relativa é idêntica.</p>
<p class="small" style="margin-bottom:0">🎚️ <b>Transparência da afinação:</b> o esqueleto (MIDI do
original) foi gravado 1 semitom acima do disco (Fá# maior); o mapa já chega transposto −1st para
<b>Fá maior</b> — o tom do disco (partitura oficial) e do single 2019 do Matthias. Se ao tocar com
o clipe soar 1 semitom deslocado, a fábrica transpõe o mapa inteiro num comando: <i>o desenho não
muda um milímetro</i>.</p>
</div>

<div class="tip">
<h3>🎭 Como este mapa foi feito (a Prova de Conceito nº 3)</h3>
Um ao vivo de TV, <b>sem MIDI próprio</b> — o problema mais duro da série. Três pilares:
<b>esqueleto</b> = MIDI do original do Bon Jovi (transposto −1st); <b>estrutura</b> = o transcript
oficial do corte de TV (o que sobreviveu aos 3min09 — sem o V3 “so far away”, bridge ou solo);
<b>tom</b> = triangulação de 4 fontes (Musicnotes, Chordify ×2, GuitarTuna). E a ferramenta nova
do bis: <b>o transcript como detector de ad-lib</b> — cada palavra que o ASR engoliu caiu em cima
de um melisma real do esqueleto (zonas A, B e C). Três vezes a fábrica corrigiu o palpite com
dados: o pico do V2 (“that I long”), o teto no “CLOSE” (não no “GHOST”) e o plano do bis inteiro
(reciclagem → o refrão já decorado do esqueleto, c. 44–49).
</div>

<h2>🖐️ O teclado do Bed of Roses</h2>
<div class="card">
{keyboard_svg()}
<p class="small" style="margin-bottom:0">Rosa = melodia e figuras do mapa (do F4 do “own” ao
Bb5 do teto). Dourado = a cama da mão esquerda (a escada Bb2·C2·D2·E2·F2 + os corpos da moldura
da intro). O ponto dourado é o dó central. E os três apontamentos: <b>o gancho F5</b>, <b>a rosa
D5</b> (a terça do Bb — a nota-cor do rocking) e <b>o teto Bb5</b>.</p>
</div>

{s_intro}

{s_v1}

{s_v2}

{s_ch1}

{s_lift}

{s_ch2}

<div class="tip">
<h3>🔑 A assinatura da música: “a nota não se mexe — só muda de função”</h3>
Quatro execuções da mesma jogada, uma por seção — a altura permanece, o acorde embaixo troca de
cor:<br>
<b>1) V1:</b> o F5 do “vot-ka's” — a nota segue enquanto a cama escurece.<br>
<b>2) V2:</b> o F5 do “that I” — de novo: mesma altura, nova função.<br>
<b>3) REFRAO 1:</b> o F5 do “of” — chega como 4ª suspensa sobre o C/E e só vira nota do acorde
(3ª) quando o Dm chega.<br>
<b>4) O TETO:</b> o Bb5 do “CLOSE” chega como 7ª sobre o C/E e vira <b>fundamental</b> quando o
Bb chega — a assinatura no seu mais alto nível. E no bis, a jogada comprimida: o Bb5 <b>já chega
fundamental</b> (o baixo em F: Bb/F).
</div>

{s_zugabe}

<div class="tip">
<h3>🎁 O clipe em uma frase</h3>
A moldura é o rocking <b>Bb↔F</b> da intro; a voz entra no Bb4, promete no F5 (“in a bed of
RO-ses”), a TV inventa uma rampa por cima dos versos, a banda explode no refrão com o teto
<span class="nt peak">Bb5</span> no “CLOSE” — e o bis devolve tudo decorado: o gancho vira 8 F5,
o “HO” vira corrida, a música <b>segura a rosa</b> (D5, a terça do Bb) e o último “down” afunda
até o F4 — a mesma nota onde o primeiro “down” resolveu. <b>Começa e termina nos mesmos dois
acordes.</b>
</div>

<div class="tip">
<h3>♻️ Reciclagens da casa (por que o mapa é menor que a música)</h3>
<b>LIFT</b> = as frases do V2 com papel novo (alavanca, não clímax). <b>REFRAO 2, linhas 1-2</b>
= o mapa da meia-voz, nota por nota. <b>ZUGABE, linhas 1-2</b> = o refrão decorado do esqueleto.
São 25 frases, mas os moldes são bem menos — quem aprende a intro, o gancho e a escada do refrão
já toca quase tudo (como o V2 do Patience, que usou o mapa do V1).
</div>

<div class="tip">
<h3>🧵 As 7 costuras (é onde tudo se encaixa)</h3>
<b>1) Intro → V1:</b> a escadinha do piano entrega a voz exatamente no <span class="nt">Bb4</span>
(c. 11).<br>
<b>2) V1 → V2:</b> o chão abre — o baixo sai das inversões (F/A) e mora na fundamental
(<span class="nt">F2</span>).<br>
<b>3) V2 → Refrão 1:</b> o refrão entra A MEIA-VOZ — a promessa antes da tempestade.<br>
<b>4) Refrão 1 → Lift:</b> a meia-voz vira rampa — e o [cheering] do transcript estoura no
“that I long”.<br>
<b>5) Lift → Refrão 2:</b> o monólito C5 do “nails” termina exatamente onde o “OH” do teto vai
saltar — o trampolim está no lugar.<br>
<b>6) Refrão 2 → Zugabe:</b> no esqueleto viria o V3 “so far away” (c. 34) — o corte de TV troca
pelo aplauso… e o bis volta ao refrão.<br>
<b>7) O fim:</b> a rosa <span class="nt hold">D5→</span> segurada quase um compasso… e o tag
“LAY YOU DOWN” afunda até o <span class="nt">F4</span> — a mesma nota onde o primeiro “down”
resolveu. O círculo fecha.
</div>

<h2>🖐️ Mão esquerda (a cama)</h2>
<div class="card">
<p>Comece simples — só o baixo, um por acorde, bem fraquinho:</p>
<table class="lh">
<tr><th>Acorde</th><th>Baixo</th><th>Com corpo (2ª etapa)</th><th>Onde mora</th></tr>
<tr><td><b>Bb</b></td><td><code>Bb2</code></td><td>+ <code>Bb3+D4+F4</code> (o Bb6 da intro)</td><td>a casa — intro, versos, refrão, final</td></tr>
<tr><td><b>F/A</b></td><td><code>A2</code></td><td>+ <code>F3</code></td><td>a 3ª no baixo — verso 1</td></tr>
<tr><td><b>Fsus2</b></td><td><code>F2</code></td><td>+ <code>G3</code></td><td>a névoa — verso 1</td></tr>
<tr><td><b>F</b></td><td><code>F2</code></td><td>+ <code>A3+C4+F4</code> (o Fadd9)</td><td>a tônica — versos, refrão, final</td></tr>
<tr><td><b>C</b></td><td><code>C2</code></td><td>—</td><td>o degrau da escada — refrão</td></tr>
<tr><td><b>C/E</b></td><td><code>E2</code></td><td>+ <code>C3+G3</code> na direita</td><td>o escurecimento — refrão (“in a bed…”)</td></tr>
<tr><td><b>Dm</b></td><td><code>D2</code></td><td>—</td><td>a sombra — refrão</td></tr>
<tr><td><b>Bb/F</b></td><td><code>F2</code></td><td>+ <code>Bb2</code></td><td>o bis — o teto já chega fundamental</td></tr>
</table>
<p class="small" style="margin-bottom:0">💡 A escada do refrão: SOBE <code>Bb2→C2→F2</code>
(“I wanna lay you DOWN” — a palavra resolve na tônica), escurece <code>E2→D2</code>, DESCE
<code>C2→Bb2→F2</code> (“for tonight…”). E a moldura de sempre: os dois acordes da intro
balançando — <b>o refrão é a intro com letra</b>.</p>
</div>

<h2>✈️ Como estudar</h2>
<div class="card">
<ol>
<li><b>A moldura primeiro:</b> Bb↔F rocking — quem aprende a intro já sabe o balanço do refrão
e o final (os mesmos dois acordes abrem e fecham a música).</li>
<li><b>O gancho:</b> os <span class="nt">F5</span> do “in a bed of RO-ses” — a nota da música.
No bis ela vira oito.</li>
<li><b>A escada na esquerda:</b> sobe <code>Bb2→C2→F2</code>, desce <code>C2→Bb2→F2</code> —
um compasso de cada, até virar músculo.</li>
<li><b>Os versos:</b> 71 + 63 sílabas — cante com o transcript do clipe (é o teste de
sincronia).</li>
<li><b>O teto:</b> <span class="nt peak">Bb5</span> no “CLOSE” — o A5 cavalgado antes é o
trampolim; não gaste tudo no “GHOST”.</li>
<li><b>O bis:</b> as zonas A/B/C — onde o ASR engole palavra, você põe melisma (a corrida
<span class="nt">A5›G5›F5›A5</span> já está no mapa).</li>
<li><b>Costure por último</b> (a lista das 7 acima) e <b>grave-se</b> tocando com o clipe. 🎹</li>
</ol>
</div>

<h2>🗺️ Guia de montagem — o clipe inteiro, de ponta a ponta</h2>
<div class="card">
<p><b>3min09 de clipe sobre 91 compassos de esqueleto.</b> A numeração é a do MIDI do original —
o corte de TV encurta a intro e pula do refrão direto ao aplauso; a estrutura relativa
frase-a-frase é idêntica. A letra entre aspas é a deixa.</p>
{guide_table_html()}
</div>

<div class="tip">
<h3>🏆 Status do projeto</h3>
<b>Toda a audição está mapeada:</b> intro, os dois versos, o refrão a meia-voz, a rampa de TV, o
refrão da banda com o teto e o bis com as zonas de ad-lib — <b>25 frases nota a nota</b>.
Transparências registradas no caminho: a transposição −1st, a meia-voz engolindo o “I wanna”, as
duas leituras do “GHO-O-OST” (as mesmas notas), a rampa do LIFT (invenção do corte de TV) e o
salto c. 44→c. 87 do bis. <b>Nada ficou pendente.</b>
</div>

<footer>Mapa conferido nota a nota com o esqueleto MIDI do original (bitmidi.com/uploads/19001,
Fá# maior, −1st = Fá), triangulado com a partitura oficial Musicnotes (“Original Published Key:
F Major”, voz Bb3–Bb5), Chordify (Bon Jovi 1992 e single 2019 do Matthias: F, Bb–F–Dm–C),
GuitarTuna/free-chords (intro Bb6–Fadd9) e o transcript oficial do clipe TVOG (18/10/2018 — a
estrutura do corte). Registros: voz C4–Bb5 · cama Bb2–F4 · teto Bb5 (o “CLOSE”).
Versão de chat e dados: <code>gera_bedofroses.py</code> — a fonte única de verdade. A gêmea meio tom acima (Fá#, o tom nativo do esqueleto): <code>mapa-musical-bed-of-roses-fasustenido.html</code>.</footer>

</div>
</body>
</html>"""
    return html


# ============================================================ VERSÃO FÁ SUSTENIDO (+1st)
# O disco e o single 2019 do Matthias moram em Fá; o esqueleto MIDI é Fá# —
# nós descemos −1st no mapa-mestre. Esta versão devolve o mapa ao tom NATIVO
# do esqueleto (meio tom acima), na grafia de Fá# maior: 6 sustenidos, e o
# único espinho é o Mi# (= Fá, enarmonia — a tecla é a mesma). Gerada por
# transposição TEXTUAL do corpo em Fá, com LISTA DE PROTEÇÃO para as citações
# de fonte (fatos históricos do disco, que NÃO transpõem) e o teclado
# REDESENHADO (a geometria não transpõe por texto: o Bb vira B — tecla
# branca! — e o gancho F#5 passa a morar numa preta).

_T_UP = {"F": "F#", "G": "G#", "A": "A#", "Bb": "B", "C": "C#", "D": "D#", "E": "E#"}
_T_DN = {v: k for k, v in _T_UP.items()}
_T_UP_AC = {"Bb6": "B6", "Fadd9": "F#add9", "Fsus2": "F#sus2", "Bb/F": "B/F#",
            "F/C": "F#/C#", "F/A": "F#/A#", "C/E": "C#/E#", "Dm": "D#m",
            "Bb": "B", "F": "F#", "C": "C#"}
_T_DN_AC = {v: k for k, v in _T_UP_AC.items()}
_ALT_FA = "Bb6|Fadd9|Fsus2|Bb/F|F/C|F/A|C/E|Dm|Bb|F|C"       # mais longos primeiro
_ALT_FAS = "B6|F#add9|F#sus2|B/F#|F#/C#|F#/A#|C#/E#|D#m|B|F#|C#"
_PROTEGE = ["F, Bb–F–Dm–C", "Bb3–Bb5", "Bb6–Fadd9", "F Major",   # citações de fonte
            "zonas A, B e C", "zonas A/B/C", "zona A do detector", "zona C: o ASR",
            "ZONA DE AD-LIB A", "ZONA DE AD-LIB B", "ZONA DE AD-LIB C"]  # rótulos estruturais

# Frases com nome de nota SEM dígito (o passe de notas exige dígito; o de acordes
# só cobre F/C/Bb/B/Dm — A e G nus ficariam presos na transposição). Pares exatos:
_FRASES_UP = {"F-C-F-G-A": "F#-C#-F#-G#-A#",    # caminhada do baixo em c32
              "Bb-A-G": "B-A#-G#",              # o pêndulo do V1
              "F-G-C": "F#-G#-C#",              # o pad = Fsus2 verticalizado
              "o G fantasma": "o G# fantasma",  # a 9ª da intro
              "Bb→A": "B→A#",                   # o baixo desliza (meio tom)
              "com A no baixo": "com A# no baixo",
              "o A do F/A": "o A# do F#/A#"}


def _t_nome(n, up=True):
    """Transpõe um nome de nota simples (“Bb4” → “B4”)."""
    m = _re.match(r"^([A-G][#b]?)(\d)$", n)
    if not m:
        return n
    d = _T_UP if up else _T_DN
    return d.get(m.group(1), m.group(1)) + m.group(2)


def _transp_corpo(html, up=True):
    """Transpõe notas e acordes de um texto/HTML; SVG, citações e frases ficam protegidos."""
    marcas, restaurar = [], []

    def _guarda(achado, devolve):
        ph = f"\x00T{len(marcas)}\x00"
        marcas.append(ph)
        restaurar.append(devolve)
        return ph

    for fa, fas in sorted(_FRASES_UP.items(), key=lambda kv: -len(kv[0])):
        if up and fa in html:
            html = html.replace(fa, _guarda(fa, fas))
        elif not up and fas in html:
            html = html.replace(fas, _guarda(fas, fa))
    for p in _PROTEGE:
        if p in html:
            html = html.replace(p, _guarda(p, p))
    m = _re.search(r"<svg.*?</svg>", html, flags=_re.S)
    if m:
        html = html[:m.start()] + _guarda(m.group(0), m.group(0)) + html[m.end():]
    d_ac = _T_UP_AC if up else _T_DN_AC
    alt = _ALT_FA if up else _ALT_FAS
    # (?!\w) e não \b: token que TERMINA em "#" (F#, C#…) nunca tem \b depois do #
    html = _re.sub(r"\b(" + alt + r")(?!\w)", lambda mm: d_ac[mm.group(1)], html)
    html = html.replace("Dm2", "D#m2") if up else html.replace("D#m2", "Dm2")
    d_nt = _T_UP if up else _T_DN
    html = _re.sub(r"\b([A-G][#b]?)(\d)",
                   lambda mm: d_nt.get(mm.group(1), mm.group(1)) + mm.group(2), html)
    for ph, txt in zip(marcas, restaurar):
        html = html.replace(ph, txt)
    return html


def _copy_fsustenido(html):
    """A copy versionada da página em Fá# (âncoras no texto em Fá — roda ANTES da transposição)."""
    html = html.replace(
        "<title>Bed of Roses — Bon Jovi · versão Matthias Nebel · O Mapa Musical</title>",
        "<title>Bed of Roses — Bon Jovi · versão Matthias Nebel · O Mapa Musical em Fá#</title>")
    html = html.replace(
        "<span>tom: Fá maior (esqueleto −1st)</span>",
        "<span>tom: Fá# maior — o tom nativo do esqueleto</span>")
    html = _re.sub(
        r"🎚️ <b>Transparência da afinação:</b>.*?milímetro</i>\.",
        "🎚️ <b>Transparência da afinação:</b> esta página é a versão MEIO TOM ACIMA — Fá#, "
        "o tom nativo do esqueleto MIDI (o disco do Bon Jovi e o single 2019 do Matthias "
        "moram 1 semitom abaixo, em Fá — a gêmea é o mapa-musical-bed-of-roses.html). A "
        "grafia é Fá# maior, seis sustenidos; o único espinho é o <b>Mi#</b>, que soa "
        "exatamente como o Fá (enarmonia — a tecla é a mesma). Se ao tocar com o clipe "
        "em Fá este mapa soar 1 semitom alto, use a gêmea: <i>o desenho não muda um "
        "milímetro</i>.",
        html, flags=_re.S)
    html = html.replace(
        "e <b>o teto Bb5</b>.</p>",
        "e <b>o teto Bb5</b>. Mi# soa como Fá — mesma tecla (enarmonia); os demais "
        "sustenidos moram nas pretas.</p>")
    html = html.replace(
        "(reciclagem → o refrão já decorado do esqueleto, c. 44–49).",
        "(reciclagem → o refrão já decorado do esqueleto, c. 44–49). "
        "<b>Esta página: a versão +1st — Fá#, os pitches nativos do esqueleto.</b>")
    html = html.replace(
        "A gêmea meio tom acima (Fá#, o tom nativo do esqueleto): "
        "<code>mapa-musical-bed-of-roses-fasustenido.html</code>.</footer>",
        "Esta página é a gêmea meio tom acima: <b>Fá#</b>, os pitches nativos do "
        "esqueleto — o disco mora 1 semitom abaixo, em Fá "
        "(<code>mapa-musical-bed-of-roses.html</code>).</footer>")
    return html


def build_html(altura=0):
    """altura=0 → Fá (o mapa-mestre, o tom do disco); altura=1 → Fá# (o tom nativo do esqueleto)."""
    html = _corpo_fa()
    if altura == 0:
        return html
    corpo = _copy_fsustenido(html)
    corpo = _transp_corpo(corpo, up=True)
    svg_fa = _re.search(r"<svg.*?</svg>", html, flags=_re.S).group(0)
    return corpo.replace(svg_fa, keyboard_svg(altura=1))


# ── saídas: a pasta ../saidas desta música (a fábrica roda de qualquer lugar) ──
from pathlib import Path as _P
SAIDAS = _P(__file__).resolve().parent.parent / "saidas"
SAIDAS.mkdir(exist_ok=True)

if __name__ == "__main__":
    print("=== SANITY ===")
    sanity()
    print()
    print(chat_bor())
    with open(SAIDAS / "mapa-musical-bed-of-roses.html", "w", encoding="utf-8") as f:
        f.write(build_html())
    with open(SAIDAS / "mapa-musical-bed-of-roses-fasustenido.html", "w", encoding="utf-8") as f:
        f.write(build_html(altura=1))
    print("\n[HTML gerado: mapa-musical-bed-of-roses.html (Fá — o tom do disco)]")
    print("[HTML gerado: mapa-musical-bed-of-roses-fasustenido.html (Fá# — o tom nativo do esqueleto)]")
    print("[gera_bedofroses.py — Bed of Roses · MAPA COMPLETO + HTML ×2 🌹]")
