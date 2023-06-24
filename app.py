from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__, static_folder='images', static_url_path='', template_folder='templates')

@app.route('/')
def index():
    image_names = os.listdir('static/images')
    return render_template('index.html', image_names=image_names)

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
