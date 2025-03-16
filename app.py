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
    
    port = int(os.environ.get("PORT", 5000))  # Get the port from the environment variable
    app.run(host="0.0.0.0", port=port, debug=True)  # Bind to all network interfaces
