import json

from flask import Blueprint, request, jsonify
from Services import groupServices

group = Blueprint('group', __name__, url_prefix='/group')


@group.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    print(requestData)
    print(groupServices.add(**requestData, createBy='test'))
    return jsonify({'data': 'ok'})


@group.route('/getList', methods=['POST'])
def getList():
    requestData = json.loads(request.data)
    return jsonify({'list': groupServices.getList(**requestData)})
