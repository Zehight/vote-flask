import json

from flask import Blueprint, request, jsonify
from Services import roleHistaryRelationServices

roleHistary = Blueprint('roleHistary', __name__, url_prefix='/roleHistary')


@roleHistary.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    result = roleHistaryRelationServices.add(**requestData, createBy='test')
    return jsonify({'data': result})


@roleHistary.route('/getList', methods=['POST'])
def getList():
    requestData = json.loads(request.data)
    return jsonify({'list': roleHistaryRelationServices.getList(**requestData)})


@roleHistary.route('/getInfo', methods=['POST'])
def getInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': roleHistaryRelationServices.getInfo(**requestData)})


@roleHistary.route('/delInfo', methods=['POST'])
def delInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': roleHistaryRelationServices.delInfo(**requestData)})
