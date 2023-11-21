from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)

@app.route('/submit_post', methods=['POST'])
def submit_post():
    username = request.form['username']
    email = request.form['email']
    content = request.form['content']

    new_comment = Comment(username=username, email=email, content=content)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)