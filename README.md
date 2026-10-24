# FastAPI — API educacional de usuários e algoritmos de grafos

Repositório de exercícios de Python/FastAPI e algoritmos de grafos. **Não é um serviço preparado para produção.**

## Executar a API

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install fastapi uvicorn
uvicorn src.main:app --reload
```

Acesse `http://127.0.0.1:8000/docs`. O armazenamento é somente em memória e é reiniciado com o processo.

### Endpoints

- `GET /` — status e acesso à documentação
- `GET /usuarios` — lista apenas `id` e `email`
- `GET /usuarios/{id_usuario}` — dados públicos ou HTTP 404
- `POST /usuario` — recebe `id`, `email` e `senha` (mínimo de 8 caracteres); devolve apenas `id` e `email`

As senhas não são registradas em claro no armazenamento temporário nem retornadas pelas rotas. A autenticação completa, controle de acesso, persistência, TLS e testes de segurança **não estão implementados**.

## Atenção à segurança

Versões antigas continham senhas fictícias no código de exemplo. Mesmo após as alterações, os commits antigos permanecem no histórico. Nunca utilize credenciais verdadeiras em código ou notebooks. O ambiente virtual anteriormente rastreado permanece no histórico e deve ser removido do controle de versão após revisão cuidadosa.

## Estrutura

- `src/main.py`: API educacional
- `src/`: implementações de algoritmos e grafos

## Autor

[Denis Correia](https://github.com/Deniscs873)
