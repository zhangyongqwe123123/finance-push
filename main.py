import requests
import os

def get_finance_top10():
    url = "https://interface.sina.cn/news/finance_index.d.html"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        news_list = data.get("list", [])[:10]  # 取前10条
        msg = "📈 财经头条 TOP10（每10分钟更新）\n\n"
        for i, item in enumerate(news_list, 1):
            title = item.get("title", "")
            msg += f"{i}. {title}\n"
        return msg
    except Exception as e:
        return f"获取新闻失败: {str(e)}"

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
