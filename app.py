from flask import Flask, request, send_file, render_template
import os
from thumbnail import thumb_maker

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')

@app.route('/')
def index():
    image_names = os.listdir('static/images')
    # thumb_names=list(map(thumb_maker,image_names))
    thumb_names=os.listdir('static/_thumb')
    thumb_names=list(map(lambda x: os.path.join('_thumb',x),thumb_names))
    file_names=zip(image_names,thumb_names)
    print(file_names)
    return render_template('index.html', file_names=file_names)

@app.route('/download')
def download_image():
    image_name = request.args.get('image_name')
    image_path = os.path.join('static/images', image_name)

    if not os.path.exists(image_path):
        return 'Image not found', 404

    return send_file(image_path, as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    app.run()
