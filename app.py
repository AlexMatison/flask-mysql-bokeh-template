from flask import Flask
import web

app = Flask(__name__)
app.register_blueprint(web.web_blueprint)

if __name__ == "__main__":
    app.run(debug=True)