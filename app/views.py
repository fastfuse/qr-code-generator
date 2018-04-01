from app import app
from flask import render_template, request

from .utils import generate_qr_code


@app.route('/', methods=["GET", "POST"])
# @app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        print(request.form['text'])

        generate_qr_code(request.form['text'])

    return render_template('index.html')
