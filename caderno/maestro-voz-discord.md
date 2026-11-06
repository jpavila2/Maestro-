# Maestro por voz no Discord

> Objetivo do João (06/11/2026): conversar com o Maestro falando, de forma fluida, inclusive no carro, passando demandas e ouvindo o andamento.
> Escolha: modo voz do próprio Hermes num canal de voz do Discord. Sem custo por minuto.

## Por que este caminho (e o que foi descartado)
- **Escolhido: Hermes + canal de voz do Discord.** Quem atende é o Maestro de verdade (caderno, fios, agenda, e-mail). Ouvido = Whisper local; boca = Edge TTS (grátis); cérebro = ChatGPT Plus. Discord grátis. Funciona como uma ligação no celular.
- **Descartado: áudio no WhatsApp.** O João não gosta: não é conversa contínua.
- **Descartado: modo voz do ChatGPT/Claude.** No relato encontrado, o modo voz do ChatGPT não usa conectores; no Claude, voz e Remote Control são separados. Não falariam com o Maestro.
- **Descartado: GPT-Live do Hermes.** O mais fluido (escuta enquanto fala), mas US$ 0,05/min e só no app de computador.
- **Limite honesto:** conversa por turnos (1,5 s de silêncio = fim da fala). Cada resposta leva alguns segundos. Latência real ainda não medida.

## Feito em 06/11
- [x] Peça do Discord instalada no Hermes (`hermes pm install --extra discord`).
- [x] Voz grátis instalada (`hermes pm install --extra edge-tts`). Faltava; sem ela a fala falhava.
- [x] `~/.hermes/config.yaml`: `tts.provider: edge`, voz `pt-BR-AntonioNeural`; `voice.stop_phrases`: "stop", "para", "pode parar", "tchau maestro". Cópia anterior: `config.yaml.bak-antes-voz-discord-2026-11-06`.
- [x] Gateway reiniciado; WhatsApp reconectou. Teste de fala pelo Hermes: áudio gerado em 1,4 s.
- Atenção: o `hermes -z` passa pelo gateway em execução. Depois de instalar peça nova, reiniciar o gateway.

## Falta (parte do João, porque envolve chave)
1. Abrir https://discord.com/developers/applications → **New Application** → nome "Maestro".
2. Menu **Bot** → **Reset Token** → copiar. **Não colar no chat.** Guardar para o passo 6.
3. Ainda em **Bot** → *Privileged Gateway Intents* → ligar **Message Content Intent** (obrigatório). Presence e Server Members podem ficar ligados também.
4. No app do Discord, criar um servidor só seu (ex.: "Maestro"), com um canal de texto e um de voz.
5. Configurações do Discord → Avançado → **Modo desenvolvedor** ligado → tocar no seu perfil → **Copiar ID do usuário**.
6. No terminal do Mac: `hermes gateway setup` → escolher Discord → colar o token (o assistente confere o token e mostra o link de convite) → aceitar liberar o seu usuário.
7. Abrir o link de convite e escolher o servidor "Maestro". Se pedir permissões, usar as de texto + voz (inteiro `309240908864`: Connect + Speak).
8. Reiniciar: `launchctl kickstart -k gui/$(id -u)/ai.hermes.gateway`.
9. Teste: entrar no canal de voz pelo celular e, no canal de texto, digitar `/voice join`. Falar. Encerrar com "tchau maestro" ou `/voice leave`.

## Depois do teste
- Medir o tempo de resposta e ajustar (modelo rápido para voz em `auxiliary.voice_chat`, respostas curtas no SOUL quando for voz).
- Mac no carro: tampa aberta (decisão do João); internet pelo hotspot.
- Programar (ex.: SDR) por voz é etapa seguinte: hoje o Maestro não mexe em código. Definir cerca antes (branch `claude/`, testes ok; push/merge/deploy/mensagem a terceiros só com o João).
