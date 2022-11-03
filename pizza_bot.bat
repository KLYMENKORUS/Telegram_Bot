@echo off

call %~dp0Telegram_Bot\venv\Scripts\activate

cd %~dp0Telegram_Bot

set TOKEN=5545642894:AAFNMgyaOJYw57-UbvEHl-1BYW0qFenpJHg
python pizza_bot.py

pause