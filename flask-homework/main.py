from flask import Flask
from logging.config import dictConfig

app = Flask(__name__)

dictConfig({
    "version": 1,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"}
    },
    "root": {"handlers": ["console"], "level": "INFO"},
})


@app.route('/')
def root():
    return '<a href="/hello">hello</a>'

@app.route('/hello')
def hello():
    app.logger.info("hello opened")
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=False)
