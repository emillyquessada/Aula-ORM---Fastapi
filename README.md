# Instalar as bibliotecas:
# pip install fastapi uvicorn sqlalchemy alembic python-dotenv

# No terminal inicie o alembic
# python -m alembic init alembic

# Configurando a conexão com o db
# ---------------------------------

# Abra o arquivo alembic.ini
# e procure a linha com essa informação (provavelmente na linha 89):
# sqlalchemy.url = driver://user:pass@localhost/dbname

# Conectando o alembic ao sqlalchemy
# ----------------------------------

# Abre o arquivo:
# alembic/env.py

# Importe a Base no arquivo env.py
# from models import Base
# Encontre a linha com:
# target_metadata = None
# e altere para:
# target_metadata = Base.metadata

# Criando as migrações - Qualquer alteração no banco
# ----------------------------------

# no terminal rodar o comando:
# python -m alembic revision --autogenerate -m "Criando as tabelas"
# Depois rodar o comando:
# python -m alembic upgrade head       
# Para executar as alterações no banco.