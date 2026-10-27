# Plano Estratégico de Execução — Projeto Edumi (Prospecção & Outreach)

> **Documento Oficial de Engenharia e Operação de Dados**  
> **Cliente:** Edumi  
> **Planilha Centralizadora Google Sheets:** [`0. Planilha centralizadora`](https://docs.google.com/spreadsheets/d/1hqgfKgMzn00-zV91sFe7a6aMK5ZV47TCvQNfMP8Ksv0/edit)  
> **Status Geral:** Em Execução (Marcos 1 e 2 Consolidados Localmente)

---

## 1. Visão Geral e Contexto Operacional

A **Edumi** possui uma equipe de operação enxuta (~3 pessoas) com foco prioritário em simplicidade, estabilidade e velocidade de disparo de mala direta / outreach. 
O desafio principal diagnosticado pela liderança da Edumi é a dispersão histórica de planilhas: *"toda vez alguém cria um arquivo novo"*. 

Este projeto tem como meta unificar, higienizar e enriquecer todos os dados em uma **Única Planilha Centralizadora (Flat Table)** no Google Sheets, dividida em 5 abas padronizadas, além de fornecer ferramentas locais para conferência antes da sincronização em nuvem.

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

## 3. Cronograma Executivo e Marcos de Entrega

```
[27/10 - 23:00]  ──► MARCO 1: DF (Universidades e IFs Públicos e Privados)
[31/10 - 23:00]  ──► MARCO 2: Resto do Brasil (Goiás + Demais Estados)
[04/11 - 23:00]  ──► MARCO 3: Artistas do DF (@edicoesmotim 2025/2026)
[08/11 - 23:00]  ──► MARCO 4: Influencers (DF, GO, PE) + Higienização Final
```

### Detalhamento por Marco

#### 🎓 Marco 1: Distrito Federal — Faculdades e IFs (Prazo: 27/10 às 23:00)
- **Status:** **CONCLUÍDO LOCALMENTE (188 Contatos)**
- **Escopo:**
  1. **UnB (75 contatos):** Reitoria, 7 Decanatos (Extensão, Graduação, Pós, etc.), Faculdades (FAC, FT, FGA, FCE, FUP, Medicina, Direito, FACE), Institutos (Artes, Biologia, Química, Física, etc.) e Departamentos de Exatas.
  2. **IFB (47 contatos):** Reitoria + 10 campi mapeados (Brasília/Asa Norte, Ceilândia, Estrutural, Gama, Planaltina, Recanto das Emas, Riacho Fundo, Samambaia, São Sebastião e Taguatinga).
  3. **Privadas e Distrital (66 contatos):** UCB, UniCEUB, IESB, UniEuro, UniProjeção, IDP, IBMEC DF, UNICEPLAC, ESCS (FEPECS), Mackenzie, Anhanguera e Estácio.

#### 🌍 Marco 2: Resto do Brasil — Faculdades e IFs (Prazo: 31/10 às 23:00)
- **Status:** **CONCLUÍDO LOCALMENTE (936 Contatos adicionais)**
- **Escopo:**
  1. **Goiás (170 contatos):** Ingestão integral da base V4 com UFG, PUC-GO, UEG, IFG, IF Goiano, UniRV, Senac, Senai e faculdades privadas.
  2. **Sudeste & Demais Estados (766 contatos):** Federais, estaduais e IFs de SP, RJ, MG, Sul e Nordeste.
  3. **Higienização:** Inferência automática de UF por domínio e remoção estrita de e-mails rejeitados (*bounce*).

#### 🎨 Marco 3: Artistas do DF (@edicoesmotim) (Prazo: 04/11 às 23:00)
- **Status:** **EM PESQUISA ATIVA**
- **Escopo:**
  - Varredura das edições N19, N20, N21, N22 e N23 (2025 e 2026) da Feira Motim no SESI Lab e no CONIC.
  - Filtro estrito de criadores residentes ou atuantes no DF.
  - Coleta: `nome`, `arroba`, `quantidade_seguidores`, `tipo` e `uf = 'DF'`.

#### 📱 Marco 4: Influenciadores (DF, GO e PE) (Prazo: 08/11 às 23:00)
- **Status:** **PLANEJADO**
- **Escopo:**
  - Triagem de criadores reais na base legada de 399 instas.
  - Prospecção de novos influenciadores universitários, vestibulandos e de tech nos 3 estados prioritários.
  - Enriquecimento com número de seguidores atualizado e nicho.

---

## 4. Procedimento de Segurança para Descarte das Bases Antigas

A Gabi solicitou a limpeza das planilhas antigas no Google Drive após a consolidação:
1. **Passo 1 (Backup Frio):** O diretório `doc/` deste repositório preserva 100% dos arquivos originais brutos.
2. **Passo 2 (Batimento de Linhas):** Nenhuma planilha antiga será apagada sem a conferência quantitativa de que todos os registros válidos foram transferidos.
3. **Passo 3 (Sincronização & Confirmação):** Apenas após a confirmação final da Gabi na planilha centralizadora os arquivos legados serão arquivados.
