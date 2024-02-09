from flask import Flask, render_template,request
import module.firebase as fb

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


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    user_data=''
    if request.method == 'POST':
        user_data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'] ,
        "phone_number": request.form['phone_number']
        }
    fb.v(user_data) 

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)