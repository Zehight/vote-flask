import json

from flask import Blueprint, request,jsonify
from Services import roundServices

round = Blueprint('round', __name__, url_prefix='/round')

@round.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    result = roundServices.add(**requestData,createBy='test')
    return jsonify({'data':result})

@round.route('/getList', methods=['POST'])
def getList():
    requestData = json.loads(request.data)
    return jsonify({'list':roundServices.getList(**requestData)})

@round.route('/getInfo', methods=['POST'])
def getInfo():
    requestData = json.loads(request.data)
    return jsonify({'data':roundServices.getInfo(**requestData)})

@round.route('/delInfo', methods=['POST'])
def delInfo():
    requestData = json.loads(request.data)
    return jsonify({'data':roundServices.delInfo(**requestData)})

