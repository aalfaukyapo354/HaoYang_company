from flask import Blueprint, render_template, jsonify
from utils import DocToHtml

mod = Blueprint('xinwenzixun', __name__, url_prefix='/xinwenzixun')


# 新闻资讯
@mod.route('/')
def index():
    return render_template('xinwenzixun/xinwenzixun.html')


# 新闻资讯/行业新闻
@mod.route('/hangyexinwen/')
def hangyexinwen():
    return render_template('xinwenzixun/hangyexinwen.html')


# 新闻资讯/行业新闻/具体新闻
@mod.route('/hangyexinwen/<page>/')
def hangyexinwen_int(page):
    neirong = DocToHtml('HaoyangFlask/static/uploads/2020年述职报告.docx')
    return render_template(f'xinwenzixun/hangyexinwen/'+str(page), neirong=neirong)


# 新闻资讯/公司动态
@mod.route('/gongsidongtai/')
def gongsidongtai():
    return render_template('xinwenzixun/gongsidongtai.html')


# 新闻资讯/公司动态/具体新闻
@mod.route('/gongsidongtai/<page>/')
def gongsidongtai_int(page):
    return render_template(f'xinwenzixun/gongsidongtai/'+str(page))