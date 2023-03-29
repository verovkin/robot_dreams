from . import app


@app.route('/')
def root():
    return '<a href="/hello">hello</a>'


@app.post('/')
def root_post():
    return '<a href="/hello">POST</a>'


@app.route('/hello')
def hello():
    app.logger.info("hello opened")
    return 'Hello World'


@app.route('/actors', methods=['GET', 'POST'])
def get_actors():
    return {'actors': []}, 200


@app.route('/actors/<int:actor_id>')
def get_actor(actor_id):
    return f'<div>actor id is - {actor_id}</div>', 200


@app.post('/actors')
def create_actor():
    app.logger.info("Actor has been created")
    return 'Created', 201
