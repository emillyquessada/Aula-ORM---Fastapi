from fastapi import FastAPI

#Inicializar o fastapi

app = FastAPI(title="Gestão escolar")

#Rota
#Métodos http: GET(pegar), POST(adicionar), PUT(atualizar), DELETE(deletar)

#Rodar API
# No terminal: python -m uvicorn main:app --reload
@app.get("/")
def tela_inicial():
    return{"mensagem": "Bem-vindo ao sistema de gestão escolar" }

#Banco de dados

alunos = {
    1: {"nome": "Emilly", "idade": 16},
    2: {"nome": "Balder", "idade": 17},
    3: {"nome": "Vitória", "idade": 17},
}

@app.get("/alunos")
def listar_alunos():
    return {"alunos": alunos}