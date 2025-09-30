# Temporary fix branch test
from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# ✅ Секрет извлекается из переменной окружения
API_KEY = os.getenv("API_KEY", None)

@app.route("/")
def index():
    # ✅ Не показываем секреты
    return "Welcome to secure demo"

# ✅ Глобальный обработчик ошибок — скрываем детали
@app.errorhandler(Exception)
def handle_exception(e):
    # Логирование (в реальном приложении логируйте в файл/систему логирования)
    print(f"ERROR: {e}")
    return jsonify({"error": "Internal Server Error"}), 500

@app.route("/deserialize", methods=["POST"])
def deserialize():
    # ✅ Принимаем JSON, не бинарные pickle данные
    try:
        data_text = request.get_data(as_text=True)
        obj = json.loads(data_text)
        # Валидация: ожидаем словарь с ключом "action"
        if not isinstance(obj, dict) or 'action' not in obj:
            return jsonify({"error": "Invalid input"}), 400
        return jsonify({"object": obj})
    except Exception as e:
        print(f"deserialize error: {e}")
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    # ✅ debug выключен
    app.run(host='0.0.0.0', port=5000, debug=False)
