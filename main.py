from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from routers import usuarios, pizzas, pedidos, auth, ingredientes
from database.config import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI(title="Pizzaria API")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Pizzaria API",
        version="1.0.0",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.include_router(usuarios.router)
app.include_router(pizzas.router)
app.include_router(ingredientes.router)
app.include_router(pedidos.router)
app.include_router(auth.router)

@app.get("/")
def raiz():
    return {"mensagem": "API da pizzaria funcionando"}
