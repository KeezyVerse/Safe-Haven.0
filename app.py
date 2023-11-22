from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

app.secret_key = 'secret key'

#auth = {"username": 'Jimmy',"password": 'Drool'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = request.form['username']
    passcode = request.form['password']
    print(user,passcode)
    if (user == "Jimmy") and (passcode == "Drool"):
        return redirect("/home")
    else:
        return 'Login unsuccessful'

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    
    comment_content = request.form.get('comment_content')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)