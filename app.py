from flask import Flask, render_template
from HaoyangFlask import app

# 网站首页
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=Flask, port=1129, use_reloader=False)