import json

from flask import Blueprint, request, jsonify
from Services import projectServices

project = Blueprint('project', __name__, url_prefix='/project')


@project.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    result = projectServices.add(**requestData, createBy='test')
    return jsonify({'data': result})


@project.route('/getList', methods=['POST'])
def getList():
    return jsonify({'list': projectServices.getList()})


@project.route('/getInfo', methods=['POST'])
def getInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': projectServices.getInfo(**requestData)})


@project.route('/delInfo', methods=['POST'])
def delInfo():
    requestData = json.loads(request.data)
    return jsonify({'data': projectServices.delInfo(**requestData)})
