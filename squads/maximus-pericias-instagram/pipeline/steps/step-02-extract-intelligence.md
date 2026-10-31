---
execution: inline
agent: mario-minerador
inputFile: squads/maximus-pericias-instagram/output/research-focus.md
outputFile: squads/maximus-pericias-instagram/output/product-intelligence.md
---

# Passo 02: Extrair Inteligência do Produto e Frames dos Vídeos

## Context Loading

Carregue e analise integralmente os seguintes arquivos antes de iniciar a mineração técnica:
- `squads/maximus-pericias-instagram/output/research-focus.md` (foco temático selecionado pelo usuário no Passo 01)
- `_opensquad/_memory/company.md` (contexto oficial da SRTecno / BTech e do SaaS Maximus Perícias)
- `squads/maximus-pericias-instagram/pipeline/data/research-brief.md` (inventário completo da landing page e dos 202 frames extraídos dos vídeos)
- `squads/maximus-pericias-instagram/references/landing-page/landing-copy.txt` (texto integral capturado de `https://pericias.btech.inf.br`)
- `squads/maximus-pericias-instagram/references/video-frames/` (frames HD extraídos de `GESTÃO DE PERITOS PROPRIETÁRIOS .mp4` e `GESTÃO DE PERITOS TERCERIZADOS.mp4`)

## Instructions

### Process

1. **Mapeamento Direcionado ao Foco da Campanha:**
   - Identifique no `research-focus.md` qual pilar ou funcionalidade foi escolhido pelo usuário para a rodada atual.
   - Selecione os argumentos técnicos, artigos legais do CPC/2015 e métricas verificadas em `landing-copy.txt` e `research-brief.md` que sustentam diretamente esse tema.
2. **Curadoria Cirúrgica de Frames Reais (`references/video-frames/`):**
   - Inspecione os frames disponíveis (`vid1_frame_01.jpg` a `vid1_frame_105.jpg` e `vid2_frame_01.jpg` a `vid2_frame_97.jpg`) e selecione no mínimo 8 frames de alta nitidez que comprovem visualmente a funcionalidade abordada.
   - Para cada frame selecionado, documente o caminho relativo exato, o vídeo de origem, os dados reais visíveis na tela (ex: valores em R$, status de alvará, fórmulas, botões e tabelas) e em qual formato (Feed, Reels ou Stories) ele deve ser aplicado.
3. **Extração de Provas Matemáticas e Contraste Operacional:**
   - Transcreva literalmente os números exatos exibidos na tela (ex: simulação de alvará de `R$ 50.000,00` com IRRF `R$ 3.750,00`, INSS `R$ 908,86`, ISSQN `R$ 1.000,00` e líquido `R$ 44.341,14` em `vid1_frame_50.jpg`, ou redução de `15-30h` no Word para `< 45 min` na MAX AI).
   - Estruture a tabela de contraste entre o "Modo Antigo (Planilhas, Word e Pastas Soltas)" e o "Modo Maximus Perícias" para municiar o estrategista de posicionamento.

## Output Format

Salve o dossiê completo em `squads/maximus-pericias-instagram/output/product-intelligence.md` contendo:

```markdown
# Dossiê de Inteligência de Produto & Mapeamento de Frames - Maximus Perícias

## 1. Síntese do Foco da Rodada
- **Pilar Selecionado:** [Nome do Pilar]
- **Público-Alvo Principal:** [Peritos Proprietários | Peritos Terceirizados B2B | Ecossistema Completo]
- **Promessa Central Verificada:** [Frase sintética baseada nos dados reais]

## 2. Métricas e Provas Factuais Extraídas (Zero Alucinação)
| Métrica / Dado Real | Valor Exato | Fonte Comprobatória | Impacto Prático para o Perito |
| :--- | :--- | :--- | :--- |

## 3. Catálogo de Frames Reais Selecionados para os Criativos
| Arquivo de Frame | Vídeo de Origem | Elementos Visíveis na Interface | Aplicação Recomendada (Feed / Reels / Stories) |
| :--- | :--- | :--- | :--- |

## 4. Matriz de Contraste Operacional (Antes vs. Depois)
| Etapa do Trabalho Pericial | Sem Maximus Perícias (Caos Manual) | Com Maximus Perícias (Engenharia Jurídica) |
| :--- | :--- | :--- |
```

## Output Example

```markdown
# Dossiê de Inteligência de Produto & Mapeamento de Frames - Maximus Perícias

## 1. Síntese do Foco da Rodada
- **Pilar Selecionado:** Pilar 2: Engenharia Financeira de Honorários & Alvarás (Peritos Proprietários)
- **Público-Alvo Principal:** Peritos Judiciais Titulares/Proprietários nomeados por Varas Cíveis
- **Promessa Central Verificada:** Previsibilidade financeira absoluta do arbitramento ao levantamento líquido do alvará com cálculo automático de retenções na fonte.

## 2. Métricas e Provas Factuais Extraídas (Zero Alucinação)
| Métrica / Dado Real | Valor Exato | Fonte Comprobatória | Impacto Prático para o Perito |
| :--- | :--- | :--- | :--- |
| Simulação Real de Alvará | Bruto R$ 50.000,00 -> Líquido R$ 44.341,14 | `vid1_frame_50.jpg` | Elimina a surpresa de perder R$ 5.658,86 em retenções não previstas de IRRF, INSS e ISSQN. |
| Estágios do Funil de Alvarás | 4 etapas (Arbitrado, Intimação, Depositado, Levantado) | `vid1_frame_50.jpg` | Impede que alvarás já depositados fiquem esquecidos nos autos sem petição de levantamento. |

## 3. Catálogo de Frames Reais Selecionados para os Criativos
| Arquivo de Frame | Vídeo de Origem | Elementos Visíveis na Interface | Aplicação Recomendada (Feed / Reels / Stories) |
| :--- | :--- | :--- | :--- |
| `vid1_frame_50.jpg` | `GESTÃO DE PERITOS PROPRIETÁRIOS .mp4` | Funil de 4 etapas de alvará + Calculadora Tributária (IRRF 7,5%, INSS R$ 908,86, ISSQN 2,0%) | Capa do Feed (Slide 1), Slide 4 de Prova e Story 03 |
| `vid1_frame_32.jpg` | `GESTÃO DE PERITOS PROPRIETÁRIOS .mp4` | Editor de Proposta de Honorários Art. 465 CPC | Slide 3 do Feed e Cena 02 do Reels |
```

## Veto Conditions

1. Rejeitar imediatamente a saída se qualquer número, funcionalidade ou artigo de lei citado não existir em `landing-copy.txt` ou nos vídeos de `Vídeos/`.
2. Rejeitar se os nomes de arquivo de frame indicados não existirem fisicamente na pasta `squads/maximus-pericias-instagram/references/video-frames/`.
3. Rejeitar se houver qualquer uso de travessão (`-`) no documento gerado.

## Quality Criteria

- **Rastreabilidade 100% Verificável:** Cada afirmação técnica está vinculada a um arquivo `.jpg` de frame real ou seção de `landing-copy.txt`.
- **Mínimo de 8 Frames Catalogados:** O dossiê fornece material visual suficiente para cobrir todos os slides do Feed, cenas do Reels e cards de Stories sem repetição monótona.
- **Conformidade Linguística:** Texto integralmente em Português Brasileiro (`pt-BR`) e sem travessões (`-`).
