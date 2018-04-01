# Add your help functions here
import os
import qrcode


def generate_qr_code(data):
    qr = qrcode.QRCode(version=1)  # initialize settings for Output Qrcode
    qr.add_data(data)  # adds the data to the qr cursor

    qr.make(fit=True)
    img = qr.make_image()

    filename = os.path.join(os.getcwd(), 'app', 'static', 'img', 'q.png')

    # with open('static/img/q.png', 'wb') as img_file:
    with open(filename, 'wb') as img_file:
        img.save(img_file, 'PNG')
