from robot_app import app
import random
from flask import request, redirect, url_for
from markupsafe import escape
import werkzeug.exceptions
import re


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

    names = ['James', 'Mary', 'Robert', 'Patricia', 'John', 'Jennifer', 'Michael', 'Linda', 'David',
             'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Lisa']

    if request.args.get("count"):
        try:
            range_count = int(request.args.get("count"))
        except ValueError:
            return "Enter a number in count param", 406
    else:
        range_count = random.randint(3,7)

    return [random.choice(names) for _ in range(range_count)], 200


@app.route('/books')
def books_list():
    books = [('Learning Python', 'Mark Lutz'),
             ('Head-First Python', 'Paul Barry'),
             ('Python Distilled', 'David Beazley'),
             ('Introducing Python (2nd Edition)', 'Bill Lubanovic'),
             ('Python Programming for Beginners (1st Edition)', 'Philip Robbins'),
             ('Learn Python in One Day and Learn It Well (2nd Edition)', 'Jamie Chan')]
    res = '<ul>'

    if request.args.get("count"):
        try:
            range_count = int(request.args.get("count"))
        except ValueError:
            return "Enter a number in count param", 406
    else:
        range_count = random.randint(2, len(books))

    for book in random.choices(books, k=range_count):
       res += f'<li><strong>{book[0]}</strong> - {book[1]}</li>'
    res += '</ul>'
    return res


@app.route('/users/<int:user_id>')
def show_user(user_id):
    return (str(user_id), 200) if not user_id % 2 else ('Not found', 404)


@app.route('/books/<title>')
def show_book(title):
    return title.capitalize()


@app.route('/params')
def show_params():
    res = '<table><tr><td>parameter</td><td>value</td></tr>'
    for key, value in request.args.items():
        res += f'<tr><td>{escape(key)}</td><td>{escape(value)}</td></tr>'
    res += '</table>'
    return res


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        html_form =  '''
        <form action="/login" method="post">
            <input type="text" name="username" value="" placeholder="username" /><BR>
            <input type="password" name="password" value="" placeholder="password"/><BR>
            <button type="submit">Log in</button>
        </form>
        '''
        return html_form, 200
    elif request.method == 'POST':
        if not request.form.get("username") or not request.form.get("password"):
            return "Error, no login data", 400
        elif len(request.form.get("username")) < 5:
            return "Wrong username", 403
        elif not re.fullmatch(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$", request.form.get("password")):
            return "Wrong password", 403
        else:
            return redirect('/users'), 302


@app.errorhandler(werkzeug.exceptions.NotFound)
def default_404(e):
    return '<h1 style "color=red">Not found</h1>'


@app.errorhandler(werkzeug.exceptions.NotFound)
def default_500(e):
    return '<h1 style "color=red">Server is burning</h1>'
