# 🎹 Mapas Musicais

Mapas musicais **nota a nota** para reprodução ao piano — cada música com sua fábrica Python
(fonte única de verdade) que gera o mapa em HTML (tela) e DOCX (atril/impressão).

| # | Música | Versão-âncora | Tom | Entregas |
|---|---|---|---|---|
| 1 | November Rain — Guns N' Roses | disco (Use Your Illusion I) | Si maior (final em Ré) | HTML + DOCX |
| 2 | Patience — Guns N' Roses | disco (Lies) | Dó maior (ponte em Ré) | HTML + DOCX |
| 3 | Bed of Roses — Bon Jovi | Matthias Nebel, The Voice of Germany 2018 | Fá maior (+ gêmea Fá#) | HTML ×2 + DOCX |
| 4 | Don't Stop Believin' — Journey | Richard Goodall, AGT 2024 | Mi maior | HTML + DOCX |

## Estrutura

```
ferramentas/          utilitários genéricos (midi_parse, vocal_dump, regenera-tudo.sh)
NN-música/
  ├── trabalho/       fábrica (gera_*.py) + fontes (MIDIs, cifras, notas)
  └── saidas/         HTML + DOCX + PNG do teclado — 100% regenerável
```

## Regenerar tudo

```bash
bash ferramentas/regenera-tudo.sh
```

Cada fábrica confere a si mesma (sanity de notas/acordes + estrutura do DOCX) antes de escrever.

## Documentação

O índice completo — história, decisões, metodologia, transparências e status de cada prova de
conceito — está no **[LEIA-ME.md](LEIA-ME.md)**.
