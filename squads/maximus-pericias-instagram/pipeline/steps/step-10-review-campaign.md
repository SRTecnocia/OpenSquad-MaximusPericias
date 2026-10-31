---
execution: inline
agent: vera-veredito
on_reject: step-05-create-feed
inputFile: squads/maximus-pericias-instagram/output/visual-assets-manifest.md
outputFile: squads/maximus-pericias-instagram/output/review-report.md
---

# Passo 10: Auditar Qualidade Técnica, Visual e Conformidade CPC/LGPD

## Context Loading

Carregue e audite minuciosamente todos os arquivos abaixo:
- `squads/maximus-pericias-instagram/output/visual-assets-manifest.md` e todas as imagens `.png` em `squads/maximus-pericias-instagram/output/assets/`
- `squads/maximus-pericias-instagram/output/feed-carousel.md`
- `squads/maximus-pericias-instagram/output/reels-script.md`
- `squads/maximus-pericias-instagram/output/stories-sequence.md`
- `squads/maximus-pericias-instagram/output/product-intelligence.md`
- `squads/maximus-pericias-instagram/pipeline/data/quality-criteria.md` e `squads/maximus-pericias-instagram/pipeline/data/anti-patterns.md`

## Instructions

### Process

1. **Auditoria Cruzada de Veracidade e Precisão Normativa (CPC/LGPD):**
   - Verifique se cada número, métrica (`-95%` triagem via IBM Docling OCR, `< 45 min` laudo MAX AI, `< 1.2s` latência RAG, `100% Art. 473 CPC`, `0% alucinação`, retenção tributária líquida `R$ 44.341,14`) e artigo do CPC/2015 citado nos textos e imagens corresponde exatamente ao `product-intelligence.md`.
2. **Inspeção Visual Independente dos Arquivos PNG (`output/assets/`):**
   - Inspecione os arquivos `.png` de Feed (`1080x1440`), Capa de Reels (`1080x1920`) e Stories (`1080x1920`).
   - Confirme que não há textos cortados, sobreposições indevidas, frames borrados ou violação das safe zones (`250px` topo e `340px` base nos Stories; zona central 4:5 na capa do Reels).
3. **Verificação Automatizada de Governança Linguística (Zero Travessões):**
   - Verifique que nenhum arquivo `.md` ou `.html` da campanha contém o caractere `-` (travessão) ou termos proibidos listados em `anti-patterns.md`.
4. **Cálculo de Scorecard e Veredito:**
   - Atribua nota de 0.0 a 10.0 para cada uma das 5 dimensões de qualidade. Se todas as dimensões obtiverem nota `>= 9.0` e nenhuma condição de veto for violada, emita o veredito `APROVADO PARA PUBLICAÇÃO`. Caso contrário, emita `REPROVADO` e especifique as correções exatas.

## Output Format

Salve o parecer completo em `squads/maximus-pericias-instagram/output/review-report.md`:

```markdown
# Relatório Oficial de Auditoria Técnica e Visual - Vera Veredito

## 1. Veredito Final
- **Status:** [APROVADO PARA PUBLICAÇÃO | REPROVADO]
- **Média Global:** [X.X / 10.0]

## 2. Scorecard de Conformidade (Mínimo 9.0 por Dimensão)
| Dimensão | Nota | Status | Observação Técnica |
| :--- | :--- | :--- | :--- |
| 1. Veracidade Factual e Conformidade CPC/LGPD | X.X | [PASS/FAIL] | [Evidência] |
| 2. Posicionamento Steve Jobs e Gancho | X.X | [PASS/FAIL] | [Evidência] |
| 3. Fidelidade Visual (Sistema A + B + C) | X.X | [PASS/FAIL] | [Evidência] |
| 4. Adequação Nativa (4:5 Feed e 9:16 Reels/Stories) | X.X | [PASS/FAIL] | [Evidência] |
| 5. Governança Linguística pt-BR (Zero Travessões) | X.X | [PASS/FAIL] | [Evidência] |

## 3. Checklist Individual de Assets PNG Auditados
- [Lista de todos os arquivos PNG verificados com status PASS/FAIL]
```

## Output Example

```markdown
# Relatório Oficial de Auditoria Técnica e Visual - Vera Veredito

## 1. Veredito Final
- **Status:** APROVADO PARA PUBLICAÇÃO
- **Média Global:** 9.8 / 10.0

## 2. Scorecard de Conformidade (Mínimo 9.0 por Dimensão)
| Dimensão | Nota | Status | Observação Técnica |
| :--- | :--- | :--- | :--- |
| 1. Veracidade Factual e Conformidade CPC/LGPD | 10.0 | PASS | Cálculos de alvará e citações dos Arts. 465, 473 e 220 do CPC 100% exatos. |
| 2. Posicionamento Steve Jobs e Gancho | 9.6 | PASS | Contraste imediato e linguagem executiva limpa de jargões vazios. |
| 3. Fidelidade Visual (Sistema A + B + C) | 9.8 | PASS | Paleta oficial `#0047AB`, `#002366`, `#0B1329`, `#FFD700` e `#F9F9FF` aplicada com rigor. |
| 4. Adequação Nativa (4:5 Feed e 9:16 Reels/Stories) | 9.8 | PASS | Todos os slides <= 25 palavras e zonas seguras 9:16 respeitadas. |
| 5. Governança Linguística pt-BR (Zero Travessões) | 10.0 | PASS | Zero ocorrências do caractere travessão em textos e imagens. |
```

## Veto Conditions

1. Reprovar obrigatoriamente se qualquer dimensão obtiver nota inferior a `9.0` ou se qualquer arquivo PNG apresentar erro gráfico.
2. Reprovar se houver qualquer dado inventado que não conste na plataforma `https://pericias.btech.inf.br` ou nos vídeos oficiais.
3. Reprovar se existir qualquer ocorrência de travessão (`-`) nos arquivos auditados.

## Quality Criteria

- **Rigor Imparcial:** Verificação real tanto do texto quanto da imagem renderizada de cada peça.
- **Rastreabilidade Completa:** Todos os PNGs de `output/assets/` nominalmente checados no relatório.
- **Conformidade Linguística:** Parecer redigido 100% em Português Brasileiro (`pt-BR`) sem travessões (`-`).
