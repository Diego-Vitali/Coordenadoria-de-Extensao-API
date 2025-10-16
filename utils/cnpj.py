import re
from .exceptions import ValidationError

def format_cnpj(cnpj: str) -> str:
    return re.sub(r'[^0-9]', '', cnpj)

def is_valid_cnpj(cnpj: str) -> bool:
    cnpj = format_cnpj(cnpj)

    if len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False
    
    weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_ = sum(int(cnpj[i]) * weights[i] for i in range(12))
    digit1 = 0 if (sum_ % 11) < 2 else 11 - (sum_ % 11)
    if int(cnpj[12]) != digit1:
        return False
        
    weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_ = sum(int(cnpj[i]) * weights[i] for i in range(13))
    digit2 = 0 if (sum_ % 11) < 2 else 11 - (sum_ % 11)
    if int(cnpj[13]) != digit2:
        return False
        
    return True

def validate_cnpj(cnpj: str):
    if not is_valid_cnpj(cnpj):
        raise ValidationError("O número do CNPJ é inválido.")

def mask_cnpj(cnpj: str) -> str:
    cnpj = format_cnpj(cnpj)
    if len(cnpj) != 14:
        return cnpj # Retorna o original se não for um CNPJ formatável
    return f"{cnpj[:2]}.***.***/{cnpj[8:12]}-**"