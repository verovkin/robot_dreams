from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return '<a href="/hello">hello</a>'

@app.route('/hello')
def hello():
    app.logger.info("hello opened")
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=False)
