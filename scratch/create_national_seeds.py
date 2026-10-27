import json
from pathlib import Path

NATIONAL_SEEDS = [
    # DF Seeds (Marco 1)
    {"inst": "Universidade de Brasília (UnB)", "uf": "DF", "url": "https://unb.br/institucional/administracao"},
    {"inst": "Universidade de Brasília (UnB)", "uf": "DF", "url": "https://unb.br/graduacao/unidades-academicas"},
    {"inst": "Escola Superior de Ciências da Saúde (ESCS)", "uf": "DF", "url": "https://www.escs.edu.br/contatos/"},
    {"inst": "Universidade Católica de Brasília (UCB)", "uf": "DF", "url": "https://ucb.catolica.edu.br/portal/atendimento/"},
    {"inst": "Centro Universitário de Brasília (UniCEUB)", "uf": "DF", "url": "https://www.uniceub.br/atendimento"},
    {"inst": "Centro Universitário IESB", "uf": "DF", "url": "https://www.iesb.br/atendimento/"},
    {"inst": "Centro Universitário do Distrito Federal (UDF)", "uf": "DF", "url": "https://www.udf.edu.br/fale-conosco/"},
    {"inst": "Instituto Brasileiro de Ensino, Desenvolvimento e Pesquisa (IDP)", "uf": "DF", "url": "https://www.idp.edu.br/contato/"},
    {"inst": "Centro Universitário UNICEPLAC", "uf": "DF", "url": "https://www.uniceplac.edu.br/contato"},
    {"inst": "Faculdade Presbiteriana Mackenzie Brasília", "uf": "DF", "url": "https://www.mackenzie.br/faculdade-brasilia/fale-conosco"},
    {"inst": "Faculdade Senac Distrito Federal", "uf": "DF", "url": "https://www.df.senac.br/faculdade/"},

    # SP
    {"inst": "Instituto Federal de São Paulo (IFSP)", "uf": "SP", "url": "https://www.ifsp.edu.br/contato"},
    {"inst": "Universidade de São Paulo (USP)", "uf": "SP", "url": "https://www5.usp.br/contato/"},
    {"inst": "Universidade Estadual de Campinas (UNICAMP)", "uf": "SP", "url": "https://www.unicamp.br/fale-conosco/"},
    {"inst": "Universidade Estadual Paulista (UNESP)", "uf": "SP", "url": "https://www2.unesp.br/portal#!/fale-conosco/"},
    {"inst": "Universidade Federal de São Paulo (UNIFESP)", "uf": "SP", "url": "https://www.unifesp.br/reitoria/contato"},
    {"inst": "Universidade Federal de São Carlos (UFSCar)", "uf": "SP", "url": "https://www.ufscar.br/fale-conosco"},

    # RJ
    {"inst": "Instituto Federal do Rio de Janeiro (IFRJ)", "uf": "RJ", "url": "https://portal.ifrj.edu.br/fale-conosco"},
    {"inst": "Instituto Federal Fluminense (IFF)", "uf": "RJ", "url": "https://www.iff.edu.br/fale-conosco"},
    {"inst": "Centro Federal de Educação Tecnológica Celso Suckow da Fonseca (CEFET-RJ)", "uf": "RJ", "url": "https://www.cefet-rj.br/index.php/fale-conosco"},
    {"inst": "Universidade Federal do Rio de Janeiro (UFRJ)", "uf": "RJ", "url": "https://ufrj.br/contato/"},
    {"inst": "Universidade Federal Fluminense (UFF)", "uf": "RJ", "url": "https://www.uff.br/fale-conosco"},

    # MG
    {"inst": "Instituto Federal de Minas Gerais (IFMG)", "uf": "MG", "url": "https://www.ifmg.edu.br/portal/sobre-o-ifmg/contato"},
    {"inst": "Instituto Federal do Norte de Minas Gerais (IFNMG)", "uf": "MG", "url": "https://www.ifnmg.edu.br/reitoria/fale-conosco"},
    {"inst": "Instituto Federal do Sul de Minas (IFSULDEMINAS)", "uf": "MG", "url": "https://portal.ifsuldeminas.edu.br/index.php/fale-conosco-reitoria"},
    {"inst": "Instituto Federal do Triângulo Mineiro (IFTM)", "uf": "MG", "url": "https://iftm.edu.br/reitoria/contato/"},
    {"inst": "Instituto Federal do Sudeste de Minas Gerais (IF Sudeste MG)", "uf": "MG", "url": "https://www.ifsudestemg.edu.br/institucional/contato"},
    {"inst": "Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG)", "uf": "MG", "url": "https://www.cefetmg.br/fale-conosco/"},
    {"inst": "Universidade Federal de Minas Gerais (UFMG)", "uf": "MG", "url": "https://ufmg.br/a-universidade/fale-conosco"},
    {"inst": "Universidade Federal de Juiz de Fora (UFJF)", "uf": "MG", "url": "https://www2.ufjf.br/ouvidoria/fale-conosco/"},

    # RS / SC / PR
    {"inst": "Instituto Federal do Rio Grande do Sul (IFRS)", "uf": "RS", "url": "https://ifrs.edu.br/contato/"},
    {"inst": "Instituto Federal Farroupilha (IFFar)", "uf": "RS", "url": "https://www.iffarroupilha.edu.br/fale-conosco"},
    {"inst": "Instituto Federal de Santa Catarina (IFSC)", "uf": "SC", "url": "https://www.ifsc.edu.br/fale-conosco"},
    {"inst": "Instituto Federal Catarinense (IFC)", "uf": "SC", "url": "https://ifc.edu.br/fale-conosco/"},
    {"inst": "Instituto Federal do Paraná (IFPR)", "uf": "PR", "url": "https://ifpr.edu.br/fale-conosco/"},
    {"inst": "Universidade Federal do Rio Grande do Sul (UFRGS)", "uf": "RS", "url": "https://www.ufrgs.br/ufrgs/fale-conosco"},
    {"inst": "Universidade Federal de Santa Catarina (UFSC)", "uf": "SC", "url": "https://ufsc.br/contato/"},
    {"inst": "Universidade Federal do Paraná (UFPR)", "uf": "PR", "url": "https://www.ufpr.br/portalufpr/fale-conosco/"},

    # Nordeste
    {"inst": "Instituto Federal de Pernambuco (IFPE)", "uf": "PE", "url": "https://portal.ifpe.edu.br/fale-conosco/"},
    {"inst": "Instituto Federal do Sertão Pernambucano (IFSertãoPE)", "uf": "PE", "url": "https://www.ifsertao-pe.edu.br/index.php/fale-conosco"},
    {"inst": "Universidade Federal de Pernambuco (UFPE)", "uf": "PE", "url": "https://www.ufpe.br/fale-conosco"},
    {"inst": "Instituto Federal da Bahia (IFBA)", "uf": "BA", "url": "https://portal.ifba.edu.br/fale-conosco"},
    {"inst": "Instituto Federal Baiano (IF Baiano)", "uf": "BA", "url": "https://ifbaiano.edu.br/portal/fale-conosco/"},
    {"inst": "Universidade Federal da Bahia (UFBA)", "uf": "BA", "url": "https://www.ufba.br/fale-conosco"},
    {"inst": "Instituto Federal do Ceará (IFCE)", "uf": "CE", "url": "https://ifce.edu.br/acesso-a-informacao/institucional/contatos"},
    {"inst": "Universidade Federal do Ceará (UFC)", "uf": "CE", "url": "https://www.ufc.br/fale-conosco"},
    {"inst": "Instituto Federal da Paraíba (IFPB)", "uf": "PB", "url": "https://www.ifpb.edu.br/contato"},
    {"inst": "Instituto Federal do Rio Grande do Norte (IFRN)", "uf": "RN", "url": "https://portal.ifrn.edu.br/institucional/contato/"},
    {"inst": "Instituto Federal de Alagoas (IFAL)", "uf": "AL", "url": "https://www2.ifal.edu.br/acesso-a-informacao/institucional/contatos-reitoria"},
    {"inst": "Instituto Federal de Sergipe (IFS)", "uf": "SE", "url": "http://www.ifs.edu.br/contatos"},
    {"inst": "Instituto Federal do Maranhão (IFMA)", "uf": "MA", "url": "https://portal.ifma.edu.br/fale-conosco/"},
    {"inst": "Instituto Federal do Piauí (IFPI)", "uf": "PI", "url": "https://www.ifpi.edu.br/contato"},

    # Norte
    {"inst": "Instituto Federal do Pará (IFPA)", "uf": "PA", "url": "https://ifpa.edu.br/fale-conosco"},
    {"inst": "Instituto Federal do Amazonas (IFAM)", "uf": "AM", "url": "http://www.ifam.edu.br/contatos"},
    {"inst": "Instituto Federal do Acre (IFAC)", "uf": "AC", "url": "https://www.ifac.edu.br/fale-conosco"},
    {"inst": "Instituto Federal de Rondônia (IFRO)", "uf": "RO", "url": "https://portal.ifro.edu.br/fale-conosco"},
    {"inst": "Instituto Federal de Roraima (IFRR)", "uf": "RR", "url": "https://www.ifrr.edu.br/fale-conosco"},
    {"inst": "Instituto Federal do Amapá (IFAP)", "uf": "AP", "url": "https://www.ifap.edu.br/index.php/fale-conosco"},
    {"inst": "Instituto Federal do Tocantins (IFTO)", "uf": "TO", "url": "https://portal.ifto.edu.br/fale-conosco"},

    # Centro-Oeste (fora DF)
    {"inst": "Instituto Federal de Goiás (IFG)", "uf": "GO", "url": "https://www.ifg.edu.br/contatos"},
    {"inst": "Instituto Federal Goiano (IF Goiano)", "uf": "GO", "url": "https://www.ifgoiano.edu.br/home/index.php/fale-conosco.html"},
    {"inst": "Universidade Federal de Goiás (UFG)", "uf": "GO", "url": "https://ufg.br/p/6276-fale-conosco"},
    {"inst": "Instituto Federal de Mato Grosso (IFMT)", "uf": "MT", "url": "https://ifmt.edu.br/conteudo/pagina/fale-conosco/"},
    {"inst": "Instituto Federal de Mato Grosso do Sul (IFMS)", "uf": "MS", "url": "https://www.ifms.edu.br/fale-conosco"},
]

out = Path("data_verified/national_seeds.json")
out.write_text(json.dumps(NATIONAL_SEEDS, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Generated {len(NATIONAL_SEEDS)} national seeds in {out}")
