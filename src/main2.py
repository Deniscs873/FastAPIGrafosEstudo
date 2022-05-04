import email
from multiprocessing.reduction import send_handle
from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def raiz():
    return {"Rotas": "Minha primeira API" }

# Criar model

class rota(BaseModel):
    id: int
    source: str
    target: str
    distance: int
    

# criar base de dados

base_de_dados = [
    # rota(id=0, source="A", target="B", distance=5)
]

# Rota getAll

@app.get("/rotas")
def get_todas_as_rotas():
    return base_de_dados


# Rota getId

@app.get("/rotas/{id_rota}")
def get_rotas_usando_id(id_rota: int):
    for rota in base_de_dados:
        if(rota.id == id_rota):
            return rota

    return {"Status": 404, "Mensagem": "Não encontrou rota"}

# Rota Insere

@app.post("/rota")
def insere_rotas(rota: rota):
    # Criar regras de negocio
    base_de_dados.append(rota)
    return rota

