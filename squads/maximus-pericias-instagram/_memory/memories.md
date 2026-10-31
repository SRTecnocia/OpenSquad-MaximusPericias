# Squad Memory: Maximus Perícias Instagram (Feed, Reels & Stories)

## Estilo de Escrita
- Seguir estritamente a filosofia de posicionamento de engenharia de produto (Steve Jobs): simplicidade extrema, foco na transformação real, contraste tangível entre o caos manual de planilhas/Word e a precisão do software Maximus Perícias.
- Idioma: Português Brasileiro (`pt-BR`) culto, técnico, executivo e sem travessões.

## Design Visual (Padrão Editorial Clean Light & Luxury Tech 2026)
- Estética 100% Clara, Luminosa e Agradável:
  - Fundo principal: Branco puro (`#FFFFFF`) e ardósia suave (`#F8FAFC`), com iluminação radial suave em azul cobalto (`rgba(37, 99, 235, 0.05)`).
  - Tipografia de alto contraste: `Hanken Grotesk 900` para títulos em grafite escuro (`#0F172A`), com destaques estratégicos em azul cobalto (`#2563EB`) e verde esmeralda (`#16A34A` para métricas e alvarás). Textos descritivos em ardósia médio (`#475569`).
  - Cards flutuantes limpos: Superfícies brancas com bordas sutis (`#E2E8F0` / `#CBD5E1`) e sombras suaves multicamadas.
  - Mockups em Janela Desktop Light: Moldura de janela macOS em cinza suave (`#F8FAFC` / `#F1F5F9`), borda `#CBD5E1`, botões circulares clássicos (vermelho `#FF5F56`, amarelo `#FFBD2E`, verde `#27C93F`) e título de janela monospace em `#64748B`.
  - Imagens de interface embutidas via Base64 para garantir carregamento instantâneo e livre de bloqueios CORS no navegador.
- Telas Reais e Contextualizadas Obrigatórias (`references/ui-mockups/`):
  - Todas as imagens de telas devem obrigatoriamente refletir dados reais, povoados e condizentes com o tema exato de cada lâmina (processos reais TJSP/TRF3, números de processo CNJ, intimações do DJEN, valores preenchidos na calculadora de alvarás, copiloto MAX AI em caso ativo, fórmulas de cálculos bancários e governança de membros).
  - Proibido usar telas genéricas de configurações (ex: "Tema & Estilo Visual") ou estados vazios com avisos de "Nenhum lançamento".
- Proibição de Temas Escuros no Feed: Manter todas as lâminas e peças de feed na identidade Clean Light de alta legibilidade.
- Proibição de Contadores de Página: Não incluir indicadores manuais de paginação como "(1/8)" ou "PASSO 1 DE 8" nos rodapés. O Instagram já possui indicadores nativos de navegação.

## Estrutura de Conteúdo
- Público-alvo: Ecossistema Completo (Peritos Proprietários/Titulares + Peritos Terceirizados/Especialistas B2B + Autoridade Institucional).
- Seleção Automática de Ângulo: Sempre escolher automaticamente o melhor ângulo estratégico utilizando critérios objetivos de retenção, engajamento (salvamentos/compartilhamentos) e relevância para o ecossistema pericial, sem pausar para perguntar qual ângulo escolher.
- Grade Principal do Instagram (`@maximus.pericias`): Manter apenas os Carrosséis de Feed (`4:5`) na grade principal do perfil; publicar Reels sempre com `show_preview_in_feed: false` para mantê-los exclusivamente na aba de Reels (`🎬`).
- Configuração do Perfil (`@maximus.pericias`): Avatar com a logo oficial em fundo azul marinho nobre (`references/logos/instagram-avatar-1080.jpg`) e biografia estruturada de alto impacto com direcionamento para `pericias.btech.inf.br`.

## Proibições Explícitas
- Proibido usar travessões (em-dash) em qualquer texto, legenda, roteiro ou slide.
- Proibido usar ícones genéricos em CSS (`[M]`, `[B2B]`) no lugar da logo oficial do Maximus Perícias.
- Proibido inventar métricas, preços ou telas fora das fontes verificadas (`https://pericias.btech.inf.br` e vídeos em `Vídeos/`).
- Proibido expor credenciais do `.env`.

## Técnico (específico do squad)
- Dimensões oficiais: `1080x1440` (4:5) para Feed Carrossel; `1080x1920` (9:16) para Reels e Stories.
- Banco de Telas Reais Focadas: `squads/maximus-pericias-instagram/references/ui-mockups/` (`focus-dashboard-processos.png`, `focus-diario-justica.png`, `focus-alvaras-tributos.png`, `focus-max-ai-laudos.png`, `focus-calculos-bancarios.png`, `focus-prazos-cpc.png`, `focus-central-b2b.png`, `focus-honorarios-pix.png`).
- Acervo de quadros em `squads/maximus-pericias-instagram/references/video-frames/`.
