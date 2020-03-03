#encoding: utf-8
from flask import Flask,render_template
from flask_cors import CORS


from api.blog import blog_app

# app = Flask(__name__)

app = Flask(__name__, static_url_path='')
CORS(app) 

app.register_blueprint(blog_app)

@app.route("/")
def index():
    return '<h1>Hello</h1>'



if __name__ == "__main__":
    app.run(host="localhost",port=9001)