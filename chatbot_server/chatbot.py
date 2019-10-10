"""

pip install requests
pip install numpy
pip install sklearn
pip install jieba
pip install flask 

"""
# flask是web服务的
from flask import Flask

app = Flask(__name__)


# 这里配置的是我们的url访问路径
@app.route("/")
def hello_world():
    return "大周老师是世界上最帅的人"


if __name__ == "__main__":
    app.run
