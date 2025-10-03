from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Configure Flask for subfolder deployment
# This tells Flask that the app is served from /goai/ subfolder
app.config['APPLICATION_ROOT'] = '/goai'

# Context processor to handle subfolder URLs
@app.context_processor
def inject_subfolder():
    return {
        'subfolder': '/goai',
        'base_url': request.url_root.rstrip('/') + '/goai'
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        company = request.form.get('company')
        service = request.form.get('service')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to database
        # For now, we'll just flash a success message
        flash('Thank you for your message! We will get back to you within 24 hours.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<slug>')
def blog_article(slug):
    # Map of article slugs to template files
    article_templates = {
        'ai-future-marketing-2024': 'blog/ai-future-marketing-2024.html',
        'ai-ppc-optimization': 'blog/ai-ppc-optimization.html',
        'ai-social-media-strategies': 'blog/ai-social-media-strategies.html',
        'email-marketing-automation-2024': 'blog/email-marketing-automation-2024.html',
        'ai-powered-seo-guide-2024': 'blog/ai-powered-seo-guide-2024.html',
        'marketing-roi-metrics': 'blog/marketing-roi-metrics.html',
        'mobile-first-marketing': 'blog/mobile-first-marketing.html'
    }
    
    if slug in article_templates:
        return render_template(article_templates[slug])
    else:
        # Return 404 for unknown articles
        from flask import abort
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
