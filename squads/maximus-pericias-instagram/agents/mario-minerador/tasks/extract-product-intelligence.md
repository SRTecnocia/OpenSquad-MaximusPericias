---
task: "Extrair Inteligência Forense do Produto e Mídia"
order: 1
input: |
  - research_focus: Foco de pauta e recorte temporal definidos pelo usuário em output/research-focus.md
  - research_brief: Dossiê mestre em pipeline/data/research-brief.md
output: |
  - product_intelligence: Dossiê estruturado com mecanismos reais, métricas, base legal e seleção de quadros HD dos vídeos em output/product-intelligence.md
---

# Extrair Inteligência Forense do Produto e Mídia

Esta tarefa analisa o foco de campanha solicitado pelo usuário e extrai de `pipeline/data/research-brief.md`, da Landing Page `https://pericias.btech.inf.br` e dos 202 quadros dos vídeos oficiais todos os elementos técnicos, numéricos e visuais necessários para a campanha.

## Process

1. **Ler o Foco da Campanha e o Dossiê Mestre:** Carregar `output/research-focus.md`, `pipeline/data/research-brief.md` e `_opensquad/_memory/company.md` para identificar se a campanha foca em Peritos Proprietários (Titulares), Peritos Terceirizados (Especialistas B2B) ou na sinergia completa do ecossistema.
2. **Mapear Mecanismos, Métricas e Base Legal:** Selecionar os módulos exatos (ex.: MAX AI com IBM Docling, Diário da Justiça DJEN, Calculadora de Retenção Tributária de Alvarás, Cálculos Bancários RMC/RCC/Anatocismo, Calculadora de Data Fatal Art. 220 CPC ou Central B2B) e listar as métricas oficiais verificadas (`-95%` triagem, `45 min` laudo ABNT, `3X` escala, `-90%` impugnações, `< 1.2s` latência RAG).
3. **Selecionar os Quadros Reais de Vídeo e Landing Page:** Indicar os arquivos exatos em `references/video-frames/` (`vid1_frame_XX.jpg` e `vid2_frame_XX.jpg`) e `references/landing-page/hero-light.png` que serão utilizados no Carrossel de Feed, no corte de Reels e na sequência de Stories.

## Output Format

```yaml
campaign_theme: "Título técnico da pauta"
target_persona: "Escritório Proprietário | Escritório Especialista B2B | Ecossistema Dual"
core_mechanisms:
  - module_name: "Nome oficial do módulo"
    pain_eliminated: "Dor manual eliminada"
    proprietary_mechanic: "Como o Maximus Perícias resolve tecnicamente"
    verified_metrics:
      - "Métrica oficial 1"
      - "Métrica oficial 2"
    legal_anchor: "Artigo do CPC / Norma ABNT / LGPD"
visual_evidence_map:
  feed_frames:
    - file: "references/video-frames/vidX_frame_YY.jpg"
      screen_description: "O que aparece na tela"
  reels_cuts:
    - source_video: "Vídeos/GESTÃO DE PERITOS PROPRIETÁRIOS .mp4"
      frames_range: "vid1_frame_XX.jpg a vid1_frame_YY.jpg"
      ui_action: "Ação demonstrada na tela"
  stories_frames:
    - file: "references/video-frames/vidX_frame_ZZ.jpg"
      usage: "Gancho visual ou prova de mecanismo"
objection_busters:
  - objection: "Objeção cética do perito"
    proof: "Fato técnico ou trava de segurança que destrói a objeção"
```

## Output Example

> Use como referência de qualidade e profundidade, não como texto fixo.

```yaml
campaign_theme: "Soberania em Laudos Periciais e Liquidação de Alvarás: Do Caos Manual ao Sistema Operacional"
target_persona: "Ecossistema Dual (Proprietário Titular + Especialista B2B)"
core_mechanisms:
  - module_name: "MAX AI (IBM Docling OCR + Copiloto RAG pgvector)"
    pain_eliminated: "15 a 30 horas gastas lendo autos de mais de 1.000 páginas e formatando laudos manualmente no Word."
    proprietary_mechanic: "Extração semântica via IBM Docling, triagem automática de 100% dos quesitos por origem (Juízo, Autor, Réu, Assistente) e redação nos 10 capítulos da ABNT com citação exata de folhas."
    verified_metrics:
      - "95% de redução operacional na triagem documental"
      - "Menos de 45 minutos para minuta completa nos 10 capítulos ABNT"
      - "Até 90% de queda em pedidos de esclarecimento e impugnações"
      - "< 1.2s de latência RAG com 0% de alucinação"
    legal_anchor: "Art. 473 §§ 1º e 2º do CPC e Normas ABNT NBR 13.752 / 14.653"
  - module_name: "Módulo Financeiro, Alvarás e Calculadora de Retenção Tributária"
    pain_eliminated: "Perda financeira e falta de controle entre arbitramento, depósito judicial e levantamento líquido do alvará."
    proprietary_mechanic: "Pipeline em 4 estágios (1. Arbitrado, 2. Intimação, 3. Depositado, 4. Levantado) somado à calculadora automática de IRRF (7,5%), trava de teto máximo do INSS (R$ 908,86) e ISSQN (2,0%)."
    verified_metrics:
      - "Cálculo instantâneo: R$ 50.000,00 brutos -> R$ 44.341,14 líquidos"
      - "Query Engine BI em < 15ms no Neon PostgreSQL"
    legal_anchor: "Legislação Previdenciária (Teto INSS) e Tributária Municipal/Federal"
  - module_name: "Central do Escritório Especialista B2B e Calculadora CPC/2015"
    pain_eliminated: "Peritos especialistas ociosos esperando nomeação de vara e perda de prazos por erro na contagem de dias úteis."
    proprietary_mechanic: "Recepção de Ordens de Serviço B2B em lote (CSV ou direto), gestão de Quesitos/Impugnações/Pareceres e simulação de Data Fatal Exata com exclusão do recesso forense."
    verified_metrics:
      - "3X mais processos gerenciados sem inflar equipe"
      - "100% de precisão na contagem de dias úteis do Art. 220 do CPC"
    legal_anchor: "Art. 220 do CPC e LGPD (Isolamento Multi-Tenant RLS + AES-256-GCM)"
visual_evidence_map:
  feed_frames:
    - file: "references/video-frames/vid1_frame_50.jpg"
      screen_description: "Painel de Gestão de Honorários & Alvarás Judiciais com Calculadora de Retenção Tributária (R$ 50.000 brutos -> R$ 44.341,14 líquidos)."
    - file: "references/video-frames/vid1_frame_80.jpg"
      screen_description: "Interface do ChatPericial AI com RAG treinado em normas ABNT/CFM/CFC/CREA e jurisprudência STJ/STF."
  reels_cuts:
    - source_video: "Vídeos/GESTÃO DE PERITOS PROPRIETÁRIOS .mp4"
      frames_range: "vid1_frame_30.jpg a vid1_frame_95.jpg"
      ui_action: "Demonstração da Varredura CNJ no Diário de Justiça, Calculadora de Retenção de Alvarás, ChatPericial AI e Cálculos Bancários SELIC."
    - source_video: "Vídeos/GESTÃO DE PERITOS TERCERIZADOS.mp4"
      frames_range: "vid2_frame_02.jpg a vid2_frame_70.jpg"
      ui_action: "Demonstração da Central B2B de Demandas Recebidas, Calculadora de Prazos Art. 220 CPC e Honorários B2B via PIX."
  stories_frames:
    - file: "references/video-frames/vid2_frame_35.jpg"
      usage: "Prova visual da Calculadora de Prazos CPC/2015 com recesso forense."
objection_busters:
  - objection: "A IA pode inventar dados e comprometer minha assinatura pericial perante o juiz."
    proof: "O MAX AI possui a Trava #1 de Soberania Estrita dos Autos: toda afirmação exige citação explícita da folha do processo, recusando qualquer inferência sem prova documental."
```

## Quality Criteria

- [ ] Todos os mecanismos extraídos pertencem comprovadamente ao Maximus Perícias.
- [ ] Há mapeamento explícito de arquivos de imagem reais para Feed, Reels e Stories.
- [ ] Métricas oficiais e artigos legais estão presentes e corretos.

## Veto Conditions

Rejeitar e refazer imediatamente se QUALQUER condição abaixo for verdadeira:
1. O dossiê citar funcionalidades inexistentes na plataforma ou nos vídeos locais.
2. Não houver indicação de arquivos reais da pasta `references/video-frames/` ou `references/landing-page/`.
3. Houver uso de traços longos (`-`) em qualquer campo.
