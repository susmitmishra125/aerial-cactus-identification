from flask import Flask

UPLOAD_FOLDER = r'C:\Users\susmi\OneDrive\Documents\GitHub\aerial-cactus-identification'

app = Flask(__name__)
app.secret_key = "secret key"
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER