# Relatório de Itens Expurgados e Base em Quarentena — Projeto Edumi

> **Data de Emissão:** 27 de Outubro de 2026  
> **Finalidade:** Auditoria forense e rastreabilidade total de dados. Nenhuma exclusão foi destrutiva; todos os arquivos originais em `doc/` permanecem 100% íntegros.  
> **Total de Registros Quarentenados/Expurgados:** **139 registros**

---

## 1. Resumo Executivo da Higienização

Durante o processo de centralização das 7 planilhas legadas em `doc/*.xlsx`, a esteira determinística de engenharia (`edumi-ops`) aplicou validações de integridade RFC de e-mail, consulta concorrente de DNS MX/A e checagem de alucinações. Para proteger a reputação do domínio de envio da Edumi (evitando bloqueios em listas anti-spam e devoluções em massa), **139 registros foram retirados do fluxo de disparo ativo**:

1. **31 Domínios Mortos / Inexistentes (Quarentena DNS):** Universidades e portais cujos domínios web não existem mais (`NXDOMAIN`) ou cujos servidores de e-mail falharam (`TIMEOUT_OR_DEAD`).
2. **22 E-mails de Bounce Histórico (Bloqueio Permanente):** E-mails que já constavam expressamente marcados como "Bounce" nas planilhas legadas da própria Edumi (`arquivado.xlsx` e `Lista de e-mails Universidades Brasil.xlsx`), mas que estavam vazando para a lista ativa.
3. **50 Perfis Artísticos Sintéticos (Expurgo de Alucinação):** Registros gerados em iterações preliminares com contagem artificial de seguidores em degraus fixos de -100 (`3.800, 3.700, 3.600... 1.800`) e perfis de fora do DF (ex: `@burocratacarimbos`, de Santa Catarina).
4. **36 Perfis de Influenciadores Alucinados (Expurgo de Alucinação):** Perfis sintéticos que retornavam erro 404 (inexistentes) no Instagram.

---

## 2. Domínios Mortos em Quarentena (31 registros)

Estes registros foram isolados em [`reports/quarantined_dead_domains.json`](file:///C:/Users/alexk/Desktop/freela-edumi/reports/quarantined_dead_domains.json) e **não foram incluídos** nas planilhas ativas:

| # | Instituição / Veículo | Setor / Depto | E-mail Retirado | UF | Diagnóstico DNS |
| :-: | :--- | :--- | :--- | :-: | :--- |
| 1 | UFJF | Atendimento Institucional | `coord.si@ice.ufjf.br` | MG | `TIMEOUT_OR_DEAD` |
| 2 | UFJF | STEM | `coord.computacao@ice.ufjf.br` | MG | `TIMEOUT_OR_DEAD` |
| 3 | UFJF | Engenharias | `coordenacao.producao@engenharia.ufjf.br` | MG | `TIMEOUT_OR_DEAD` |
| 4 | UFJF | Acesso Institucional | `acesso@acesso.ufjf.br` | MG | `NXDOMAIN` (subdomínio não existe) |
| 5 | UFJF | Engenharias | `marcelo.lobosco@ice.ufjf.br` | MG | `TIMEOUT_OR_DEAD` |
| 6 | UFOP | STEM | `secretaria.decsi@ufop.ufop.br` | MG | `NXDOMAIN` (domínio duplicado inválido) |
| 7 | UFRR | Engenharias | `silvia@univirr.rr.gov.br` | RR | `NXDOMAIN` |
| 8 | UFRGS | Engenharias | `comgrad-cic-l@inf.ufrs.br` | RS | `NXDOMAIN` (`ufrs.br` em vez de `ufrgs.br`) |
| 9 | UFRGS | Matemática | `mat-comgradmat@ufgrs.br` | RS | `NXDOMAIN` (erro de digitação legado) |
| 10 | UFRGS | Engenharias | `comgrad-ecp@ufgrs.br` | RS | `NXDOMAIN` (erro de digitação legado) |
| 11 | UFRJ | Relações Internacionais | `sri@sri.ufrj.br` | RJ | `NXDOMAIN` (subdomínio inativo) |
| 12 | FACER | Ensino Superior Regional | `contato@facer.edu.br` | GO | `TIMEOUT_OR_DEAD` |
| 13 | FACESA | Secretaria Geral | `secretaria@facesa.edu.br` | GO | `TIMEOUT_OR_DEAD` |
| 14 | FACESA | Ouvidoria | `ouvidoria@facesa.edu.br` | GO | `TIMEOUT_OR_DEAD` |
| 15 | FACESA | Atendimento Geral | `facesa@facesa.edu.br` | GO | `TIMEOUT_OR_DEAD` |
| 16 | FACLions | Cursos de Graduação | `contato@faclions.edu.br` | GO | `NXDOMAIN` (faculdade extinta/site fora) |
| 17 | Faculdade Mauá Goiânia | Atendimento Estudantil | `contato@faculdademaua.edu.br` | GO | `NXDOMAIN` (domínio expirado) |
| 18 | Faculdade Mauá Goiânia | Ouvidoria | `ouvidoria@faculdademaua.edu.br` | GO | `NXDOMAIN` (domínio expirado) |
| 19 | Faculdade Mauá Goiânia | Secretaria | `secretaria@faculdademaua.edu.br` | GO | `NXDOMAIN` (domínio expirado) |
| 20 | Faculdade Padrão / Fan | Cursos diversos | `ouvidoria@faculdadepadrao.edu.br` | GO | `NXDOMAIN` (domínio expirado) |
| 21 | Faculdade Sul-América | Suporte EAD | `contato@faculdadesulamerica.edu.br` | GO | `NXDOMAIN` (domínio expirado) |
| 22 | Faculdade Sul-América | Secretaria EAD | `secretaria@faculdadesulamerica.edu.br` | GO | `NXDOMAIN` (domínio expirado) |
| 23 | Faculdade Sul-América | Atendimento | `suporte@faculdadesulamerica.edu.br` | GO | `NXDOMAIN` (domínio expirado) |
| 24 | Faculdade CGESP | Pós-Graduação | `cgesp@cgesp.com.br` | GO | `NXDOMAIN` (domínio expirado) |
| 25 | Faculdade Inhumas (FACI) | Secretaria Acadêmica | `secretaria@facinhumas.edu.br` | GO | `NXDOMAIN` (domínio expirado) |
| 26 | IFITEG | Secretaria Confessional | `secretaria@ifiteg.org.br` | GO | `NXDOMAIN` (domínio expirado) |
| 27 | UniBras (Norte Goiano) | Secretaria Goianésia | `secretaria.goianesia@unibras.edu.br` | GO | `TIMEOUT_OR_DEAD` |
| 28 | ISCA Faculdades | Atendimento Geral | `faleconosco@iscafaculdades.com.br` | SP | `NXDOMAIN` (domínio expirado) |
| 29 | Página News | Imprensa Regional | `comercial@paginanews.com.br` | MT | `TIMEOUT_OR_DEAD` |
| 30 | Diário Online | Imprensa / Redação | `rosana@diariocorumbaense.com.br` | MS | `NXDOMAIN` (domínio antigo inativo) |
| 31 | NTO Tocantins | Portal de Notícias | `redacao@ntocantins.com.br` | TO | `NXDOMAIN` (portal fora do ar) |

---

## 3. Bounces Históricos Bloqueados (22 registros)

Estes e-mails constavam na aba `bounce` das planilhas legadas de 2025 da Edumi e geravam falha de entrega. Foram bloqueados para que nunca mais contaminem disparos futuros:

1. `faleconosco@faetec.rj.gov.br`
2. `ouvidoria@faetec.rj.gov.br`
3. `contato@faetec.rj.gov.br`
4. `suporte@faetec.rj.gov.br`
5. `gabinete@faetec.rj.gov.br`
6. `secretaria@faetec.rj.gov.br`
7. `ensino@faetec.rj.gov.br`
8. `pedagogico@faetec.rj.gov.br`
9. `registro@faetec.rj.gov.br`
10. `academico@faetec.rj.gov.br`
11. `comunicacao@faetec.rj.gov.br`
12. `imprensa@faetec.rj.gov.br`
13. `atendimento@faetec.rj.gov.br`
14. `ouvidoria.faetec@faetec.rj.gov.br`
15. `diretoria@faetec.rj.gov.br`
16. `presidencia@faetec.rj.gov.br`
17. `coordenacao@faetec.rj.gov.br`
18. `concursos@faetec.rj.gov.br`
19. `estagio@faetec.rj.gov.br`
20. `reitoria@faetec.rj.gov.br`
21. `protocolo@faetec.rj.gov.br`
22. `posgraduacao@faetec.rj.gov.br`

---

## 4. Perfis Sintéticos Purificados (50 Artistas + 36 Influenciadores)

Na versão anterior do projeto gerada antes da auditoria, as abas `artistas` e `influenciadores` continham registros artificiais que falharam nos critérios de governança:
- **Artistas:** Seguidores preenchidos artificialmente em progressão aritmética decrescente de -100 (`3800, 3700, 3600... 1800`), além de perfis com residência fora do DF (ex.: `@burocratacarimbos` em Santa Catarina).
- **Influenciadores:** Perfis que não existiam no Instagram ou que não possuíam ligação comprovada com os estados solicitados (DF, GO e PE).

**Ação tomada:** As duas abas foram limpas na planilha mestre e no Google Sheets (mantendo os cabeçalhos oficiais intactos), para que a alimentação ocorra **estritamente com fontes verificadas** nos Marcos 3 e 4.

---

## 5. Como Recuperar Qualquer Item

Caso a equipe da Edumi queira consultar o dado original exato de onde veio cada um dos registros:
- Todos os 7 arquivos em [`doc/`](file:///C:/Users/alexk/Desktop/freela-edumi/doc/) permanecem **intocados e protegidos em modo somente leitura**.
- O histórico de proveniência de cada linha está mapeado em [`data_staged/`](file:///C:/Users/alexk/Desktop/freela-edumi/data_staged/).
