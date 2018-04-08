# Add your help functions here
import os
import qrcode
import uuid
from .consts import DATA_TEMPLATES


def generate_qr_code(form_data):
    data_type = form_data.pop('type')

    template = DATA_TEMPLATES.get(data_type)

    data = template.format(**form_data)

    return _generate(data)


def _generate(data):
    qr = qrcode.QRCode(version=1)  # initialize settings for Output Qrcode
    qr.add_data(data)  # adds the data to the qr cursor

    qr.make(fit=True)
    img = qr.make_image()

    file_name = f'{uuid.uuid4()}.png'

    file_path = os.path.join(os.getcwd(), 'app', 'static', 'img', file_name)

    with open(file_path, 'wb') as img_file:
        img.save(img_file, 'PNG')

    return file_name
