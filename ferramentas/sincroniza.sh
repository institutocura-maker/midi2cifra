#!/usr/bin/env bash
# Sincroniza o workspace com o GitHub (puxa o que o usuário subiu — repo público, sem senha).
# Nota: o .git/config NÃO sobrevive entre sessões do workspace (regra da plataforma) —
# este script repõe o remote sozinho, então sempre rodar por ele.
# Uso (de qualquer lugar): bash ferramentas/sincroniza.sh
set -u
cd "$(dirname "$0")/.."
URL="https://github.com/institutocura-maker/midi2cifra.git"
git remote remove origin 2>/dev/null
git remote add origin "$URL"
if ! git fetch origin main 2>/dev/null; then
  echo "✗ não consegui falar com o GitHub (rede fora do ar?)"; exit 1
fi
LOCAL=$(git rev-parse HEAD); REMOTO=$(git rev-parse origin/main)
if [ "$LOCAL" = "$REMOTO" ]; then
  echo "✓ workspace e GitHub em sincronia ($(git rev-parse --short HEAD))"
elif git merge-base --is-ancestor HEAD origin/main; then
  echo "↓ GitHub tem novidades — avançando (fast-forward)…"
  git merge --ff-only origin/main && echo "✓ atualizado com o que você subiu"
else
  echo "↕ histórios divergiram — rebase dos commits locais em cima do GitHub…"
  git rebase origin/main && echo "✓ sincronizado (rebase)" || { echo "✗ CONFLITO — resolver manualmente"; exit 1; }
fi
