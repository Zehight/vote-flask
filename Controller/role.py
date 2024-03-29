import json

from flask import Blueprint, request, jsonify
from Services import roleServices

role = Blueprint('role', __name__, url_prefix='/role')


@role.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    print(roleServices.add(**requestData, createBy='test'))
    return jsonify({'data': 'ok'})


@role.route('/getList', methods=['POST'])
def getList():
    return jsonify({'list': roleServices.getList()})

@role.route('/getInfo', methods=['POST'])
def getInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': roleServices.getInfo(**requestData)})

@role.route('/delInfo', methods=['POST'])
def delInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': roleServices.delInfo(**requestData)})
