import requests
import os

import requests
import re

import requests

import requests
import re

def get_finance_top10():
    # 东方财富网滚动新闻页面（稳定可靠）
    url = "https://finance.eastmoney.com/news/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://finance.eastmoney.com/"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.encoding = "utf-8"
        html = resp.text
        
        # 匹配东方财富新闻标题（适配页面结构）
        pattern = r'<a href="https://finance.eastmoney.com/news/[^\"]+" target="_blank" title="([^"]+)">'
        matches = re.findall(pattern, html)
        
        # 去重并取前10条
        news_list = []
        seen = set()
        for title in matches:
            clean_title = title.strip()
            if clean_title and clean_title not in seen:
                seen.add(clean_title)
                news_list.append(clean_title)
                if len(news_list) >= 10:
                    break
                    
        if not news_list:
            return ["获取财经头条失败：未匹配到有效新闻"]
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
