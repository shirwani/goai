#!/usr/bin/env python3
"""
WSGI configuration for GO AI Marketing Services
Deploy this with your web server (nginx + uWSGI/gunicorn)
"""

import os
import sys

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Add virtual environment to Python path if it exists
venv_path = os.path.join(project_dir, 'venv', 'lib', 'python3.12', 'site-packages')
if os.path.exists(venv_path):
    sys.path.insert(0, venv_path)

# Import the Flask app
from app import app

# Configure for subfolder deployment
app.config['APPLICATION_ROOT'] = '/goai'

# For production deployment
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=False)
