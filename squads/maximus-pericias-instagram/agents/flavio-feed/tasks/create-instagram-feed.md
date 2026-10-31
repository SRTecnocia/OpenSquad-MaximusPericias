---
task: "Criar Carrossel de Feed Instagram (8 a 10 Lâminas) e Legenda"
order: 1
input: |
  - selected_angle: Ângulo em 3 atos e tom de voz escolhidos pelo usuário em output/selected-angle.md
  - product_intelligence: Dossiê técnico e mapa de frames em output/product-intelligence.md
output: |
  - feed_post: Estrutura completa de 8 a 10 lâminas (40-80 palavras/lâmina), 3 ganchos, mapeamento visual A+B+C e legenda em output/feed-post.md
---

# Criar Carrossel de Feed Instagram (8 a 10 Lâminas) e Legenda

Esta tarefa redige a publicação completa de Feed em formato Carrossel (`1080x1440px`, 8 a 10 lâminas), integrando a narrativa em 3 atos, os quadros reais do software e o Sistema Unificado de Templates (Modelos A, B e C).

## Process

1. **Formular 3 Opções de Gancho e Definir o Formato de Carrossel:** Com base em `output/selected-angle.md`, criar 3 ganchos distintos para a capa e escolher o formato estrutural do carrossel (`Editorial / Tese`, `Problema -> Solução`, `Antes e Depois`, `Mito vs Realidade` ou `Tutorial / Passo-a-passo`).
2. **Escrever as 8 a 10 Lâminas com 40 a 80 Palavras Cada:** Redigir `Headline` + `Supporting text` para cada lâmina, verificando a contagem de palavras (mínimo 40, máximo 80 palavras por lâmina), indicando as `Accent keywords` e alternando o `Background / Template` entre `Modelo A (Dark Royal + UI Frame)`, `Modelo B (Clean Light #F9F9FF)` e `Modelo C (Liquid Metal Data & ROI)`.
3. **Redigir a Legenda e Seleção de Hashtags:** Escrever a legenda iniciando com um gancho de até 125 caracteres, corpo escaneável com quebras de linha, neutralizador de objeção, pergunta final de engajamento, CTA de salvamento/DM e 8 a 12 hashtags segmentadas.

## Output Format

```yaml
chosen_carousel_format: "Problema -> Solução | Editorial | Antes e Depois | Listicle | Tutorial"
hooks_presented:
  - id: "Hook A"
    type: "Contraste Numérico"
    text: "..."
    rationale: "..."
  - id: "Hook B"
    type: "Provocação de Perda"
    text: "..."
    rationale: "..."
  - id: "Hook C"
    type: "Ruptura de Mecanismo"
    text: "..."
    rationale: "..."
slides:
  - slide_number: 1
    role: "Cover"
    template_model: "Modelo A"
    headline: "..."
    supporting_text: "..."
    accent_keywords: ["..."]
    ui_frame: "references/video-frames/vid1_frame_50.jpg"
    word_count: 48
caption:
  hook_125_chars: "..."
  body: "..."
  objection_neutralizer: "..."
  closing_question_and_cta: "..."
  hashtags: ["#periciajudicial", "..."]
```

## Output Example

> Use como referência de qualidade e densidade (40 a 80 palavras por lâmina).

```yaml
chosen_carousel_format: "Problema -> Solução (8 Lâminas)"
hooks_presented:
  - id: "Hook A"
    type: "Contraste de Tempo e Produtividade"
    text: "De 30 horas no Word para 45 minutos no Sistema Operacional: como a elite pericial entrega laudos ABNT sem virar a noite."
    rationale: "Ataca diretamente a dor física da sobrecarga de trabalho com números auditados da plataforma."
  - id: "Hook B"
    type: "Auditoria Financeira de Alvará"
    text: "R$ 50.000 arbitrados no processo. Você sabe exatamente quanto cai líquido após o teto do INSS, IRRF e ISSQN?"
    rationale: "Desperta aversão imediata à perda financeira usando o exemplo real da Calculadora de Retenção Tributária."
  - id: "Hook C"
    type: "Autoridade e Blindagem Forense"
    text: "Quatro travas invioláveis que impedem o MAX AI de alucinar folhas dos autos e reduzem em 90% as impugnações."
    rationale: "Neutraliza o ceticismo técnico do perito sênior e posiciona a superioridade do RAG forense."
slides:
  - slide_number: 1
    role: "Cover"
    template_model: "Modelo A (Dark Royal + UI Frame)"
    headline: "De 30 horas no Word para 45 minutos no Sistema Operacional Forense."
    supporting_text: "Enquanto o método artesanal drena sua semana na leitura manual de autos volumosos e planilhas paralelas, peritos de elite centralizam prazos do CPC, laudos ABNT e alvarás em uma única infraestrutura neural."
    accent_keywords: ["45 minutos", "Sistema Operacional"]
    ui_frame: "references/video-frames/vid1_frame_80.jpg"
    word_count: 45
  - slide_number: 2
    role: "Problem"
    template_model: "Modelo B (Clean Light #F9F9FF)"
    headline: "O gargalo invisível que trava o crescimento do seu gabinete pericial."
    supporting_text: "A cada nova nomeação judicial no PJe, e-SAJ ou Eproc, o ciclo manual se repete: baixar centenas de páginas em PDF, caçar quesitos espalhados em petições avulsas, conferir suspensão forense no calendário e controlar honorários no Excel."
    accent_keywords: ["gargalo invisível", "ciclo manual"]
    ui_frame: "none"
    word_count: 44
  - slide_number: 3
    role: "Agitate / Data"
    template_model: "Modelo C (Liquid Metal Data & ROI)"
    headline: "O custo real de operar sem inteligência documental e controle tributário."
    supporting_text: "Operar no improviso custa caro: são 15 a 30 horas perdidas por laudo, risco constante de omitir quesitos das partes, prazos fatais calculados sem o artigo 220 do CPC e retenções de INSS e IRRF distorcidas no levantamento do alvará."
    accent_keywords: ["15 a 30 horas", "artigo 220 do CPC"]
    ui_frame: "none"
    word_count: 47
  - slide_number: 4
    role: "Mechanism 1 (MAX AI)"
    template_model: "Modelo A (Dark Royal + UI Frame)"
    headline: "Motor IBM Docling OCR e Copiloto RAG com zero alucinação nos autos."
    supporting_text: "O MAX AI varre processos de mais de 1.000 páginas reduzindo 95% do tempo de triagem. Ele separa 100% dos quesitos por origem e redige a minuta nos 10 capítulos da ABNT e artigo 473 do CPC citando a folha exata."
    accent_keywords: ["IBM Docling OCR", "10 capítulos da ABNT"]
    ui_frame: "references/video-frames/vid1_frame_80.jpg"
    word_count: 49
  - slide_number: 5
    role: "Mechanism 2 (Alvarás)"
    template_model: "Modelo A (Dark Royal + UI Frame)"
    headline: "R$ 50.000,00 brutos viram R$ 44.341,14 líquidos auditados na tela."
    supporting_text: "No Módulo Financeiro e Alvarás, você acompanha os 4 estágios do recebimento (Arbitrado, Intimação, Depositado e Levantado) e simula na hora a retenção de IRRF (7,5%), a trava do teto máximo do INSS (R$ 908,86) e o ISSQN."
    accent_keywords: ["R$ 44.341,14 líquidos", "4 estágios"]
    ui_frame: "references/video-frames/vid1_frame_50.jpg"
    word_count: 46
  - slide_number: 6
    role: "Mechanism 3 (Ecossistema B2B)"
    template_model: "Modelo B (Clean Light #F9F9FF)"
    headline: "Um único sistema para Escritórios Proprietários e Especialistas B2B."
    supporting_text: "Carteira lotada? O Perito Titular emite Ordens de Serviço B2B com SLA e sigilo LGPD. O Escritório Especialista recebe a demanda na sua central, elabora o parecer técnico ou cálculo bancário RMC/RCC e fatura via PIX com rastreabilidade."
    accent_keywords: ["Escritórios Proprietários", "Especialistas B2B"]
    ui_frame: "references/video-frames/vid2_frame_02.jpg"
    word_count: 46
  - slide_number: 7
    role: "Proof & Security"
    template_model: "Modelo C (Liquid Metal Data & ROI)"
    headline: "Custódia forense de nível militar e escala de 3X na sua carteira."
    supporting_text: "Seus laudos, anamneses e cálculos rodam sob criptografia de campo AES-256-GCM, trilha imutável AuditLog Hash-Chain e isolamento multi-tenant no Neon PostgreSQL. Você multiplica em 3 vezes sua capacidade operacional com blindagem contra impugnações."
    accent_keywords: ["AES-256-GCM", "3 vezes"]
    ui_frame: "none"
    word_count: 41
  - slide_number: 8
    role: "CTA"
    template_model: "Modelo A (Dark Royal + UI Frame)"
    headline: "Deixe as planilhas no passado. Opere no padrão Perito de Elite."
    supporting_text: "Comente SISTEMA aqui embaixo para receber o acesso à demonstração executiva ou acesse pericias.btech.inf.br pelo link da nossa bio. Salve este carrossel e envie para o colega perito que precisa escalar sua operação este mês."
    accent_keywords: ["Comente SISTEMA", "Perito de Elite"]
    ui_frame: "references/video-frames/vid1_frame_01.jpg"
    word_count: 43
caption:
  hook_125_chars: "Você ainda gasta 30 horas no Word para entregar um único laudo pericial? O jogo técnico nos tribunais mudou."
  body: |
    A diferença entre o perito sobrecarregado e o escritório pericial que gerencia 3X mais processos sem inflar a equipe não é esforço braçal. É infraestrutura.

    O Maximus Perícias foi arquitetado como o Primeiro Sistema Operacional completo para Peritos Judiciais (Titulares de Varas) e Escritórios Especialistas B2B:

    1. Triagem IBM Docling OCR: leitura de autos de +1.000 páginas com 95% de redução operacional.
    2. MAX AI (Art. 473 CPC): minuta nos 10 capítulos da ABNT em menos de 45 minutos, citando a folha exata dos autos com 0% de alucinação.
    3. Financeiro & Alvarás: controle dos 4 estágios do honorário + Calculadora de Retenção Tributária (IRRF, teto máximo do INSS e ISSQN).
    4. Central B2B Multi-Tenant: emissão e recepção de Ordens de Serviço técnicas com sigilo LGPD e criptografia AES-256-GCM.
  objection_neutralizer: "Preocupado com sigilo judicial? Seus documentos processuais ficam em tenant isolado com criptografia de nível bancário e jamais são usados para treinar modelos públicos."
  closing_question_and_cta: "Qual é o maior gargalo da sua operação hoje: redigir laudos, calcular prazos do Art. 220 do CPC ou controlar alvarás? Comente SISTEMA abaixo ou acesse o link na bio (@maximus.pericias)."
  hashtags:
    - "#periciajudicial"
    - "#peritojudicial"
    - "#assistentetecnico"
    - "#engenhariadeavaliacoes"
    - "#periciacontabil"
    - "#periciamedica"
    - "#periciagrafotecnica"
    - "#calculosjudiciais"
    - "#legaltechbrasil"
    - "#maximuspericias"
```

## Quality Criteria

- [ ] Contém entre 8 e 10 lâminas completas, cada uma com 40 a 80 palavras.
- [ ] Alterna explicitamente os Modelos A, B e C e indica os quadros reais de `references/`.
- [ ] A legenda respeita o limite de 125 caracteres no gancho inicial e não contém links crus nem traços longos (`-`).

## Veto Conditions

Rejeitar e refazer se QUALQUER condição abaixo ocorrer:
1. Qualquer lâmina tiver menos de 40 palavras ou mais de 80 palavras.
2. Faltar o mapeamento do Modelo Visual (`Modelo A`, `Modelo B`, `Modelo C`) ou houver traços longos (`-`).
