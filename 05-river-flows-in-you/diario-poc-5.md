# 🌊 Diário da PoC 5 — River Flows in You (Yiruma)

**Registro de decisões e aprendizados · 12/10/2026**
Arquivado a pedido do usuário, como "memória das decisões, não só do código".
Contexto: primeiro mapa da casa pra ALUNO (filho do usuário — iniciante, não lê
partitura, objetivo = versão integral, ~30 min/dia). Fonte inédita na série:
partitura MuseScore 4.40 (.mscz) subida via `upload/`, em vez de MIDI.

---

## Temos um produto?

Na engenharia, a diferença entre protótipo e produto não é beleza, é **determinismo
e manutenção**. Por esse critério: 5 músicas, 10 fábricas, build único
(`ferramentas/regenera-tudo.sh`), teste de regressão (19 arquivos não-DOCX byte a
byte idênticos; DOCXs com auto-checagem de estrutura), sincronização GitHub que
se auto-repara, tudo versionado. Isso é produto no sentido de *pipeline*.

O que ainda falta é produto no sentido de *usuário*: **o dedilhado é hipótese até
a mão do aluno tocar**. A seção Anotações do atril é o primeiro teste de
aceitação da casa — a Fase 0 do aluno é o nosso beta. O produto fecha o círculo
no dia em que as linhas em branco voltarem preenchidas e a fábrica absorver.

## .mscz vs .midi — a mudança de epistemologia

Não foi uma troca de formato, foi uma **inversão do pipeline**:

- **MIDI é o registro de um efeito**: diz *quando* cada nota soou, em ticks. Nas
  PoCs 1–4 o trabalho era arqueologia — performance → tentar recuperar a intenção.
- **.mscz é a declaração da intenção**: diz *o que foi meant*. Aqui, a direção
  inverteu — intenção → **derivar** as performances. Os 9 MIDIs de estudo são
  efeitos computados da causa.

O poder disso apareceu nos detalhes: no MIDI, uma notinha curta antes de outra é
ambígua (grace? staccato? erro de quantização?). No .mscz, o `<acciaccatura/>`
está **escrito** — a verdade semântica veio de graça.

O preço: o formato é **vivo e versionado**. MS 4.40 com seus `concertKey`/
`concertClefType`, o texto de tempo aninhando `<sym>` (o `findtext` voltava vazio
— foi preciso cavar no XML bruto pra achar o "♩ = 78"). O MIDI é chato e estável;
o MuseScore é rico e mudável. Escolhemos o rico — e registramos as armadilhas
no LEIA-ME, porque a próxima partitura cobra o pedágio de novo.

## As duas claves — o problema não era ler, era pensar em 2D

Ler 2 staves é trivial. A dificuldade real foi conceitual: nas PoCs 1–4 o mapa
era uma **linha** (sílaba↔nota, voz→nota). Aqui cada compasso é um **objeto
bidimensional** — MD e ME simultâneos, cada qual com sua lógica. E a partitura
diz *o que toca*, mas não diz *os papéis*: em lugar nenhum está escrito que a
esquerda é "o rio", que o A4 é "o pedal onde o polegar mora", que a cascata E6
é "o teto". Isso virou **camada de interpretação** — maior que a camada de
transcrição. Pela primeira vez a fábrica não descreve música: ela ensina.

O problema intelectual mais duro foi a **inferência das células do rio**. Regras
por baixo falham (m13: F#2→D3 **sobe**), por primeira nota falham. Solução:
subir de abstração — conjuntos de classes de altura contra o canônico de cada
acorde, com desempate pela fundamental no baixo. O desempate só apareceu
*depois* do erro: m47, m2 e m4 (um E sozinho) rotulados como D, porque o
pitch-class de E pertence aos dois conjuntos. Bugs harmônicos são os mais
bonitos: o código estava "certo" e a música, errada.

## As dificuldades, do ponto de vista da fábrica

1. **O mistério dos 12 compassos** (a melhor parte do projeto). Durações que não
   somavam 4.0. Duas hipóteses: partitura errada ou modelo errado. Confiando
   que uma peça publicada em 4/4 não quebra compasso, o modelo é que estava
   incompleto — e estava: 19 notas de graça com tempo métrico **zero** + 1 gap
   de `<location>` de 1/16 (m19). Lição que vale o projeto inteiro: **quando o
   dado discorda da realidade, quem está incompleto é o modelo**. E a auditoria
   não foi perfeccionismo — era estrutural: sem os 4.0 exatóticos, as duas
   timelines do MIDI dessincronizam silenciosamente, compasso a compasso.
2. **E6 = MIDI 88, não 76** (76 é E5). Aritmética de oitava é armadilha. O mais
   revelador foi o impulso quando o sanity acusou: achei que *o dado* estava
   errado. Estava errada a *expectativa*. O check funcionou exatamente como
   projetado — pegou um bug, só não onde se supunha que ele morava.
3. **Validar música que não se ouve.** A fábrica não escuta os MIDIs nem vê o
   HTML renderizado. Toda validação foi matemática: round-trip pelo parser de
   MIDI da casa (556+298 notas, 47.00 compassos de timeline, tempos exatos),
   contagem de tags, md5s. O ouvido desta operação é o aluno — a estrutura
   existe pra que o ouvido dele seja o juiz final com o menor risco possível.
4. **`edit_file` sem `path` — quatro vezes.** O equivalente a sair de casa sem
   chave, repetidamente. Chegou ao ponto de a memória da sessão carregar um
   post-it "SEMPRE incluir path" — o equivalente de lembrete na geladeira.
   Debugar o próprio processo de trabalho também é engenharia.
5. **O metabolismo do workspace.** Permissões de SSH, `.git/config`, identidade
   de commit — tudo decai entre sessões (nesta rodada, o commit falhou por
   isso). Resposta: ensinar os scripts a se auto-repararem (o `sincroniza.sh`
   agora repõe a identidade junto com o remote). Workspace vivo precisa de
   sistema imunológico.
6. **Regex no XML bruto: 0 compassos.** Blocos repetidos de layout enganam
   expressão regular. ElementTree, sempre. (Segunda vez que essa lição cobra
   juros.)

## Avaliação geral

**O que funcionou muito bem:** disciplina da fonte única (854 notas, nenhuma
digitada à mão); sanity como contrato (13 checks que pegaram 2 bugs reais); o
`mscx_parse` virou patrimônio da casa — a próxima partitura já tem porta de
entrada; convenções consistentes (dourado = mão esquerda, do DSB ao River).

**O que faria diferente:** escrever grace+gap no parser *antes* da primeira
auditoria teria economizado um ciclo. Mas, honestamente, o mistério rendeu mais
entendimento do que a solução direta teria rendido. Às vezes o caminho errado é
o professor.

**Dívidas declaradas:** fragilidade aos caprichos de versão do MuseScore; o
"crush" das graças nos MIDIs é simplificação (declarada); toda a camada
pedagógica é hipótese até a primeira semana de prática.

---

*Entregas: `05-river-flows-in-you/saidas/` (HTML + DOCX + 9 MIDIs + PNG).
Regenera: `python3 05-river-flows-in-you/trabalho/gera_river.py` (e o
`_docx`). Fábricas: `gera_river.py` + `gera_river_docx.py`. Plano pedagógico
completo: seção PoC 5 do `LEIA-ME.md`.*
