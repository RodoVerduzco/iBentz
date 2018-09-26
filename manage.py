""" This file contains the manage for the flask """
import os
import config
from application import create_app

app = create_app(config, debug=('DEBUG' in os.environ and bool(os.environ['DEBUG'])))
PORT = int(os.getenv('PORT', config.PORT))

@app.route('/')
def hello():
    """ Return a friendly HTTP greeting. """
    return 'Hello World!'

# Run Configuration
if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.HOST, port=PORT)
