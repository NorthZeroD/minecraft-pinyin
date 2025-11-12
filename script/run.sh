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

if [ -f "download/version_manifest.json" ]; then
    rm "download/version_manifest.json"
fi

echo Running the main script...
python3 src/main.py
