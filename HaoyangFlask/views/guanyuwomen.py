from flask import Blueprint, render_template, jsonify

mod = Blueprint('guanyuwomen', __name__, url_prefix='/guanyuwomen')


# 关于我们
@mod.route('/')
def index():
    return render_template('guanyuwomen/guanyuwomen.html')


# 关于我们/公司简介
@mod.route('/gongsijianjie/')
def gongsijianjie():
    return render_template('guanyuwomen/gongsijianjie.html')


# 关于我们/公司简介/组织架构
@mod.route('/zuzhijiagou/')
def zuzhijiagou():
    return render_template('guanyuwomen/zuzhijiagou.html')


# 关于我们/公司简介/企业文化
@mod.route('/qiyewenhua/')
def qiyewenhua():
    return render_template('guanyuwomen/qiyewenhua.html')


# 关于我们/公司简介/公司资质
@mod.route('/gongsizizhi/')
def gongsizizhi():
    return render_template('guanyuwomen/gongsizizhi.html')
