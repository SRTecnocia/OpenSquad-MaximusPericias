---
execution: inline
agent: paulo-publicador
inputFile: squads/maximus-pericias-instagram/output/publication-approval.md
outputFile: squads/maximus-pericias-instagram/output/publication-receipt.md
---

# Passo 12: Publicar Campanha no Instagram (@maximus.pericias) e Emitir Recibo

## Context Loading

Carregue e verifique os seguintes arquivos antes de iniciar a rotina de publicação:
- `squads/maximus-pericias-instagram/output/publication-approval.md` (decisão do usuário no Checkpoint do Passo 11)
- `squads/maximus-pericias-instagram/output/visual-assets-manifest.md` (caminhos exatos dos arquivos PNG em `output/assets/`)
- `squads/maximus-pericias-instagram/output/feed-carousel.md` (legenda oficial aprovada para o Feed)
- `squads/maximus-pericias-instagram/output/reels-script.md` (roteiro e legenda oficial do Reels)
- `squads/maximus-pericias-instagram/output/stories-sequence.md` (sequência de Stories e coordenadas de stickers nativos)
- `squads/maximus-pericias-instagram/output/review-report.md` (confirmação do status `APROVADO PARA PUBLICAÇÃO`)
- `skills/instagram-publisher/SKILL.md` (protocolo de publicação de carrosséis no Instagram)

## Instructions

### Process

1. **Protocolo Estrito de Segurança de Credenciais (`.env`):**
   - Carregue as variáveis do arquivo `.env` da raiz exclusivamente em memória via Node.js (`dotenv`), verificando a presença de `IMGBB_API_KEY`, `INSTAGRAM_ACCESS_TOKEN`, `INSTAGRAM_USER_ID`, `USER_INSTAGRAM` e `PASSWORD_INSTAGRAM`.
   - **REGRA INVIOLÁVEL:** Nunca imprima, exiba no terminal ou escreva em arquivos os valores das senhas ou tokens do `.env`. Mascarar qualquer referência nos logs como `***REDACTED***`.
2. **Execução da Publicação Conforme a Escolha do Usuário no Passo 11:**
   - Se o usuário escolheu a **Opção 1 (Publicar Agora em `@maximus.pericias`)**:
     - Caso `IMGBB_API_KEY`, `INSTAGRAM_ACCESS_TOKEN` e `INSTAGRAM_USER_ID` estejam configurados, execute o fluxo completo da Graph API conforme `skills/instagram-publisher/SKILL.md` para publicar o carrossel de Feed (`feed-slide-01.png` a `feed-slide-XX.png`) com a legenda oficial e obter o `permalink`.
     - Caso o ambiente utilize `USER_INSTAGRAM` e `PASSWORD_INSTAGRAM`, execute o script Playwright autenticado utilizando o perfil persistente `_opensquad/_browser_profile/` para realizar o upload ordenado dos slides `feed-slide-01.png` a `feed-slide-XX.png` em proporção original (`4:5`), inserir a legenda oficial, compartilhar no perfil `@maximus.pericias` e capturar a URL pública da postagem. Se o Instagram solicitar código 2FA, pause e peça o código ao usuário.
   - Se o usuário escolheu a **Opção 2 (Apenas Pacote Pronto)**:
     - Consolide todos os arquivos PNG e legendas prontas para cópia em um diretório final organizado e emita o recibo de entrega.
3. **Emissão do Recibo Auditável (`publication-receipt.md`):**
   - Documente o permalink oficial da publicação no Instagram, o horário exato de execução, a lista de slides enviados, o guia rápido de ativação dos Stories/Reels e o atestado de segurança das credenciais.

## Output Format

Salve o recibo final em `squads/maximus-pericias-instagram/output/publication-receipt.md`:

```markdown
# Recibo Oficial de Publicação e Entrega - @maximus.pericias

## 1. Resumo Operacional e Segurança
- **Perfil Oficial:** https://www.instagram.com/maximus.pericias/
- **Timestamp de Execução:** [YYYY-MM-DD HH:MM:SS BRT]
- **Modo Executado:** [Publicação Automática Realizada | Pacote Pronto Entregue]
- **Proteção de Credenciais (.env):** PASS (Nenhuma credencial exposta em logs ou arquivos)

## 2. Status do Carrossel de Feed (1080x1440)
- **Status:** [PUBLICADO COM SUCESSO | PACOTE PRONTO | AGUARDANDO 2FA]
- **Permalink Oficial:** [URL da postagem ou caminho local]
- **Ordem de Slides Verificada:** `feed-slide-01.png` a `feed-slide-XX.png`

## 3. Guia de Ativação Complementar (Reels & Stories 1080x1920)
| Formato | Arquivos PNG em `output/assets/` | Ação / Sticker / Link |
| :--- | :--- | :--- |
```

## Output Example

```markdown
# Recibo Oficial de Publicação e Entrega - @maximus.pericias

## 1. Resumo Operacional e Segurança
- **Perfil Oficial:** https://www.instagram.com/maximus.pericias/
- **Timestamp de Execução:** 2026-10-29 16:45:12 BRT
- **Modo Executado:** Publicação Automática Realizada
- **Proteção de Credenciais (.env):** PASS (Nenhuma credencial exposta em logs ou arquivos)

## 2. Status do Carrossel de Feed (1080x1440)
- **Status:** PUBLICADO COM SUCESSO
- **Permalink Oficial:** https://www.instagram.com/p/DB9xYz123Ab/
- **Ordem de Slides Verificada:** `feed-slide-01.png` a `feed-slide-08.png`

## 3. Guia de Ativação Complementar (Reels & Stories 1080x1920)
| Formato | Arquivos PNG em `output/assets/` | Ação / Sticker / Link |
| :--- | :--- | :--- |
| Stories (6 Cards) | `story-01.png` a `story-06.png` | Story 01: Enquete Nativa; Story 05: Link `https://pericias.btech.inf.br` |
| Reels (Capa + Roteiro) | `reels-cover.png` | Roteiro completo disponível em `output/reels-script.md` |
```

## Veto Conditions

1. Abortar imediatamente se qualquer comando tentar exibir ou registrar em texto aberto as variáveis sensíveis do `.env`.
2. Abortar se o usuário não tiver aprovado os assets no Checkpoint do Passo 11.
3. Rejeitar se o recibo final contiver qualquer ocorrência do caractere `-` (travessão).

## Quality Criteria

- **Conformidade de Segurança (LGPD & DevSecOps):** Zero vazamento de segredos do `.env`.
- **Rastreabilidade Completa:** Registro claro dos arquivos publicados, URL pública resultante e instruções de Stories/Reels.
- **Conformidade Linguística:** Documento 100% em Português Brasileiro (`pt-BR`) sem travessões (`-`).
