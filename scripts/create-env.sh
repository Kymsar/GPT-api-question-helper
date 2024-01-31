#!bin/bash
echo 'Creating virtual environment in scripts/.gpt-venv'
python3 -m venv scripts/.gpt-venv

echo 'Installing dependencies'
./scripts/.gpt-venv/bin/python -m pip install -r scripts/requirements.txt

echo 'Preparations done!'

