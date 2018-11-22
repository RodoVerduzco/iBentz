""" This file contains the manage for the flask """
import os
import config
from application import create_app
from flask import Flask, request
from werkzeug.utils import secure_filename

app = create_app(config, debug=('DEBUG' in os.environ and bool(os.environ['DEBUG'])))
PORT = int(os.getenv('PORT', config.PORT))
app.config['UPLOAD_FOLDER'] = '.\img\gallery'
@app.route('/')
def hello():
    """ Return a friendly HTTP greeting. """
    return 'Hello World!'

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('.\FrontEnd\img\gallery\\'+secure_filename(f.filename))
      #f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
      print(f.filename)
      
      return 'file uploaded successfully'

# Run Configuration
if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.HOST, port=PORT)
