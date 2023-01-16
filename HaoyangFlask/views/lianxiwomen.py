from flask import Blueprint, render_template, jsonify

mod = Blueprint('lianxiwomen', __name__, url_prefix='/lianxiwomen')


# 联系我们
@mod.route('/')
def index():
    return render_template('lianxiwomen/lianxiwomen.html')