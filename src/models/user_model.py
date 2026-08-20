users_db = [
    {"id": 1, "nome": "Ana Silva", "email": "ana.silva@email.com", "cargo": "Desenvolvedora"},
    {"id": 2, "nome": "Carlos Souza", "email": "carlos.souza@email.com", "cargo": "Designer"}
]

class UserModel:
    @staticmethod
    def generate_next_id():
        return max(user["id"] for user in users_db) + 1 if users_db else 1

    @staticmethod
    def get_all():
        return users_db

    @staticmethod
    def create(data):
        new_user = {
            "id": UserModel.generate_next_id(),
            "nome": data.get("nome"),
            "email": data.get("email"),
            "cargo": data.get("cargo", "Não especificado")
        }
        users_db.append(new_user)
        return new_user