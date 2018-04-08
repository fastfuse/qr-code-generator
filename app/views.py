from app import app
from flask import render_template, request, redirect, url_for, \
    send_from_directory

from .utils import generate_qr_code
from .consts import IMG_PATH_TEMPLATE


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = {k: v for k, v in request.form.items()}
        file = generate_qr_code(form_data)

        return render_template('index.html',
                               img_path=IMG_PATH_TEMPLATE.format(filename=file),
                               filename=file)

    return render_template('index.html',
                           img_path=IMG_PATH_TEMPLATE.format(filename='123.jpg'),
                           filename='123.jpg')


@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):

    return send_from_directory(app.config.get('UPLOAD_FOLDER'), filename,
                               as_attachment=True)


# TODO:
# * fix return when post (to prevent form re-submission);
# * fix img size on smaller screens;
# * remove image after it was downloaded and user left page;
# * check Geo accuracy; investigate in general;
# * implement calendar event;
