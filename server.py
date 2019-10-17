from flask import Flask
from flask import send_file , request, abort
import os
app = Flask(__name__)

@app.route('/getimage', methods=['GET'])
def returnimage():
    search = request.args.get('imageName')
    path="spriteImages/"
    try:
        filestat = os.stat(path+search)
        return send_file(path+search)
    except FileNotFoundError:
        abort(404)
