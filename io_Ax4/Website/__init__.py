from flask import Flask


def IO():
    app = Flask(__name__)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app