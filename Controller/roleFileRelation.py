import json

from flask import Blueprint, request, jsonify
from Services import roleFileRelationServices

roleFrontImg = Blueprint('roleFrontImg', __name__, url_prefix='/roleFrontImg')


@roleFrontImg.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    print(requestData)
    print(roleFileRelationServices.add(**requestData, createBy='test'))
    return jsonify({'data': 'ok'})


@roleFrontImg.route('/getList', methods=['POST'])
def getList():
    requestData = json.loads(request.data)
    return jsonify({'list': roleFileRelationServices.getList(**requestData)})

@roleFrontImg.route('/delInfo', methods=['POST'])
def delInfo():
    requestData = json.loads(request.data)
    return jsonify({'list': roleFileRelationServices.delInfo(**requestData)})