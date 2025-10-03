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

# Import the Flask app
from app import app

# Configure for subfolder deployment
app.config['APPLICATION_ROOT'] = '/goai'

# For production deployment
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=False)
