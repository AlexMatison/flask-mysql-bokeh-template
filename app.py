from flask import Flask
import web
import settings

app = Flask(__name__)

def configure_app(flask_app):
    #flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    pass

def initialise_app(flask_app):
    configure_app(flask_app)
    flask_app.register_blueprint(web.web_blueprint)

if __name__ == "__main__":
    initialise_app(app)
    app.run(debug=True,
            host=settings.FLASK_SERVER_NAME,
            port=settings.FLASK_SERVER_PORT)