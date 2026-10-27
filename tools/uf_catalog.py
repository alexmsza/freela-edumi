"""Catálogo determinístico de domínios acadêmicos, UFs, siglas da UnB e campi de IFs."""

from __future__ import annotations

import re

VALID_UFS: set[str] = {
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
    "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR",
    "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO",
}

STATE_NAME_TO_UF: dict[str, str] = {
    "acre": "AC",
    "alagoas": "AL",
    "amazonas": "AM",
    "amapa": "AP",
    "amapá": "AP",
    "bahia": "BA",
    "ceara": "CE",
    "ceará": "CE",
    "distrito federal": "DF",
    "brasilia": "DF",
    "brasília": "DF",
    "espirito santo": "ES",
    "espírito santo": "ES",
    "goias": "GO",
    "goiás": "GO",
    "maranhao": "MA",
    "maranhão": "MA",
    "minas gerais": "MG",
    "mato grosso do sul": "MS",
    "mato grosso": "MT",
    "para": "PA",
    "pará": "PA",
    "paraiba": "PB",
    "paraíba": "PB",
    "pernambuco": "PE",
    "piaui": "PI",
    "piauí": "PI",
    "parana": "PR",
    "paraná": "PR",
    "rio de janeiro": "RJ",
    "rio grande do norte": "RN",
    "rondonia": "RO",
    "rondônia": "RO",
    "roraima": "RR",
    "rio grande do sul": "RS",
    "santa catarina": "SC",
    "sergipe": "SE",
    "sao paulo": "SP",
    "são paulo": "SP",
    "tocantins": "TO",
}

# Mapeamento determinístico de domínios acadêmicos brasileiros -> UF oficial (2 letras)
DOMAIN_TO_UF: dict[str, str] = {
    # DF
    "unb.br": "DF", "ifb.edu.br": "DF", "ucb.br": "DF", "uniceub.br": "DF",
    "iesb.br": "DF", "udf.edu.br": "DF", "unieuro.edu.br": "DF", "projecao.br": "DF",
    "idp.edu.br": "DF", "uniceplac.edu.br": "DF", "fepecs.edu.br": "DF",
    "faculdaderepublicana.org.br": "DF", "df.senac.br": "DF", "sistemafibra.org.br": "DF",
    "faculdadejk.edu.br": "DF",
    # GO
    "ufg.br": "GO", "ufcat.edu.br": "GO", "ufj.edu.br": "GO", "ifg.edu.br": "GO",
    "ifgoiano.edu.br": "GO", "ueg.br": "GO", "pucgoias.edu.br": "GO", "unirv.edu.br": "GO",
    "unievangelica.edu.br": "GO", "unialfa.com.br": "GO", "cambury.br": "GO",
    "fasam.edu.br": "GO", "unifan.edu.br": "GO", "go.senac.br": "GO", "sistemafieg.org.br": "GO",
    # PE
    "ufpe.br": "PE", "ufrpe.br": "PE", "ufape.edu.br": "PE", "univasf.edu.br": "PE",
    "upe.br": "PE", "ifpe.edu.br": "PE", "ifsertao-pe.edu.br": "PE", "unicap.br": "PE",
    "cesar.school": "PE", "fbv.edu.br": "PE", "fps.edu.br": "PE",
    # SP
    "usp.br": "SP", "unicamp.br": "SP", "unesp.br": "SP", "unifesp.br": "SP",
    "ufscar.br": "SP", "ufabc.edu.br": "SP", "ifsp.edu.br": "SP", "pucsp.br": "SP",
    "puc-campinas.edu.br": "SP", "mackenzie.br": "SP", "fgv.br": "SP", "insper.edu.br": "SP",
    "anhembi.br": "SP", "fmu.br": "SP", "unip.br": "SP", "uninove.br": "SP",
    "metodista.br": "SP", "usjt.br": "SP", "unisa.br": "SP", "ita.br": "SP",
    "ceunsp.edu.br": "SP", "oswaldocruz.br": "SP", "ibirapuera.br": "SP",
    # RJ
    "ufrj.br": "RJ", "uff.br": "RJ", "uerj.br": "RJ", "unirio.br": "RJ",
    "ufrrj.br": "RJ", "uenf.br": "RJ", "ifrj.edu.br": "RJ", "iff.edu.br": "RJ",
    "cefet-rj.br": "RJ", "puc-rio.br": "RJ", "uva.br": "RJ", "estacio.br": "RJ",
    "ibge.gov.br": "RJ", "aedb.br": "RJ", "unigranrio.com.br": "RJ",
    # MG
    "ufmg.br": "MG", "ufu.br": "MG", "ufjf.br": "MG", "ufv.br": "MG",
    "ufop.br": "MG", "ufsj.edu.br": "MG", "ufla.br": "MG", "unifal-mg.edu.br": "MG",
    "unifei.edu.br": "MG", "uftm.edu.br": "MG", "ufvjm.edu.br": "MG", "uemg.br": "MG",
    "unimontes.br": "MG", "cefetmg.br": "MG", "ifmg.edu.br": "MG", "ifnmg.edu.br": "MG",
    "ifsudestemg.edu.br": "MG", "ifsuldeminas.edu.br": "MG", "iftm.edu.br": "MG",
    "pucminas.br": "MG", "fumec.br": "MG", "asmec.br": "MG",
    # RS / SC / PR
    "ufrgs.br": "RS", "ufsm.br": "RS", "ufpel.edu.br": "RS", "furg.br": "RS",
    "unipampa.edu.br": "RS", "uffs.edu.br": "SC", "ufcspa.edu.br": "RS",
    "ifrs.edu.br": "RS", "ifsul.edu.br": "RS", "iffarroupilha.edu.br": "RS",
    "pucrs.br": "RS", "unisinos.br": "RS", "ucs.br": "RS",
    "ufsc.br": "SC", "udesc.br": "SC", "ifsc.edu.br": "SC", "ifc.edu.br": "SC",
    "univali.br": "SC", "furb.br": "SC",
    "ufpr.br": "PR", "utfpr.edu.br": "PR", "unila.edu.br": "PR", "uel.br": "PR",
    "uem.br": "PR", "uepg.br": "PR", "unioeste.br": "PR", "ifpr.edu.br": "PR",
    "pucpr.br": "PR",
    # Nordeste (demais)
    "ufba.br": "BA", "ufrb.edu.br": "BA", "ufsb.edu.br": "BA", "ufob.edu.br": "BA",
    "uneb.br": "BA", "uefs.br": "BA", "uesb.br": "BA", "uesc.br": "BA",
    "ifba.edu.br": "BA", "ifbaiano.edu.br": "BA",
    "ufc.br": "CE", "unilab.edu.br": "CE", "ufca.edu.br": "CE", "uece.br": "CE",
    "ifce.edu.br": "CE", "unifor.br": "CE",
    "ufpb.br": "PB", "ufcg.edu.br": "PB", "uepb.edu.br": "PB", "ifpb.edu.br": "PB",
    "ufrn.br": "RN", "ufersa.edu.br": "RN", "uern.br": "RN", "ifrn.edu.br": "RN",
    "ufal.br": "AL", "uncisal.edu.br": "AL", "ifal.edu.br": "AL",
    "ufs.br": "SE", "ifs.edu.br": "SE",
    "ufma.br": "MA", "uema.br": "MA", "ifma.edu.br": "MA",
    "ufpi.edu.br": "PI", "ufdpar.edu.br": "PI", "uespi.br": "PI", "ifpi.edu.br": "PI",
    # Norte
    "ufpa.br": "PA", "ufra.edu.br": "PA", "ufopa.edu.br": "PA", "unifesspa.edu.br": "PA",
    "uepa.br": "PA", "ifpa.edu.br": "PA",
    "ufam.edu.br": "AM", "uea.edu.br": "AM", "ifam.edu.br": "AM",
    "ufac.br": "AC", "ifac.edu.br": "AC",
    "unir.br": "RO", "ifro.edu.br": "RO",
    "ufrr.br": "RR", "uerr.edu.br": "RR", "ifrr.edu.br": "RR",
    "unifap.br": "AP", "ifap.edu.br": "AP",
    "uft.edu.br": "TO", "ufnt.edu.br": "TO", "unitins.br": "TO", "ifto.edu.br": "TO",
    # Centro-Oeste (MT / MS) e ES
    "ufmt.br": "MT", "ufr.edu.br": "MT", "unemat.br": "MT", "ifmt.edu.br": "MT",
    "ufms.br": "MS", "ufgd.edu.br": "MS", "uems.br": "MS", "ifms.edu.br": "MS",
    "ufes.br": "ES", "ifes.edu.br": "ES",
}

# Siglas de institutos/universidades no nome quando o e-mail é @gmail/@hotmail/@outlook
INST_TOKEN_TO_UF: dict[str, str] = {
    "UNB": "DF", "IFB": "DF", "UCB": "DF", "UNICEUB": "DF", "IESB": "DF", "UDF": "DF", "ESCS": "DF",
    "UFG": "GO", "UFCAT": "GO", "UFJ": "GO", "IFG": "GO", "IFGOIANO": "GO", "UEG": "GO", "PUC-GO": "GO",
    "UFGD": "MS", "UFMS": "MS", "IFMS": "MS",
    "UFMT": "MT", "UFR": "MT", "IFMT": "MT",
    "UFPE": "PE", "UFRPE": "PE", "UPE": "PE", "IFPE": "PE", "UNIVASF": "PE",
    "UFBA": "BA", "UFRB": "BA", "UFSB": "BA", "UFOB": "BA", "IFBA": "BA",
    "UFC": "CE", "UFCA": "CE", "UNILAB": "CE", "IFCE": "CE", "UNIFOR": "CE",
    "UFPB": "PB", "UFCG": "PB", "IFPB": "PB",
    "UFRN": "RN", "UFERSA": "RN", "IFRN": "RN",
    "UFAL": "AL", "IFAL": "AL",
    "UFS": "SE", "IFS": "SE",
    "UFMA": "MA", "IFMA": "MA",
    "UFPI": "PI", "IFPI": "PI",
    "UFPA": "PA", "UFRA": "PA", "UFOPA": "PA", "UNIFESSPA": "PA", "IFPA": "PA",
    "UFAM": "AM", "IFAM": "AM",
    "UFAC": "AC", "IFAC": "AC",
    "UNIR": "RO", "IFRO": "RO",
    "UFRR": "RR", "IFRR": "RR",
    "UNIFAP": "AP", "IFAP": "AP",
    "UFT": "TO", "IFTO": "TO",
    "UFES": "ES", "IFES": "ES",
    "UFMG": "MG", "UFU": "MG", "UFJF": "MG", "UFV": "MG", "UFOP": "MG", "UFSJ": "MG",
    "UFLA": "MG", "UNIFAL": "MG", "UNIFEI": "MG", "UFTM": "MG", "UFVJM": "MG", "IFNMG": "MG", "IFMG": "MG",
    "UFRJ": "RJ", "UFF": "RJ", "UERJ": "RJ", "UNIRIO": "RJ", "UFRRJ": "RJ", "IFRJ": "RJ", "IFF": "RJ",
    "USP": "SP", "UNICAMP": "SP", "UNESP": "SP", "UNIFESP": "SP", "UFSCAR": "SP", "UFABC": "SP", "IFSP": "SP",
    "UFPR": "PR", "UTFPR": "PR", "UNILA": "PR", "UEL": "PR", "UEM": "PR", "IFPR": "PR",
    "UFSC": "SC", "UDESC": "SC", "UFFS": "SC", "IFSC": "SC", "IFC": "SC", "UNIVALI": "SC",
    "UFRGS": "RS", "UFSM": "RS", "UFPEL": "RS", "FURG": "RS", "UNIPAMPA": "RS", "UFCSPA": "RS", "IFRS": "RS",
}

UNB_ACRONYMS: dict[str, str] = {
    "DEX": "Decanato de Extensão (DEX)",
    "DEG": "Decanato de Ensino de Graduação (DEG)",
    "DPG": "Decanato de Pós-Graduação (DPG)",
    "DAC": "Decanato de Assuntos Comunitários (DAC)",
    "DPO": "Decanato de Planejamento, Orçamento e Avaliação Institucional (DPO)",
    "DAF": "Decanato de Administração (DAF)",
    "DGP": "Decanato de Gestão de Pessoas (DGP)",
    "DPI": "Decanato de Pesquisa e Inovação (DPI)",
    "DCADE": "Diretoria de Capacitação, Desenvolvimento e Educação (DCADE)",
    "CAC": "Coordenadoria de Acompanhamento da Carreira (CAC)",
    "COGED": "Coordenadoria de Gestão de Desempenho (COGED)",
    "PROCAP": "Coordenadoria de Capacitação (PROCAP)",
    "CDT": "Centro de Apoio ao Desenvolvimento Tecnológico (CDT)",
    "CDS": "Centro de Desenvolvimento Sustentável (CDS)",
    "CEAM": "Centro de Estudos Avançados Multidisciplinares (CEAM)",
    "CCOM": "Centro de Comunicação (CCOM)",
    "FAV": "Faculdade de Agronomia e Medicina Veterinária (FAV)",
    "FAU": "Faculdade de Arquitetura e Urbanismo (FAU)",
    "FCI": "Faculdade de Ciência da Informação (FCI)",
    "FAC": "Faculdade de Comunicação (FAC)",
    "DAP": "Departamento de Audiovisuais e Publicidade (DAP)",
    "COM": "Departamento de Comunicação Organizacional (COM)",
    "JOR": "Departamento de Jornalismo (JOR)",
    "FACE": "Faculdade de Economia, Administração, Contabilidade e Gestão de Políticas Públicas (FACE)",
    "ADM": "Departamento de Administração (ADM)",
    "CCA": "Departamento de Ciências Contábeis e Atuariais (CCA)",
    "ECO": "Departamento de Economia (ECO)",
    "GPP": "Departamento de Gestão de Políticas Públicas (GPP)",
    "FE": "Faculdade de Educação (FE)",
    "FT": "Faculdade de Tecnologia (FT)",
    "ENC": "Departamento de Engenharia Civil e Ambiental (ENC)",
    "EPR": "Departamento de Engenharia de Produção (EPR)",
    "ENE": "Departamento de Engenharia Elétrica (ENE)",
    "EFL": "Departamento de Engenharia Florestal (EFL)",
    "ENM": "Departamento de Engenharia Mecânica (ENM)",
    "EAS": "Coordenação de Engenharia Aeroespacial (EAS)",
    "FCTS": "Faculdade de Ciências e Tecnologias em Saúde — Campus Ceilândia (FCE/FCTS)",
    "FCE": "Faculdade UnB Ceilândia (FCE)",
    "FCTE": "Faculdade de Ciências e Tecnologias em Engenharia — Campus Gama (FGA/FCTE)",
    "FGA": "Faculdade UnB Gama (FGA)",
    "FUP": "Faculdade UnB Planaltina (FUP)",
    "IDA": "Instituto de Artes (IdA)",
    "DIN": "Departamento de Design (DIN)",
    "IPOL": "Instituto de Ciência Política (IPOL)",
    "IB": "Instituto de Ciências Biológicas (IB)",
    "IE": "Instituto de Ciências Exatas (IE)",
    "CIC": "Departamento de Ciência da Computação (CIC)",
    "EST": "Departamento de Estatística (EST)",
    "MAT": "Departamento de Matemática (MAT)",
    "ICS": "Instituto de Ciências Sociais (ICS)",
    "DAN": "Departamento de Antropologia (DAN)",
    "ELA": "Departamento de Estudos Latino-Americanos (ELA)",
    "SOL": "Departamento de Sociologia (SOL)",
    "IF": "Instituto de Física (IF)",
    "IL": "Instituto de Letras (IL)",
    "IP": "Instituto de Psicologia (IP)",
    "IQ": "Instituto de Química (IQ)",
    "IREL": "Instituto de Relações Internacionais (IREL)",
    "IG": "Instituto de Geociências (IG)",
    "FD": "Faculdade de Direito (FD)",
    "FM": "Faculdade de Medicina (FM)",
    "FS": "Faculdade de Ciências da Saúde (FS)",
    "DCE": "Diretório Central dos Estudantes Honestino Guimarães (DCE)",
}


def resolve_uf(raw_uf: str | None, email: str = "", institution_name: str = "") -> str:
    """Resolve deterministicamente a UF de 2 letras a partir de valor bruto, domínio ou sigla."""
    if raw_uf:
        cleaned = raw_uf.strip()
        upper = cleaned.upper()
        if upper in VALID_UFS:
            return upper
        lower = cleaned.lower()
        if lower in STATE_NAME_TO_UF:
            return STATE_NAME_TO_UF[lower]

    domain = email.split("@")[-1].strip().lower() if "@" in email else ""
    if domain:
        for dom_suffix, uf in DOMAIN_TO_UF.items():
            if domain == dom_suffix or domain.endswith("." + dom_suffix):
                return uf

    upper_name = (institution_name or "").upper()
    for token, uf in sorted(INST_TOKEN_TO_UF.items(), key=lambda kv: -len(kv[0])):
        if re.search(rf"\b{re.escape(token)}\b", upper_name):
            return uf

    for state_name, uf in STATE_NAME_TO_UF.items():
        if state_name in (institution_name or "").lower():
            return uf

    return ""


def normalize_department(raw_dept: str | None, email: str = "", inst_name: str = "") -> str:
    """Limpa artefatos de planilha ('nan', 'Unnamed:', siglas soltas) e infere setor real pelo e-mail."""
    dept = (raw_dept or "").strip()
    if dept.lower() in {"nan", "none", "null", "-", "setor específico", "departamento (outros)"}:
        dept = ""
    if "unnamed:" in dept.lower():
        dept = ""

    # Se for sigla da UnB isolada, expande para nome oficial
    upper_dept = dept.upper()
    if upper_dept in UNB_ACRONYMS:
        return UNB_ACRONYMS[upper_dept]

    # Se departamento ainda estiver vazio ou genérico (ex: 'Instituto Federal (Várias Cidades)')
    generic_markers = (
        "instituto federal (",
        "faculdade privada (",
        "centro universitário privado (",
        "universidade privada (",
        "universidade federal (",
        "universidade estadual (",
    )
    if not dept or dept.lower().startswith(generic_markers):
        local = email.split("@")[0].lower() if "@" in email else ""
        if local.startswith("gabinete.") and len(local.split(".")) >= 2:
            campus = local.split(".", 1)[1].replace("_", " ").title()
            return f"Gabinete da Direção-Geral — Campus {campus}"
        if local.startswith("secretaria.") and len(local.split(".")) >= 2:
            sector = local.split(".", 1)[1].replace("_", " ").title()
            return f"Secretaria — {sector}"
        if "psicologia" in local or "psico" in local:
            return "Departamento / Coordenação de Psicologia"
        if any(k in local for k in ("reitor", "gabinete")):
            return "Reitoria / Gabinete"
        if any(k in local for k in ("prograd", "graduacao", "deg", "prg", "proen")):
            return "Pró-Reitoria / Coordenação de Graduação"
        if any(k in local for k in ("proex", "extensao", "dex")):
            return "Pró-Reitoria / Coordenação de Extensão"
        if any(k in local for k in ("pesquisa", "pos", "prppg", "dpg")):
            return "Pró-Reitoria / Coordenação de Pós-Graduação e Pesquisa"
        if any(k in local for k in ("ascom", "comunicacao", "imprensa")):
            return "Assessoria de Comunicação (ASCOM)"
        if any(k in local for k in ("secretaria", "registro", "cra", "daa", "sga")):
            return "Secretaria Acadêmica / Registro Escolar"
        if local.startswith("ca") and ("unb" in email or "gmail.com" in email):
            return f"Centro Acadêmico ({dept or local.upper()})"
        if not dept:
            return "Atendimento Institucional / Secretaria Geral"

    return re.sub(r"\s+", " ", dept).strip()
