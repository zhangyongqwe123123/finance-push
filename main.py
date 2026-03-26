import requests
import os

import requests
import re

import requests

import requests
import re

import feedparser

def get_finance_top10():
    # 网易财经RSS源（稳定可靠，无需解析HTML）
    rss_url = "https://money.163.com/special/feed/biz_top/"
    try:
        feed = feedparser.parse(rss_url)
        if feed.bozo != 0:
            return ["获取财经头条失败：RSS源解析错误"]
            
        news_list = []
        for entry in feed.entries[:10]:
            title = entry.get("title", "").strip()
            if title:
                news_list.append(title)
                
        if not news_list:
            return ["获取财经头条失败：未获取到有效新闻"]
        return news_list
    except Exception as e:
        return [f"获取新闻失败: {str(e)}"]
def send_wechat(msg):
    key = os.environ.get("SERVERCHAN_KEY")
    if not key:
        print("未配置KEY")
        return

    api = f"https://sctapi.ftqq.com/{key}.send"
    requests.post(api, data={
        "title": "财经头条推送",
        "desp": msg
    })
    print("推送成功")

if __name__ == "__main__":
    content = get_finance_top10()
    send_wechat(content)
