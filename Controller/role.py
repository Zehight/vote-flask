import json

from flask import Blueprint, request,jsonify
from Services import roleServices

role = Blueprint('role', __name__, url_prefix='/role')

@role.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    print(requestData)
    print(roleServices.add(**requestData,createBy='test'))
    return jsonify({'data':'ok'})

@role.route('/getList', methods=['POST'])
def getList():
    print(roleServices.getList())
    return jsonify({'list':roleServices.getList()})

