# 🛡️ Relatório Oficial de Itens Expurgados e Base em Quarentena — Projeto Edumi

> **Atualizado em:** 27/10/2026 às 21:26 UTC  
> **Status:** Ativo e Rastreável  
> **Total de Registros Quarentenados/Expurgados:** **77 categorias/registros**  
> **Exportação em Planilha:** [`csv_exports/itens_expurgados_e_quarentena.csv`](file:///C:/Users/alexk/Desktop/freela-edumi/csv_exports/itens_expurgados_e_quarentena.csv)

---

## 1. Princípio de Não-Destruição e Segurança

Conforme as diretrizes do projeto e solicitação expressa da Gabi:
- **Nenhum arquivo original em `doc/` foi alterado ou apagado.** Os 7 arquivos originais (`doc/*.xlsx`) continuam 100% íntegros e preservados como histórico intocável.
- Os itens abaixo foram **retirados unicamente do fluxo de envio ativo da Planilha Centralizadora** (`0. Planilha centralizadora.xlsx` e Google Sheets da Gabi).
- O objetivo é **proteger a reputação do domínio de e-mail da Edumi**, evitando que envios caiam em listas negras (Spamhaus, Barracuda), tenham bounce rate elevado ou tentem disparar para arrobas inexistentes no Instagram.

---

## 2. Resumo Quantitativo por Categoria

| Categoria | Quantidade | Causa Raiz do Expurgo |
| :--- | :---: | :--- |
| **Domínios Inexistentes (DNS Dead/NXDOMAIN)** | 31 | Domínios desativados, expirados ou faculdades extintas |
| **Bounces Históricos Bloqueados** | 22 | E-mails marcados como falha permanente nas planilhas legadas da Edumi |
| **Perfis Artísticos Sintéticos Purificados** | 50 | Contagens artificiais de seguidores (-100 degraus) e perfis de fora do DF |
| **Influenciadores Alucinados Purificados** | 36 | Arrobas artificiais que retornavam erro 404 no Instagram |
| **Novos Perfis Inacessíveis (Probe em Tempo Real)** | 22 | Tentativas de acesso que falharam na verificação pública via Instaloader |

---

## 3. Tabela Completa de Itens Retirados

| # | Categoria | Entidade / Instituição | Contato Retirado | UF | Motivo Técnico do Expurgo |
| :-: | :--- | :--- | :--- | :-: | :--- |
| 1 | Universidades (Domínio Morto) | UFJF | `coord.si@ice.ufjf.br` | MG | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 2 | Universidades (Domínio Morto) | Instituição Acadêmica | `coord.computacao@ice.ufjf.br` | MG | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 3 | Universidades (Domínio Morto) | Instituição Acadêmica | `secretaria.decsi@ufop.ufop.br` | MG | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 4 | Universidades (Domínio Morto) | UFRR | `silvia@univirr.rr.gov.br` | RR | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 5 | Universidades (Domínio Morto) | Instituição Acadêmica | `coordenacao.producao@engenharia.ufjf.br` | MG | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 6 | Universidades (Domínio Morto) | UFRGS | `comgrad-cic-l@inf.ufrs.br` | RS | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 7 | Universidades (Domínio Morto) | Instituição Acadêmica | `sri@sri.ufrj.br` | RJ | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 8 | Universidades (Domínio Morto) | Instituição Acadêmica | `acesso@acesso.ufjf.br` | MG | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 9 | Universidades (Domínio Morto) | Faculdade de Ciências e Educação de Rubiataba (FACER) | `contato@facer.edu.br` | GO | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 10 | Universidades (Domínio Morto) | Faculdade de Ciências e Educação Sena Aires (FACESA) | `secretaria@facesa.edu.br` | GO | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 11 | Universidades (Domínio Morto) | Faculdade de Ciências e Educação Sena Aires (FACESA) | `ouvidoria@facesa.edu.br` | GO | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 12 | Universidades (Domínio Morto) | Faculdade de Ciências e Educação Sena Aires (FACESA) | `facesa@facesa.edu.br` | GO | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 13 | Universidades (Domínio Morto) | Faculdade Lions (FACLions) | `contato@faclions.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 14 | Universidades (Domínio Morto) | Faculdade Mauá Goiânia | `contato@faculdademaua.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 15 | Universidades (Domínio Morto) | Faculdade Mauá Goiânia | `ouvidoria@faculdademaua.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 16 | Universidades (Domínio Morto) | Faculdade Mauá Goiânia | `secretaria@faculdademaua.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 17 | Universidades (Domínio Morto) | Faculdade Padrão / Fan Padrão | `ouvidoria@faculdadepadrao.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 18 | Universidades (Domínio Morto) | Faculdade Sul-América | `contato@faculdadesulamerica.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 19 | Universidades (Domínio Morto) | Faculdade Sul-América | `secretaria@faculdadesulamerica.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 20 | Universidades (Domínio Morto) | Faculdade Sul-América | `suporte@faculdadesulamerica.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 21 | Universidades (Domínio Morto) | Faculdade CGESP | `cgesp@cgesp.com.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 22 | Universidades (Domínio Morto) | Faculdade Inhumas (FACI) | `secretaria@facinhumas.edu.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 23 | Universidades (Domínio Morto) | Instituto de Filosofia e Teologia de Goiás (IFITEG) | `secretaria@ifiteg.org.br` | GO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 24 | Universidades (Domínio Morto) | Faculdade Norte Goiano (UniBras) | `secretaria.goianesia@unibras.edu.br` | GO | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 25 | Universidades (Domínio Morto) | ISCA | `faleconosco@iscafaculdades.com.br` | SP | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 26 | Universidades (Domínio Morto) | Instituição Acadêmica | `marcelo.lobosco@ice.ufjf.br` | MG | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 27 | Universidades (Domínio Morto) | UFRGS | `mat-comgradmat@ufgrs.br` | RS | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 28 | Universidades (Domínio Morto) | UFRGS | `comgrad-ecp@ufgrs.br` | RS | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 29 | Universidades (Domínio Morto) | Página News | `comercial@paginanews.com.br` | MT | Falha de DNS (TIMEOUT_OR_DEAD) - Domínio inexistente ou sem resposta MX |
| 30 | Universidades (Domínio Morto) | Diario Online | `rosana@diariocorumbaense.com.br` | MS | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 31 | Universidades (Domínio Morto) | NTO Tocantins | `redacao@ntocantins.com.br` | TO | Falha de DNS (NXDOMAIN) - Domínio inexistente ou sem resposta MX |
| 32 | Universidades (Bounce Histórico) | FAETEC | `faleconosco@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 33 | Universidades (Bounce Histórico) | FAETEC | `ouvidoria@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 34 | Universidades (Bounce Histórico) | FAETEC | `contato@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 35 | Universidades (Bounce Histórico) | FAETEC | `suporte@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 36 | Universidades (Bounce Histórico) | FAETEC | `gabinete@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 37 | Universidades (Bounce Histórico) | FAETEC | `secretaria@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 38 | Universidades (Bounce Histórico) | FAETEC | `ensino@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 39 | Universidades (Bounce Histórico) | FAETEC | `pedagogico@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 40 | Universidades (Bounce Histórico) | FAETEC | `registro@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 41 | Universidades (Bounce Histórico) | FAETEC | `academico@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 42 | Universidades (Bounce Histórico) | FAETEC | `comunicacao@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 43 | Universidades (Bounce Histórico) | FAETEC | `imprensa@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 44 | Universidades (Bounce Histórico) | FAETEC | `atendimento@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 45 | Universidades (Bounce Histórico) | FAETEC | `ouvidoria.faetec@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 46 | Universidades (Bounce Histórico) | FAETEC | `diretoria@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 47 | Universidades (Bounce Histórico) | FAETEC | `presidencia@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 48 | Universidades (Bounce Histórico) | FAETEC | `coordenacao@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 49 | Universidades (Bounce Histórico) | FAETEC | `concursos@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 50 | Universidades (Bounce Histórico) | FAETEC | `estagio@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 51 | Universidades (Bounce Histórico) | FAETEC | `reitoria@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 52 | Universidades (Bounce Histórico) | FAETEC | `protocolo@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 53 | Universidades (Bounce Histórico) | FAETEC | `posgraduacao@faetec.rj.gov.br` | RJ | Bounce permanente catalogado na base legada de 2025 |
| 54 | Artistas (Alucinação Sintética) | 50 perfis sintéticos purificados | `@artistas_sinteticos (lote legado com seguidores 3800, 3700...)` | Fora do DF / Sintéticos | Contagem de seguidores forjada em degraus decrescentes de -100 e perfis fora do DF (ex: @burocratacarimbos SC) |
| 55 | Influenciadores (Alucinação Sintética) | 36 perfis sintéticos purificados | `@influenciadores_sinteticos (lote legado 404)` | Inexistente | Perfis artificiais que retornavam erro 404 (inexistentes) no Instagram |
| 56 | Social Probe (artistas) | Clube de Colagem de Brasília | `@clubedecolagemdebrasilia` | DF | Instaloader error / profile not found: Profile clubedecolagemdebrasilia does not exist. |
| 57 | Social Probe (artistas) | Gráfica Autônoma | `@graficaautonoma` | DF | Instaloader error / profile not found: Profile graficaautonoma does not exist. |
| 58 | Social Probe (artistas) | Declarações Gráficas | `@declaracoesgraficas` | DF | Instaloader error / profile not found: Profile declaracoesgraficas does not exist. |
| 59 | Social Probe (artistas) | Estúdio Leoa | `@estudioleoa` | DF | Instaloader error / profile not found: Profile estudioleoa does not exist. |
| 60 | Social Probe (artistas) | Cores de Ellen | `@coresdeellen` | DF | Instaloader error / profile not found: Profile coresdeellen does not exist. |
| 61 | Social Probe (artistas) | Cris Assanuma | `@crisassanuma` | DF | Instaloader error / profile not found: Profile crisassanuma does not exist. |
| 62 | Social Probe (artistas) | Fiztiz Cerâmica | `@fiztizceramica` | DF | Instaloader error / profile not found: Profile fiztizceramica does not exist. |
| 63 | Social Probe (artistas) | Caio Montanini | `@caiomontanini` | DF | Instaloader error / profile not found: Profile caiomontanini does not exist. |
| 64 | Social Probe (artistas) | Catharina Baltar | `@catharinabaltar` | DF | Instaloader error / profile not found: Profile catharinabaltar does not exist. |
| 65 | Social Probe (artistas) | Cauê Xopó | `@cauexopo` | DF | Instaloader error / profile not found: Profile cauexopo does not exist. |
| 66 | Social Probe (artistas) | Evermore Papelaria | `@evermorepapelaria` | DF | Instaloader error / profile not found: Profile evermorepapelaria does not exist. |
| 67 | Social Probe (influenciadores) | UniCEUB Oficial | `@uniceuboficial` | DF | Instaloader error / profile not found: Profile uniceuboficial does not exist. |
| 68 | Social Probe (influenciadores) | IESB Brasília | `@iesbbrasilia` | DF | Instaloader error / profile not found: Profile iesbbrasilia does not exist. |
| 69 | Social Probe (influenciadores) | UNICEPLAC Gama | `@uniceplac` | DF | Instaloader error / profile not found: Profile uniceplac does not exist. |
| 70 | Social Probe (influenciadores) | ADUnB Sindicato | `@adunb.sindicato` | DF | Instaloader error / profile not found: Profile adunb.sindicato does not exist. |
| 71 | Social Probe (influenciadores) | CAENE UnB | `@caene.unb` | DF | Instaloader error / profile not found: Profile caene.unb does not exist. |
| 72 | Social Probe (influenciadores) | PET Computação UnB | `@petcomputacaounb` | DF | Instaloader error / profile not found: Profile petcomputacaounb does not exist. |
| 73 | Social Probe (influenciadores) | IFG Oficial | `@ifgoiasoficial` | DF | Instaloader error / profile not found: Profile ifgoiasoficial does not exist. |
| 74 | Social Probe (influenciadores) | UEG Oficial | `@ueg.oficial` | DF | Instaloader error / profile not found: Profile ueg.oficial does not exist. |
| 75 | Social Probe (influenciadores) | Atlética Medicina UFG | `@atleticamedufg` | DF | Instaloader error / profile not found: Profile atleticamedufg does not exist. |
| 76 | Social Probe (influenciadores) | UPE Oficial | `@upe_oficial` | DF | Instaloader error / profile not found: Profile upe_oficial does not exist. |
| 77 | Social Probe (influenciadores) | CIn UFPE | `@cin_ufpe` | DF | Instaloader error / profile not found: Profile cin_ufpe does not exist. |

---

## 4. Como Reativar um Contato se Necessário

Se algum dos contatos acima for reativado pela instituição ou obtido por outro canal:
1. Verifique a resolução MX no terminal: `uv run python -c "import dns.resolver; print(dns.resolver.resolve('dominio.com.br', 'MX'))"`
2. Adicione-o manualmente à planilha centralizadora ou inclua-o no catálogo verificado `data_verified/`.
3. Execute `uv run edumi build` para recompilar as planilhas oficiais.
