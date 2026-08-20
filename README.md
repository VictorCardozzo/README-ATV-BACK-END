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

   pip install flask

   python app.py

   {
  "nome": "Mariana Costa",
  "email": "mariana.costa@email.com",
  "cargo": "Desenvolvedora Frontend"
}

{
  "status": "success",
  "data": {
    "id": 3,
    "nome": "Mariana Costa",
    "email": "mariana.costa@email.com",
    "cargo": "Desenvolvedora Frontend"
  }
}

{
  "status": "success",
  "data": {
    "id": 3,
    "nome": "Mariana Costa",
    "email": "mariana.costa@email.com",
    "cargo": "Desenvolvedora Frontend"
  }
}

{
  "nome": "Usuário Sem Email"
}

{
  "status": "error",
  "error": "Campos 'nome' e 'email' são obrigatórios."
}

{
  "status": "error",
  "error": "Usuário não encontrado."
}