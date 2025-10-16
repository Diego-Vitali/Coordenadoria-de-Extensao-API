import re
from .exceptions import ValidationError

def format_cep(cep: str) -> str:
    return re.sub(r'[^0-9]', '', cep)

def is_valid_cep(cep: str) -> bool:
    cep = format_cep(cep)
    return cep.isdigit() and len(cep) == 8

def validate_cep(cep: str):
    cep = format_cep(cep)
    if not cep.isdigit():
        raise ValidationError("CEP inválido: deve conter apenas números.")
    if len(cep) != 8:
        raise ValidationError(f"CEP inválido: deve conter 8 dígitos, mas contém {len(cep)}.")