import email
from multiprocessing.reduction import send_handle
from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def raiz():
    return {"Hello World": "Minha primeira API" }

# Criar model

class Usuario(BaseModel):
    id: int
    email: str
    senha: str

# criar base de dados

base_de_dados = [
    Usuario(id=1, email="deniscs873@hotmail.com", senha="Deniscs873"),
    Usuario(id=2, email="teste@teste.com.br", senha="teste123")
]

# Rota getAll

@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados


# Rota getId

@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario

    return {"Status": 404, "Mensagem": "Não encontrou usuario"}

# Rota Insere

@app.post("/usuario")
def insere_usuario(usuario: Usuario):
    # Criar regras de negocio
    base_de_dados.append(usuario)
    return usuario