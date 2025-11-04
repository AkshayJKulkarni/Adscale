@echo off
echo Setting up AdScale virtual environment...

cd adscale
python -m venv venv
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete! To activate the environment, run:
echo cd adscale
echo venv\Scripts\activate.bat
echo python main.py