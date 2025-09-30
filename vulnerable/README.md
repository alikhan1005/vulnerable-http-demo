# Vulnerable demo

Запустить (локально):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Эндпоинты:
- `/` — выводит API_KEY
- `/error` — вызывает ошибку (stacktrace)
- `/deserialize` — принимает бинарный payload и делает pickle.loads
