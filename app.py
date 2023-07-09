from flask import Flask, request, send_file, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os
from thumbnail import thumb_maker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your own secret key
jwt = JWTManager(app)

# Define a mock user for demonstration purposes
USER = {
    'username': 'admin',
    'password': 'admin'
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username or password is missing'}), 400

    if username != USER['username'] or password != USER['password']:
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

@app.route('/images', methods=['GET'])
@jwt_required()
def get_images():
    image_names = os.listdir('static/images')
    check_files()

    if False in present:
        thumb_names = map(thumb_maker, image_names)
    else:
        thumb_names = os.listdir('static/_thumb')

    thumb_names = list(map(lambda x: os.path.join('_thumb', x), thumb_names))
    file_names = list(zip(image_names, thumb_names))

    return jsonify(file_names)

@app.route('/images/<image_name>', methods=['GET'])
@jwt_required()
def download_image(image_name):
    image_path = os.path.join('static/images', image_name)

    if not os.path.exists(image_path):
        return jsonify({'error': 'Image not found'}), 404

    return send_file(image_path, as_attachment=True)

def check_files():
    global present
    present = []
    image_names = os.listdir('static/images')

    for i in image_names:
        img = os.path.join("static/images", i).split(".")[0] + "_thumb"

        if img not in os.listdir("static/_thumb"):
            present.append(False)
        else:
            present.append(True)

    if False in present:
        thumb_names = map(thumb_maker, image_names)
    else:
        print("All files are present")

if __name__ == '__main__':
    check_files()
    app.run()
