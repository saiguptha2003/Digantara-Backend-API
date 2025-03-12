import os
from flask import Flask
from config import Config
from flask_migrate import init, Migrate
from config import db
from routes import algorithmBp
from routes import logBp
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(algorithmBp, url_prefix="/api")
app.register_blueprint(logBp, url_prefix="/api")

if __name__ == '__main__':
    
    app.run(debug=True)
