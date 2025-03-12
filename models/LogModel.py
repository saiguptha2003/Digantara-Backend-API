from config import  db
from datetime import datetime
import json

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    algorithmName = db.Column(db.String(255), nullable=False)
    inputData = db.Column(db.Text, nullable=False)
    outputData = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def toDict(self):
        return {
            "algorithmName": self.algorithmName,
            "inputData": json.loads(self.inputData),
            "outputData": json.loads(self.outputData),
            "timestamp": self.timestamp.isoformat(),
        }
