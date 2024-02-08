from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio-details.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/termofservice')
def termofservice():
    return render_template('termofservice.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog-single')
def blogsingle():
    return render_template('blog-single.html')

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacypolicy.html')

if __name__ == '__main__':
    app.run(debug=True)