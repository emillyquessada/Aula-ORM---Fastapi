from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Curso, Aluno

#pip install jinja2 python-multipart
#Inicializar o fastapi

app = FastAPI(title="Gestão escolar")

templates = Jinja2Templates(directory="templates")

#Rota
#Métodos http: GET(pegar), POST(adicionar), PUT(atualizar), DELETE(deletar)

#Rodar API
# No terminal: python -m uvicorn main:app --reload

@app.get("/cursos/cadastro")
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "cadastrar_curso.html",
        {"request": request}
    )

# rota para cadastrar um curso
@app.post("/cursos")
def criar_curso(
    nome: str = Form(...),
    carga_hr: int = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    #cadastrar o curso no banco
    novo_curso = Curso(nome=nome, carga_hr=carga_hr, descricao=descricao)
    db.add(novo_curso)
    db.commit()

    return RedirectResponse(url="/cursos", status_code=303)


@app.get("/")
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request}
    )

@app.get("/listar_cursos")
def listar_cursos(
    request: Request,
    db: Session = Depends(get_db)
    ):

    cursos = db.query(Curso).all()
    return templates.TemplateResponse(
        request,
        "listar_cursos.html",
        {"request": request, "cursos":cursos}
    )

#Rota para deletar

@app.post("/cursos/{id}/deletar")
def deletar_curso(
    id: int, 
    db: Session = Depends(get_db)
):
    curso = db.query(Curso).get(id)

    if curso:
        db.delete(curso)
        db.commit()

    return RedirectResponse(url="/listar_cursos", status_code=303)