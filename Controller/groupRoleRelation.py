import json

from flask import Blueprint, request, jsonify
from Services import groupRoleRelationServices

roleInGroup = Blueprint('roleInGroup', __name__, url_prefix='/roleInGroup')


@roleInGroup.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    result = groupRoleRelationServices.add(**requestData, createBy='test')
    return jsonify({'data': result})


@roleInGroup.route('/getInfo', methods=['POST'])
def getInfo():
    requestData = json.loads(request.data)
    return jsonify({'list': groupRoleRelationServices.getInfo(**requestData)})


@roleInGroup.route('/delInfo', methods=['POST'])
def delInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': groupRoleRelationServices.delInfo(**requestData)})
