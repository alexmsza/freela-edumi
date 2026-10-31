# Edumi — Centralizador de Prospecção & Engenharia de Dados

Esteira determinística de consolidação, higienização, auditoria DNS MX, visualização e exportação de dados para campanhas de prospecção acadêmica, imprensa, parcerias e influenciadores da **Edumi**.

---

## 🎯 Objetivo do Projeto

Unificar o acervo histórico disperso da Edumi (`doc/*.xlsx`) e enriquecê-lo com contatos institucionais verificados em uma **única planilha centralizadora padronizada (Flat Table)** compatível com o Google Sheets oficial da cliente ([`0. Planilha centralizadora`](https://docs.google.com/spreadsheets/d/1hqgfKgMzn00-zV91sFe7a6aMK5ZV47TCvQNfMP8Ksv0/edit)), com **zero bounces, zero domínios mortos e zero dados sintéticos**.

> **Posição em 29/10/2026:** os CSVs e as três planilhas `.xlsx` locais estão alinhados. A leitura da planilha online confirmou paridade exata em `universidades`, `artistas` e `influenciadores`; `midias` e `parceiros` ainda divergem. A base universitária também não contém AP (26 das 27 UFs).

O projeto inclui:
1. **CLI de Engenharia de Dados (`edumi-ops` via `uv`):** Extração determinística do acervo legado, raspagem institucional com rastreabilidade (`source_url`), resolução concorrente de DNS MX/A e trava de auditoria (`total_blockers == 0`).
2. **Aplicações Web Locais Autônomas (`app.html`, `index.html` e `dashboard.html`):** Gestão tabular e dashboard analítico interativo consumindo `data_payload.js` versionado por hash SHA-256.

---

## 📊 Estrutura Atual Auditada (5 Abas Oficiais)

Todas as abas seguem rigorosamente as colunas de [`0. Planilha centralizadora.xlsx`](file:///C:/Users/alexk/Desktop/freela-edumi/0.%20Planilha%20centralizadora.xlsx):

1. **`universidades`**: `nome_faculdade`, `nome_departamento`, `email`, `uf`  
   - **Total local:** **604 contatos departamentais** (166 DF, 47 GO e 391 nas demais UFs), em 26 UFs; AP está ausente. Auditoria registrada: 0 bloqueadores.
2. **`artistas`**: `nome`, `arroba`, `quantidade_seguidores`, `tipo`, `uf`  
   - **66 artistas reais e ativos** da Feira Motim DF com contagem exata de seguidores via `instaloader` (ex.: `@cartumante`, `@camisacritica`, `@batatinhafantasma`, `@brunayonashiro`, `@dessamore`, `@gurulino`...).
3. **`influenciadores`**: `nome`, `arroba`, `quantidade_seguidores`, `tipo`, `uf`  
   - **25 perfis** em DF, GO e PE, presentes no CSV atual e na aba online.
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

* **`app.html` / `index.html` (Gestão Tabular):** Busca, filtros, cópia de e-mails e importação/exportação CSV. Os totais por UF são calculados a partir da base carregada.
* **`dashboard.html` (Dashboard Analítico):** Gráficos Chart.js e contagens de categorias calculadas a partir de `data_payload.js`, sem números fixos no filtro.

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

## 📅 Status dos Marcos (posição em 29/10/2026)

* **Marco 1 (27/10):** concluído na base local; 166 contatos do DF na planilha nacional atual.
* **Marco 2 (31/10):** parcial; há 604 contatos locais, mas falta cobrir AP. A aba online `universidades` está idêntica ao CSV.
* **Marco 3 (04/11):** 66 artistas disponíveis localmente e sincronizados na aba online.
* **Marco 4 (08/11):** 25 perfis disponíveis localmente e sincronizados na aba online.
* **Fechamento:** confirmar com a cliente a aba `LIMPEZAS`/aprovação final e atualizar `midias` e `parceiros` no Sheets.

---

## 🔒 Segurança, Governança e Quarentena

* **Acervo Original Intacto:** Os arquivos de origem em `doc/` são preservados.
* **Entregáveis locais:** 604 universidades, 66 artistas, 25 influenciadores, 219 mídias e 523 parceiros (**1.437 linhas** no total). Os três `.xlsx` locais correspondem às abas do CSV.
* **Sheets online (leitura verificada):** `universidades` 604/604, `artistas` 66/66 e `influenciadores` 25/25 correspondem ao CSV. `midias` tem 152/219 e `parceiros` 4/523; falta sincronizar essas duas abas. A verificação foi somente leitura.
* **Cobertura:** `01_universidades.csv` contém 26 UFs; AP não aparece. Portanto, não afirmar cobertura nacional completa até pesquisar, validar e incluir contatos do Amapá.
* **Transparência de Expurgo:** Todos os 77 registros retirados do disparo (domínios mortos, bounces históricos e perfis não encontrados) estão catalogados com motivo técnico e impacto em [`LISTA_DE_ITENS_EXPURGADOS_E_QUARENTENA.md`](file:///C:/Users/alexk/Desktop/freela-edumi/LISTA_DE_ITENS_EXPURGADOS_E_QUARENTENA.md) e [`csv_exports/itens_expurgados_e_quarentena.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/itens_expurgados_e_quarentena.csv).
* **Contagem a reconciliar:** `csv_exports/01_universidades_removed.csv` contém 651 linhas de dados; documentos anteriores mencionam 644.
