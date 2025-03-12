from flask import Blueprint, jsonify
from models import LogEntry

logBp = Blueprint('log', __name__)

@logBp.route('/logs', methods=['GET'])
def getLogs():
    logs = LogEntry.query.all()
    return jsonify([log.toDict() for log in logs])
