import requests
import json
import pandas as pd
from utils import get_random_browser
from ips import get_random_ip



def get_request_url_and_headers():
    try:
        user_agent = get_random_browser()
        ip = get_random_ip()
    except:
        get_request_url_and_headers()

    
    # 用户代理
    headers = {
        "user-agent": user_agent
    }

    # ip代理池
    proxies = {
        "url": ip
    }

    response = requests.get("https://www.toutiao.com/api/pc/feed/?max_behot_time=1570014119&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A165FDC914FD035&cp=5D948DB0E3B5EE1&_signature=53TC5xAWuusPruCa3WRkJOd0wv",
                             headers=headers,
                             proxies=proxies)
    # print(response.text.encode("utf-8").decode("unicode_escape"))
    respose_json = json.loads(response.text)
    # print(respose_json)
    print(respose_json["message"])
    if respose_json["message"] == "error":
        get_request_url_and_headers()
    return respose_json


# json_content = get_request_url_and_headers()



# def data_to_file():
#     data = json_content["data"]
#     for i in range(len(data)):
#         data_dict = data[i]
#         print(data_dict)
#         with open("toutiao.json", "a+") as f:
#             json.dump(data_dict, f, ensure_ascii=False)
#             f.write("\n")


# data_to_file()


"""
pip install pandas
pip install openpyxl
"""


df = pd.read_json("toutiao.json", lines=True)
print(df)
df.to_excel("toutiao.xlsx")




