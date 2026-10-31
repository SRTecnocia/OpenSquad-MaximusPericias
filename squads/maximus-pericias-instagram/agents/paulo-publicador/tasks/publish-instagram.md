---
task: "Publicar Campanha Aprovada no Instagram (@maximus.pericias)"
order: 1
input: |
  - visual_assets_manifest: Manifesto de imagens PNG aprovadas em squads/maximus-pericias-instagram/output/visual-assets-manifest.md
  - feed_carousel: Legenda final e estrutura do carrossel em squads/maximus-pericias-instagram/output/feed-carousel.md
  - reels_script: Roteiro técnico e legenda do Reels em squads/maximus-pericias-instagram/output/reels-script.md
  - stories_sequence: Sequência de Stories e coordenadas de stickers em squads/maximus-pericias-instagram/output/stories-sequence.md
  - review_report: Parecer de aprovação da Vera Veredito em squads/maximus-pericias-instagram/output/review-report.md
output: |
  - publication_receipt: Recibo auditável de publicação com permalink e manifesto final em squads/maximus-pericias-instagram/output/publication-receipt.md
---

# Publicar Campanha Aprovada no Instagram (@maximus.pericias)

Processo seguro de publicação no perfil oficial `https://www.instagram.com/maximus.pericias/` dos assets visuais renderizados em `squads/maximus-pericias-instagram/output/assets/` e das legendas aprovadas, respeitando o protocolo estrito de segurança de credenciais do `.env`.

## Process

1. **Verificação de Pré-Condições e Segurança de Ambiente:**
   - Confirmar que `squads/maximus-pericias-instagram/output/review-report.md` contém o status `APROVADO PARA PUBLICAÇÃO` e que o usuário autorizou o disparo no Checkpoint do Passo 11.
   - Verificar a existência física e integridade (> 0 bytes) de todos os arquivos PNG em `squads/maximus-pericias-instagram/output/assets/` (`feed-slide-01.png` a `feed-slide-XX.png`, `reels-cover.png`, `story-01.png` a `story-XX.png`).
   - Verificar silenciosamente via script Node.js (sem imprimir valores no console) quais credenciais estão configuradas no arquivo `.env` da raiz (`IMGBB_API_KEY`, `INSTAGRAM_ACCESS_TOKEN`, `INSTAGRAM_USER_ID`, `USER_INSTAGRAM`, `PASSWORD_INSTAGRAM`).

2. **Execução do Fluxo de Publicação do Carrossel de Feed:**
   - **Modo A - Instagram Graph API (`skills/instagram-publisher/SKILL.md`):** Se `IMGBB_API_KEY`, `INSTAGRAM_ACCESS_TOKEN` e `INSTAGRAM_USER_ID` estiverem definidos no `.env`, realizar o upload sequencial dos slides `feed-slide-01.png` a `feed-slide-XX.png` para o imgBB, criar os containers de item (`is_carousel_item: true`), criar o container pai (`media_type: CAROUSEL`) com a legenda aprovada de `feed-carousel.md`, aguardar `status_code: FINISHED`, publicar via `media_publish` e consultar o `permalink` oficial.
   - **Modo B - Sessão Autenticada Playwright (`_opensquad/_browser_profile/`):** Caso as chaves da Graph API não estejam presentes e o `.env` contenha `USER_INSTAGRAM` e `PASSWORD_INSTAGRAM`, utilizar um script Playwright seguro que carrega o `.env` via `dotenv` em memória, reutiliza a sessão persistente em `_opensquad/_browser_profile/`, autentica em `https://www.instagram.com/` (se necessário, sem expor credenciais no output), aciona o fluxo de criação de postagem (`Novo post`), seleciona os arquivos `feed-slide-01.png` a `feed-slide-XX.png` na proporção original (`4:5`), insere a legenda aprovada e finaliza o compartilhamento, capturando a URL pública gerada.
   - Se o Instagram solicitar verificação 2FA ou confirmação no dispositivo durante o login, pausar imediatamente e informar o usuário para concluir a verificação antes de prosseguir.

3. **Consolidação dos Pacotes de Reels e Stories e Emissão do Recibo:**
   - Organizar os arquivos finais de Stories (`story-01.png` a `story-XX.png`) e Capa/Key-frames de Reels (`reels-cover.png`) juntamente com o guia rápido de stickers interativos (Enquete, Caixa de Perguntas e Sticker de Link apontando para `https://pericias.btech.inf.br`).
   - Salvar o recibo completo em `squads/maximus-pericias-instagram/output/publication-receipt.md` com o permalink real do post, data/hora, lista de arquivos publicados e registro de conformidade de segurança (`Credenciais do .env protegidas: PASS`).

## Output Format

```markdown
# Recibo Oficial de Publicação - @maximus.pericias

## 1. Status da Operação
- **Conta Destino:** https://www.instagram.com/maximus.pericias/
- **Data/Hora de Execução:** [YYYY-MM-DD HH:MM:SS BRT]
- **Método de Publicação Utilizado:** [Instagram Graph API | Playwright Sessão Autenticada | Pacote Pronto de Publicação]
- **Auditoria de Segurança (.env):** [PASS - Zero credenciais expostas]

## 2. Carrossel de Feed Publicado (1080x1440)
- **Status:** [PUBLICADO | AGUARDANDO 2FA]
- **Permalink Oficial:** [URL pública da postagem]
- **Slides Enviados em Ordem:** `feed-slide-01.png` a `feed-slide-XX.png`

## 3. Guia de Ativação de Stories e Reels (1080x1920)
| Formato | Arquivos Prontos em `output/assets/` | Sticker / Link / Áudio |
| :--- | :--- | :--- |
| Stories (Sequência) | `story-01.png` a `story-XX.png` | Sticker de Link: `https://pericias.btech.inf.br` |
| Reels (Vídeo + Capa) | `reels-cover.png` | Legenda em `output/reels-script.md` |
```

## Output Example

```markdown
# Recibo Oficial de Publicação - @maximus.pericias

## 1. Status da Operação
- **Conta Destino:** https://www.instagram.com/maximus.pericias/
- **Data/Hora de Execução:** 2026-10-29 16:30:00 BRT
- **Método de Publicação Utilizado:** Playwright Sessão Autenticada (`_opensquad/_browser_profile/`)
- **Auditoria de Segurança (.env):** PASS - Variáveis lidas exclusivamente em memória (`***REDACTED***`)

## 2. Carrossel de Feed Publicado (1080x1440)
- **Status:** PUBLICADO COM SUCESSO
- **Permalink Oficial:** https://www.instagram.com/p/DB9xYz123Ab/
- **Slides Enviados em Ordem:** `feed-slide-01.png`, `feed-slide-02.png`, `feed-slide-03.png`, `feed-slide-04.png`, `feed-slide-05.png`, `feed-slide-06.png`, `feed-slide-07.png`, `feed-slide-08.png`

## 3. Guia de Ativação de Stories e Reels (1080x1920)
| Formato | Arquivos Prontos em `output/assets/` | Sticker / Link / Áudio |
| :--- | :--- | :--- |
| Stories (6 Cards) | `story-01.png` a `story-06.png` | Story 01: Enquete Nativa; Story 05: Sticker de Link `https://pericias.btech.inf.br` |
| Reels (Capa + Roteiro) | `reels-cover.png` | Roteiro sincronizado com frames `vid1_frame_50.jpg` e `vid1_frame_95.jpg` |
```

## Quality Criteria

- **Mascaramento Total de Credenciais:** Nenhum comando ou saída pode exibir valores de senhas ou tokens do arquivo `.env`.
- **Verificação Real de Permalink:** Sempre validar que a URL retornada responde com a publicação ativa ou documentar com exatidão qualquer bloqueio de 2FA da plataforma.

## Veto Conditions

Abortar imediatamente a execução da tarefa se:
1. Qualquer script tentar imprimir ou salvar em disco o conteúdo das variáveis `PASSWORD_INSTAGRAM`, `INSTAGRAM_ACCESS_TOKEN` ou `IMGBB_API_KEY`.
2. O relatório `review-report.md` da Vera Veredito não estiver com status `APROVADO PARA PUBLICAÇÃO`.
3. Os arquivos de imagem em `squads/maximus-pericias-instagram/output/assets/` estiverem ausentes ou fora da ordem numérica.
