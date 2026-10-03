# 🎹 Mapas Musicais — workspace

---

## 🗂️ ESTRUTURA DO WORKSPACE (reorganizada em 03/10/2026)

```
mapas-musicais/
├── LEIA-ME.md .................... este índice (o mapa do mapa)
├── README.md ..................... capa do repositório GitHub
├── .gitignore · mapas-musicais.zip (export p/ download — gitignored)
├── ferramentas/ .................. utilitários genéricos (não pertencem a uma música só)
│   ├── midi_parse.py ............. dissect de MIDIs (pistas, notas, compassos)
│   ├── vocal_dump.py ............. dump da pista vocal
│   └── regenera-tudo.sh .......... roda as 8 fábricas e confere (de qualquer lugar)
├── 01-november-rain/
│   ├── trabalho/ ................. gera_mapa.py · gera_docx.py · novemberrain.mid
│   └── saidas/ .................. mapa-musical-november-rain.html · .docx
├── 02-patience/
│   ├── trabalho/ ................. gera_patience.py · gera_patience_docx.py · patience.mid
│   └── saidas/ .................. mapa-musical-patience.html · .docx · teclado-pat.png
├── 03-bed-of-roses/
│   ├── trabalho/ ................. gera_bedofroses.py · gera_bedofroses_docx.py · bed-of-roses.mid
│   └── saidas/ .................. mapa-musical-bed-of-roses.html · -fasustenido.html · .docx · teclado-bor.png
└── 04-dont-stop-believin/
    ├── trabalho/ ................. gera_dsb.py · gera_dsb_docx.py · dont-stop-believin.mid ·
    │                             dsb-piano-solo-referencia.mid · cifra-usuario-dsb.txt ·
    │                             dsb-cama-e-transcricao.md · imagens-referencia/ (4 prévias — beco sem saída)
    └── saidas/ .................. mapa-musical-dont-stop-believin.html · .docx · teclado-dsb.png
```

**Convenções:**
- **`trabalho/`** = a fábrica (script Python, fonte única de verdade) + as fontes (MIDIs, cifras,
  notas de trabalho). **`saidas/`** = só o que a fábrica gera (HTML, DOCX, PNG do teclado) —
  100% regenerável, nunca editar à mão.
- Cada fábrica escreve em `../saidas/` **de onde for chamada** (âncora `SAIDAS` no pé de cada
  script). Roda da raiz: `python3 04-dont-stop-believin/trabalho/gera_dsb.py`.
- Tudo de uma vez: `bash ferramentas/regenera-tudo.sh`.
- Verificação pós-mudança (03/10/2026): 8/8 fábricas ✓ · 5/5 HTMLs byte a byte idênticos aos
  anteriores · DOCXs com auto-checagem de estrutura ✓.

## 🐙 GITHUB (plano de migração e compartilhamento)

- Repositório: **`https://github.com/USUARIO/mapas-musicais` (preencher ao criar)** — inicializar
  SEM README/licença/gitignore (já temos os nossos).
- **Upload do usuário** (arquivos que o chat não aceita — MIDI, PDF etc.): subir no repo → avisar
  o caminho no chat → o agente baixa com `curl` (rede do sandbox verificada ✓ — github.com 200).
  ⚠ Para esse fluxo funcionar **sem autenticação**, o repo (ou um repo-portal separado) precisa
  ser **público**; repos privados exigem token no raw URL — e **token NUNCA se cola no chat**.
- O `.git` local sobrevive entre sessões do workspace, **menos o `.git/config`** (regra da
  plataforma). Se `git remote -v` vier vazio numa sessão nova:
  `git remote add origin <URL> && git push`.
- **Migração de contexto** (quando a janela desta conversa encher): abrir conversa nova e apontar
  o agente para o `LEIA-ME.md` — ele contém o mapa completo do projeto. O GitHub é o seguro
  extra: duplicata fora da plataforma + histórico de versões + canal de arquivos.

## 🌹 Bed of Roses — Bon Jovi · versão Matthias Nebel (The Voice of Germany 2018) — PROVA DE CONCEITO Nº 3 · COMPLETA (CHAT + HTML + DOCX)

A terceira prova do sistema — e a mais dura: **um ao vivo de TV, sem MIDI próprio**. Metodologia
adaptada e documentada: **esqueleto** = MIDI do original (`03-bed-of-roses/trabalho/bed-of-roses.mid`, bitmidi.com/uploads/19001,
format 1, 9 pistas, 60 bpm, 91 compassos, melodia vocal própria) **transposto −1 semitom (F#→F)**;
**estrutura** = transcript oficial do clipe (autoridade do corte de TV); **tom** = triangulação de 4
fontes: partitura oficial Musicnotes ("Original Published Key: F Major", voz Bb3–Bb5), Chordify no
clipe oficial do Bon Jovi (F, Bb–F–Dm–C), cifras GuitarTuna/free-chords (F, intro Bb6–Fadd9) e
Chordify no single 2019 do Matthias (F, por áudio). Cruzamento: pico do MIDI B5 −1st = Bb5 = teto
vocal da partitura ✓; intro do MIDI −1st = Bb6–Fadd9 das cifras ✓.

**Performance:** clipe oficial TVOG (18/10/2018), 3min09, 75 mi de views, 4 cadeiras, coach Michael
Patrick Kelly, **Zugabe (bis)**. Estrutura do corte: INTRO piano (rocking Bb6↔Fadd9, 12/8 lento) →
V1 (5 frases, "Sitting here wasted…") → V2 (5, "ironclad fist…") → REFRAO 1 (2 linhas, meia-voz) →
LIFT-reprise ("About all of the things…") → REFRAO 2 (4 linhas, banda, pico Bb5 no "CLOSE") →
ZUGABE (refrão decorado, rosa D5 segurada, tag grave "LAY YOU DOWN"). Sem os versos "so far away"/hotel bar/spotlight — corte de TV.

**Transparência ativa:** se ao tocar com o clipe o mapa soar um semitom acima ou abaixo, a fábrica
transpõe o mapa inteiro num comando.

**Progresso:** ✅ INTRO, ✅ V1 (71 sílabas), ✅ V2 (63, pico F5 "that I long"), ✅ REFRAO 1 (c27–29,
meia-voz: 6 F5 do gancho, "down" G4›F4→, salto de oitava, F5 suspenso→3ª, linha 2 em terças
E5-D5-C5, monólito C5 "nails"), ✅ LIFT (a rampa do corte de TV = reprise dos mapas V2·3/V2·4) e
✅ REFRAO 2 (4 linhas: 1-2 reaproveitam o mapa da meia-voz; 3-4 novas, com o TETO DO MAPA Bb5 no
"CLOSE" — 2ª correção da fábrica: não era no "GHOST"; "down" invertido: plana em F5→; linha 4
fecha o arco F↔Bb) e ✅ ZUGABE (o bis: o refrão 2 do original c44–49 JÁ vem decorado — gancho de
8 F5, corrida A5›G5›F5›A5 no "HO" = a zona de ad-lib que o ASR ouve como "just as cold as this";
final c87–91: última declaração sobre o balanço F↔Bb, ROSA D5 (a terça do Bb) segurada ~1 compasso,
tag grave "LAY YOU DOWN" afundando Bb4-A4-G4-G4-F4→) — 25 frases nas 7 seções.
`python3 03-bed-of-roses/trabalho/gera_bedofroses.py` reconfere, reimprime e regenera os DOIS HTMLs.
✅ DOCX entregue: `03-bed-of-roses/trabalho/gera_bedofroses_docx.py` + **`03-bed-of-roses/saidas/mapa-musical-bed-of-roses.docx`** — a versão de
ATRIL (A4, editável, estilo November Rain, identidade veludo-vermelho em papel): 25 frases em
**grade de tempos do 12/8** (linhas Acorde/Tempo/Sílaba/Nota; tempos grandes com células mescladas
e até 3 tercinas lado a lado; coluna "e" = anacruze), picos em vermelho (28), notas rosas (291),
teclado-guia PIL com o gancho F5 / a rosa D5 / o teto Bb5 apontados (soletração em Fá via geo),
cama (8 acordes), 7 costuras, como estudar, guia das 7 seções, Anotações pautadas · `python3
03-bed-of-roses/trabalho/gera_bedofroses_docx.py` regenera · validação 18/18 · fonte única `03-bed-of-roses/trabalho/gera_bedofroses.py` via
import · em Fá; a gêmea Fá# continua só em HTML (a fábrica transpõe num comando se pedir).
✅ HTML entregue: `03-bed-of-roses/saidas/mapa-musical-bed-of-roses.html` (veludo vermelho 🌹 · CSS inline, sem recursos
externos · células por tempo grande com as 3 tercinas · teclado guia com o gancho F5 / a rosa D5 /
o teto Bb5 apontados · zonas de ad-lib A/B/C em dourado · mão esquerda, costuras, guia de montagem)
— o mapa-mestre, **em Fá (o tom do disco)**.
✅ A GÊMEA +1st: `03-bed-of-roses/saidas/mapa-musical-bed-of-roses-fasustenido.html` — o mesmo mapa devolvido ao **tom
nativo do esqueleto (Fá# maior, 6 sustenidos, Mi# = Fá por enarmonia)**, com teclado redesenhado
(teto B5 em tecla branca, gancho F#5 e rosa D#5 nas pretas, Mi#5 rotulado na tecla branca de Fá) e
as citações de fonte preservadas em Fá (Musicnotes/Chordify/GuitarTuna — fatos do disco não
transpõem). Gerada por transposição textual dos mesmos dados: **Fá continua sendo a fonte única de
verdade**; round-trip Fá→Fá#→Fá validado caractere a caractere, rótulos estruturais (zonas A/B/C)
e frases com nota sem dígito protegidos por lista. Correção de dados nesta rodada (MIDI como
árbitro): V1·4 "me" = **Bb4** (era B4 — sobra da grafia nativa; a voz canta C#5–B4–A#4 no esqueleto
= C5–Bb4–A4 em Fá).

---

## 🎹 Don't Stop Believin' — Journey · versão Richard Goodall (AGT 2024, Golden Buzzer) — PROVA DE CONCEITO Nº 4 · MAPA COMPLETO (CHAT + HTML)

A quarta prova — e a mais pessoal: o usuário já toca a música de ouvido em **Mi maior** (o tom do
disco) e quer um documento para reproduzi-la depois de um tempo sem tocar. Performance-âncora: a
audição de Richard Goodall (faxineiro de Terre Haute, AGT S19, 28/05/2024, Golden Buzzer da Heidi
Klum — venceu a temporada e cantou com o próprio Journey na final): a tese "é uma cópia do
original" vira hipótese a verificar. Original: **Mi maior, 118 bpm, voz E4–C#5** (Wikipedia +
Musicnotes MN0100427, partitura oficial publicada em Mi).

- **Esqueleto**: `04-dont-stop-believin/trabalho/dont-stop-believin.mid` (bitmidi.com/uploads/63595) — a banda do disco: 17 pistas
  nomeadas (piano do riff, baixo caminhante, guitarra abafada, bateria completa, orchestra hit,
  pads, choir), 118 bpm, 129 compassos — porém em **Dó# maior com enarmonias selvagens (F=E#,
  C=B#)**: a fábrica transpõe **+3 semitons ao importar**; o mapa nasce em Mi. **SEM pista de voz**
  — a linha vocal será transcrição auditiva arbitra-la pela harmonia do esqueleto (máquina), pela
  extensão oficial E4–C#5 e pela partitura oficial (preview), com o ouvido do usuário como juiz final.
- **Cifra do usuário**: `04-dont-stop-believin/trabalho/cifra-usuario-dsb.txt` — estrutura completa em Mi colada pelo usuário
  (ponto de partida pessoal); o mapa auditará onde ela já está certa e onde faltam os "ajustes".
- **Referência secundária**: `04-dont-stop-believin/trabalho/dsb-piano-solo-referencia.mid` (bitmidi 14642, "played by Bob Mace") —
  arranho livre de piano solo em Sol maior, 83 compassos, condensado.
- **Descartados na caçada** (18 arquivos testados): bitmidi 40610 (mal etiquetado — nem é DSB:
  vamp Lá/Si), 63597 (medley ao vivo de Journey, 13min27, 3 músicas), 97361 (versão country
  banjo/steel-guitar), 3764 (fragmento de 25s) + 12 candidatos sem voz/sem relação (EDM etc.);
  scorely.org (morto), freemidi/midiworld (sem DSB utilizável).
- **✅ ENTREGUE**: `04-dont-stop-believin/saidas/mapa-musical-dont-stop-believin.html` (visual streetlights 🌃 · CSS inline,
  sem recursos externos · teclado-guia SVG com o riff B3·E4·G#4·B4+C#5, o pico C#5 do "be-LIEV",
  a rampa B4, o fundão B3 e o E5-do-solo apontados · 17 grades de frase sílaba↔nota · camada
  Goodall com a timeline da audição e o buzzer · mão esquerda do trem · 6 costuras · guia de
  montagem em 8 passos · transparência da fábrica · validação 16/16). `python3 04-dont-stop-believin/trabalho/gera_dsb.py`
  reconfere, reimprime o chat e regenera o HTML.
- **✅ ENTREGUE (impressão)**: `04-dont-stop-believin/saidas/mapa-musical-dont-stop-believin.docx` (A4, editável, estilo
  November Rain: uma tabela por frase — Acorde/Sílaba/Nota —, seções navegáveis no painel do
  Word, pico C#5 em vermelho e fundão B3 em azul, cortes do TV riscados, teclado-guia embutido,
  guia das 12 seções, costuras, ordem de estudar em 8 passos e página de Anotações com linhas
  pautadas · fonte única `04-dont-stop-believin/trabalho/gera_dsb.py` via import · `python3 04-dont-stop-believin/trabalho/gera_dsb_docx.py` regenera ·
  validação 17/17).
- **Metodologia da voz** (a novidade da PoC 4): sem pista vocal no esqueleto — transcrição
  auditiva validada pelo ouvido do usuário (5/5 perguntas) dentro das cercas do Hooktheory
  (verso B3–B4, strangers E4–B4, refrão E4–C#5, 100% diatônica, 69% notas de acorde). Decisões
  validadas: verso baixo/contido ("commuter" — Goodall é barítono), cauda "anywhere" rachando
  C#4→B3, strangers B4-centrada (a rampa), pico C#5 no "be-LIEV", riff candidato A (voicings
  corroboradas pelo esqueleto: E B3-E4-G#4 / B B3-D#4-F#4 / C#m G#3-C#4-E4 / G#m G#3-B3-D#4 /
  A A3-C#4-E4). Micro-checagens 🟡 restantes: B4 fugaz no "TRAIN", caudas "on and on".
- **A cópia é real**: Chordify ×2 na audição = Mi maior, ~120 bpm, A·E·B·G#m — mesmo tom,
  mesmo tempo, mesmo loop do disco de 1981. Goodall (barítono na parte do tenor) venceu a S19
  e cantou a música na final com o próprio Journey.

---

Aplicando ao Patience a mesma metodologia do November Rain: MIDI como autoridade, entrega por
seção em chat, gerador Python como fonte única de verdade. Tom: **Dó maior** (transparência: a
cifa UG diz "meio tom abaixo" — se soar diferente do disco, transpõe-se o mapa inteiro).
**60 frases em 9 seções — tudo entregue no chat. HTML ✅ e DOCX ✅ (atril).**

| Seção | Compassos | No `02-patience/trabalho/gera_patience.py` | Status |
|---|---|---|---|
| 🎵 INTRO — o assobio | c. 2–25 | `INTRO` | ✅ entregue |
| 🎤 VERSO 1 — "Shed a tear…" | c. 26–41 | `VERSO_1` | ✅ entregue |
| REFRAO 1 — "Said, woman…" | c. 42–57 | `REFRAO_1` | ✅ entregue |
| ECO — falsete G5–A5 (toca 2×) | c. 57–63 e 95–101 | `ECO` | ✅ entregue |
| VERSO 2 (= mapa do V1) | c. 64–79 | `VERSO_1` | ✅ confirmado no MIDI (nota por nota) |
| REFRAO 2 — a variação + "We won't fake it" | c. 80–101 | `REFRAO_2` | ✅ entregue |
| 🎸 SOLO — a guitarra canta o refrão (teto F#6) | c. 102–121 | `SOLO` | ✅ entregue |
| Interlúdio — a aterrissagem | c. 122–128 | `INTERLUDIO` | ✅ entregue |
| 🌉 PONTE — em Ré maior (+ Dm7, a única cor menor) | c. 129–147 | `PONTE` | ✅ entregue |
| FINAL — o adeus | c. 148–150 | `FINAL` | ✅ entregue |

Estrutura (150 compassos): intro c2–25 · V1 c26–41 · R1 c42–57 · eco c58–63 · V2 c64–79 (=V1) ·
R2 c80–101 · solo c102–121 · interlúdio c122–128 · ponte c129–147 · final c148–150. Verso 2 usa
o MESMO mapa do Verso 1, nota por nota.

- **`02-patience/trabalho/gera_patience.py`** — a "fábrica" do mapa do Patience (dados + versão de chat + HTML).
- **`02-patience/saidas/mapa-musical-patience.html`** ← **O MAPA do Patience** (60 frases em cartões, picos em
  vermelho, teclado-guia, mão esquerda, 7 costuras, guia de montagem e as transparências).
  Abre em qualquer navegador, com ou sem internet. Baixe e guarde!
- **`02-patience/trabalho/gera_patience_docx.py`** + **`02-patience/saidas/mapa-musical-patience.docx`** ← a versão de ATRIL (A4,
  editável, estilo November Rain: uma tabela por frase — Acorde/Canto-Conta/Notas —, 17 seções
  navegáveis, picos em vermelho (25), notas azuis em registro real (324), teclado-guia PIL
  embutido com os callouts G5/G4/F#6, cama, 7 costuras, como estudar, guia das 11 seções,
  Anotações pautadas · `python3 02-patience/trabalho/gera_patience_docx.py` regenera · validação 17/17 · fonte
  única `02-patience/trabalho/gera_patience.py` via import).
- **`02-patience/trabalho/patience.mid`** — a fonte (bitmidi.com/uploads/51380.mid; 6 pistas, 120 bpm, sem bateria).

```bash
cd /home/user && python3 02-patience/trabalho/gera_patience.py   # imprime o chat e recria o HTML
```

---

# 🌧️ November Rain — Mapa Musical (PROJETO COMPLETO)

**Status:** ✅ COMPLETO — todas as seções entregues, validadas e integradas · *out/2026*

## O que já está pronto (tudo!)

| Seção | Compassos | No `01-november-rain/trabalho/gera_mapa.py` |
|---|---|---|
| 🌧️ Intro A — tema do piano | c. 1–15 | `INTRO` |
| 🌩️ Intro B — banda + fanfarra | c. 16–24 | `GROOVE` |
| Verso 1 / Verso 2 / Verso 3 | c. 24–43 / 44–67 / 110–123 | `P1` / `P2` / `P3` |
| Refrão (+ variação do 2º) | c. 68–76 / 93–100 | `CH` |
| 🌉 Ponte — cama + letra | c. 77–84* | `PONTE` |
| 🎸 Solo 1 (transcrito) | c. 77–92 | `SOLO1` |
| 🎸 Solo 2 (transcrito) | c. 100–109 | `SOLO2` |
| 🎸 Solo 3 — o gigante (transcrito) | c. 122–151 | `SOLO3` |
| 🌟 Final em Ré maior | c. 150–169 | `OUT` |
| 🗺️ Guia de montagem (12 seções) | música inteira | `GUIDE` |

**Teto do mapa:** `C#6` (Solo 3, c. 143/148) — a nota mais aguda da música inteira no nosso MIDI.

## Arquivos do workspace

- **`01-november-rain/saidas/mapa-musical-november-rain.html`** ← **O MAPA** (o entregável final). Abre em qualquer navegador, com ou sem internet. Baixe e guarde!
- **`01-november-rain/saidas/mapa-musical-november-rain.docx`** ← versão **editável no Word** (97 frases = 97 tabelas independentes; seções = Heading 1 pra navegar/reorganizar; notas de pico em vermelho; teclado-guia embutido). Ideal pra criar versões compactas.
- `01-november-rain/trabalho/gera_mapa.py` — a "fábrica" do mapa: gera o HTML e imprime a versão de chat.
- `01-november-rain/trabalho/gera_docx.py` — gera o DOCX a partir de `01-november-rain/trabalho/gera_mapa.py` (importa os dados — fonte única de verdade). Requer `pip install python-docx pillow`.
- `01-november-rain/trabalho/novemberrain.mid` — a fonte (MIDI da performance, baixado do bitmidi).
- `ferramentas/midi_parse.py` — parser MIDI minimalista (usar `parse_midi`).
- `ferramentas/vocal_dump.py` — ⚠️ executa código no import; **não importar**.

## Como regenerar o mapa

```bash
cd /home/user && python3 01-november-rain/trabalho/gera_mapa.py     # recria o HTML (16 seções, tags balanceadas, 50 teclas)
pip install python-docx pillow            # só na 1ª vez (bibliotecas não persistem entre sessões)
python3 01-november-rain/trabalho/gera_docx.py                      # recria o DOCX (97 tabelas de frase + mão esquerda + guia)
```

Recria o HTML (validado: 16 seções `<h2>`, tags balanceadas, 50 teclas no teclado-guia, 21 linhas de tabela) e imprime a versão de chat no terminal.

## O que NÃO existe (e por quê)

- **Linha cantada da ponte** ("I know it's hard…"): o MIDI fica mudo nessa seção (a pista vocal não canta lá) e não há transcrição confiável. Por decisão do projeto, **não se inventa nota** — o mapa traz a cama de acordes + a letra, conferidas em 4 fontes independentes.

## Nota sobre os erros de sessão

No fim do projeto o usuário reportou vários erros "Something went wrong" do lado dele. Auditorias repetidas confirmaram: **nenhum dano** — o mapa sempre regenerou idêntico e completo. Se esta conversa der erro, ignore: o workspace é a fonte da verdade, e ele está inteiro.
