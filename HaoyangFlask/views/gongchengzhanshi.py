from flask import Blueprint, render_template, jsonify

mod = Blueprint('gongchengzhanshi', __name__, url_prefix='/gongchengzhanshi')


# 工程展示
@mod.route('/')
def index():
    return render_template('gongchengzhanshi/gongchengzhanshi.html')


# 工程展示/房屋结构
@mod.route('/fangwujiegou/')
def fangwujiegou():
    return render_template('gongchengzhanshi/fangwujiegou.html')


# 工程展示/市政公路
@mod.route('/shizhenggonglu/')
def shizhenggonglu():
    return render_template('gongchengzhanshi/shizhenggonglu.html')


# 工程展示/机电安装
@mod.route('/jidiananzhuang/')
def jidiananzhuang():
    return render_template('gongchengzhanshi/jidiananzhuang.html')


# 工程展示/装饰装修
@mod.route('/zhuangshizhuangxiu/')
def zhuangshizhuangxiu():
    return render_template('gongchengzhanshi/zhuangshizhuangxiu.html')


# 工程展示/钢结构
@mod.route('/gangjiegou/')
def gangjiegou():
    return render_template('gongchengzhanshi/gangjiegou.html')