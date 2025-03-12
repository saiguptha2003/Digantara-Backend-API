from models import LogEntry
from config import db
import json

def logAlgorithm(algorithmName, inputData, outputData):
    logEntry = LogEntry(
        algorithmName=algorithmName,
        inputData=json.dumps(inputData),
        outputData=json.dumps(outputData)
    )
    db.session.add(logEntry)
    db.session.commit()
