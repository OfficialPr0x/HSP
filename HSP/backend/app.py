from flask import Flask
from flask_cors import CORS
from config import Config
from routes import auth, guide, tools
from models import db
from logging.config import dictConfig

# Configure logging
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(guide.bp)
    app.register_blueprint(tools.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)