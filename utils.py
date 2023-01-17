
from pydocx import PyDocX
from bs4 import BeautifulSoup
import os

# 默认style
init_style = """
* { margin: 0;padding: 0;}
body { padding: 10px !important;}
table td {border-style: solid;}
"""


class DocToHtml:
    def __init__(self, file):
        self.soup = None
        self.file = file
    # 获取文档内容

    def get_doc_content(self):
        html = PyDocX.to_html(self.file)
        self.soup = BeautifulSoup(html, 'html.parser')  # 使用lxml解析库

    # 修改html内容
    def update_html(self):
        # 插入新的meta
        meta = self.soup.new_tag(
            'meta', content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0;')
        self.soup.head.insert(1, meta)
        # 删除style
        self.soup.style.clear()
        self.soup.style.append(init_style)
        # 格式化代码，自动补全代码
        self.soup.prettify()
        self.soup = self.soup.body


    # 生成html文件
    def save_html(self):
        filename = os.path.basename(self.file)
        filename = filename.split('.')[0]
        path = os.path.dirname(self.file)
        print(os.path.dirname(self.file))
        f = open(path + '/' + filename+'.html', 'w', encoding="utf-8")
        f.write(str(self.soup))
        f.close()

    def run(self):
        self.get_doc_content()
        self.update_html()
        self.save_html()


if __name__=='__main__':
    d = DocToHtml('HaoyangFlask/static/uploads/2020年述职报告.docx')
    d.run()