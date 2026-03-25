import requests
import os

import requests
import re

import requests

def get_finance_top10():
    # 新浪财经滚动新闻API（稳定可靠）
    url = "https://api.finance.sina.com.cn/index.php?page=1&num=10&column=stock&keyword=&type=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        data = resp.json()
        
        if data.get("status") != "ok":
            return ["获取新浪财经头条失败：API返回状态异常"]
            
        news_list = []
        for item in data.get("data", []):
            title = item.get("title", "").strip()
            if title:
                news_list.append(title)
                if len(news_list) >= 10:
                    break
                    
        if not news_list:
            return ["获取新浪财经头条失败：未获取到有效新闻"]
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
