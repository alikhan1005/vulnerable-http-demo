# Fixed demo

Перед запуском: поставь переменную окружения `API_KEY` и не коммить `.env`.

Запустить:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export API_KEY="set_real_api_key_here"
python app.py
```

Эндпоинты:
- `/` — приветствие, без секретов
- `/deserialize` — только JSON вход, с валидацией
