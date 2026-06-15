#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Installing dependencies..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install pynput requests beautifulsoup4

echo ""
echo "Installation complete. Run ./run.sh to start the app."
