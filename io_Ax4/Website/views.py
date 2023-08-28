from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def app():
    return render_template("io.html")