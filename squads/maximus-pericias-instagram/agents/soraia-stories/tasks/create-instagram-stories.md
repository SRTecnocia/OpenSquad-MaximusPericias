---
task: "Criar Sequência de 4 a 6 Instagram Stories (9:16) com Interação e Conversão"
order: 1
input: |
  - reels_script: Roteiro de Reel em output/reels-script.md
  - feed_post: Carrossel de Feed em output/feed-post.md
  - product_intelligence: Dossiê técnico e quadros em output/product-intelligence.md
output: |
  - stories_sequence: Sequência estruturada de 4 a 6 lâminas de Stories (1080x1920) com enquete/quiz e Link Sticker em output/stories-sequence.md
---

# Criar Sequência de 4 a 6 Instagram Stories (9:16) com Interação e Conversão

Esta tarefa desenvolve a sequência completa de 4 a 6 lâminas verticais (`1080x1920px`) para os Stories do `@maximus.pericias`, desenhada para ser renderizada em alta definição por Davi Designer e publicada para retenção e conversão imediata.

## Process

1. **Desenhar o Arco de 5 Quadros Rápidos (3 a 5 segundos por lâmina):**
   - `FRAME 1 (Opener)`: Pergunta ou choque numérico sobre o tema da campanha em 2 linhas grandes.
   - `FRAME 2 (Context & Dor)`: Contraste visual entre o improviso manual e o rigor pericial.
   - `FRAME 3 (Interactive Poll / Quiz)`: Enquete binária ou Quiz técnico sobre a dor operacional.
   - `FRAME 4 (UI Proof)`: Demonstração do quadro real do software (`vid1_frame_XX.jpg` ou `vid2_frame_YY.jpg`) resolvendo o problema.
   - `FRAME 5 (Closer / CTA)`: Chamada direta com Link Sticker para `https://pericias.btech.inf.br` e gatilho de palavra-chave na DM.
2. **Mapear o Modelo Visual Vertical (A, B ou C em `1080x1920`) para Cada Lâmina:** Indicar cores, badge superior, texto principal, texto secundário e arquivo de imagem para que Davi Designer gere `story-01.html` a `story-05.html`.
3. **Validar Limites de Leitura e Zona Segura:** Garantir que todas as lâminas tenham no máximo 2 a 3 linhas de texto principal e respeitem o recuo de segurança superior e inferior do Instagram Stories.

## Output Format

```markdown
# Sequência de Instagram Stories (1080x1920)

=== STORY SEQUENCE ===

FRAME 1 (Opener):
[Template Vertical]: Modelo A | Modelo B | Modelo C (1080x1920)
[Visual / UI Frame]: ...
[Badge]: ...
[Text Overlay]: ...
[Supporting Line]: ...
[Sticker/Element]: ...

(Repetir até FRAME 5)

=== SEQUENCE NOTES ===
Total frames: 5
Estimated view time: 20 seconds total
Primary goal: Engagement + Traffic to https://pericias.btech.inf.br
```

## Output Example

> Use como referência de ritmo rápido, clareza e poder de conversão.

```markdown
# Sequência de Instagram Stories (1080x1920)

=== STORY SEQUENCE ===

FRAME 1 (Opener):
[Template Vertical]: Modelo A Dark Royal (1080x1920)
[Visual / UI Frame]: `references/video-frames/vid1_frame_50.jpg` (Calculadora de Retenção Tributária de Alvarás)
[Badge]: AUDITORIA DE HONORÁRIOS
[Text Overlay]: R$ 50.000,00 arbitrados pelo juiz. Quanto cai líquido no seu alvará?
[Supporting Line]: Se você respondeu de cabeça ou olhou uma planilha simples, cuidado com o teto do INSS.
[Sticker/Element]: Nenhum

FRAME 2 (Context):
[Template Vertical]: Modelo B Clean Light #F9F9FF (1080x1920)
[Visual / UI Frame]: Nenhum (Cards de contraste tipográfico)
[Badge]: O PONTO CEGO DO ESCRITÓRIO
[Text Overlay]: Entre o arbitramento e o alvará levantado existem 4 estágios e 3 retenções fiscais.
[Supporting Line]: Sem trava automática do teto previdenciário (R$ 908,86), IRRF (7,5%) e ISSQN (2%), sua margem real fica no escuro.
[Sticker/Element]: Nenhum

FRAME 3 (Interactive):
[Template Vertical]: Modelo C Liquid Metal (1080x1920)
[Visual / UI Frame]: Nenhum (Foco central no elemento interativo)
[Badge]: DIAGNÓSTICO RÁPIDO
[Text Overlay]: Como você controla seus alvarás judiciais e prazos do CPC hoje?
[Supporting Line]: Toque na opção que reflete a realidade atual do seu gabinete pericial:
[Interactive Element]: Poll: "Planilha + PJe no braço" vs "Sistema Operacional"

FRAME 4 (UI Proof):
[Template Vertical]: Modelo A Dark Royal (1080x1920)
[Visual / UI Frame]: `references/video-frames/vid1_frame_80.jpg` (ChatPericial AI + Laudos em 10 Capítulos ABNT)
[Badge]: PROVA REAL NA TELA
[Text Overlay]: Triagem IBM Docling (-95% tempo) + Minuta ABNT em 45 minutos + Alvará auditado.
[Supporting Line]: E se a carteira lotar, delegue Ordens de Serviço na Central B2B com criptografia AES-256-GCM.
[Sticker/Element]: Nenhum

FRAME 5 (Closer/CTA):
[Template Vertical]: Modelo C Liquid Metal + Corporate Gold (1080x1920)
[Visual / UI Frame]: `references/video-frames/vid1_frame_01.jpg` (Portal Oficial Maximus Perícias)
[Badge]: ACESSO EXECUTIVO
[Text Overlay]: Pare de operar no improviso. Conheça o Primeiro Sistema Operacional para Peritos Judiciais:
[Supporting Line]: Toque no link abaixo para acessar pericias.btech.inf.br ou responda este Story com SISTEMA.
[Sticker/Element]: Link sticker com URL https://pericias.btech.inf.br ("Acessar Maximus Perícias")

=== SEQUENCE NOTES ===
Total frames: 5
Estimated view time: 20 seconds total
Primary goal: Engajamento na enquete do Quadro 3 + Tráfego qualificado para https://pericias.btech.inf.br e DMs
```

## Quality Criteria

- [ ] A sequência possui entre 4 e 6 quadros verticais (`1080x1920px`).
- [ ] Cada quadro tem texto curto (2 a 3 linhas) consumível em até 4 segundos.
- [ ] Inclui elemento interativo binário no Quadro 3 e Link Sticker contextualizado no fechamento.

## Veto Conditions

Rejeitar e refazer se QUALQUER condição abaixo ocorrer:
1. Faltar elemento interativo (Enquete ou Quiz) na sequência.
2. Qualquer quadro tiver parede de texto ou contiver traços longos (`-`).
