# 🚀 API de Foco e Produtividade

API backend desenvolvida em Python com FastAPI para registro e análise de produtividade baseada em nível de foco durante sessões de estudo ou trabalho.

O sistema registra sessões e gera um diagnóstico automático com base nos dados inseridos.

---

# 🧠 Objetivo do projeto

O objetivo é simular um log de performance pessoal, onde o usuário registra seu nível de foco durante atividades e recebe um diagnóstico inteligente sobre sua produtividade.

---

# 🛠 Tecnologias utilizadas

- Python 3.11+
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Uvicorn
- Alembic (migrations)

---

# 📦 Instalação

## Clonar o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPO.git  
cd SEU_REPO  

## Criar ambiente virtual
python -m venv .venv  

## Ativar ambiente virtual (Windows PowerShell)
.venv\Scripts\activate  

## Instalar dependências
pip install fastapi uvicorn sqlalchemy pymysql alembic pydantic  

---

# 🗄 Configuração do banco (MySQL)

## Criar banco
CREATE DATABASE produtividade;

## Configurar conexão (database.py)
DATABASE_URL = "mysql+pymysql://root:SUA_SENHA@localhost/produtividade"

## Rodar migrations
alembic upgrade head  

---

# ▶️ Como rodar o projeto

uvicorn app.main:app --reload  

ou  

python -m uvicorn app.main:app --reload  

---

# 🌐 Acessos

Swagger da API:
http://127.0.0.1:8000/docs  

---

# 📡 Endpoints

## POST /registro-foco

Registra uma sessão de produtividade:

{
  "nivel_foco": 5,
  "tempo_minutos": 60,
  "comentario": "estudando FastAPI",
  "categoria": "estudo"
}

---

## GET /registros

Lista todos os registros salvos.

---

## GET /diagnostico-produtividade

Retorna análise da produtividade:

{
  "media_foco": 4.2,
  "tempo_total": 120,
  "feedback": "Excelente produtividade"
}

---

# 📊 Regras de negócio

- nível de foco: 1 a 5  
- tempo mínimo: maior que 0  
- dados armazenados em MySQL  
- data de criação automática (UTC)

---

# ⚠️ Validações

- nível de foco inválido → erro 400  
- tempo inválido → erro 400  

---

# 🧱 Estrutura do projeto

app/  
 ├── main.py  
 ├── routes/  
 ├── models/  
 ├── schemas/  
 ├── services/  
 ├── database.py  
 └── core/  

---

# 💡 Diferenciais implementados

- validação de dados com Pydantic  
- arquitetura modular (routes/services/models)  
- persistência em banco MySQL  
- diagnóstico automático de produtividade  
- tratamento de exceções
