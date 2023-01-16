from flask import Blueprint, render_template, jsonify

mod = Blueprint('rencaizhaopin', __name__, url_prefix='/rencaizhaopin')


# 人才招聘
@mod.route('/')
def index():
    return render_template('rencaizhaopin/rencaizhaopin.html')