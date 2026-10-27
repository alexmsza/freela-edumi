# Plano Estratégico de Execução — Projeto Edumi (Prospecção & Outreach)

> **Documento Oficial de Engenharia e Operação de Dados**  
> **Cliente:** Edumi  
> **Planilha Centralizadora Google Sheets:** [`0. Planilha centralizadora`](https://docs.google.com/spreadsheets/d/1hqgfKgMzn00-zV91sFe7a6aMK5ZV47TCvQNfMP8Ksv0/edit)  
> **Status Geral:** **Marco 1 Concluído & Auditado Localmente (0 Bloqueadores)** • Marcos 2, 3 e 4 em Esteira Determinística (`edumi-ops`)

---

## 1. Visão Geral e Contexto Operacional

A **Edumi** possui uma equipe de operação enxuta (~3 pessoas) com foco prioritário em simplicidade, estabilidade e velocidade de disparo de mala direta / outreach.  
O desafio principal diagnosticado pela liderança da Edumi é a dispersão histórica de planilhas: *"toda vez alguém cria um arquivo novo"*.

A meta deste projeto é unificar, higienizar e enriquecer todos os dados em uma **Única Planilha Centralizadora (Flat Table)** no Google Sheets, dividida em 5 abas padronizadas, sustentada localmente pela esteira determinística `edumi-ops` (`uv run edumi ...`) com auditoria DNS MX, bloqueio de bounces e rastreabilidade de fonte (`source_url`).

> [!IMPORTANT]
> **Regra de Governança e Integridade:**
> 1. **Sincronização Não-Destrutiva:** A planilha central online ([`0. Planilha centralizadora`](https://docs.google.com/spreadsheets/d/1hqgfKgMzn00-zV91sFe7a6aMK5ZV47TCvQNfMP8Ksv0/edit)) foi alimentada (`append`) com todos os registros higienizados sem apagar nenhuma estrutura ou planilha anterior.
> 2. **Zero Alucinação / Zero Dados Sintéticos:** E-mails adivinhados, domínios sem registro MX/A ativo e perfis sociais não verificados são bloqueados automaticamente por `uv run edumi audit`.

---

## 2. Padrão de Schemas (5 Abas Oficiais da Gabi)

Todas as tabelas seguem o padrão estrito *Flat Table* (linha por linha, células atômicas, sem células mescladas, compatível com importação direta CSV / Sheets):

### Aba 1: `universidades`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome_faculdade` | Texto | Nome oficial por extenso da instituição e campus |
| `nome_departamento` | Texto | Setor legível (Reitoria, Decanato, Diretoria, Secretaria ou Coordenação) |
| `email` | Texto | E-mail funcional higienizado (minúsculo, RFC-válido, DNS MX ativo, 0 bounces) |
| `uf` | Sigla (2 letras) | Unidade Federativa oficial (`DF`, `GO`, `SP`, etc. — proibido `BR` ou texto livre) |

### Aba 2: `artistas`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | Texto | Nome real do artista, coletivo ou estúdio |
| `arroba` | Texto | `@` verificada no Instagram |
| `quantidade_seguidores`| Número | Contagem real verificada (proibida estimativa sintética) |
| `tipo` | Texto | Linguagem artística (Ilustração, Gravura, Zine, HQ, Serigrafia, Cerâmica) |
| `uf` | Sigla | Estado confirmado na bio/portfólio (`DF`) |

### Aba 3: `influenciadores`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | Texto | Nome real do criador ou canal |
| `arroba` | Texto | `@` verificada no Instagram/TikTok |
| `quantidade_seguidores`| Número | Contagem real verificada |
| `tipo` | Texto | Nicho (Educação, Vida Universitária, PAS-UnB, Vestibular, Tech) |
| `uf` | Sigla | UF confirmada (`DF`, `GO` ou `PE`) |

### Aba 4: `midias`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | Texto | Nome do portal, jornal, rádio ou emissora |
| `link` | URL | Endereço do site ou perfil institucional |
| `email` | Texto | E-mail atômico de pauta / redação (1 endereço por linha) |
| `telefone` | Texto | Telefone ou WhatsApp higienizado |
| `uf` | Sigla | Estado de abrangência (2 letras) |
| `obs` | Texto | Editoria / observações |

### Aba 5: `parceiros`
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `nome` | Texto | Nome da entidade, canal estudantil, empresa júnior ou parceiro |
| `link` | URL | Perfil no Instagram, site ou LinkedIn |
| `email` | Texto | E-mail institucional (quando disponível) |
| `telefone` | Texto | WhatsApp / telefone higienizado |
| `uf` | Sigla | UF de 2 letras (ou vazio quando nacional sem sede fixa) |
| `obs` | Texto | Histórico de contato / status extraído das bases legadas |

---

## 3. Cronograma Executivo e Status Real dos Marcos

```
[27/10 - 23:00]  ──► MARCO 1: DF (Universidades, IFB, Públicas Distritais e Privadas) ──► [CONCLUÍDO & AUDITADO LOCALMENTE]
[31/10 - 23:00]  ──► MARCO 2: Resto do Brasil (Base Legada Higienizada + Expansão IES) ─► [BASE LEGADA PRONTA (1.005) / EXPANSÃO AGENDADA]
[04/11 - 23:00]  ──► MARCO 3: Artistas do DF (@edicoesmotim 2025/2026 Verificados) ─────► [AGENDADO — DADOS SINTÉTICOS EXPURGADOS]
[08/11 - 23:00]  ──► MARCO 4: Influenciadores (DF, GO, PE Verificados) + Fechamento ────► [AGENDADO — DADOS SINTÉTICOS EXPURGADOS]
```

### Detalhamento por Marco

#### 🎓 Marco 1: Distrito Federal — Universidades, IFB e Faculdades (Prazo: 27/10 às 23:00)
- **Status:** **CONCLUÍDO & AUDITADO LOCALMENTE (`total_blockers = 0`, 215 Contatos Verificados)**
- **Arquivo de Entrega Específica:** [`csv_exports/01_universidades_DF_marco1.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/01_universidades_DF_marco1.csv)
- **Relatório de Auditoria:** [`reports/AUDITORIA_QUALIDADE.md`](file:///C:/Users/alexk/Desktop/freela-edumi/reports/AUDITORIA_QUALIDADE.md)
- **Escopo Verificado no DF (215 registros com DNS MX/A ativo e 0 bounces):**
  1. **Universidades Federais & Escolas Superiores Federais no DF (91 contatos):**
     - **Universidade de Brasília (UnB — 89 contatos):** Gabinete da Reitoria, Ouvidoria, SAA, SECOM, todos os 8 Decanatos (`DEG`, `DPG`, `DEX`, `DAC`, `DAF`, `DGP`, `DPI`, `DPO`), Faculdades e Campi (`Darcy Ribeiro`, `FGA/FCTE Gama`, `FCE/FCTS Ceilândia`, `FUP Planaltina`, `FT`, `FACE`, `FD`, `FM`, `FAU`, `FAC`, `FAV`, `FCI`, `FE`), Institutos (`CIC/IE`, `MAT`, `IF`, `IQ`, `IB`, `IdA`, `IL`, `IP`, `IPOL`, `IREL`, `ICS`), Centros (`CDT`, `CDS`, `CEAM`), DCE e Centros Acadêmicos de Engenharia.
     - **ENAP (1 contato):** Secretaria Escolar de Pós-Graduação e Mestrado (`secretariaescolar@enap.gov.br`).
     - **Escola de Governo Fiocruz Brasília (1 contato):** Secretaria Acadêmica (`secad@fiocruz.br`).
  2. **Instituto Federal de Brasília (IFB — 62 contatos reais verificados):**
     - **Reitoria (12 setores):** Gabinete Digital, Ouvidoria, Protocolo Central, Processo Seletivo Geral, `PREN`, `PREX`, `PRPI`, `PRAF`, `DRPE`, `DICOM`, `DTIC` e `CPAPE`.
     - **Todos os 10 Campi do DF (50 setores):** `Brasília`, `Ceilândia`, `Estrutural`, `Gama`, `Planaltina`, `Recanto das Emas`, `Riacho Fundo`, `Samambaia`, `São Sebastião` e `Taguatinga` (Chefias de Gabinete, Diretorias de Ensino `DREP`, Coordenações de Registro Acadêmico `CDRA`, Assistência Estudantil `CDAE` e Comissões de Processo Seletivo com a nomenclatura real `<setor>.<campus>@ifb.edu.br`).
  3. **Públicas Distritais — GDF (23 contatos raspados ao vivo via HTTP 200):**
     - **Escola Superior de Ciências da Saúde — ESCS (16 contatos):** Direção-Geral, `SAA`, `SAD`, Coordenações, Secretarias e Gerências de Medicina (`CCM`) e Enfermagem (`CCE`) e Biblioteca Samambaia. *(Nota técnica: o endereço com erro de digitação `escs.ed.br` publicado na página da ESCS foi automaticamente barrado pelo gate DNS).*
     - **FEPECS (7 contatos):** Diretoria Executiva, Coordenação de Processos Seletivos (`CPS`), Comitê de Ética (`CEP`), `CPLAGE`, Biblioteca Central, `ASCOM` e Ouvidoria.
  4. **Privadas, Confessionais e Sistema S no DF (39 contatos em 15 instituições):**
     - `UniProjeção` (6), `CEUB / UniCEUB` (5), `Faculdade Republicana` (4), `SENAI-DF / Sistema FIBRA` (4), `Centro Universitário IESB` (3), `Faculdade Senac-DF` (3), `Universidade Católica de Brasília — UCB` (3), `IDP` (2), `FGV Brasília — EPPG & Educação Executiva` (2), `UDF` (1), `UNICEPLAC Gama` (1), `UNIEURO` (1), `UniLS` (1), `UniProcessus` (1), `Mackenzie Brasília — FPMB` (1) e `Faculdade CNA` (1).

#### 🌍 Marco 2: Resto do Brasil — Universidades e IFs (Prazo: 31/10 às 23:00)
- **Status:** **BASE LEGADA HIGIENIZADA (1.005 contatos fora do DF; Total Nacional Atual: 1.220 em todas as 27 UFs)**
- **Arquivo de Entrega Específica:** [`csv_exports/01_universidades.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/01_universidades.csv)
- **Já Executado:**
  - Extração determinística das 7 planilhas em `doc/`, expurgo dos 22 bounces históricos, quarentena de 31 domínios expirados (`NXDOMAIN` documentados em [`reports/quarantined_dead_domains.json`](file:///C:/Users/alexk/Desktop/freela-edumi/reports/quarantined_dead_domains.json)), normalização de 100% das UFs (eliminação de `BR` e `- novas`) e recuperação de **219 mídias atômicas** + **523 parceiros**.
- **Próximo Passo do Marco 2:** Expansão web verificada via `uv run edumi scrape-ies` para novos portais `.edu.br` estaduais/federais/IFs do restante do país até 31/10.

#### 🎨 Marco 3: Artistas do DF (@edicoesmotim 2025/2026) (Prazo: 04/11 às 23:00)
- **Status:** **AGENDADO (`csv_exports/02_artistas.csv` limpo; 50 linhas antigas não verificadas removidas)**
- **Execução:** Extração nominal dos expositores reais de 2025/2026 da `@edicoesmotim` e validação individual via `uv run edumi verify-social` (confirmando existência do `@`, seguidores reais e vínculo com o DF).

#### 📱 Marco 4: Influenciadores (DF, GO e PE) (Prazo: 08/11 às 23:00)
- **Status:** **AGENDADO (`csv_exports/03_influenciadores.csv` limpo; 36 `@` alucinados anteriores removidos)**
- **Execução:** Curadoria e verificação HTTP/perfil real de criadores universitários, ENEM/PAS e educação em `DF`, `GO` e `PE`, seguida de consolidação final.

---

## 4. Comandos da Esteira de Engenharia (`edumi-ops`)

```powershell
# 1. Reprocessar e higienizar as 7 planilhas brutas em doc/
uv run edumi ingest-legacy

# 2. Executar coleta institucional verificada (.edu.br / .br) + checagem DNS MX
uv run edumi scrape-ies

# 3. Compilar CSVs oficiais, planilhas .xlsx da Gabi e data_payload.js (com trava de bloqueio)
uv run edumi build

# 4. Executar auditoria forense independente (Schema + Bounces + DNS MX + Proveniência)
uv run edumi audit
```

---

## 5. Procedimento de Segurança para Descarte das Bases Antigas

1. **Backup Frio Imutável:** O diretório `doc/` preserva intactos os 7 arquivos `.xlsx` originais da cliente.
2. **Rastreabilidade de Quarentena:** Domínios expirados e bounces descartados ficam documentados em `reports/` para eventual conferência da Edumi.
3. **Sincronização Controlada:** O arquivamento da pasta antiga no Google Drive da cliente só deve ocorrer após aprovação dos marcos na planilha centralizadora oficial.
