---
task: "Roteirizar Instagram Reel Vertical (15 a 30s) com Cortes dos Vídeos Oficiais"
order: 1
input: |
  - feed_post: Carrossel de Feed da campanha em output/feed-post.md
  - product_intelligence: Mapa de vídeos e quadros em output/product-intelligence.md
output: |
  - reels_script: Roteiro completo de Reel (15-30s) com cortes de 3-5s, quadros-fonte, capa 1080x1920 e legenda em output/reels-script.md
---

# Roteirizar Instagram Reel Vertical (15 a 30s) com Cortes dos Vídeos Oficiais

Esta tarefa cria o roteiro técnico completo de Instagram Reels (`9:16`, `1080x1920px`), sincronizado com a campanha do Feed e construído sobre os cortes reais de `GESTÃO DE PERITOS PROPRIETÁRIOS .mp4` e `GESTÃO DE PERITOS TERCERIZADOS.mp4`.

## Process

1. **Criar 3 Opções de Gancho de 2 Segundos:** Elaborar 3 aberturas visuais e verbais de impacto imediato (Contraste de Tempo, Choque Financeiro de Alvará e Desafio de Prazo CPC).
2. **Estruturar o Roteiro Cronometrado (15 a 30s) com Cortes de 3 a 5s:** Detalhar `HOOK (0-2s)`, `SETUP (2-5s)`, `DELIVERY (5-24s)` (dividido em 4 cortes rápidos apontando para os arquivos exatos `vid1_frame_XX.jpg` e `vid2_frame_YY.jpg` e seus vídeos-fonte) e `CTA + LOOP (24-28s)`.
3. **Especificar a Capa do Reel (`1080x1920`), Legenda e Direção de Áudio:** Definir o layout da capa vertical (que será renderizada por Davi Designer), a legenda com os primeiros 125 caracteres otimizados e as hashtags da publicação.

## Output Format

```markdown
# Roteiro Técnico de Instagram Reels

## 1. Opções de Gancho (0-2s)
- **Gancho 1:** ...
- **Gancho 2:** ...
- **Gancho 3:** ...

## 2. Script Cronometrado (=== REEL SCRIPT ===)
...

## 3. Especificação da Capa Vertical (1080x1920) para Renderização
- **Badge Superior:** ...
- **Título Principal (Zona Segura):** ...
- **Quadro de Interface Embutido:** ...

## 4. Legenda, Hashtags e Direção de Áudio
...
```

## Output Example

> Use como referência de ritmo, precisão visual e estrutura.

```markdown
# Roteiro Técnico de Instagram Reels

## 1. Opções de Gancho (0-2s)
- **Gancho 1 (Tempo Brutal):** "Você ainda gasta 30 horas no Word para entregar um laudo pericial?"
- **Gancho 2 (Bolso / Alvará):** "R$ 50.000 arbitrados pelo juiz. Quanto o imposto leva se você errar o cálculo do alvará?"
- **Gancho 3 (Ecossistema B2B):** "Carteira de perícias lotada ou esperando nomeação da vara? Olhe esta tela."

## 2. Script Cronometrado

=== REEL SCRIPT ===

HOOK (0-2s):
[Visual]: Abertura em moldura vertical 9:16 Dark Royal (#0B1329) exibindo em zoom o quadro `references/video-frames/vid1_frame_80.jpg` (ChatPericial AI).
[Audio]: "Você ainda gasta 30 horas no Word para digitar um laudo pericial?"
[Text Overlay]: 30 HORAS NO WORD vs. 45 MINUTOS NO SISTEMA OPERACIONAL

SETUP (2-5s):
[Visual]: Corte seco para `references/video-frames/vid1_frame_30.jpg` (Diário de Justiça DJEN do vídeo `GESTÃO DE PERITOS PROPRIETÁRIOS .mp4` com 61 intimações rastreadas).
[Script]: "Enquanto o método manual te prende em PDFs gigantes e planilhas soltas, peritos de elite operam em outra velocidade."
[Text Overlay]: VARREDURA CNJ DIÁRIA NO DJEN + PJE

DELIVERY (5-24s):
[Visual]:
- Corte 1 (05s-09s): Vídeo `GESTÃO DE PERITOS PROPRIETÁRIOS .mp4` (`vid1_frame_80.jpg`) destacando a geração do laudo em 10 capítulos da ABNT com citação de folhas pelo motor IBM Docling e RAG pgvector.
- Corte 2 (09s-14s): Vídeo `GESTÃO DE PERITOS PROPRIETÁRIOS .mp4` (`vid1_frame_50.jpg`) dando zoom na Calculadora de Retenção Tributária: R$ 50.000,00 brutos convertidos em R$ 44.341,14 líquidos após teto do INSS e IRRF.
- Corte 3 (14s-19s): Vídeo `GESTÃO DE PERITOS TERCERIZADOS.mp4` (`vid2_frame_35.jpg`) mostrando a Calculadora de Prazos CPC/2015 simulando dias úteis e recesso forense (Art. 220 do CPC).
- Corte 4 (19s-24s): Vídeo `GESTÃO DE PERITOS TERCERIZADOS.mp4` (`vid2_frame_02.jpg`) exibindo a Central do Escritório Especialista B2B recebendo Ordens de Serviço de Quesitos e Impugnações.
[Script]: "No Maximus Perícias, o motor IBM Docling lê autos de mil páginas reduzindo 95% da triagem e o MAX AI estrutura os 10 capítulos da ABNT citando a folha exata. A calculadora financeira trava o teto do INSS no seu alvará, o motor CPC crava sua data fatal pelo artigo 220 e a Central B2B conecta titulares e especialistas com sigilo LGPD."
[Text Overlays]:
- 05s-09s: IBM DOCLING: -95% DE TRIAGEM + 10 CAPÍTULOS ABNT
- 09s-14s: ALVARÁ AUDITADO: R$ 50.000 BRUTO -> R$ 44.341 LÍQUIDO
- 14s-19s: DATA FATAL EXATA (ART. 220 DO CPC)
- 19s-24s: CENTRAL B2B: TITULARES + ESPECIALISTAS

CTA (24-28s):
[Visual]: Quadro `references/video-frames/vid1_frame_01.jpg` (Tela Institucional Maximus Perícias) com transição de corte que recomeça exatamente no frame do segundo 00:00.
[Script]: "Comente SISTEMA aqui embaixo para acessar a demonstração em pericias.btech.inf.br. Porque a pergunta real é:"
[Text Overlay]: COMENTE "SISTEMA" OU ACESSE O LINK DA BIO

=== CAPTION ===
De 30 horas no Word para 45 minutos no Primeiro Sistema Operacional para Peritos Judiciais.

Veja nos cortes reais da plataforma como o Maximus Perícias integra:
• Leitura de autos volumosos com IBM Docling OCR e MAX AI (Art. 473 CPC)
• Calculadora de Retenção Tributária de Alvarás (IRRF, teto do INSS e ISSQN)
• Calculadora de Prazos CPC/2015 com recesso forense (Art. 220 CPC)
• Central B2B Multi-Tenant para Peritos Proprietários e Especialistas Terceirizados

Comente SISTEMA abaixo para receber o link direto na sua DM ou acesse o link na bio (@maximus.pericias).

=== HASHTAGS ===
#periciajudicial #peritojudicial #assistentetecnico #maximuspericias #engenhariacivil #periciacontabil #periciamedica #periciagrafotecnica #legaltech

=== AUDIO NOTE ===
Locução firme, direta e cadenciada (145 palavras/minuto) sobre trilha instrumental minimalista de pulso tecnológico (baixo volume, -18dB) para destacar a autoridade da voz.

## 3. Especificação da Capa Vertical (1080x1920) para Renderização
- **Arquivo de Saída:** `reel-cover.html` -> `reel-cover.png`
- **Badge Superior:** `SISTEMA OPERACIONAL FORENSE`
- **Título Principal (Zona Segura 3:4):** `30h no Word vs. 45 min no Maximus Perícias`
- **Quadro Embutido:** `references/video-frames/vid1_frame_50.jpg`
```

## Quality Criteria

- [ ] O roteiro dura entre 15 e 30 segundos e possui cortes a cada 3 a 5 segundos.
- [ ] Referencia explicitamente os vídeos locais em `Vídeos/` e os quadros em `references/video-frames/`.
- [ ] Contém `Text Overlays` em todas as etapas, conexão de loop e especificação da Capa `1080x1920`.

## Veto Conditions

Rejeitar e refazer se QUALQUER condição for verdadeira:
1. O roteiro não referenciar os vídeos/quadros reais do Maximus Perícias.
2. Faltarem legendas queimadas (`Text Overlays`) ou houver uso de traços longos (`-`).
