import os

from functools import wraps
import flask
from robot_app import app, db
from flask import request, redirect, url_for, session, render_template
from .models import *
import werkzeug.exceptions
import re


app.secret_key = app.config.get('SECRET_KEY')


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def root():
    return '''
        <a href="/users">users</a><BR>
        <a href="/books">books</a><BR>
        <a href="/purchases">purchases</a><BR>
        <a href="/login">login</a><BR>
    '''


@app.route('/users')
@login_required
def users_list():
    query = db.select(User)

    if request.args.get("size"):
        try:
            size = int(request.args.get("size"))
        except ValueError:
            return "Error. Enter an int in size param", 406
        query = query.limit(size)

    users = db.session.scalars(query)
    return render_template('users.html', users=users)


@app.route('/users/<int:user_id>')
@login_required
def show_user(user_id):

    user = db.get_or_404(User, user_id)
    return render_template('user.html', user=user)


@app.route('/books')
@login_required
def books_list():
    if request.args.get("size"):
        try:
            size = int(request.args.get("size"))
        except ValueError:
            return "Error. Enter an int in size param", 406

        books = db.session.query(Book, Publishing_house).join(Publishing_house).limit(size).all()
    else:
        books = db.session.query(Book, Publishing_house).join(Publishing_house).all()

    return render_template('books.j2', books=books)


@app.route('/books/<int:book_id>')
@login_required
def show_book(book_id):
    book = db.session.query(Book, Publishing_house).join(Publishing_house).filter_by(id=book_id).all()

    if len(book) < 1:
        return flask.render_template('404.html'), 404
    return render_template('books.j2', books=book)


@app.route('/purchases')
@login_required
def purchases_list():
    if request.args.get("size"):
        try:
            size = int(request.args.get("size"))
        except ValueError:
            return "Error. Enter an int in size param", 406
        purchases = db.session.query(Purchase, User, Book).join(User).join(Book).limit(size).all()

    else:
        purchases = db.session.query(Purchase, User, Book).join(User).join(Book).all()

    return render_template('purchases.j2', purchases=purchases)


@app.route('/purchases/<int:purchase_id>')
@login_required
def show_purchase(purchase_id):
    purchase = db.session.query(Purchase, User, Book).join(User).join(Book).filter(Purchase.id == purchase_id).all()
    print(len(purchase))
    if len(purchase) < 1:
        return flask.render_template('404.html'), 404
    return render_template('purchases.j2', purchases=purchase)


@app.post('/users')
# @login_required    # commented for postman POST request
def add_user():

    user = User(
        first_name=request.form.get("first_name"),
        last_name=request.form.get("last_name"),
        age=request.form.get("age"),
    )
    db.session.add(user)
    db.session.commit()
    return f'User created', 201


@app.post('/books')
# @login_required    # commented for postman POST request
def add_book():

    publishing_house_id = request.form.get("publishing_house_id")
    if not db.session.query(Publishing_house).filter_by(id=publishing_house_id).count():
        return f"Error, no publishing house with ID={publishing_house_id}", 400

    book = Book(
        title=request.form.get("title"),
        author=request.form.get("author"),
        year=request.form.get("year"),
        price=request.form.get("price"),
        publishing_house_id=publishing_house_id,
    )
    db.session.add(book)
    db.session.commit()
    return f'Book created', 201


@app.post('/purchases')
# @login_required    # commented for postman POST request
def add_purchase():
    if not request.form.get("user_id") or not request.form.get("book_id"):
        return "Error, not all required data", 400

    user_id = request.form.get("user_id")
    book_id = request.form.get("book_id")

    if not db.session.query(Book).filter_by(id=book_id).count() or \
            not db.session.query(User).filter_by(id=user_id).count():
        return "Error, book or user not exist", 400

    purchase = Purchase(
        user_id=user_id,
        book_id=book_id,
    )
    db.session.add(purchase)
    db.session.commit()
    return f'Purchase created', 201


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
