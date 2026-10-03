# 📥 upload/ — a caixa de entrada do projeto

Suba aqui qualquer arquivo que o chat não aceita (MIDI, PDF, cifras, imagens, o que for).

**Como usar:**
1. No GitHub, entre nesta pasta → **Add file → Upload files** → arraste os arquivos → **Commit changes**.
2. Avise no chat (ex.: "subi um MIDI em upload/").
3. O agente roda `bash ferramentas/sincroniza.sh`, baixa, processa e **move o arquivo pra casa dele**
   (a pasta `trabalho/` da música correspondente) — caixa de entrada sempre volta a ficar vazia,
   e nada se perde: o git guarda o histórico de tudo.

**Dica:** um nome tipo `patience-ao-vivo.mid` ou `dsb-partitura.pdf` já ajuda a despachar certo.
