# Edumi — Centralizador de Prospecção & Inteligência de Dados

Sistema de consolidação, higienização, visualização e exportação de dados para campanhas de prospecção acadêmica, parcerias culturais e influenciadores da **Edumi**.

---

## 🎯 Objetivo do Projeto

Centralizar todo o acervo histórico disperso da Edumi em uma **única planilha centralizadora padronizada no Google Sheets**, eliminando a criação desordenada de múltiplos arquivos e garantindo uma base limpa para mala direta e parcerias.

O projeto conta também com uma **aplicação web local autônoma (`app.html` / `dashboard.html`)** com dashboard analítico interativo, busca em tempo real, filtros por estado (UF), gráficos dinâmicos, adição manual de registros e importação de novos dados via CSV.

---

## 📊 Estrutura dos Dados (5 Abas Padronizadas)

Todas as bases seguem o formato de tabela plana (*Flat Table*), conforme a estrutura oficial criada na planilha [`0. Planilha centralizadora`](https://docs.google.com/spreadsheets/d/1hqgfKgMzn00-zV91sFe7a6aMK5ZV47TCvQNfMP8Ksv0/edit):

1. **`universidades`**: `nome_faculdade`, `nome_departamento`, `email`, `uf` *(1.158 contatos consolidados: 223 DF, 170 GO e 765 Brasil)*.
2. **`artistas`**: `nome`, `arroba`, `quantidade_seguidores`, `tipo`, `uf` *(20 artistas e coletivos do DF da @edicoesmotim em 2025/2026)*.
3. **`influenciadores`**: `nome`, `arroba`, `quantidade_seguidores`, `tipo`, `uf` *(17 criadores regionais categorizados por nicho em DF, GO e PE)*.
4. **`midias`**: `nome`, `link`, `email`, `telefone`, `uf`, `obs` *(194 veículos de comunicação de 13 estados)*.
5. **`parceiros`**: `nome`, `link`, `email`, `telefone`, `uf`, `obs` *(104 contatos de parcerias e WhatsApp)*.

---

## 🖥️ Aplicações Web Locais (Tabela & Dashboard Dedicado)

Não requer nenhuma instalação, servidor Node.js ou dependências externas. Basta dar um duplo clique para abrir no navegador:

### 1. 📊 Dashboard Analítico & Métricas (`dashboard.html`)
Tela dedicada com painel visual completo e segmentação dinâmica por assunto e categoria:
* **Filtro por Assunto (Pills):** Alterna as análises entre `🎓 Universidades & IFs`, `📱 Influenciadores (DF, GO, PE)`, `🎨 Artistas Motim DF`, `📰 Mídias & Imprensa` e `🤝 Parceiros & Redes`.
* **Filtro por Tipo de Instituição:** Segmenta instantaneamente entre:
  - 🏛️ **Institutos Federais (IF)** (212 contatos e campi)
  - 🎓 **Universidades Federais** (345 contatos)
  - 🏢 **Faculdades Privadas / Particulares** (507 contatos)
  - 🏫 **Universidades Estaduais** (56 contatos)
  - 🏥 **Pública Distrital (DF)** (4 contatos)
* **Filtro por UF:** Dropdown dinâmico com todas as unidades federativas (DF, GO, SP, RJ, MG, PE...).
* **Gráficos Dinâmicos (Chart.js):**
  - Gráfico Donut de Proporção por Tipo (IFs vs Federais vs Privadas vs Estaduais).
  - Gráfico de Barras do Ranking das Top 10 UFs filtradas.
* **KPIs Reativos:** Métricas calculadas instantaneamente conforme os filtros selecionados.
* **Tabela de Prévia Analítica:** Visualização tabular direta dos dados filtrados com exportação em CSV com 1 clique.

### 2. 📋 Centralizador & Gestão de Dados (`app.html` / `index.html`)
Tela focada na operação, edição e alimentação das planilhas:
* **🔍 Busca em Tempo Real:** Filtre instantaneamente por faculdade, departamento, e-mail, cidade ou palavras-chave.
* **🏷️ Filtros Rápidos por UF:** Seletores de 1 clique para `Só DF (223)`, `Só GO (170)`, `SP`, `RJ`, `MG` e dropdown geral.
* **➕ Adição Manual de Registros:** Cadastre novos contatos diretamente na interface com validação de colunas.
* **📥 Importação de CSV:** Importe novas listas em formato `.csv` com prévia automática e mapeamento de campos.
* **📋 Cópia Rápida:** Botão para copiar e-mail ou a linha inteira para a área de transferência.
* **💾 Exportação de CSV:** Baixe um arquivo CSV com os dados exatamente como filtrados na tela.

Ambas as telas possuem um **menu superior integrado (*Top Nav Switcher*)**, permitindo alternar livremente entre a visão analítica e a visão tabular.

---

## 📁 Estrutura de Diretórios do Repositório

```
freela-edumi/
│
├── 0. Planilha centralizadora - Gabi.xlsx # Planilha oficial baixada do Google Sheets da Gabi e populada localmente
├── Planilha_Centralizadora_Edumi.xlsx    # Planilha mestre de trabalho (5 abas oficiais)
├── app.html                             # Aplicação Web de Gestão e Operação Tabular
├── index.html                           # Ponto de entrada padrão
├── dashboard.html                       # Dashboard Analítico Dedicado com Gráficos Chart.js
├── data_payload.js                      # Base de dados estruturada consumida pelas aplicações
├── PLANO_DE_EXECUCAO.md                 # Cronograma detalhado, prazos e critérios técnicos
├── README.md                            # Documentação geral do projeto
├── oquefazer.txt                        # Briefing original e requisitos da Edumi
│
├── csv_exports/                         # Arquivos CSV prontos para importação no Google Sheets
│   ├── 01_universidades.csv             # 1.158 contatos com UF
│   ├── 01_universidades_DF_marco1.csv   # 223 contatos exclusivos do DF (UnB, IFB, privadas)
│   ├── 02_artistas.csv                  # 20 artistas da Feira Motim DF 2025/2026
│   ├── 03_influenciadores.csv           # 17 criadores regionais (DF, GO, PE)
│   ├── 04_midias.csv                    # 194 veículos de mídia de 13 UFs
│   └── 05_parceiros.csv                 # 104 contatos de parceiros e canais de WhatsApp
│
└── doc/                                 # Acervo legado original preservado para auditoria
    ├── Audiencias faculdades.xlsx
    ├── Contas instagram parcerias para divulgação.xlsx
    ├── Contatos de Universidades, Faculdades, SENAC e SENAI em Goiás V4.xlsx
    ├── Lista de e-mails Universidades Brasil.xlsx
    ├── Lista de Psicologia - Parcerias UFS Universidades, departamentos.xlsx
    ├── Mídias (jornal).xlsx
    └── arquivado.xlsx
```

---

## 📅 Cronograma de Entregas (Milestones)

* **[x] Marco 1 (27/10 - 23:00):** Mapeamento do Distrito Federal (223 contatos: UnB 95 setores, IFB Reitoria + 10 campi, ESCS, privadas e Sistema S).
* **[x] Marco 2 (31/10 - 32:00):** Mapeamento do Resto do Brasil (Goiás V4 + Federais, Estaduais e 212 Institutos Federais de todo o país).
* **[x] Marco 3 (04/11 - 23:00):** Mapeamento dos Artistas do DF do perfil `@edicoesmotim` (anos 2025 e 2026).
* **[x] Marco 4 (08/11 - 23:00):** Mapeamento dos Influenciadores de DF, GO e PE por nicho.

---

## 🔒 Segurança e Integridade dos Dados

* **Nenhum arquivo do acervo legado (`/doc`) foi apagado**, permanecendo como fonte primária para auditoria.
* **Nenhum dado foi enviado online para o Google Sheets ainda**, aguardando aprovação explícita do usuário.
