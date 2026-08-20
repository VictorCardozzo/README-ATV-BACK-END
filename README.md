# API Connect - Gerenciamento de Usuários

O **API Connect** é uma API RESTful desenvolvida em Python com o framework Flask para o gerenciamento e cadastro de colaboradores de uma aplicação.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework:** Flask
* **Arquitetura:** MVC (Model-View-Controller)
* **Testes de API:** Postman

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.x instalado na máquina.
* Git instalado.

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/VictorCardozzo/README-ATV-BACK-END.git](https://github.com/VictorCardozzo/README-ATV-BACK-END.git)
   cd README-ATV-BACK-END

   Instalar as dependências:Bashpip install flask
   
Iniciar o servidor:Bashpython app.py
O servidor iniciará em http://localhost:5000.📌 Documentação dos EndpointsMétodoEndpointDescriçãoStatus SucessoStatus ErroGET/usersLista todos os usuários.200 OK500 Internal ErrorPOST/usersCadastra um novo usuário.201 Created400 Bad RequestGET/users/<id>Busca um usuário por ID.200 OK404 Not FoundExemplos de Requisição e Resposta1. Criar Usuário (POST /users)Body (JSON):JSON{
  "nome": "Mariana Costa",
  "email": "mariana.costa@email.com",
  "cargo": "Desenvolvedora Frontend"
}
Resposta (201 Created):JSON{
  "status": "success",
  "data": {
    "id": 3,
    "nome": "Mariana Costa",
    "email": "mariana.costa@email.com",
    "cargo": "Desenvolvedora Frontend"
  }
}
2. Erro de Validação (POST /users)Body (JSON):JSON{
  "nome": "Usuário Sem Email"
}
Resposta (400 Bad Request):JSON{
  "status": "error",
  "error": "Campos 'nome' e 'email' são obrigatórios."
}
3. Usuário Não Encontrado (GET /users/999)Resposta (404 Not Found):JSON{
  "status": "error",
  "error": "Usuário não encontrado."
}

---

#### 2. Envie o arquivo para o GitHub
Abra o terminal do VS Code e rode estes comandos:

```bash
git add README.md
git commit -m "docs: adiciona o arquivo README.md"
git push