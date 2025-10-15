#!/bin/bash

if [ ! -d ".venv" ]; then
    echo Creating virtual environment...
    python3 -m venv .venv
    source .venv/bin/activate
    echo Installing dependencies...
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

echo Running the main script...
python3 src/main.py
