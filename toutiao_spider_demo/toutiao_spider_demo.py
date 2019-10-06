import requests
import json
import random

# 用户代理
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

# ip代理池
proxies = {
    "url": "http://39.137.107.98:80"
}

response = requests.get("https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1A5AD09E1882D6&cp=5D9148F2FDB6FE1&_signature=A8v6tBATXmDrEdjJZn-axgPL-q",
                         headers=headers,
                         proxies=proxies)
print(response.text.encode("utf-8").decode("unicode_escape"))



def get_one_user_agent():
    my_user_agent = requests.get("http://fake-useragent.herokuapp.com/browsers/0.1.11")
    agent_json = json.loads(my_user_agent.text)
    print(agent_json)
    browsers = agent_json["browsers"]
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
    
    print("所获得的浏览器名字是:{}".format(browser_name))

    print(browsers[browser_name])

    final_browser = browsers[browser_name][random.randint(0, len(browsers[browser_name])-1)]
    print("所获得的浏览器是:{}".format(final_browser))


# get_one_user_agent()