#!/usr/bin/env bash
# Sincroniza workspace <-> GitHub (github.com/institutocura-maker/midi2cifra).
#
#   • SEM deploy key registrada no GitHub: só PUXA (HTTPS — repo público, sem senha).
#   • COM deploy key registrada (write):   puxa E EMPURRA (SSH, roteado pela porta 443).
#
# O .git/config NÃO sobrevive entre sessões do workspace (regra da plataforma) —
# este script repõe o remote sozinho. Sempre sincronizar por ele.
# Uso (de qualquer lugar): bash ferramentas/sincroniza.sh
set -u
cd "$(dirname "$0")/.."
HTTPS_URL="https://github.com/institutocura-maker/midi2cifra.git"
SSH_URL="git@github.com:institutocura-maker/midi2cifra.git"

MODO="puxa (HTTPS, sem chave)"
URL="$HTTPS_URL"
if [ -f "$HOME/.ssh/id_ed25519" ]; then
  MSG=$(ssh -o BatchMode=yes -o ConnectTimeout=10 -T git@github.com 2>&1 || true)
  case "$MSG" in
    *"successfully authenticated"*) MODO="puxa+empurra (SSH/deploy key)"; URL="$SSH_URL" ;;
  esac
fi

git remote remove origin 2>/dev/null
git remote add origin "$URL"
if ! git fetch origin main 2>/dev/null; then
  echo "✗ GitHub inacessível (rede fora do ar?)"; exit 1
fi

LOCAL=$(git rev-parse HEAD)
REMOTO=$(git rev-parse origin/main)

if [ "$LOCAL" = "$REMOTO" ]; then
  echo "✓ workspace e GitHub em sincronia ($(git rev-parse --short HEAD)) · modo: $MODO"
elif git merge-base --is-ancestor HEAD origin/main; then
  echo "↓ GitHub tem novidades — avançando (fast-forward)…"
  git merge --ff-only origin/main && echo "✓ atualizado com o que você subiu"
elif git merge-base --is-ancestor origin/main HEAD; then
  N=$(git rev-list --count origin/main..HEAD)
  echo "↑ workspace à frente do GitHub por $N commit(s)"
  if [ "$URL" = "$SSH_URL" ]; then
    if git push origin main 2>/dev/null; then
      echo "✓ $N commit(s) ENVIADOS pro GitHub (push automático)"
    else
      echo "✗ push falhou — conferir a deploy key no GitHub (Settings → Deploy keys)"; exit 1
    fi
  else
    echo "  (modo: $MODO — o GitHub receberá via zip/push do seu lado)"
  fi
else
  echo "↕ histórios divergiram — rebase dos commits locais em cima do GitHub…"
  if git rebase origin/main; then
    echo "✓ rebase ok"
    if [ "$URL" = "$SSH_URL" ]; then
      git push origin main 2>/dev/null && echo "✓ push pós-rebase" || { echo "✗ push falhou"; exit 1; }
    fi
  else
    echo "✗ CONFLITO — resolver manualmente"; exit 1
  fi
fi
