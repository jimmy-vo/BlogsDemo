import os

from flask import Flask, render_template, request, redirect, url_for, session
from db import init_db, fetch_blog_all, fetch_blog_single, create_user, fetch_user_all, insert_blog_single, update_blog_single, delete_blog_single, fetch_user_id

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/Init')
def Init():
    init_db()
    return ""


@app.route('/blog/<id>')
@app.route('/blog', defaults={'id': ''})
def blog(id):
    author = session['User'];
    if '' != id:
        return render_template("blog.html", data=fetch_blog_single(id, author))
    else:
        return render_template("blog.html", data=fetch_blog_all(author))


@app.route('/edit/<id>')
@app.route('/edit',  methods=['POST', 'GET'], defaults={'id': ''})
def edit(id):
    author = session['User'];
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Check if delete request
        try:
            delete = request.form['delete']
        except:
            delete = None

        # Check id is available
        try:
            id = request.form['id']
            if not id.isdigit():
                id = None
        except:
            id = None

        if delete is not None:
            delete_blog_single(id)
            return render_template("blog.html", data=fetch_blog_all(author))
        elif id is None:
            insert_blog_single(author, title, content)
            return render_template("blog.html", data=fetch_blog_all(author))
        else:
            update_blog_single(id, author, title, content)
            return render_template("blog.html", data=fetch_blog_single(id, author))
    else:
        if '' != id:
            return render_template("edit.html", data=fetch_blog_single(id, author)[0])
        else:
            return render_template("edit.html", data=None)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if not username.isalnum():
            return render_template("login.html", data=fetch_user_all())

        password = request.form['password']
        if not password.isalnum():
            return render_template("login.html", data=fetch_user_all())

        try:
            register = request.form['register']
        except:
            register = None

        if register is not None:
            create_user(username, password)
            session['User'] = fetch_user_id(username)[0]['Id']
            return redirect(url_for('blog'))
        else:
            for user in fetch_user_all():
                if user['UserName'] == username and user['Password'] == password:
                    session['User'] = fetch_user_id(username)[0]['Id']
                    return redirect(url_for('blog'))
    return render_template("login.html", data=fetch_user_all())



if __name__ == "__main__":
    # init_db()
    # FOR SESSION
    app.secret_key = os.urandom(24)
    app.run()
else:
    print("is being imported into another module")
