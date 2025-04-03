# API de Biblioteca de Livros

Este projeto implementa uma **API de Biblioteca de Livros** utilizando o framework **FastAPI** para o backend e **MongoDB** como banco de dados NoSQL. A API permite que usuários consultem, adicionem, atualizem e excluam livros em uma biblioteca digital.

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno e rápido para construção de APIs com Python.
- **MongoDB**: Banco de dados NoSQL, utilizado para armazenar os dados dos livros.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **Jinja2**: Motor de templates utilizado para renderizar as páginas HTML.
- **Pydantic**: Biblioteca para validação e definição de modelos de dados.

## Funcionalidades da API

A API oferece as seguintes rotas para gerenciamento da biblioteca de livros:

- **GET /**: Exibe a lista de livros em uma página HTML, com a possibilidade de paginar.
- **GET /books**: Exibe os livros em uma página HTML.
- **POST /books**: Adiciona um novo livro à biblioteca.
- **PUT /books/{book_id}**: Atualiza um livro existente.
- **DELETE /books/{book_id}**: Exclui um livro da biblioteca.

## Requisitos

Antes de rodar o projeto, você precisa ter os seguintes requisitos instalados:

- **Python 3.7 ou superior**
- **MongoDB** (local ou na nuvem, como o MongoDB Atlas)

## Como Rodar o Projeto

### 1. Clonando o Repositório

Primeiro, faça o clone do repositório:

```bash
git clone https://github.com/NowhereSA/GUI-Example.git
cd GUI-Example
```

### 2. Instalando as Dependências

Crie um ambiente virtual e instale as dependências do projeto:

```bash
pip install fastapi uvicorn pymongo jinja2 pydantic
```

### 3. Configuração do MongoDB

Certifique-se de que o **MongoDB** esteja rodando. Você pode usar uma instância local do MongoDB ou configurar um banco de dados na nuvem com o **MongoDB Atlas**.

No arquivo `database.py`, configure a URL de conexão com o MongoDB:

```python
from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017")
    db = client.biblioteca
    return db
```

### 4. Rodando a Aplicação

Execute o servidor utilizando o comando:

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

## Endpoints da API

### **GET /**

Recupera a lista de livros da biblioteca e exibe em uma página HTML com paginação.

**Parâmetros de Query (opcionais):**
- `skip` (default: 0): Número de livros a serem pulados.
- `limit` (default: 10): Número máximo de livros a serem retornados.

### **GET /books**

Exibe todos os livros cadastrados em uma página HTML.

### **POST /books**

Adiciona um novo livro à biblioteca. O corpo da requisição deve conter as informações do livro no formato:

```json
{
  "titulo": "O Senhor dos Anéis",
  "autor": "J.R.R. Tolkien",
  "genero": "Fantasia",
  "status": "Disponível",
  "descricao": "Um épico de fantasia."
}
```

**Resposta:**

```json
{
  "message": "Adicionado com sucesso!"
}
```

### **PUT /books/{book_id}**

Atualiza as informações de um livro existente. O `book_id` é o identificador único do livro a ser atualizado.

**Exemplo de corpo da requisição:**

```json
{
  "titulo": "O Senhor dos Anéis - Edição Especial",
  "autor": "J.R.R. Tolkien",
  "genero": "Fantasia",
  "status": "Em processo de devolução",
  "descricao": "Uma edição especial do épico de fantasia."
}
```

**Resposta:**

```json
{
  "message": "Livro atualizado com sucesso!"
}
```

### **DELETE /books/{book_id}**

Deleta um livro da biblioteca. O `book_id` é o identificador único do livro a ser deletado.

**Resposta:**

```json
{
  "message": "Deletado com sucesso"
}
```

## Estrutura do Projeto

```
.
├── app
│   ├── __init__.py
│   ├── main.py           # Arquivo principal da API
│   ├── models.py         # Modelos de dados
│   ├── routes.py         # Endpoint da API
│   ├── database.py       # Conexão com o MongoDB
│   ├── static            # Arquivos CSS
│   └── templates         # Arquivos HTML renderizados com Jinja2
└── README.md             # Este arquivo
```