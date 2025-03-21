#!/bin/bash

# Install dependencies (only needed for local setup)
pip install -r requirements.txt  

# Start the chatbot server
gunicorn -w 4 -b 0.0.0.0:5000 app:app

