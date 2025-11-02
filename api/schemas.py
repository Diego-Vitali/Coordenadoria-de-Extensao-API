from pydantic import BaseModel
from typing import Optional
from datetime import date, time

# Esses Schemas se referem aos aninhamentos internos dos nós

class EnderecoSchema(BaseModel):
    endereco: str
    cep: str
    bairro: str
    cidade: str
    estado: str

class RepresentanteSchema(BaseModel):
    nome: str
    cargo: str

class RegistroProfissionalSchema(BaseModel):
    numero: str
    orgao: str

# Esses schemas se referem aos nós principais

class UnidadeConcedenteSchema(BaseModel):
    razao_social: str
    cnpj: Optional[str] = None
    insc_estadual: Optional[str] = None
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    endereco: EnderecoSchema
    representante_legal: RepresentanteSchema

class SupervisorSchema(BaseModel):
    nome: str
    cpf: str
    cargo: str
    formacao_academica: str
    registro_profissional: RegistroProfissionalSchema
    email: str

class EstagiarioSchema(BaseModel):
    nome: str
    curso: str
    periodo: str
    prontuario: str
    rg: str
    cpf: str
    data_nascimento: date
    endereco: EnderecoSchema
    telefone: Optional[str] = None
    celular: Optional[str] = None
    email: str
    estagio_obrigatorio: bool
    portador_de_deficiencia: bool

class DadosEstagioSchema(BaseModel):
    data_inicio: date
    data_termino: date
    horario_inicio: time
    horario_termino: time
    horas_semanais: int
    nome_seguradora: str
    numero_apolice_seguro: str
    valor_seguro: float
    valor_bolsa_auxilio: float

# Schema principal para o JSON que será recebido:

class ValidacaoDocumentoSchema(BaseModel):
    unidade_concedente: UnidadeConcedenteSchema
    supervisor: SupervisorSchema
    estagiario: EstagiarioSchema
    dados_estagio: DadosEstagioSchema