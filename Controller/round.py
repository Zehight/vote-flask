import json

from flask import Blueprint, request,jsonify
from Services import roundServices

round = Blueprint('round', __name__, url_prefix='/round')

@round.route('/add', methods=['POST'])
def add():
    requestData = json.loads(request.data)
    print(requestData)
    print(roundServices.add(**requestData,createBy='test'))
    return jsonify({'data':'ok'})

@round.route('/getList', methods=['POST'])
def getList():
    requestData = json.loads(request.data)
    print(requestData)
    return jsonify({'list':roundServices.getList(**requestData)})

