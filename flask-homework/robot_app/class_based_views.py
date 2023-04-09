from flask.views import View
from flask import request
from robot_app import app


class MyViews(View):
    methods = ['GET', 'POST']

    def __init__(self, data, template_name):
        self.data = data
        self.template = template_name
    def dispatch_request(self):
        if request.method == 'GET':
            return (f"Data: {self.data}, template name {self.template}"), 200
        else:
            return 'ok', 201


users = ['First' , 'Second']
books = ['234', '234234']
movies = ['sdfsd', 'sdfsd']

app.add_url_rule('/class/users', view_func=MyViews.as_view('class-users', users, 'users.html'))
app.add_url_rule('/class/books', view_func=MyViews.as_view('class-books', books, 'books.j2'))
app.add_url_rule('/class/books', view_func=MyViews.as_view('class-movies', books, 'movies.html'))

