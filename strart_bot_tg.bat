@echo off

call %~dp0venv\Scripts\activate
echo "call %~dp0venv\Scripts\activate"

set TOKEN=5562475997:AAE9ID-AKZDbbBMkQ9YYCGSvoIruwTXzMnA
rem set HTTP_PROXY_TG=http://10.22.1.135:3128

python %~dp0bot_telegram.py
echo "python %~dp0bot_telegram.py"


pause