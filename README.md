# 🐾 Petfy API

API REST desenvolvida com **FastAPI** para gerenciar pets disponíveis para adoção.  
Projeto dockerizado, organizado em pastas e pronto pra escalar, testar e conquistar aquele trampo tech.  
Feito por uma dev braba com carinho, persistência e um tiquinho de caos. ❤️‍🔥

---

## 🛠️ Tecnologias usadas

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy + SQLite**
- **Docker + Docker Compose**
- *(Em breve)* Pytest para testes automatizados

---

## 📁 Estrutura de pastas

```

petfy\_api/
├── app/
│   ├── core/         # Configurações (ex: banco)
│   ├── crud/         # Funções de acesso ao banco
│   ├── models/       # Modelos SQLAlchemy
│   ├── routes/       # Rotas da API
│   ├── schemas/      # Schemas do Pydantic
│   └── main.py       # Arquivo principal da FastAPI
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

````

---

## ▶️ Como rodar com Docker

1. Clone o projeto:

```bash
git clone https://github.com/seu-usuario/petfy_api.git
cd petfy_api
````

2. Gere o `requirements.txt` com:

```bash
pip freeze > requirements.txt
```

3. Construa e rode o container:

```bash
docker-compose up --build
```

4. Acesse a documentação da API:

* Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
* Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📮 Endpoints da API

| Método | Rota       | Descrição            |
| ------ | ---------- | -------------------- |
| GET    | /pets      | Lista todos os pets  |
| GET    | /pets/{id} | Detalha um pet       |
| POST   | /pets      | Cadastra um novo pet |
| PUT    | /pets/{id} | Atualiza um pet      |
| DELETE | /pets/{id} | Remove um pet        |

---

## 🧪 Testes (em breve)

```bash
pytest
```

---

## 🤟 Sobre

Feito por **[Karol](https://github.com/KarolNutty)** — dev em formação, futura AI Developer, encantada por containers, automações e APIs com propósito.
💼 Em busca de criar soluções reais com tecnologia e amor.

---




