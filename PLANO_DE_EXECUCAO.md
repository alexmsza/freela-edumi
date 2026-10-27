# Plano Estratégico de Execução — Projeto Edumi (Prospecção & Outreach)

> **Documento Oficial de Engenharia e Operação de Dados**  
> **Cliente:** Edumi  
> **Planilha Centralizadora Google Sheets:** [`0. Planilha centralizadora`](https://docs.google.com/spreadsheets/d/1hqgfKgMzn00-zV91sFe7a6aMK5ZV47TCvQNfMP8Ksv0/edit)  
> **Status Geral:** Fase 1 Concluída Localmente (5 Abas Consolidadas e Populadas em Formato Oficial)

---

## 1. Visão Geral e Contexto Operacional

A **Edumi** possui uma equipe de operação enxuta (~3 pessoas) com foco prioritário em simplicidade, estabilidade e velocidade de disparo de mala direta / outreach. 
O desafio principal diagnosticado pela liderança da Edumi é a dispersão histórica de planilhas: *"toda vez alguém cria um arquivo novo"*. 

A meta deste projeto é unificar, higienizar e enriquecer todos os dados em uma **Única Planilha Centralizadora (Flat Table)** no Google Sheets, dividida em 5 abas padronizadas, além de fornecer ferramentas locais para conferência antes da sincronização em nuvem.

> [!IMPORTANT]
> **Regra de Transição:** Conforme instrução do usuário, **nenhum dado foi enviado ao Google Sheets online ainda**. Toda a centralização, validação e raspagem foi realizada localmente nas planilhas `.xlsx`, nos arquivos `.csv` e no `data_payload.js` dos dashboards. O upload para o Google Sheets oficial só ocorrerá após a aprovação explícita.

---

## 2. Padrão de Schemas (5 Abas Oficiais)

Todas as tabelas foram estruturadas no padrão estrito *Flat Table* (linha por linha, sem células mescladas, compatível com importação CSV / Sheets):

### Aba 1: `universidades`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome_faculdade` | Texto | Nome por extenso da instituição e campus |
| `nome_departamento` | Texto | Setor, Reitoria, Decanato, Diretoria ou Coordenação |
| `email` | Texto | E-mail funcional higienizado (minúsculo, sem espaços) |
| `uf` | Sigla (2 letras) | Unidade Federativa (DF, GO, SP, etc.) |

### Aba 2: `artistas`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | Texto | Nome do artista, coletivo ou marca |
| `arroba` | Texto | @ do perfil no Instagram |
| `quantidade_seguidores`| Número | Volume de seguidores no Instagram |
| `tipo` | Texto | Linguagem artística (Ilustração, Gravura, Zine, HQ, Música) |
| `uf` | Sigla | Estado de residência/atuação (DF) |

### Aba 3: `influenciadores`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | Texto | Nome do criador ou canal |
| `arroba` | Texto | @ do perfil no Instagram/TikTok |
| `quantidade_seguidores`| Número | Volume de seguidores |
| `tipo` | Texto | Nicho (Educação, Vida Universitária, PAS-UnB, Tech) |
| `uf` | Sigla | UF de atuação (DF, GO ou PE) |

### Aba 4: `midias`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | Texto | Nome do portal, jornal ou emissora |
| `link` | URL | Endereço do site ou rede social |
| `email` | Texto | E-mail de pauta / redação |
| `telefone` | Texto | Telefone ou WhatsApp de contato |
| `uf` | Sigla | Estado de abrangência |
| `obs` | Texto | Notas e editoria |

### Aba 5: `parceiros`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | Texto | Nome da entidade, empresa júnior ou parceiro |
| `link` | URL | Perfil no Instagram ou LinkedIn |
| `email` | Texto | E-mail institucional |
| `telefone` | Texto | WhatsApp direto da pessoa de contato |
| `uf` | Sigla | Estado ou abrangência nacional (BR) |
| `obs` | Texto | Histórico de contato / status |

---

## 3. Cronograma Executivo e Status dos Marcos de Entrega

```
[27/10 - 23:00]  ──► MARCO 1: DF (Universidades e IFs Públicos e Privados) ───► [CONCLUÍDO LOCALMENTE]
[31/10 - 23:00]  ──► MARCO 2: Resto do Brasil (Goiás + Demais Estados) ────────► [CONCLUÍDO LOCALMENTE]
[04/11 - 23:00]  ──► MARCO 3: Artistas do DF (@edicoesmotim 2025/2026) ────────► [CONCLUÍDO LOCALMENTE]
[08/11 - 23:00]  ──► MARCO 4: Influencers (DF, GO, PE) + Higienização Final ───► [CONCLUÍDO LOCALMENTE]
```

### Detalhamento por Marco

#### 🎓 Marco 1: Distrito Federal — Faculdades e IFs (Prazo: 27/10 às 23:00)
- **Status:** **CONCLUÍDO LOCALMENTE (223 Contatos Consolidados)**
- **Arquivo de Entrega Específica:** [`csv_exports/01_universidades_DF_marco1.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/01_universidades_DF_marco1.csv)
- **Escopo Mapeado no DF:**
  1. **Universidade de Brasília (UnB — 95 contatos):** Reitoria, todos os 7 Decanatos (DEX, DEG, DPG, DAC, DPO, DAF, DGP), Faculdades (FAU, FAC, FT, FGA Gama, FCE Ceilândia, FUP Planaltina, Medicina, Direito, FACE), Institutos (Artes, Biologia, Química, Física, etc.) e Departamentos Acadêmicos (Ciência da Computação, Engenharias, Matemática).
  2. **Instituto Federal de Brasília (IFB — 58 contatos):** Reitoria + os **10 campi do DF** (Brasília/Asa Norte, Ceilândia, Estrutural, Gama, Planaltina, Recanto das Emas, Riacho Fundo, Samambaia, São Sebastião e Taguatinga) com Direção-Geral, Ensino, Registro Escolar, Extensão e Pesquisa de cada unidade.
  3. **Pública Distrital (5 contatos):** Escola Superior de Ciências da Saúde (ESCS / FEPECS) — Direção, Secretaria Acadêmica, Medicina, Enfermagem e Pós-Graduação.
  4. **Privadas, Confessionais e Sistema S (65 contatos):**
     - Centro Universitário do Distrito Federal (UDF — 7 contatos)
     - Universidade Católica de Brasília (UCB — 7 contatos)
     - Centro Universitário de Brasília (UniCEUB — 7 contatos)
     - Centro Universitário IESB (6 contatos)
     - Centro Universitário Planalto do DF / UNIP Brasília (UNIPLAN — 4 contatos)
     - Centro Universitário EuroAmericano (UniEuro — 3 contatos)
     - Centro Universitário Projeção (UniProjeção — 3 contatos)
     - Instituto Brasileiro de Ensino, Desenv. e Pesquisa (IDP — 3 contatos)
     - Centro Universitário UNICEPLAC Gama (3 contatos)
     - Faculdade Republicana Asa Norte (3 contatos)
     - Faculdade Senac Distrito Federal (3 contatos)
     - Faculdade JK Brasília (3 contatos)
     - Faculdade SENAI de Tecnologia DF (2 contatos)
     - IBMEC Brasília (2 contatos)
     - Faculdade Presbiteriana Mackenzie Brasília (2 contatos)
     - Centro Universitário Estácio de Brasília (2 contatos)
     - Faculdade Anhanguera Brasília (2 contatos)
     - Faculdade Mauá de Brasília (1 contato)
     - Centro Universitário UNINTER Polo Brasília (1 contato)

#### 🌍 Marco 2: Resto do Brasil — Faculdades e IFs (Prazo: 31/10 às 23:00)
- **Status:** **CONCLUÍDO LOCALMENTE (935 Contatos adicionais; Total Brasil: 1.158)**
- **Arquivo de Entrega Específica:** [`csv_exports/01_universidades.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/01_universidades.csv)
- **Escopo:**
  1. **Goiás (170 contatos):** Ingestão integral da base V4 com UFG, PUC-GO, UEG, IFG, IF Goiano, UniRV, Senac, Senai e faculdades privadas.
  2. **Sudeste & Demais Estados (765 contatos):** Federais, estaduais e IFs de SP, RJ, MG, Sul e Nordeste (212 IFs no total nacional).
  3. **Higienização:** Inferência automática de UF por domínio e remoção de e-mails de bounce.

#### 🎨 Marco 3: Artistas do DF (@edicoesmotim 2025/2026) (Prazo: 04/11 às 23:00)
- **Status:** **CONCLUÍDO LOCALMENTE (20 Artistas e Coletivos do DF Mapeados)**
- **Arquivo de Entrega Específica:** [`csv_exports/02_artistas.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/02_artistas.csv)
- **Escopo:**
  - Varredura e raspagem das edições 2025 e 2026 da Feira Motim no SESI Lab, Galeria dos Estados e CONIC (N19, N20, N21, N22 e N23).
  - Seleção criteriosa de artistas locais do DF com perfil ativo, volume de seguidores e categorização por linguagem (HQ, serigrafia, gravura, lambe-lambe, zine, ilustração, arte-educação).

#### 📱 Marco 4: Influenciadores (DF, GO e PE) (Prazo: 08/11 às 23:00)
- **Status:** **CONCLUÍDO LOCALMENTE (17 Criadores Mapeados)**
- **Arquivo de Entrega Específica:** [`csv_exports/03_influenciadores.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/03_influenciadores.csv)
- **Escopo:**
  - Mapeamento segmentado por nicho universitário, pré-vestibular/ENEM, vida acadêmica e ecossistema de tecnologia nos 3 estados prioritários solicitados (DF, GO e PE).

---

## 4. Procedimento de Segurança para Descarte das Bases Antigas

A Gabi solicitou a limpeza das planilhas antigas no Google Drive após a consolidação:
1. **Passo 1 (Backup Frio):** O diretório `doc/` deste repositório preserva 100% dos arquivos originais brutos.
2. **Passo 2 (Batimento de Linhas):** Nenhuma planilha antiga será apagada sem a conferência quantitativa de que todos os registros válidos foram transferidos.
3. **Passo 3 (Sincronização & Confirmação):** Apenas após a confirmação final da Gabi na planilha centralizadora os arquivos legados serão arquivados.
