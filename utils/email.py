import re
from .exceptions import ValidationError

def is_valid_email(email: str) -> bool:
    if not email: return False
    pattern = re.compile(
        r"^[a-zA-Z0-9_+-]+(?:\.[a-zA-Z0-9_+-]+)*@"
        r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
        r"[a-zA-Z]{2,63}$"
    )
    return re.fullmatch(pattern, email) is not None

def validate_email(email: str):
    if not is_valid_email(email):
        raise ValidationError("O formato do e-mail é inválido.")

def mask_email(email: str) -> str:
    try:
        local_part, domain = email.split('@')
        if len(local_part) <= 4:
            return email
        masked_local = local_part[:4] + '*' * (len(local_part) - 4)
        return f"{masked_local}@{domain}"
    except ValueError:
        return email