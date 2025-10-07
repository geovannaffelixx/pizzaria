from database.config import SessionLocal
from models.pizza import PizzaDB
from models.usuario import UsuarioDB
from models.ingrediente import IngredienteDB


pizzas_data = [
    {"nome": "Pizza de chocolate com morango", "ingredientes": "Chocolate ao leite e morango", "preco": 55, "tamanho": "Grande"},
    {"nome": "Pizza de chocolate com morango", "ingredientes": "Chocolate ao leite e morango", "preco": 45, "tamanho": "Média"},
    {"nome": "Pizza de chocolate com morango", "ingredientes": "Chocolate ao leite e morango", "preco": 30, "tamanho": "Pequena"},
    {"nome": "Pizza de frango com catupiry", "ingredientes": "Molho, queijo, frango, catupiry e milho", "preco": 30, "tamanho": "Pequena"},
    {"nome": "Pizza de frango com catupiry", "ingredientes": "Molho, queijo, frango, catupiry e milho", "preco": 45, "tamanho": "Média"},
    {"nome": "Pizza de frango com catupiry", "ingredientes": "Molho, queijo, frango, catupiry e milho", "preco": 55, "tamanho": "Grande"},
    {"nome": "Pizza de calabresa", "ingredientes": "Molho, queijo, calabresa, cebola e azeitona", "preco": 55, "tamanho": "Grande"},
    {"nome": "Pizza de calabresa", "ingredientes": "Molho, queijo, calabresa, cebola e azeitona", "preco": 45, "tamanho": "Média"},
]

usuarios_data = [
    {"nome": "Bruno", "tipo": "cliente"},
    {"nome": "Vinicius", "tipo": "cliente"},
    {"nome": "Geovanna", "tipo": "cliente"},
    {"nome": "Samuel", "tipo": "cliente"},
    {"nome": "Pedro", "tipo": "cliente"},
    {"nome": "Rafael", "tipo": "cliente"},
    {"nome": "Amanda", "tipo": "funcionario"},
]

ingredientes_data = [
    {"nome": "Bacon crocante", "preco": 5.0},
    {"nome": "Milho extra", "preco": 3.5},
    {"nome": "Azeitona preta", "preco": 2.5},
    {"nome": "Borda recheada com catupiry", "preco": 6.0},
    {"nome": "Catupiry extra", "preco": 4.0},
    {"nome": "Cebola caramelizada", "preco": 3.0},
    {"nome": "Molho barbecue", "preco": 3.5},
]

def seed_data():
    db = SessionLocal()
    try:
        # Evita duplicar dados
        if db.query(PizzaDB).count() == 0:
            for pizza in pizzas_data:
                db.add(PizzaDB(**pizza))
            print("Pizzas inseridas!")

        if db.query(UsuarioDB).count() == 0:
            for usuario in usuarios_data:
                db.add(UsuarioDB(**usuario))
            print("✅ Usuários inseridos!")

        if db.query(IngredienteDB).count() == 0:
            for ingrediente in ingredientes_data:
                db.add(IngredienteDB(**ingrediente))
            print("✅ Ingredientes extras!")

        db.commit()
        print("🎉 Banco populado!")

    except Exception as e:
        print("Erro ao inserir dados:", e)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
