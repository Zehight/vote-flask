import json

from flask import Blueprint, request,jsonify
from Services import projectServices

project = Blueprint('project', __name__, url_prefix='/project')

@project.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    print(requestData)
    print(projectServices.add(**requestData,createBy='test'))
    return jsonify({'data':'ok'})

@project.route('/getList', methods=['POST'])
def getList():
    print(projectServices.getList())
    return jsonify({'list':projectServices.getList()})

