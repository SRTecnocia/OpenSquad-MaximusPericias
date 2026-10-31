---
task: "Auditar Campanha Completa (Copy + Assets Visuais Renderizados)"
order: 1
input: |
  - feed_carousel: Roteiro e legenda do Carrossel de Feed em squads/maximus-pericias-instagram/output/feed-carousel.md
  - reels_script: Roteiro técnico de Reels em squads/maximus-pericias-instagram/output/reels-script.md
  - stories_sequence: Sequência de Stories em squads/maximus-pericias-instagram/output/stories-sequence.md
  - visual_assets_manifest: Manifesto e arquivos PNG gerados em squads/maximus-pericias-instagram/output/visual-assets-manifest.md e squads/maximus-pericias-instagram/output/assets/
  - quality_criteria: Critérios de qualidade e anti-patterns em squads/maximus-pericias-instagram/pipeline/data/quality-criteria.md e anti-patterns.md
output: |
  - review_report: Relatório de auditoria técnica e visual em squads/maximus-pericias-instagram/output/review-report.md com veredito APROVADO ou REPROVADO
---

# Auditar Campanha Completa (Copy + Assets Visuais Renderizados)

Auditoria técnica, jurídica, editorial e visual de todos os entregáveis de texto e imagem da campanha de `@maximus.pericias` antes da submissão ao checkpoint de aprovação final e publicação.

## Process

1. **Auditoria de Veracidade Factual e Conformidade Legal (CPC/LGPD):**
   - Confrontar todas as afirmações técnicas de `feed-carousel.md`, `reels-script.md` e `stories-sequence.md` com o dossiê `product-intelligence.md` e `research-brief.md`.
   - Confirmar que todas as métricas (`-95%` triagem via IBM Docling OCR, `15-30h` para `< 45 min` na MAX AI, `< 1.2s` latência RAG, `100% Art. 473 CPC`, `0% alucinação`, `3X` mais processos, cálculo líquido de alvará `R$ 44.341,14`) estão reproduzidas com exatidão matemática.
   - Verificar citações de artigos do CPC/2015 (Art. 473, Art. 465, Art. 220, Art. 523), Lei 14.181 e segurança LGPD (`AES-256-GCM`, `PBKDF2-SHA512`, `AuditLog Hash-Chain`).

2. **Varredura de Governança Linguística e Anti-Patterns:**
   - Executar verificação de caracteres para garantir **zero ocorrências de travessão (`-`)** em todos os arquivos `.md` e `.html` gerados.
   - Verificar ausência total de palavras banidas em `pipeline/data/anti-patterns.md` (clickbait, promessas financeiras fáceis, jargões de marketing genérico).
   - Auditar a contagem de palavras de cada slide do Feed (máximo 25 palavras de texto visível por card) e de cada card de Stories (máximo 20 palavras).

3. **Inspeção Visual dos PNGs Renderizados (`output/assets/`):**
   - Ler e inspecionar visualmente cada imagem PNG gerada (`feed-slide-01.png` a `feed-slide-XX.png`, `reels-cover.png`, `story-01.png` a `story-XX.png`).
   - Confirmar aplicação correta do Sistema Unificado A + B + C (Template A Dark Royal `#0B1329`/`#002366`, Template B Editorial Light `#F9F9FF`, Template C B2B Bento Grid `#001946`), nitidez dos prints reais do software e respeito às zonas seguras de `1080x1440` e `1080x1920`.

4. **Emissão do Veredito e Plano de Ação:**
   - Calcular a nota de cada uma das 5 dimensões e a média global.
   - Se a média for `>= 9.0/10` e nenhum item crítico falhar, emitir veredito `APROVADO PARA PUBLICAÇÃO` em `squads/maximus-pericias-instagram/output/review-report.md`.
   - Se houver qualquer falha, emitir `REPROVADO` detalhando as correções obrigatórias para reexecução a partir da etapa correspondente.

## Output Format

```markdown
# Relatório de Auditoria de Qualidade - Campanha @maximus.pericias

## 1. Resumo Executivo e Veredito
- **Status Final:** [APROVADO PARA PUBLICAÇÃO | REPROVADO]
- **Pontuação Global:** [X.X / 10.0]

## 2. Scorecard por Dimensão
| Dimensão Auditada | Nota (0-10) | Status | Evidência Verificada |
| :--- | :--- | :--- | :--- |
| 1. Veracidade Factual e Conformidade CPC/LGPD | X.X | [PASS/FAIL] | [Resumo] |
| 2. Posicionamento Steve Jobs e Gancho | X.X | [PASS/FAIL] | [Resumo] |
| 3. Fidelidade Visual (Sistema A + B + C) | X.X | [PASS/FAIL] | [Resumo] |
| 4. Adequação Nativa (4:5 Feed e 9:16 Reels/Stories) | X.X | [PASS/FAIL] | [Resumo] |
| 5. Governança Linguística pt-BR (Zero Travessões) | X.X | [PASS/FAIL] | [Resumo] |

## 3. Auditoria Individual dos Assets PNG
- [Lista de verificação slide a slide e story a story]

## 4. Instruções de Correção (Apenas se REPROVADO)
- [Ações corretivas exatas]
```

## Output Example

```markdown
# Relatório de Auditoria de Qualidade - Campanha @maximus.pericias

## 1. Resumo Executivo e Veredito
- **Status Final:** APROVADO PARA PUBLICAÇÃO
- **Pontuação Global:** 9.8 / 10.0

## 2. Scorecard por Dimensão
| Dimensão Auditada | Nota (0-10) | Status | Evidência Verificada |
| :--- | :--- | :--- | :--- |
| 1. Veracidade Factual e Conformidade CPC/LGPD | 10.0 | PASS | Dados de retenção tributária (R$ 50.000,00 bruto -> R$ 44.341,14 líquido) idênticos ao frame `vid1_frame_50.jpg`. |
| 2. Posicionamento Steve Jobs e Gancho | 9.6 | PASS | Contraste imediato no Slide 1 entre controle manual em planilhas e engenharia financeira pericial. |
| 3. Fidelidade Visual (Sistema A + B + C) | 9.8 | PASS | Alternância exata: Slides 1, 5 e 8 em Template A; Slides 2, 3, 4 e 6 em Template B; Slide 7 em Template C. |
| 4. Adequação Nativa (4:5 Feed e 9:16 Reels/Stories) | 9.8 | PASS | Todos os 8 slides de Feed em 1080x1440 (< 22 palavras/slide) e 6 Stories em 1080x1920 com zonas seguras livres. |
| 5. Governança Linguística pt-BR (Zero Travessões) | 10.0 | PASS | Varredura regex confirmou 0 ocorrências de travessão nos arquivos `.md` e `.html`. |
```

## Quality Criteria

- **Inspeção Baseada em Evidências:** O relatório deve citar nominalmente os arquivos `.png` inspecionados e os números conferidos.
- **Zero Complacência:** Qualquer violação da regra de travessão (`-`) ou erro em número do software resulta automaticamente em nota 0 na respectiva dimensão e reprovação imediata.

## Veto Conditions

Reprovar obrigatoriamente a campanha (`status: REPROVADO`) se:
1. Qualquer arquivo `.png` previsto no roteiro não existir em `squads/maximus-pericias-instagram/output/assets/` ou apresentar falha de renderização.
2. Houver qualquer divergência entre as funcionalidades reais do Maximus Perícias e o texto prometido na campanha.
3. For detectado qualquer caractere `-` (travessão) ou termo de marketing apelativo listado em `anti-patterns.md`.
