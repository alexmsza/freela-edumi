# Edumi — Centralizador de Prospecção & Engenharia de Dados

Esteira determinística de consolidação, higienização, auditoria DNS MX, visualização e exportação de dados para campanhas de prospecção acadêmica, imprensa, parcerias e influenciadores da **Edumi**.

---

## 🎯 Objetivo do Projeto

Unificar o acervo histórico disperso da Edumi (`doc/*.xlsx`) e enriquecê-lo com contatos institucionais verificados em uma **única planilha centralizadora padronizada (Flat Table)** compatível com o Google Sheets oficial da cliente ([`0. Planilha centralizadora`](https://docs.google.com/spreadsheets/d/1hqgfKgMzn00-zV91sFe7a6aMK5ZV47TCvQNfMP8Ksv0/edit)), com **zero bounces, zero domínios mortos e zero dados sintéticos**.

O projeto inclui:
1. **CLI de Engenharia de Dados (`edumi-ops` via `uv`):** Extração determinística do acervo legado, raspagem institucional com rastreabilidade (`source_url`), resolução concorrente de DNS MX/A e trava de auditoria (`total_blockers == 0`).
2. **Aplicações Web Locais Autônomas (`app.html`, `index.html` e `dashboard.html`):** Gestão tabular e dashboard analítico interativo consumindo `data_payload.js` versionado por hash SHA-256.

---

## 📊 Estrutura Atual Auditada (5 Abas Oficiais)

Todas as abas seguem rigorosamente as colunas de [`0. Planilha centralizadora.xlsx`](file:///C:/Users/alexk/Desktop/freela-edumi/0.%20Planilha%20centralizadora.xlsx):

1. **`universidades`**: `nome_faculdade`, `nome_departamento`, `email`, `uf`  
   - **Total Nacional Auditado:** **1.220 contatos** distribuídos nas **27 UFs** (`215 DF`, `172 GO` e `833` nos demais 25 estados), com **0 bounces** e **100% de domínios com DNS ativo**.
   - **Recorte Marco 1 (Distrito Federal):** **215 contatos verificados** em [`csv_exports/01_universidades_DF_marco1.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/01_universidades_DF_marco1.csv) (`UnB`: 89, `IFB Reitoria + 10 Campi`: 62, `ESCS + FEPECS`: 23, `ENAP + Fiocruz Brasília`: 2, e 15 instituições privadas/Sistema S: 39).
2. **`artistas`**: `nome`, `arroba`, `quantidade_seguidores`, `tipo`, `uf`  
   - *0 registros no momento (dados sintéticos anteriores expurgados; coleta verificada `@edicoesmotim` agendada para o **Marco 3 — 04/11**).*
3. **`influenciadores`**: `nome`, `arroba`, `quantidade_seguidores`, `tipo`, `uf`  
   - *0 registros no momento (perfis alucinados anteriores expurgados; coleta verificada DF/GO/PE agendada para o **Marco 4 — 08/11**).*
4. **`midias`**: `nome`, `link`, `email`, `telefone`, `uf`, `obs`  
   - **219 contatos atômicos de imprensa** em **11 UFs** (células multi-email desmembradas individualmente e higienizadas).
5. **`parceiros`**: `nome`, `link`, `email`, `telefone`, `uf`, `obs`  
   - **523 canais estudantis, empresas juniores e parceiros** recuperados e padronizados das planilhas legadas.

---

## 🛠️ CLI de Operação e Auditoria (`uv`)

Requisitos: Python 3.11+ gerenciado via [`uv`](https://docs.astral.sh/uv/).

```powershell
# Instalar/sincronizar ambiente virtual (.venv) a partir do uv.lock
uv sync

# 1. Extrair e higienizar as 7 planilhas originais de doc/ -> data_staged/
uv run edumi ingest-legacy

# 2. Coletar e validar contatos institucionais (.edu.br / .br) -> data_verified/ies_scraped.json
uv run edumi scrape-ies

# 3. Compilar CSVs, planilhas .xlsx e data_payload.js (aborta se houver qualquer bloqueador)
uv run edumi build

# 4. Rodar auditoria de qualidade e gerar reports/AUDITORIA_QUALIDADE.md
uv run edumi audit
```

---

## 🖥️ Aplicações Web Locais (`app.html` & `dashboard.html`)

Basta abrir no navegador (sem necessidade de servidor backend):

* **[`app.html`](file:///C:/Users/alexk/Desktop/freela-edumi/app.html) / [`index.html`](file:///C:/Users/alexk/Desktop/freela-edumi/index.html) (Gestão Tabular):** Busca instantânea, filtros rápidos (`Só DF (215)`, `Só GO (172)`, `SP`, `RJ`, `MG`), cópia rápida de e-mails, importação/exportação CSV compatível com o schema oficial da Gabi e invalidação automática de cache via `MASTER_PAYLOAD_VERSION`.
* **[`dashboard.html`](file:///C:/Users/alexk/Desktop/freela-edumi/dashboard.html) (Dashboard Analítico):** Gráficos Chart.js e segmentação por Tipo de Instituição (`Universidades Federais: 443`, `Institutos Federais: 345`, `Privadas / Particulares: 342`, `Universidades Estaduais: 67`, `Pública Distrital DF: 23`) e por UF.

---

## 📁 Estrutura de Diretórios

```text
freela-edumi/
├── 0. Planilha centralizadora.xlsx        # Template original em branco da Gabi (referência de schema)
├── 0. Planilha centralizadora - Gabi.xlsx # Planilha populada localmente (5 abas auditadas)
├── Planilha_Centralizadora_Edumi.xlsx     # Cópia mestre de trabalho (5 abas auditadas)
├── app.html / index.html                  # Interface Web de Gestão Tabular
├── dashboard.html                         # Dashboard Analítico com Chart.js
├── data_payload.js                        # Payload JSON + MASTER_PAYLOAD_VERSION
├── pyproject.toml / uv.lock               # Configuração determinística Python (uv)
├── tools/                                 # Pacote CLI edumi-ops (audit, etl_legacy, scraper_ies, exporter...)
├── data_staged/                           # Camada intermediária extraída de doc/
├── data_verified/                         # Contatos raspados com source_url + cache DNS MX
├── reports/                               # AUDITORIA_QUALIDADE.md + domínios em quarentena
├── csv_exports/                           # CSVs oficiais prontos para importação no Google Sheets
└── doc/                                   # 7 planilhas legadas originais (intactas / somente leitura)
```

---

## 📅 Cronograma de Entregas (Milestones)

* **[x] Marco 1 (27/10 - 23:00):** Distrito Federal concluído, auditado e **sincronizado no Google Sheets da Gabi** (**215 contatos verificados**, 0 bloqueadores).
* **[ ] Marco 2 (31/10 - 23:00):** Resto do Brasil (1.005 contatos legados já alimentados no Google Sheets + expansão nacional `.edu.br` agendada).
* **[ ] Marco 3 (04/11 - 23:00):** Artistas do DF do perfil `@edicoesmotim` (edições 2025 e 2026 verificadas).
* **[ ] Marco 4 (08/11 - 23:00):** Influenciadores verificados de DF, GO e PE + consolidação final.

---

## 🔒 Segurança e Governança

* **Acervo Original Intacto:** Nenhum arquivo local ou no Drive da cliente foi modificado ou excluído.
* **Planilha Central Alimentada:** Os **1.962 registros auditados** (`1.220 universidades`, `219 midias` e `523 parceiros`) já foram alimentados de forma não-destrutiva no Google Sheets oficial da Gabi.
