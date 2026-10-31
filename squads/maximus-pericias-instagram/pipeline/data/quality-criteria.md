# Critérios de Qualidade e Rubrica de Auditoria: maximus-pericias-instagram

Este arquivo define os padrões mensuráveis que **Vera Veredito** utiliza para aprovar (`APPROVE`) ou rejeitar (`REJECT`) qualquer entregável do esquadrão.

## Regras de Decisão Global
- **APPROVE:** Nota média geral `>= 7.0/10` E nenhum critério individual abaixo de `4.0/10`.
- **CONDITIONAL APPROVE:** Nota média `>= 7.0/10`, mas com ajustes menores não-bloqueantes entre `4.0` e `6.0`.
- **REJECT (Gatilho Automático):** Nota média `< 7.0/10` OU qualquer critério crítico abaixo de `4.0/10`.

---

## Rubrica de Pontuação (Escala 1 a 10)

| # | Critério | Peso | Exigência Mínima para Aprovação (7+/10) | Gatilho de Rejeição Imediata (< 4/10) |
|---|----------|------|-----------------------------------------|---------------------------------------|
| 1 | **Fidelidade Factual ao Produto (Zero Alucinação)** | Crítico | Cita apenas módulos, cálculos, normas e métricas reais de `pericias.btech.inf.br` e dos 2 vídeos oficiais. | Inventa funcionalidade inexistente ou distorce dados técnicos/legais. |
| 2 | **Força do Gancho e Posicionamento (Padrão Steve Jobs)** | Crítico | Gancho para o scroll em 2 segundos; ataca o trabalho manual e apresenta o mecanismo único sem clichês. | Abertura genérica ("Você sabia?", "No mundo atual") ou tom de cursinho amador. |
| 3 | **Estrutura e Densidade de Copy (Feed, Reels, Stories)** | Alto | Carrossel com 8 a 10 lâminas (40 a 80 palavras/lâmina); Reel de 15 a 30s com loop; Stories de 4 a 6 quadros com enquete binária. | Lâminas de carrossel rasas (< 40 palavras) ou prolixas (> 80 palavras); Stories com parede de texto. |
| 4 | **Conformidade com o Design System Oficial (A+B+C)** | Crítico | Usa exclusivamente a paleta (`#0047AB`, `#002366`, `#0B1329`, `#FFD700`, `#C5A021`, `#F9F9FF`, `#111318`) e fontes `Hanken Grotesk` + `Inter`. | Usa cores fora da marca, fontes incorretas ou inclui contador de lâminas (`1/8`). |
| 5 | **Legibilidade, Viewport e Contraste (WCAG AA)** | Crítico | Dimensões exatas (`1080x1440` Feed, `1080x1920` Stories/Reels); fontes acima do piso mínimo (`58px`/`43px`/`34px`/`24px`); contraste `>= 4.5:1`. | Texto cortado (`overflow`), fonte menor que `20px` ou baixo contraste ilegível no celular. |
| 6 | **Governança Linguística e Pontuação (`pt-BR`)** | Alto | Português brasileiro impecável, acentuação completa, frases cirúrgicas e zero traços longos (`-`). | Presença de traço longo (`-`), erros gramaticais ou texto sem acentuação. |

---

## Checklist de Verificação Pré-Publicação
- [ ] Todos os fatos e telas correspondem ao ecossistema real do Maximus Perícias.
- [ ] O Carrossel de Feed possui entre 8 e 10 lâminas e alterna os Modelos A, B e C.
- [ ] Cada lâmina do Carrossel possui entre 40 e 80 palavras (soma de título e texto de apoio).
- [ ] Os primeiros 125 caracteres da legenda funcionam como gancho autônomo antes do "...mais".
- [ ] O roteiro de Reels indica minutagens/quadros reais dos vídeos em `Vídeos/`.
- [ ] A sequência de Stories contém pelo menos 1 elemento interativo binário específico (Enquete ou Quiz).
- [ ] Nenhum arquivo de texto ou imagem contém o caractere `-` (traço Em).
- [ ] Nenhum slide de carrossel contém numeração de página (`1/8`, `2/8`).
