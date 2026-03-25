import requests
import os

def get_finance_top10():
    url = "https://api.jinse.com/v3/information/lists?limit=10"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        msg = "📈 财经头条 TOP10（每10分钟更新）\n\n"
        for i, item in enumerate(data["list"][:10], 1):
            msg += f"{i}. {item['title']}\n"
        return msg
    except:
        return "获取新闻失败"

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
