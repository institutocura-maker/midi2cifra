#!/usr/bin/env bash
# Regenera TODAS as saídas (14 fábricas → 8 HTMLs + 7 DOCXs + 36 MIDIs + 6 PNGs) a partir das fábricas.
# Uso (de qualquer lugar): bash ferramentas/regenera-tudo.sh
set -u
cd "$(dirname "$0")/.."
fail=0
for f in 01-november-rain/trabalho/gera_mapa.py \
         01-november-rain/trabalho/gera_docx.py \
         02-patience/trabalho/gera_patience.py \
         02-patience/trabalho/gera_patience_docx.py \
         03-bed-of-roses/trabalho/gera_bedofroses.py \
         03-bed-of-roses/trabalho/gera_bedofroses_docx.py \
         04-dont-stop-believin/trabalho/gera_dsb.py \
         04-dont-stop-believin/trabalho/gera_dsb_docx.py \
         05-river-flows-in-you/trabalho/gera_river.py \
         05-river-flows-in-you/trabalho/gera_river_docx.py \
         06-forest-corciolli/trabalho/gera_forest.py \
         06-forest-corciolli/trabalho/gera_forest_docx.py \
         07-billie-jean-retalianist/trabalho/gera_billie_jean.py \
         07-billie-jean-retalianist/trabalho/gera_billie_jean_docx.py; do
  printf '%s ' "$f"
  if python3 "$f" > /dev/null 2>&1; then echo '✓'; else echo '✗ FALHOU (rodar manualmente p/ ver o erro)'; fail=1; fi
done
if [ $fail -eq 0 ]; then echo 'TUDO REGENERADO ✓'; else echo 'HOUVE FALHAS ✗'; fi
exit $fail
