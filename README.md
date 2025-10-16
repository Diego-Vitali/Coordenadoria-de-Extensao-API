# Coordenadoria de Extensão API

API para o projeto da Coordenadoria de Extensão.

Siga estas instruções para configurar e rodar o projeto em seu ambiente de desenvolvimento local.

### Pré-requisitos

-   [Python 3.8+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Diego-Vitali/Coordenadoria-de-Extensao-API.git](https://github.com/Diego-Vitali/Coordenadoria-de-Extensao-API.git)
    cd Coordenadoria-de-Extensao-API
    ```

2.  **Crie e ative o ambiente virtual:**

    -   **Windows:**
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```

    -   **Linux / macOS:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    > O ambiente virtual isola as dependências do projeto, evitando conflitos com outros projetos em sua máquina.

3.  **Instale as dependências:**
    Com o ambiente virtual ativo, instale as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```

### Rodando a Aplicação

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn api.main:app --reload
```

Após executar o comando, o servidor estará ativo nos endereços:

-   **URL Local:** `http://127.0.0.1:8000`
-   **Documentação (Swagger UI):** `http://127.0.0.1:8000/docs`