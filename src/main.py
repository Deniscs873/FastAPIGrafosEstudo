"""API educacional de usuários: dados demonstrativos, sem senhas nas respostas.

Não utilize armazenamento em memória nem usuários demonstrativos em produção.
"""
from hashlib import pbkdf2_hmac
from hmac import compare_digest
from os import urandom

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI — Estudo de Rotas", version="1.1.0")


class UsuarioEntrada(BaseModel):
    id: int = Field(gt=0)
    email: str = Field(min_length=3)
    senha: str = Field(min_length=8)


class UsuarioPublico(BaseModel):
    id: int
    email: str


def hash_senha(senha: str) -> tuple[bytes, bytes]:
    """PBKDF2 com salt aleatório; em produção use autenticação dedicada."""
    salt = urandom(16)
    digest = pbkdf2_hmac("sha256", senha.encode(), salt, 600_000)
    return salt, digest


def senha_confere(senha: str, salt: bytes, digest: bytes) -> bool:
    return compare_digest(pbkdf2_hmac("sha256", senha.encode(), salt, 600_000), digest)


# Armazenamento temporário exclusivamente para estudo. Sem credenciais embutidas.
base_de_dados: dict[int, dict] = {}


@app.get("/")
def raiz():
    return {"mensagem": "API de exemplo educacional", "docs": "/docs"}


@app.get("/usuarios", response_model=list[UsuarioPublico])
def get_todos_os_usuarios():
    return [UsuarioPublico(id=u["id"], email=u["email"]) for u in base_de_dados.values()]


@app.get("/usuarios/{id_usuario}", response_model=UsuarioPublico)
def get_usuario_usando_id(id_usuario: int):
    usuario = base_de_dados.get(id_usuario)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return UsuarioPublico(id=usuario["id"], email=usuario["email"])


@app.post("/usuario", response_model=UsuarioPublico, status_code=status.HTTP_201_CREATED)
def insere_usuario(usuario: UsuarioEntrada):
    if usuario.id in base_de_dados:
        raise HTTPException(status_code=409, detail="ID já cadastrado")
    salt, digest = hash_senha(usuario.senha)
    base_de_dados[usuario.id] = {
        "id": usuario.id,
        "email": usuario.email,
        "salt": salt,
        "hash": digest,
    }
    return UsuarioPublico(id=usuario.id, email=usuario.email)
