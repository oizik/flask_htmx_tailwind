__version__ = '0.1.0'

from flask import Flask
from flask_assets import Bundle, Environment


def create_app():
    app = Flask(__name__)

    assets = Environment(app)
    css = Bundle("main.css", output="dist/main.css", filters="postcss")
    js = Bundle("js/*.js", output="dist/main.js")

    assets.register("css", css)
    assets.register("js", js)
    css.build()
    js.build()

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
