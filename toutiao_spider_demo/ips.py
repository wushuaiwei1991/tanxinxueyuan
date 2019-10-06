import random


ip_list = [
"http://113.103.226.147:",	
"http://134.175.81.16:1080",	
"http://113.103.227.147:",	
"http://180.104.63.194:9000",
"http://114.239.144.187:",	
"http://113.123.28.125:",	
"http://106.42.161.222:",	
"http://222.184.7.206:43327",
"http://121.232.148.28:9000",	
"http://110.86.139.146:",	
"http://180.150.185.191:10820",	
"http://14.29.232.142:8082",	
"http://136.228.128.14:61158",	
"http://125.123.64.221:",          
]


def get_random_ip():
    return ip_list[random.randint(0, len(ip_list)-1)]


get_random_ip()
    
# import requests
# response = requests.get("https://www.kuaidaili.com/free/inha/")
# print(response.text)

# from fake_useragent import UserAgent
# ua = UserAgent()

# print(ua.ie)
# print(ua.msie)


