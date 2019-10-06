import requests
import json
import random


def write_browser_info_to_file():
    my_user_agent = requests.get("http://fake-useragent.herokuapp.com/browsers/0.1.11")

    with open("browser_info.json", "w") as f:
        # f.write写入到文件中的是一个字符串
        # f.write(my_user_agent.text)  # 1
        # json.dump写入到文件中的是一个json格式的数据，后边可以使用json.load拿出来，直接当做一个json来进行数据的获取
        json.dump(my_user_agent.text, f) # 2

# write_browser_info_to_file()


"""
操作文件
json.dump  数据将以json数据的格式写入到文件中
json.load  数据将以json数据的格式读取文件
操作对象
json.dumps 将一个python数据类型转换为json数据类型
json.loads 将一个json数据类型转换为python数据类型
"""


def get_random_browser():
    with open("browser_info.json", "r") as f:
        browsers_json = json.load(f)
        # print(type(browsers_json))
        browsers_json = json.loads(browsers_json)
        # print(type(browsers_json))
        browsers = browsers_json["browsers"]
        i = random.randint(0, len(browsers))
    browser_name = ""
    if i == 0:
        browser_name = "chrome"
    elif i == 1:
        browser_name = "opera"
    elif i == 2:
        browser_name = "firefox"
    elif i == 3:
        browser_name = "internetexplorer"
    elif i == 4:
        browser_name = "safari"
    
    # print("所获得的浏览器名字是:{}".format(browser_name))
    # print(browsers[browser_name])
    final_browser = browsers[browser_name][random.randint(0, len(browsers[browser_name])-1)]
    # print("所获得的浏览器是:{}".format(final_browser))
    return final_browser


get_random_browser()
        


"""
open一个文件    r w a r+ w+ a+ b t +
w 是写，会覆盖与运来的文件么
原文件内容：我爱大周老师
写入内容：喜欢
问: 用w权限写入 喜欢 两个字后，文件的内容是什么？

"""

# s = open("1.txt", "w")
# s.write("lo")