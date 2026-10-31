---
execution: inline
agent: renato-reels
format: instagram-reels
inputFile: squads/maximus-pericias-instagram/output/selected-angle.md
outputFile: squads/maximus-pericias-instagram/output/reels-script.md
---

# Passo 06: Criar Roteiro Técnico e Visual de Reels (1080x1920 - 9:16)

## Context Loading

Carregue e analise os seguintes arquivos antes de estruturar o roteiro de Reels:
- `squads/maximus-pericias-instagram/output/selected-angle.md` (ângulo aprovado pelo usuário no Passo 04)
- `squads/maximus-pericias-instagram/output/product-intelligence.md` (frames reais de `GESTÃO DE PERITOS PROPRIETÁRIOS .mp4` e `GESTÃO DE PERITOS TERCERIZADOS.mp4`)
- `squads/maximus-pericias-instagram/output/feed-carousel.md` (carrossel do Feed recém-criado para garantir sinergia temática sem duplicação mecânica)
- `squads/maximus-pericias-instagram/pipeline/data/visual-identity.md` (especificações 9:16 `1080x1920` e zonas seguras)
- `squads/maximus-pericias-instagram/pipeline/data/tone-of-voice.md` (tom de voz executivo e restrições de estilo)

## Instructions

### Process

1. **Roteiro Cronometrado Segundo a Segundo (30s a 45s):**
   - Estruture o vídeo em 5 a 6 blocos dinâmicos com mudanças visuais a cada 3 a 4 segundos:
     - **00s a 03s (Hook Disruptivo):** Pergunta ou afirmação de alto impacto com corte imediato para o frame mais revelador do software.
     - **03s a 10s (Diagnóstico do Gargalo Manual):** Exposição objetiva do tempo ou dinheiro perdido pelo perito no Word/Excel.
     - **10s a 28s (Demonstração guiada nas Telas do Maximus Perícias):** Sequência de 3 a 4 cenas com zoom dinâmico (`pan & zoom`) sobre os frames reais (`vid1_frame_XX.jpg` / `vid2_frame_XX.jpg`), destacando badges em Solar Gold (`#FFD700`) e Cobalt Blue (`#0047AB`).
     - **28s a 38s (Resultado Tangível e Prova Técnica):** Contraste numérico final (`-95%` triagem, `< 45 min` laudo ou líquido exato do alvará) e loop de fechamento com CTA para `pericias.btech.inf.br`.
2. **Design da Capa do Reels (`reels-cover.png` em `1080x1920`):**
   - Especifique a arte da capa em `1080x1920` garantindo que todo o texto principal e o mockup do software estejam contidos na zona central `1080x1440` (Y: `240px` a `1680px`) para visualização perfeita tanto na aba Reels quanto na grade 4:5 do perfil `@maximus.pericias`.
3. **Legenda Otimizada para Reels:**
   - Escreva a legenda de acompanhamento (90 a 140 palavras) com chamada imediata na primeira linha, resumo em 3 tópicos objetivos, CTA para o link da bio (`pericias.btech.inf.br`) e 6 hashtags estratégicas.

## Output Format

Salve o roteiro completo em `squads/maximus-pericias-instagram/output/reels-script.md`:

```markdown
# Roteiro Técnico de Reels (1080x1920) - @maximus.pericias

## 1. Especificações Técnicas do Vídeo
- **Duração Total:** [30s a 45s]
- **Resolução e Proporção:** 1080x1920px (9:16 Vertical)
- **Direção de Áudio:** [Locução firme 155 ppm + Trilha instrumental minimalista]

## 2. Especificação da Capa do Reels (`reels-cover.png`)
- **Template Base:** [Template A Dark Royal | Template C B2B Grid]
- **Frame Real em Destaque:** `references/video-frames/[arquivo.jpg]`
- **Headline na Zona Segura 4:5 (Máx. 8 palavras):** "[Texto]"
- **Badge de Apoio:** "[Texto]"

## 3. Tabela de Decupagem Segundo a Segundo
| Tempo | Cena / Frame Real Utilizado | Movimento de Câmera / UI | Texto On-Screen (Safe Zone) | Locução (Voiceover em pt-BR) |
| :--- | :--- | :--- | :--- | :--- |

## 4. Legenda Oficial do Reels (Caption)
[Texto completo da legenda com hashtags]
```

## Output Example

```markdown
| Tempo | Cena / Frame Real Utilizado | Movimento de Câmera / UI | Texto On-Screen (Safe Zone) | Locução (Voiceover em pt-BR) |
| :--- | :--- | :--- | :--- | :--- |
| **00s - 03s** | `vid1_frame_50.jpg` (Módulo Financeiro) | Zoom rápido no card `Líquido R$ 44.341,14` | **ALVARÁ DE R$ 50 MIL = R$ 44.341 LÍQUIDOS?** | Quando o juiz arbitra cinquenta mil reais de honorários, quanto realmente entra no seu caixa? |
| **03s - 09s** | `vid1_frame_50.jpg` (Detalhe Impostos) | Destaque em `#FFD700` sobre IRRF, INSS e ISSQN | **IRRF 7,5% + INSS TETO + ISSQN 2%** | Na planilha comum você só vê o valor bruto. No levantamento, cinco mil e seiscentos reais ficam retidos na fonte. |
```

## Veto Conditions

1. Rejeitar se o roteiro não especificar os arquivos `.jpg` exatos de `references/video-frames/` em cada cena de demonstração.
2. Rejeitar se o texto on-screen ou a capa invadir as zonas mortas do Reels (`220px` topo, `420px` base, `120px` lateral direita).
3. Rejeitar se houver qualquer caractere `-` (travessão) no roteiro, nas legendas on-screen ou na caption.

## Quality Criteria

- **Ritmo de Alta Retenção:** Mudança visual ou de callout a cada 3 a 4 segundos mantendo o olho do espectador preso à tela real do software.
- **Capa Compatível com a Grade 4:5:** Headline curta (até 8 palavras) posicionada rigorosamente no centro seguro da imagem `1080x1920`.
- **Conformidade Linguística:** Texto 100% em Português Brasileiro (`pt-BR`) sem travessões (`-`).
