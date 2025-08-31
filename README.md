
# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde (Back-End)

Este projeto é uma API desenvolvida em Python com FastAPI, que faz parte do Trabalho de Conclusão de Curso (TCC) focado na gestão de pacientes, consultas, prontuários e controle de usuários em um sistema de saúde.

---

## 🚀 Funcionalidades principais

- 🔐 **Autenticação com JWT**
- 👥 **CRUD de Usuários**
- 🧑‍⚕️ **CRUD de Pacientes**
- 📅 **CRUD de Consultas**
- 📄 **CRUD de Prontuários**
- 📝 **Logs automáticos** de operações realizadas no sistema

---

## 🛠️ Tecnologias utilizadas

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Uvicorn**
- **Pydantic**
- **Passlib (Hash de senha)**
- **PyJWT (Token JWT)**

---

## 🎯 Como rodar o projeto localmente

### 🔥 Pré-requisitos

- Python instalado (versão 3.10 ou superior)
- PostgreSQL instalado e rodando

### 🚧 Clone o repositório

```bash
git clone https://github.com/gabrieleMarciano/TCCAPIBACKEND.git
cd TCCAPIBACKEND
```

### 📦 Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 📜 Instale as dependências

```bash
pip install -r requirements.txt
```

### 🗄️ Configure o banco de dados

- Crie um banco chamado **`sghss`** no PostgreSQL.

- Execute o script SQL em `/sql/script.sql` para criar as tabelas:

```bash
psql -U seu_usuario -d sghss -f sql/script.sql
```

### ⚙️ Configure o ambiente (opcional)

Crie um arquivo `.env` (se desejar centralizar configs) com:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/sghss
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 🚀 Rode a API

```bash
uvicorn main:app --reload
```

---

## 📑 Documentação interativa

- Acesse a documentação automática em:

```plaintext
http://127.0.0.1:8000/docs
```

ou

```plaintext
http://127.0.0.1:8000/redoc
```

---

## 🗺️ Estrutura de pastas

```plaintext
app/
│
├── auth/                 # Gerenciamento de autenticação e tokens
├── crud/                 # Operações CRUD (database)
├── database.py           # Conexão com banco
├── models/               # Models (ORM)
├── routers/              # Rotas da API
├── schemas/              # Validações e serialização (Pydantic)
├── logs/                 # Lógica de geração de logs
main.py                   # Arquivo principal da API
sql/                      # Scripts SQL de criação de tabelas
requirements.txt          # Dependências
README.md                 # Descrição do projeto
```

---

## 📜 Script SQL de criação das tabelas

Disponível em: [`/sql/script.sql`](./sql/script.sql)

---

## 👩‍💻 Autor

Desenvolvido por [Gabriele Marciano](https://github.com/gabrieleMarciano) 🎓💙

---

## 🏁 Status do Projeto

✔️ **Concluído - TCC 2025**

