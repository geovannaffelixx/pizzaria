from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta
from fastapi import Request, HTTPException

SECRET_KEY = "chave-da-pizzaria"
ALGORITHM = "HS256"

def criar_token(usuario_id: int, nome: str, tipo: str):
    payload = {"sub": str(usuario_id), "nome": nome, "tipo": tipo, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def validar_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

def obter_usuario_atual(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token não fornecido")
    token = auth_header.split(" ")[1]
    dados = validar_token(token)
    if "sub" not in dados or "tipo" not in dados:
        raise HTTPException(status_code=401, detail="Token malformado")
    return {"id": int(dados["sub"]), "nome": dados["nome"], "tipo": dados["tipo"]}
