import os

import flask
from robot_app import app
import random
from flask import request, redirect, url_for, make_response, session
from markupsafe import escape
import werkzeug.exceptions
import re


app.secret_key = b'secret'



def check_logged_in():
    return session.get('user')


@app.route('/')
def root():
    return '''
        <a href="/hello">hello</a><BR>
        <a href="/users">users</a><BR>
        <a href="/books">books</a><BR>
        <a href="/params?abc=123&p=asdjfh">params</a><BR>
        <a href="/login">login</a><BR>
    '''


@app.route('/hello')
def hello():
    app.logger.info("hello opened")
    return 'Hello World'


@app.route('/users')
def users_list():
    if not check_logged_in():
        return redirect('/login')

    names = ['James', 'Mary', 'Robert', 'Patricia', 'John', 'Jennifer', 'Michael', 'Linda', 'David',
             'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Lisa']

    if request.args.get("count"):
        try:
            range_count = int(request.args.get("count"))
        except ValueError:
            return "Enter a number in count param", 406
    else:
        range_count = random.randint(3,7)

    selected_names = [random.choice(names) for _ in range(range_count)]

    resp = make_response(flask.render_template('users.html', names=selected_names))
    resp.status_code = 200
    return resp


@app.route('/books')
def books_list():
    if not check_logged_in():
        return redirect('/login')

    books = [('Learning Python', 'Mark Lutz'),
             ('Head-First Python', 'Paul Barry'),
             ('Python Distilled', 'David Beazley'),
             ('Introducing Python (2nd Edition)', 'Bill Lubanovic'),
             ('Python Programming for Beginners (1st Edition)', 'Philip Robbins'),
             ('Learn Python in One Day and Learn It Well (2nd Edition)', 'Jamie Chan')]

    if request.args.get("count"):
        try:
            range_count = int(request.args.get("count"))
        except ValueError:
            return "Enter a number in count param", 406
    else:
        range_count = random.randint(2, len(books))

    selected_books = []

    for book in random.choices(books, k=range_count):
       selected_books.append({'book': book[0], 'author': book[1]})

    return flask.render_template('books.html', books=selected_books)


@app.route('/users/<int:user_id>')
def show_user(user_id):
    if not check_logged_in():
        return redirect('/login')

    if user_id % 2:
        return flask.render_template('404.html'), 404
    else:
        return flask.render_template('user.html', user=user_id), 200
    #
    # return (str(user_id), 200) if not user_id % 2 else ('Not found', 404)


@app.route('/books/<title>')
def show_book(title):
    if not check_logged_in():
        return redirect('/login')

    app.logger.info(f"The title is {title}")
    return flask.render_template('book.html', title='title'), 200


@app.route('/params')
def show_params():
    if not check_logged_in():
        return redirect('/login')
    return flask.render_template('params.html', params=request.args), 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return flask.render_template('login.html')

    elif request.method == 'POST':
        if not request.form.get("username") or not request.form.get("password"):
            return "Error, no login data", 400
        elif len(request.form.get("username")) < 5:
            return "Wrong username", 403
        elif not re.fullmatch(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$", request.form.get("password")):
            return "Wrong password", 403
        else:
            username = request.form.get('username')
            session['user'] = username
            return redirect('/users')

    else:
        return "Bad request", 400


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.errorhandler(werkzeug.exceptions.NotFound)
def default_404(e):
    return flask.render_template('404.html'), 404
