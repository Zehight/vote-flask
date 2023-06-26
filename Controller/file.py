import os

from flask import Blueprint, request, send_from_directory

from models import File, db

file = Blueprint('file', __name__, url_prefix='/file')
from Services import fileServices

img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img'))
if not os.path.exists(img_folder):
    os.makedirs(img_folder)


@file.route('/add', methods=['POST'])
def add():
    image = request.files['file']
    name: str = image.filename
    image.save(os.path.join(img_folder, name))
    result = fileServices.add(name)
    return {'id': result}


@file.route('/preview/<id>')
def preview(id):
    name = File.query.filter_by(id=id).first().imgName
    # 通过send_from_directory函数返回图片文件
    return send_from_directory('./img', name)
