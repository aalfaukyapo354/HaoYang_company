from flask import Blueprint, render_template, jsonify

mod = Blueprint('rencaizhaopin', __name__, url_prefix='/rencaizhaopin')


# ไบบๆๆ่
@mod.route('/')
def index():
    return render_template('rencaizhaopin/rencaizhaopin.html')