from fastapi import FastAPI
from schemas import ValidacaoDocumentoSchema
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Coordenadoria": "Extensão"}

@app.post("/validacao/")
async def validar_documento_estagio(doc: ValidacaoDocumentoSchema):
    # Aqui a gente adicionar a lógica de validação dos dados e etc...
    return {"status": "Documento de estágio validado com sucesso."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)