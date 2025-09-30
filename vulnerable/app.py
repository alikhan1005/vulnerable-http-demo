from flask import Flask, request
import pickle

app = Flask(__name__)

# ❌ Хардкод секретов
API_KEY = "supersecretapikey123"

@app.route("/")
def index():
    # ❌ Утечка секрета в ответ
    return f"Welcome! API_KEY={API_KEY}"

@app.route("/error")
def error():
    # ❌ Искусственная ошибка — покажет stacktrace при debug=True
    return 1 / 0

@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.data
    # ❌ Небезопасная десериализация
    obj = pickle.loads(data)
    return f"Deserialized object: {obj}"

if __name__ == "__main__":
    # ❌ debug=True выводит stacktrace в браузер
    app.run(host='0.0.0.0', port=5000, debug=True)
