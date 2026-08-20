from flask import request, jsonify
from src.models.user_model import UserModel

class UserController:
    @staticmethod
    def list_users():
        return jsonify({"status": "success", "data": UserModel.get_all()}), 200

    @staticmethod
    def create_user():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"status": "error", "error": "JSON inválido."}), 400

        nome, email = data.get("nome"), data.get("email")
        if not nome or not email:
            return jsonify({"status": "error", "error": "Campos 'nome' e 'email' são obrigatórios."}), 400

        new_user = UserModel.create(data)
        return jsonify({"status": "success", "data": new_user}), 201


    from flask import request, jsonify
from src.models.user_model import UserModel

class UserController:
    @staticmethod
    def list_users():
        return jsonify({"status": "success", "data": UserModel.get_all()}), 200

    @staticmethod
    def create_user():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"status": "error", "error": "JSON inválido."}), 400

        nome, email = data.get("nome"), data.get("email")
        if not nome or not email:
            return jsonify({"status": "error", "error": "Campos 'nome' e 'email' são obrigatórios."}), 400

        new_user = UserModel.create(data)
        return jsonify({"status": "success", "data": new_user}), 201

    @staticmethod
    def get_user_by_id(user_id):
        user = next((u for u in UserModel.get_all() if u["id"] == user_id), None)
        if not user:
            return jsonify({"status": "error", "error": "Usuário não encontrado."}), 404
        return jsonify({"status": "success", "data": user}), 200