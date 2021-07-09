from flask import Blueprint, request

exam_bp = Blueprint("example", __name__)

@exam_bp.route("/hello")
def print_hello():
    return "Hello"