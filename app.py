from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

app.secret_key = 'secret key'

users = {'Jimmy': 'Drool'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        if user in users and users[user] == password:
            return redirect(url_for('home'))
        return 'Login unsuccessful'
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)