import re
from .exceptions import ValidationError

def format_cpf(cpf: str) -> str:
    return re.sub(r'[^0-9]', '', cpf)

def is_valid_cpf(cpf: str) -> bool:
    cpf = format_cpf(cpf)
    
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    sum_ = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digit1 = 0 if (sum_ % 11) < 2 else 11 - (sum_ % 11)
    if int(cpf[9]) != digit1:
        return False
        
    sum_ = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digit2 = 0 if (sum_ % 11) < 2 else 11 - (sum_ % 11)
    if int(cpf[10]) != digit2:
        return False
        
    return True

def validate_cpf(cpf: str):
    if not is_valid_cpf(cpf):
        raise ValidationError("O número do CPF é inválido.")

def mask_cpf(cpf: str) -> str:
    cpf = format_cpf(cpf)
    if len(cpf) != 11:
        return cpf # Retorna o original se não for um CPF formatável
    return f"{cpf[:3]}.***.***-{cpf[9:]}"