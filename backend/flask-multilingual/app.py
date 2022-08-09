from flask import Flask, g, request
from flask_restplus import Resource, Api
from flask_babel import Babel, gettext

app = Flask(__name__)
api = Api(app)
app.config["BABEL_DEFAULT_LOCALE"] = "en"
babel = Babel(app)


@babel.localeselector
def get_locale():
    translations = [str(translation) for translation in babel.list_translations()]
    return request.accept_languages.best_match(translations)


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return gettext("Hello World")


@api.route("/great")
class Great(Resource):
    def get(self):
        return gettext("Great")


if __name__ == "__main__":
    app.run(debug=True)
