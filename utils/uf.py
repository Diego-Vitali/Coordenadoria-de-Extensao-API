from .exceptions import ValidationError

UFS = {
    "AC": "Acre", 
    "AL": "Alagoas", 
    "AP": "Amapá", 
    "AM": "Amazonas",
    "BA": "Bahia", 
    "CE": "Ceará", 
    "DF": "Distrito Federal", 
    "ES": "Espírito Santo",
    "GO": "Goiás", 
    "MA": "Maranhão", 
    "MT": "Mato Grosso", 
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais", 
    "PA": "Pará", 
    "PB": "Paraíba", 
    "PR": "Paraná",
    "PE": "Pernambuco", 
    "PI": "Piauí", 
    "RJ": "Rio de Janeiro", 
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul", 
    "RO": "Rondônia", 
    "RR": "Roraima", 
    "SC": "Santa Catarina",
    "SP": "São Paulo", 
    "SE": "Sergipe", 
    "TO": "Tocantins",
}

def is_valid_uf(uf: str) -> bool:
    return uf.upper() in UFS

def validate_uf(uf: str):
    if not is_valid_uf(uf):
        raise ValidationError("UF inválida.")