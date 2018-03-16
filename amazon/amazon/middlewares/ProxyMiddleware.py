import json
import random
import requests


class ProxyMiddleware(object):
    valid_proxies = []

    def __init__(self):
        with open('proxy.json', 'r') as f:
            self.proxies = json.load(f)
        print("start init")
        url = "http://ip.chinaz.com/getip.aspx"
        url = "https://www.baidu.com/"
        for proxy in self.proxies:
            p = {"http:": "http://"+proxy,
                 "https:": "http://" + proxy}
            try:
                requests.get(url, proxies=p)
                self.valid_proxies.append(proxy)
            except Exception as e:
                print(e)
        print("valid proxies number : %d" % len(self.valid_proxies))

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://{}'.format(random.choice(self.valid_proxies))
