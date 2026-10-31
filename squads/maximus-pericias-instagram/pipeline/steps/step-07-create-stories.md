---
execution: inline
agent: soraia-stories
format: instagram-stories
inputFile: squads/maximus-pericias-instagram/output/selected-angle.md
outputFile: squads/maximus-pericias-instagram/output/stories-sequence.md
---

# Passo 07: Criar Sequência Interativa de Stories (1080x1920 - 9:16)

## Context Loading

Carregue e estude os seguintes arquivos antes de criar a sequência de Stories:
- `squads/maximus-pericias-instagram/output/selected-angle.md` (ângulo aprovado pelo usuário no Passo 04)
- `squads/maximus-pericias-instagram/output/product-intelligence.md` (frames reais de `references/video-frames/` e métricas verificadas)
- `squads/maximus-pericias-instagram/output/feed-carousel.md` e `squads/maximus-pericias-instagram/output/reels-script.md` (peças irmãs da campanha para manter unidade narrativa)
- `squads/maximus-pericias-instagram/pipeline/data/visual-identity.md` (regras de safe zones para Stories 9:16: `250px` topo e `340px` base)
- `squads/maximus-pericias-instagram/pipeline/data/tone-of-voice.md` (diretrizes de comunicação direta e autoridade técnica)

## Instructions

### Process

1. **Arquitetura de Funil Interativo em 6 Cards (`1080x1920`):**
   - Desenvolva uma sequência de 6 cards de Stories estruturada para engajamento algorítmico e clique qualificado:
     - **Story 01 (Micro-Compromisso Inicial - Template A Dark Royal):** Pergunta direta sobre o gargalo operacional do perito + área demarcada para **Sticker de Enquete Nativa** (2 opções contrastantes).
     - **Story 02 (Diagnóstico Visual do Problema - Template B Clean Editorial Light):** Revelação do custo oculto do processo manual em planilhas/Word com dado factual do dossiê.
     - **Story 03 (Bastidores da Solução no Software - Template A ou B):** Demonstração da funcionalidade em tela real (`vid1_frame_XX.jpg` ou `vid2_frame_XX.jpg`) com callout em Solar Gold (`#FFD700`).
     - **Story 04 (Detalhe de Precisão / Segurança - Template C B2B Bento Grid):** Foco em um diferencial técnico decisivo (ex: retenção de IRRF/INSS/ISSQN, Prazos CPC com recesso forense ou criptografia LGPD) + **Slider de Reação** ou **Teste Rápido**.
     - **Story 05 (Conversão Direta - Template A Dark Royal):** Prova de resultado + área reservada na metade inferior segura para **Sticker de Link Oficial (`https://pericias.btech.inf.br`)**.
     - **Story 06 (Fechamento e Canal Direto - Template B ou C):** Chamada para o novo Carrossel do Feed + **Caixa de Perguntas / DM** para diagnóstico de escritório ou cadastro na rede de peritos.
2. **Controle Rígido de Densidade e Zonas Seguras:**
   - Limite cada card de Story a **no máximo 20 palavras** de texto visível (excluindo o texto interno do sticker nativo).
   - Mantenha obrigatoriamente `250px` livres no topo e `340px` livres na base em todos os 6 cards.

## Output Format

Salve a especificação completa em `squads/maximus-pericias-instagram/output/stories-sequence.md`:

```markdown
# Sequência Estratégica de Stories (1080x1920) - @maximus.pericias

## 1. Visão Geral da Sequência
- **Objetivo Principal:** [Engajamento em Enquete + Cliques para pericias.btech.inf.br]
- **Total de Cards:** 6 Stories em 1080x1920px (9:16)

## 2. Especificação Card a Card (Para Renderização HTML/Playwright)
### Story 01 - [Função no Funil]
- **Template Visual:** [Template A | Template B | Template C]
- **Frame Real Integrado:** `references/video-frames/[arquivo.jpg]`
- **Headline Curta (Hanken Grotesk 800/900):** "[Texto]"
- **Texto de Apoio (Inter 600):** "[Texto]"
- **Sticker Interativo Nativo + Coordenada Y:** [Tipo de Sticker, texto das opções e posição em pixels]
- **Contagem de Palavras no Card:** [X palavras - máx. 20]

[Repetir para os Stories 01 a 06]
```

## Output Example

```markdown
### Story 01 - Micro-Compromisso Inicial (Enquete de Dor)
- **Template Visual:** Template A (Dark Royal Prestige - `#0B1329` -> `#002366`)
- **Frame Real Integrado:** `references/video-frames/vid1_frame_50.jpg`
- **Headline Curta (Hanken Grotesk 900):** "Quando sai um alvará de R$ 50 mil, você já sabe o valor líquido real?"
- **Texto de Apoio (Inter 600):** "Responda com sinceridade:"
- **Sticker Interativo Nativo + Coordenada Y:** Sticker de Enquete centralizado em `Y: 1280px` | Opção A: "Sim, calculo na ponta do lápis" | Opção B: "Só descubro quando cai na conta"
- **Contagem de Palavras no Card:** 18 palavras
```

## Veto Conditions

1. Rejeitar se qualquer card de Story ultrapassar 20 palavras de texto visível na arte.
2. Rejeitar se qualquer texto ou sticker for posicionado acima de `Y: 250px` ou abaixo de `Y: 1580px` (`340px` da base).
3. Rejeitar se houver qualquer uso de travessão (`-`) em qualquer card.

## Quality Criteria

- **Interatividade Real em Múltiplos Pontos:** Presença obrigatória de Enquete no Story 01, Sticker de Link (`https://pericias.btech.inf.br`) no Story 05 e Caixa de Perguntas/DM no Story 06.
- **Integração com Frames Reais:** Uso de capturas autênticas do Maximus Perícias em molduras limpas.
- **Conformidade Linguística:** Texto 100% em Português Brasileiro (`pt-BR`) sem travessões (`-`).
