#!/bin/bash

# GO AI Marketing Services Deployment Script
# Run this on your server after uploading the files

echo "🚀 Deploying GO AI Marketing Services..."

# Set your project directory
PROJECT_DIR="/path/to/your/goai-site"  # Update this path
NGINX_SITES="/etc/nginx/sites-available"
NGINX_ENABLED="/etc/nginx/sites-enabled"

# Update project directory in this script
sed -i "s|/path/to/your/goai-site|$PROJECT_DIR|g" nginx.conf

# Copy nginx configuration
echo "📝 Setting up nginx configuration..."
sudo cp nginx.conf $NGINX_SITES/goai
sudo ln -sf $NGINX_SITES/goai $NGINX_ENABLED/

# Update nginx configuration with correct paths
sudo sed -i "s|/path/to/your/goai-site|$PROJECT_DIR|g" $NGINX_SITES/goai

# Test nginx configuration
echo "🔍 Testing nginx configuration..."
sudo nginx -t

if [ $? -eq 0 ]; then
    echo "✅ Nginx configuration is valid"
    sudo systemctl reload nginx
    echo "🔄 Nginx reloaded"
else
    echo "❌ Nginx configuration error. Please check the config."
    exit 1
fi

# Set up Python virtual environment
echo "🐍 Setting up Python environment..."
cd $PROJECT_DIR
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set proper permissions
echo "🔐 Setting permissions..."
sudo chown -R www-data:www-data $PROJECT_DIR
sudo chmod -R 755 $PROJECT_DIR

echo "✅ Deployment complete!"
echo ""
echo "📋 Next steps:"
echo "1. Update the PROJECT_DIR path in this script"
echo "2. Update your domain in nginx.conf"
echo "3. Start your Flask app: python wsgi.py"
echo "4. Or use a process manager like systemd/supervisor"
echo ""
echo "🌐 Your app should be available at: http://your-domain.com/goai/"
