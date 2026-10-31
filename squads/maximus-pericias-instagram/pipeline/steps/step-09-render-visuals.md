---
execution: inline
agent: davi-designer
inputFile: squads/maximus-pericias-instagram/output/approved-content.md
outputFile: squads/maximus-pericias-instagram/output/visual-assets-manifest.md
---

# Passo 09: Renderizar Imagens Finais HTML/CSS + Playwright (Sistema A + B + C)

## Context Loading

Carregue e inspecione os seguintes arquivos antes de iniciar a compilação HTML e a renderização via Playwright:
- `squads/maximus-pericias-instagram/output/feed-carousel.md` (especificação aprovada de todos os slides `1080x1440`)
- `squads/maximus-pericias-instagram/output/reels-script.md` (especificação aprovada da capa de Reels `1080x1920`)
- `squads/maximus-pericias-instagram/output/stories-sequence.md` (especificação aprovada dos 6 cards de Stories `1080x1920`)
- `squads/maximus-pericias-instagram/pipeline/data/template-reference.html` (código HTML/CSS canônico com as variações Template A Dark Royal, Template B Clean Editorial Light e Template C B2B Command Bento Grid)
- `squads/maximus-pericias-instagram/pipeline/data/visual-identity.md` (tokens de cor, tipografia `Hanken Grotesk` + `Inter` e safe zones)
- `skills/image-creator/SKILL.md` (instruções de renderização de HTML para PNG via Playwright)

## Instructions

### Process

1. **Geração dos Arquivos HTML Individuais (`output/assets/html/`):**
   - Crie o diretório `squads/maximus-pericias-instagram/output/assets/html/` caso não exista.
   - Para cada slide especificado em `feed-carousel.md`, gere um arquivo HTML autônomo (`feed-slide-01.html` até `feed-slide-XX.html`) com viewport exata `width: 1080px; height: 1440px;`, aplicando fielmente a classe/estrutura do Template A, Template B ou Template C e apontando o `src` da imagem para o frame real correspondente em `../../../../references/video-frames/` (ou caminho relativo exato verificado).
   - Gere o arquivo `reels-cover.html` em `1080x1920px` garantindo que o conteúdo central respeite a zona segura 4:5 (`Y: 240px` a `1680px`).
   - Para cada card de `stories-sequence.md`, gere `story-01.html` até `story-06.html` em `1080x1920px`, preservando `250px` livres no topo, `340px` livres na base e o container visual reservado para o sticker interativo.
2. **Renderização Pixel-Perfect via Playwright (`output/assets/`):**
   - Execute um script Node.js com Playwright que abra cada arquivo HTML gerado, aguarde o carregamento completo das fontes Google Fonts (`Hanken Grotesk` e `Inter`) e das imagens locais (`waitUntil: 'networkidle'`), e capture os screenshots em PNG sem compressão (`feed-slide-01.png` a `feed-slide-XX.png` em `1080x1440`, `reels-cover.png` em `1080x1920` e `story-01.png` a `story-06.png` em `1080x1920`).
3. **Inspeção Visual Pós-Renderização e Emissão do Manifesto:**
   - Utilize a ferramenta de leitura de imagem (`read_file`) para inspecionar os PNGs gerados e confirmar que nenhum frame ficou quebrado, nenhum texto sofreu corte (overflow) e o contraste está impecável.
   - Registre todos os caminhos gerados e o status de verificação em `squads/maximus-pericias-instagram/output/visual-assets-manifest.md`.

## Output Format

Salve o manifesto completo em `squads/maximus-pericias-instagram/output/visual-assets-manifest.md`:

```markdown
# Manifesto de Assets Visuais Renderizados - @maximus.pericias

## 1. Resumo da Renderização Playwright
- **Total de Imagens PNG Geradas:** [X arquivos]
- **Resolução Feed:** 1080x1440px (Proporção 4:5 Vertical)
- **Resolução Reels & Stories:** 1080x1920px (Proporção 9:16 Vertical)
- **Sistema Visual Aplicado:** Sistema Unificado A (Dark Royal) + B (Editorial Light) + C (B2B Bento Grid)

## 2. Inventário do Carrossel de Feed (`1080x1440`)
| Slide | Variação de Template | Frame do Software Integrado | Caminho do Arquivo PNG | Status da Inspeção Visual |
| :--- | :--- | :--- | :--- | :--- |

## 3. Inventário de Reels e Stories (`1080x1920`)
| Peça | Variação de Template | Frame do Software Integrado | Caminho do Arquivo PNG | Safe Zone Verificada |
| :--- | :--- | :--- | :--- | :--- |
```

## Output Example

```markdown
## 2. Inventário do Carrossel de Feed (`1080x1440`)
| Slide | Variação de Template | Frame do Software Integrado | Caminho do Arquivo PNG | Status da Inspeção Visual |
| :--- | :--- | :--- | :--- | :--- |
| Slide 01 | Template A (Dark Royal) | `vid1_frame_50.jpg` | `squads/maximus-pericias-instagram/output/assets/feed-slide-01.png` | PASS (1080x1440, Zero CLS) |
| Slide 02 | Template B (Editorial Light) | `vid1_frame_32.jpg` | `squads/maximus-pericias-instagram/output/assets/feed-slide-02.png` | PASS (1080x1440, Contraste AAA) |
```

## Veto Conditions

1. Rejeitar imediatamente se qualquer arquivo `.png` não for criado fisicamente em `squads/maximus-pericias-instagram/output/assets/` ou tiver dimensões diferentes de `1080x1440` (Feed) e `1080x1920` (Reels/Stories).
2. Rejeitar se qualquer imagem interna (`<img>`) do frame do software aparecer em branco ou quebrada no screenshot final.
3. Rejeitar se aparecer qualquer caractere `-` (travessão) renderizado dentro de qualquer imagem PNG.

## Quality Criteria

- **Fidelidade Visual 100% Idêntica a `pericias.btech.inf.br`:** Paleta cromática oficial (`#0047AB`, `#002366`, `#0B1329`, `#FFD700`, `#C5A021`, `#F9F9FF`, `#111318`) e tipografia `Hanken Grotesk` + `Inter`.
- **Inspeção Real dos PNGs:** Todos os PNGs gerados foram abertos e verificados visualmente antes da conclusão da etapa.
- **Zero Travessões:** Nenhum arquivo HTML ou manifesto contém o caractere `-`.
