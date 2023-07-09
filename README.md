Certainly! Here's a manual for using the Flask REST API with user authentication:

**Prerequisites:**
- Python and pip are installed on your system.
- You have a working knowledge of Python and Flask.

**Step 1: Installation**

1. Open a terminal or command prompt.

2. Create a new directory for your project and navigate to it:
   ```
   mkdir flask-api
   cd flask-api
   ```

3. Create and activate a new virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

4. Install the required packages:
   ```
   pip install flask flask_jwt_extended
   ```

**Step 2: Code Setup**

1. Open a text editor and create a new file named `app.py`.

2. Copy the modified code provided earlier into the `app.py` file.

3. Set a strong and unique secret key in the `SECRET_KEY` variable inside the `app.py` file. For example:
   ```
   app.config['SECRET_KEY'] = 'your-secret-key'
   ```

4. Save the `app.py` file.

**Step 3: Starting the Flask Server**

1. In the terminal, make sure you are in the project's directory (`flask-api`).

2. Run the Flask server:
   ```
   python app.py
   ```

3. The Flask server should start running, and you will see output similar to the following:
   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

**Step 4: User Authentication**

1. Open a new terminal or use an API testing tool like Postman.

2. To obtain an access token, send a POST request to `http://localhost:5000/login` with the following JSON payload:
   ```
   {
     "username": "admin",
     "password": "admin"
   }
   ```

3. If the username and password are correct, you will receive a response with an access token:
   ```
   {
     "access_token": "your-access-token"
   }
   ```

4. Copy the access token as you'll need it to access the protected routes.

**Step 5: Accessing the API**

1. To access the list of images, send a GET request to `http://localhost:5000/images`.

   - Include the access token in the request header:
     ```
     Authorization: Bearer your-access-token
     ```

   - The response will be a JSON object containing the list of image names and their corresponding thumbnail names.

2. To download an image, send a GET request to `http://localhost:5000/images/<image_name>`, replacing `<image_name>` with the actual name of the image you want to download.

   - Include the access token in the request header as before.

   - If the image exists, it will be downloaded as an attachment.

   - If the image is not found, you will receive a JSON response with an error message.

**Important Notes:**

- Ensure that the images and thumbnails are present in the correct directories (`static/images` and `static/_thumb`, respectively). If they are not, you may need to modify the code or create the directories manually.

- Remember to secure your secret key and use proper authentication mechanisms in a production environment. The provided example is simplified for demonstration purposes only.

- This manual assumes you are running the Flask server on your local machine (localhost) with the default port of 5000. Modify the URLs accordingly if you are using a different setup.

That's it! You now have a Flask REST API with user authentication. You can explore further by adding more features, enhancing security, or integrating additional functionalities based on your project requirements.
