from flask import Flask, render_template,request,redirect,url_for,flash,jsonify
import module.firebase as fb
import module.sendEmail as se

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio-details.html')

@app.route('/register', methods=['POST','GET'])
def register():
    err=''
    if request.method == 'POST':
        try:
            user_data = {
                "first_name": request.form['fname'],
                "email": request.form['email'],
                "phone_number": request.form['phone_number'],
                "course_type": request.form['course_type']
            }

            message = fb.create_db_candidates(user_data)
            err=message
            # flash(message)
            if message is None:
                err="already Registered"
                print(err)            

        except Exception as e:
            # Handle any exceptions, and provide an error flash message
            print(f"Registration failed: {str(e)}", "danger")
            print(f"Registration failed: {str(e)}", "danger")

    return render_template('register.html',err=err)

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
    # user_data=''
    
    if request.method == 'POST':
        user_data = {
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email":request.form['email'] ,
            "phone_number": request.form['phone_number']
            }

        message=fb.create_db_client(user_data) 
        print(message)
        print(message)
        print(message)
        print(message)


    return message


@app.route('/contact', methods=['POST','GET'])
def contact_form():
    try:
        if request.method=='POST':
            message={
                "name":request.form["name"],
                "number":request.form["number"],
                "message":request.form["message"]
        }
            se.send_mes(message)
            
        return 'OK'

    except Exception as err :
        return err

            


@app.route('/subscribe',methods=['POST','GET'])
def subscribe():
    mess=''
    try:
        if request.method=='POST':
            email=request.form['email']
            mess=fb.SubscribeList(email)
        return mess
    except Exception:
        return 'No'


if __name__ == '__main__':
    app.run(debug=True)