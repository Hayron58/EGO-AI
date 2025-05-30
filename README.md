# EGO AI Telegram Bot

## Описание:
Telegram-бот, создающий мотивационные образы личности и AI-аватары на основе пользовательского запроса.

## Как запустить:

1. Получи Telegram Token в @BotFather
2. Получи бесплатный API-ключ на https://deepai.org/
3. Замени `YOUR_TELEGRAM_BOT_TOKEN` и `YOUR_DEEPAI_API_KEY` в `config.py`
4. Установи зависимости:
```bash
pip install -r requirements.txt
```
5. Запусти бота:
```bash
python main.py
```

## Бесплатный хостинг:
1. Зарегистрируйся на https://render.com/
2. Создай новый Web Service → подключи GitHub или загрузи ZIP проекта
3. В настройках добавь переменные окружения:
- `TELEGRAM_TOKEN`
- `DEEPAI_KEY`
4. Запусти сервис
