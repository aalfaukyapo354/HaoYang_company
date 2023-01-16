from flask import Blueprint, render_template, jsonify

mod = Blueprint('xinwenzixun', __name__, url_prefix='/xinwenzixun')


# 新闻资讯
@mod.route('/')
def index():
    return render_template('xinwenzixun/xinwenzixun.html')


# 新闻资讯/行业新闻
@mod.route('/hangyexinwen/')
def hangyexinwen():
    return render_template('xinwenzixun/hangyexinwen.html')


# 新闻资讯/公司动态
@mod.route('/gongsidongtai/')
def gongsidongtai():
    return render_template('xinwenzixun/gongsidongtai.html')