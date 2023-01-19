from flask import Blueprint, render_template, jsonify

mod = Blueprint('gongchengzhanshi', __name__, url_prefix='/gongchengzhanshi')


# 工程展示
@mod.route('/')
def index():
    return render_template('gongchengzhanshi/gongchengzhanshi.html')


# 工程展示/隧道工程
@mod.route('/suidaogongcheng/')
def suidaogongcheng():
    return render_template('gongchengzhanshi/suidaogongcheng.html')


# 工程展示/高速公路
@mod.route('/gaosugonglu/')
def gaosugonglu():
    return render_template('gongchengzhanshi/gaosugonglu.html')


# 工程展示/桥梁工程
@mod.route('/qiaolianggongcheng/')
def qiaolianggongcheng():
    return render_template('gongchengzhanshi/qiaolianggongcheng.html')


# 工程展示/地下管廊
@mod.route('/dixiaguanlang/')
def dixiaguanlang():
    return render_template('gongchengzhanshi/dixiaguanlang.html')


# 工程展示/房屋建筑
@mod.route('/fangwujianzhu/')
def fangwujianzhu():
    return render_template('gongchengzhanshi/fangwujianzhu.html')