from flask import Flask
from flask import send_file , request, abort
from PIL import Image
import os
app = Flask(__name__)

newsize=(300,300)
@app.route('/getimage', methods=['GET'])
def returnimage():
    search = request.args.get('imageName')
    path="spriteImages/"
    try:
        filestat = os.stat(path+search)
        im = Image.open(path+search)
        im.resize(newsize).save(path+"tmp.png")
        return send_file(path+"tmp.png")
    except FileNotFoundError:
        abort(404)
