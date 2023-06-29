import json

from flask import Blueprint, request, jsonify

health = Blueprint('health', __name__, url_prefix='/health')


@health.route('/check', methods=['GET'])
def add():
    return jsonify({'result': 'health'})
