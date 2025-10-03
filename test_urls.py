#!/usr/bin/env python3
"""
Test script to verify URL generation for subfolder deployment
"""

from app import app

# Test URL generation
with app.test_request_context('/goai/'):
    print("Testing URL generation for subfolder deployment:")
    print("=" * 50)
    
    # Test basic routes
    from flask import url_for
    
    print(f"Home URL: {url_for('home')}")
    print(f"Services URL: {url_for('services')}")
    print(f"About URL: {url_for('about')}")
    print(f"Contact URL: {url_for('contact')}")
    print(f"Portfolio URL: {url_for('portfolio')}")
    print(f"Blog URL: {url_for('blog')}")
    
    # Test static files
    print(f"Logo URL: {url_for('static', filename='images/GoAI_Logo__1_-removebg-preview.png')}")
    print(f"CSS URL: {url_for('static', filename='css/style.css')}")
    print(f"JS URL: {url_for('static', filename='js/main.js')}")
    
    print("\n" + "=" * 50)
    print("All URLs should start with /goai/ for subfolder deployment")
