import json

from flask import Blueprint, request, jsonify
from Services import groupServices

group = Blueprint('group', __name__, url_prefix='/group')


@group.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    result = groupServices.add(**requestData, createBy='test')
    return jsonify({'data': result})


@group.route('/getList', methods=['POST'])
def getList():
    requestData = json.loads(request.data)
    return jsonify({'list': groupServices.getList(**requestData)})


@group.route('/getInfo', methods=['POST'])
def getInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': groupServices.getInfo(**requestData)})


@group.route('/delInfo', methods=['POST'])
def delInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': groupServices.getInfo(**requestData)})
