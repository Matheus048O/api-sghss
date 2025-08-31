
# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde (Back-End)

Este projeto é a API back-end para um Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS) A API, construída com Python e FastAPI, fornece uma base robusta para gerenciar pacientes, consultas, prontuários e o controle de acesso de usuários.

---

## Principais características

-   **Gestão de Pacientes**: CRUD para o registro de informações dos pacientes.
-   **Agendamento de Consultas**: CRUD para marcar e gerenciar consultas.
-   **Administração de Prontuários**: CRUD para o histórico clínico dos pacientes.
-   **Logs de Auditoria**: Registro automático de operações críticas realizadas no sistema para garantir rastreabilidade
-   **Autenticação Segura**: Sistema de login baseado em tokens JWT (JSON Web Token).
-   **Gestão de Usuários**: CRUD completo para criação, visualização, atualização e exclusão de usuários.
.

---

## requisitos

-   **Linguagem**: Python 3.11
-   **Framework**: FastAPI
-   **Banco de Dados**: PostgreSQL
-   **ORM**: SQLAlchemy
-   **Servidor ASGI**: Uvicorn
-   **Validação de Dados**: Pydantic
-   **Segurança**:
    -   `Passlib` para hashing de senhas.
    -   `PyJWT` para geração e validação de tokens de acesso.

---

## Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar a API em seu ambiente de desenvolvimento.

### 1. Pré-requisitos

-   Python 3.10 ou superior instalado.
-   PostgreSQL instalado e com o serviço em execução.

### 2. Clone o Repositório

```bash
git clone https://github.com/Matheus048O/api-sghss.git
cd api-sghss
```

### 3. Crie e Ative um Ambiente Virtual (venv)

Um ambiente virtual isola as dependências do projeto.

```bash
# Criar o ambiente
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/Mac
source venv/bin/activate
```

### 4. Instale as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias.

```bash
pip install -r requirements.txt
```

### 5. Configure o Banco de Dados

-   No seu servidor PostgreSQL, crie um novo banco de dados com o nome `sghss`.
-   **Importante**: A estrutura das tabelas é gerenciada automaticamente pelo SQLAlchemy (ORM) ao iniciar a aplicação, então não é necessário executar scripts SQL manualmente.

### 7. Inicie a API

Execute o servidor Uvicorn. A flag `--reload` reinicia o servidor automaticamente a cada alteração no código.

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

## 🗺️ Estrutura do Projeto

A organização das pastas segue as melhores práticas para projetos FastAPI, separando as responsabilidades:

```
app/
│
├── auth/         # Lógica de autenticação, tokens e segurança.
├── crud/         # Funções que interagem diretamente com o banco de dados.
├── models/       # Definição das tabelas do banco (Modelos SQLAlchemy).
├── routers/      # Definição dos endpoints da API (as rotas).
├── schemas/      # Validação da estrutura de dados de entrada e saída (Esquemas Pydantic).
├── logs/         # Módulos para configuração e gerenciamento de logs.
│
├── database.py   # Configuração da sessão e conexão com o banco.
└── main.py       # Ponto de entrada da aplicação FastAPI.
```