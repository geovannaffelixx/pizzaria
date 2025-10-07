Sistema backend para pizzaria com autenticação JWT, desenvolvido em FastAPI (Python).

- Login com JWT
- CRUD
- Registro e cálculo de pedidos
- Organização por separada (Routers, Controllers, Models, Database, Autenticação)
- Uso de SOLID

Linguagem: Python 3.13
Framework: FastAPI
ORM: SQLAlchemy
Banco de Dados: SQLite
Autenticação: JWT (python-jose)
Validação: Pydantic v2
Servidor: Uvicorn

--------------------------------------------------------------------------------------

Como executar o Projeto


- Execute em ordem os comandos abaixo no terminal

Dentro da pasta do projeto
py -m venv .venv
source .venv/Scripts/activate
pip install fastapi uvicorn sqlalchemy python-jose[cryptography]

uvicorn main:app --reload
ou
py -m uvicorn main:app --reload 


- Acesse

http://127.0.0.1:8000/docs

