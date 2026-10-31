# Foco de Pesquisa: Tema 3 (Rede B2B, Gestão de Equipe e Prazos Art. 220 CPC)

## 1. Contexto Forense & Problema do Perito
- **O risco fatal do perito:** Perda de prazo processual resulta em destituição do cargo, comunicação à Corregedoria do Tribunal e até penalidade de suspensão de 1 a 5 anos (Art. 468, II, e Art. 477 do CPC).
- **A armadilha da contagem:** Desde o CPC/2015, prazos processuais são computados exclusivamente em **dias úteis** (Art. 220 e Art. 219 do CPC). Feriados municipais, estaduais, pontos facultativos dos Tribunais de Justiça e o Recesso Forense (20 de dezembro a 20 de janeiro) suspendem prazos. Planilhas Excel comuns e agendas do Google erram feriados locais, criando falso sentimento de segurança.
- **O gargalo do crescimento solo:** Peritos que recebem 30, 50 ou 100 nomeações por mês não conseguem executar todas as vistorias e laudos sozinhos. Precisam delegar a assistentes técnicos, redatores e calculistas parceiros. Sem controle rigoroso de acesso (RBAC), compartilhar pastas no Google Drive ou senhas de tribunais gera vazamento de dados judiciais protegidos por segredo de justiça (violação da LGPD) e descontrole total sobre quem está fazendo o que.

## 2. Solução Tecnológica Maximus Perícias
- **Motor de Prazos Art. 220 CPC:** Cálculo em tempo real dos dias úteis, sincronizado com o calendário de feriados nacionais, estaduais e dos Tribunais (TJSP, TJRJ, TRT, TRF, etc.), contemplando automaticamente o recesso forense de 20/12 a 20/01.
- **Kanban Forense 5F:** Visualização ágil do fluxo processual em 5 estágios: 1. Aceitação & Proposta, 2. Agendamento de Vistoria, 3. Redação Técnica (MAX AI), 4. Revisão & Impugnações, 5. Conclusão & Alvará.
- **Rede B2B & Delegação em Lote:** Importação de centenas de processos via CSV/planilha ou sincronização DJEN/PJe e atribuição imediata a peritos assistentes ou parceiros de bancada.
- **Segurança RBAC (Role-Based Access Control):** Cada integrante da equipe tem perfil restrito (Perito Titular, Assistente Técnico de Vistoria, Calculista, Revisor, Apoio Financeiro), acessando unicamente os autos e campos estritamente necessários, com log de auditoria forense de todas as ações.
- **Prorrogação Inteligente com IA:** Caso surja imprevisto, o sistema gera minuta automática fundamentada de pedido de dilação de prazo nos termos do Art. 477, § 1º do CPC, pronta para assinatura e protocolo.

