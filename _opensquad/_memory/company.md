# Company Profile: Maximus Perícias

## Visão Geral
- **Nome da Marca:** Maximus Perícias (Bureau Tech Tecnologia da Informação, Recife/PE)
- **Website Oficial:** https://pericias.btech.inf.br
- **Instagram Oficial:** https://www.instagram.com/maximus.pericias/
- **Setor:** LegalTech / ForensicTech SaaS B2B Multi-Tenant
- **Posicionamento Central:** O Primeiro Sistema Operacional completo para Peritos Judiciais, Escritórios Periciais e Assistentes Técnicos.

## Público-Alvo (Dois Modelos de Empresa Pericial em um Único Sistema)
1. **Escritório Proprietário (Titular de Nomeações):** Peritos Oficiais e Escritórios com carteira direta de nomeações em Varas Cíveis, Trabalhistas e Federais. Gerencia prazos e intimações via integrações diretas (PJe, e-SAJ, Eproc, Projudi, MNI e DJEN), lidera equipes internas e emite Ordens de Serviço B2B para terceirizar pareceres complexos.
2. **Escritório Especialista (Consultoria B2B / Perito Terceirizado):** Consultorias técnicas e especialistas setoriais (Engenharia Civil, Medicina Forense, Contábil/Bancária, Grafotécnica, Ambiental, Mecânica e TI) que atuam como Assistentes Técnicos das partes ou atendem demandas de outros escritórios periciais sob regime de prestação de serviços B2B (Recepção de OS B2B, Pareceres e Quesitos Setoriais, Faturamento e Split Direto).

## Métricas e Provas de Valor Oficialmente Verificadas
- **95% de Redução Operacional:** Otimização na extração e leitura de autos volumosos (+1.000 páginas) pelo motor IBM Docling integrado.
- **3X de Faturamento Escalado (+300%):** Peritos gerenciam três vezes mais processos judiciais sem inflar a equipe de assistentes.
- **De 15-30 horas para menos de 45 minutos:** Redução drástica do tempo entre a triagem dos autos e a minuta completa estruturada com citação exata de folhas.
- **Redução de até 90% nas impugnações:** Laudos timbrados no padrão ABNT e Art. 473 do CPC com 100% dos quesitos mapeados por origem.
- **Métricas do MAX AI:** `< 1.2s` de latência RAG, `100%` aderente ao Art. 473 do CPC, `0%` de alucinação (Soberania Estrita dos Autos) e estruturação em `10 Capítulos ABNT`.

## Os 12 Módulos Integrados da Plataforma
1. **Gestão de Processos (Core System):** Visibilidade unificada em qualquer tribunal (PJe, e-SAJ, Eproc, Projudi e MNI).
2. **Diário de Justiça (DJEN):** Monitoramento diário autônomo de publicações e novas nomeações com vinculação ativa.
3. **Prazos CPC:** Cálculo automático de dias úteis periciais com exclusão de feriados e recesso forense (Art. 220 CPC) e alertas graduais (7, 3 e 1 dias).
4. **Cálculos Financeiros e Bancários:** Liquidação de sentenças (Art. 523 CPC), SELIC, IPCA, Amortização e Anatocismo, Revisional, Cartão Consignado RMC/RCC e Superendividamento (Lei 14.181).
5. **Laudos com IA (IBM Docling & Copiloto):** Geração contextual baseada em RAG (`pgvector`) de laudos nos 10 capítulos da ABNT e Art. 473 do CPC.
6. **Cloud Forense (GED):** Armazenamento blindado com OCR e indexação de linha para buscas instantâneas.
7. **Agenda Sync:** Sincronização bidirecional com Google Calendar para vistorias, diligências e entregas de laudo.
8. **Financeiro, Honorários e Alvarás:** Controle em 4 etapas (Arbitrado, Intimação, Depositado, Levantado) e Calculadora de Retenção Tributária (IRRF, INSS com teto máximo e ISSQN).
9. **MAX AI (6 Habilidades Cognitivas e 4 Travas Éticas):** Varredura Documental (IBM Docling), Triagem de Quesitos por Origem, Redação Forense (10 capítulos), Visão Computacional de Patologias (vistorias/fotos), Motor Matemático Auditável e Conformidade Normativa (STJ/STF/CFM/CREA/CFC/CAU).
10. **Kanban de Tarefas:** Delegação de digitação, cálculos e vistorias para a equipe.
11. **Gestão de Acessos (RBAC):** Permissões granulares (Perito Titular, Assistente Técnico, Especialista B2B e Digitador).
12. **Studio BI & Gerador de Relatórios:** Consultas visuais com NLP to Query, Joins 1:N automáticos, execução `< 15ms` no Neon PostgreSQL e 3 modos (Data Grid, Ficha e Dashboard BI).

## Infraestrutura de Segurança Militar e Custódia Forense
- **Criptografia em Nível de Campo (`AES-256-GCM`):** Campos sensíveis cifrados (`enc:v1:iv:tag:cipher`) sob padrão NIST e OWASP SP 800-38D.
- **Autenticação Irreversível (`PBKDF2-SHA512`):** 100.000 iterações com salt individual e zero plaintext.
- **Garantia Anti-Adulteração (`MAC HMAC-SHA256`) e `AuditLog Hash-Chain`:** Cadeia de custódia pericial imutável válida em juízo.
- **Busca Segura Cega (`Blind Index B-Tree`):** Pesquisa de CPF/CNPJ cifrados em `< 5ms` com complexidade $O(\log N)$.
- **Isolamento Multi-Tenant:** RLS no PostgreSQL Neon, Cloudflare R2 e conformidade estrita com o Art. 5º, II da LGPD.

## Identidade Visual Oficial (Design System)
- **Cores Primárias:** Cobalt Blue (`#0047AB` / `#0052CC`), Royal Deep Blue (`#002366` / `#002060` / `#00327D`), Dark Surface (`#0B1329` / `#0F172A`).
- **Cores de Destaque (Autoridade):** Solar Gold (`#FFD700`), Satin Gold (`#C5A021` / `#AA771C`).
- **Superfícies e Contraste:** Canvas Pure (`#FFFFFF` / `#F9F9FF` / `#F8F9FA`), Graphite Black (`#111318`).
- **Gradientes Assinatura:** Liquid Metal (`linear-gradient(135deg, #0047AB 0%, #002366 100%)`) e Corporate Gold (`linear-gradient(135deg, #FFD700 0%, #C5A021 100%)`).
- **Tipografia Oficial:** `Hanken Grotesk` (títulos/display 700-900), `Outfit` (display) e `Inter` (corpo e UI 400-700).

## Filosofia de Branding e Tom de Voz
- **Estilo:** Direto, provocador, minimalista e obcecado por excelência brutal (mentalidade Steve Jobs).
- **Narrativa em 3 Atos:** Origem (o caos artesanal das planilhas e abas do PJe), Conflito (o risco de perder prazos fatais, sofrer impugnações e travar honorários) e Transformação (a soberania operacional de 45 minutos por laudo com o Maximus Perícias).
- **Restrição Gramatical:** Proibido usar traços longos (`-`). Usar pontuação direta, dois-pontos ou frases curtas.
