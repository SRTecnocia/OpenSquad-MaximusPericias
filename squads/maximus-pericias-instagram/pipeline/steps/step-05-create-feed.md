---
execution: inline
agent: flavio-feed
format: instagram-feed
inputFile: squads/maximus-pericias-instagram/output/selected-angle.md
outputFile: squads/maximus-pericias-instagram/output/feed-carousel.md
---

# Passo 05: Criar Carrossel Estratégico de Feed (1080x1440 - 4:5)

## Context Loading

Carregue os seguintes arquivos obrigatórios antes de redigir o carrossel de Feed:
- `squads/maximus-pericias-instagram/output/selected-angle.md` (decisão do usuário sobre o ângulo vencedor no Passo 04)
- `squads/maximus-pericias-instagram/output/campaign-angles.md` (detalhamento do ângulo selecionado)
- `squads/maximus-pericias-instagram/output/product-intelligence.md` (métricas reais e catálogo de frames verificados)
- `squads/maximus-pericias-instagram/pipeline/data/visual-identity.md` (regras do Sistema Unificado A + B + C e limites tipográficos)
- `squads/maximus-pericias-instagram/pipeline/data/output-examples.md` e `pipeline/data/tone-of-voice.md` (padrões ouro de escrita e restrições de estilo)

## Instructions

### Process

1. **Arquitetura de 8 a 10 Slides em Proporção 4:5 (`1080x1440`):**
   - Estruture o carrossel seguindo o arco de retenção de alta conversão:
     - **Slide 1 (Capa Magnética - Template A Dark Royal):** Gancho de até 12 palavras + badge dourada Solar Gold (`#FFD700`) + janela de navegador com o frame principal do software.
     - **Slides 2 e 3 (Agitação da Dor e Custo Invisível - Template B Clean Editorial Light):** Demonstre matematicamente onde o perito perde tempo ou dinheiro no modelo manual.
     - **Slides 4, 5 e 6 (Engenharia da Solução Maximus Perícias - Alternância Templates A e B):** Apresente passo a passo a funcionalidade real na interface (ex: IBM Docling OCR, MAX AI Art. 473 CPC, Funil de Alvarás de 4 etapas ou Cálculos Bancários), vinculando um frame real diferente (`vid1_frame_XX.jpg` ou `vid2_frame_XX.jpg`) a cada slide.
     - **Slide 7 (Integração B2B / Segurança Multi-Tenant - Template C Command Bento Grid):** Destaque a governança entre Perito Proprietário e Perito Terceirizado, Prazos CPC ou criptografia LGPD.
     - **Slide 8 (Resumo de Impacto e CTA Institucional - Template A Dark Royal):** Quadro sintético de ganhos reais + chamada direta para acessar `pericias.btech.inf.br` no link da bio e salvar o post.
2. **Controle Rígido de Densidade Visual:**
   - Limite o texto visível dentro da arte de cada slide (soma de título, subtítulo e badges) a **no máximo 25 palavras**.
3. **Redação da Legenda Estruturada (Caption):**
   - Escreva uma legenda profunda de 180 a 260 palavras com primeira linha magnética (antes do "...mais"), desenvolvimento analítico em parágrafos curtos, referência normativa (CPC/2015 / ABNT / LGPD), CTA claro para `pericias.btech.inf.br` e 6 hashtags de nicho pericial.

## Output Format

Salve o roteiro completo e a legenda em `squads/maximus-pericias-instagram/output/feed-carousel.md`:

```markdown
# Carrossel de Feed (1080x1440) - @maximus.pericias

## 1. Metadados da Publicação
- **Ângulo Aplicado:** [Nome do Ângulo]
- **Quantidade de Slides:** [8 a 10 slides]
- **Proporção:** 1080x1440px (4:5 Vertical)

## 2. Especificação Slide a Slide (Para Renderização HTML/Playwright)
### Slide 01 - [Função Narrativa]
- **Template Visual:** [Template A | Template B | Template C]
- **Frame Real Integrado:** `references/video-frames/[arquivo.jpg]`
- **Badge Superior:** "[Texto curto]"
- **Título Principal (Hanken Grotesk 800/900):** "[Texto]"
- **Subtítulo / Callout (Inter 500/600):** "[Texto]"
- **Contagem de Palavras no Slide:** [X palavras - máx. 25]

[Repetir para todos os slides]

## 3. Legenda Oficial da Publicação (Caption)
[Texto completo da legenda com quebras de linha e hashtags]
```

## Output Example

```markdown
### Slide 01 - Capa Magnética (Contraste Financeiro)
- **Template Visual:** Template A (Dark Royal Prestige - `#0B1329` -> `#002366` + `#FFD700`)
- **Frame Real Integrado:** `references/video-frames/vid1_frame_50.jpg`
- **Badge Superior:** "ENGENHARIA FINANCEIRA PERICIAL"
- **Título Principal (Hanken Grotesk 900):** "Seu alvará de R$ 50 mil rende R$ 44.341 líquidos. Você calculou?"
- **Subtítulo / Callout (Inter 600):** "A diferença entre o valor arbitrado e o caixa real em 1 tela."
- **Contagem de Palavras no Slide:** 24 palavras
```

## Veto Conditions

1. Rejeitar imediatamente se qualquer slide exceder 25 palavras de texto visível na arte.
2. Rejeitar se algum slide de demonstração de produto não especificar um arquivo existente em `references/video-frames/` ou `references/landing-page/`.
3. Rejeitar se houver qualquer caractere `-` (travessão) nos slides ou na legenda.

## Quality Criteria

- **Sequência Visual Ritmada (Sistema A + B + C):** Uso equilibrado dos 3 templates aprovados para manter o contraste visual ao deslizar o carrossel.
- **Ancoragem em Dados Reais:** Citação exata das métricas e telas verificadas do Maximus Perícias.
- **Legenda Pronta para Produção:** Sem placeholders, 100% em Português Brasileiro (`pt-BR`) e sem travessões (`-`).
