# Foco de Pesquisa: Tema 5 (Automação PJe/MNI & Monitoramento DJEN)

## 1. Contexto Forense & Problema do Perito
- **O inferno dos portais judiciais:** No Brasil, o Poder Judiciário é fragmentado em dezenas de sistemas distintos: PJe (Processo Judicial Eletrônico), e-SAJ (Tribunal de Justiça de SP, SC, etc.), Projudi, Eproc e Creta. O perito precisa acessar individualmente cada portal para verificar se houve nomeação, intimação de honorários ou quesitos das partes.
- **O colapso dos Diários Oficiais em PDF:** Com a implantação do DJEN (Diário de Justiça Eletrônico Nacional - Resolução CNJ nº 455/2022), todas as publicações judiciais dos tribunais brasileiros passaram a ser centralizadas. No entanto, vasculhar diários oficiais de milhares de páginas diariamente em busca do próprio nome ou número de registro profissional é um processo manual, exaustivo e vulnerável a falhas.
- **Download Fragmentado e Lento:** Baixar processos judiciais com mais de 1.000 páginas em portais lentos resulta em arquivos PDF divididos em dezenas de partes de 10MB ou arquivos ZIP corrompidos. O perito gasta horas apenas organizando os arquivos no computador antes de começar a ler o processo.

## 2. Solução Tecnológica Maximus Perícias
- **Monitoramento Centralizado do DJEN:** Varredura diária automatizada de publicações judiciais em todos os tribunais do país. O sistema detecta instantaneamente o nome ou documento do perito entre 61+ intimações diárias, classificando por comarca, vara e natureza do despacho.
- **Integração MNI / PJe via mTLS (Certificado Digital A3/A4):** Conexão direta com a API do Modelo Nacional de Interoperabilidade (MNI) do CNJ utilizando autenticação segura mTLS por certificado digital (token físico A3 ou nuvem A4).
- **Importação de Autos em 1 Clique:** O perito digita o número CNJ do processo (formato `NNNNNNN-DD.AAAA.J.TR.OOOO`) e o sistema sincroniza a íntegra dos autos diretamente dos servidores do tribunal, sem necessidade de download manual.
- **Triagem Imediata via Docling OCR:** Ao importar os autos, o motor de inteligência artificial já indexa automaticamente despacho de nomeação, quesitos das partes, contestação, inicial e documentos técnicos, gerando o resumo executivo da perícia em segundos.

