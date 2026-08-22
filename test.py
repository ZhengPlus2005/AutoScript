import os

import requests

URL = "https://www.shiyuyouios.com/wp-admin/admin-ajax.php"

# 从环境变量读取登录凭据，避免把 Cookie 提交到 Git 仓库。
COOKIE = os.environ["SHIYUYOU_COOKIE"]

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.shiyuyouios.com/users?tab=credit",
    "Origin": "https://www.shiyuyouios.com",
    "Cookie": COOKIE,
}

data = {
    "action": "daily_sign"
}

try:
    response = requests.post(
        URL,
        headers=headers,
        data=data,
        timeout=15
    )
    result = response.json()

    print("状态：", result["success"])
    print("消息：", result["msg"])
    #print("HTTP 状态码：", response.status_code)
    #print("服务器响应：", response.text)

except requests.RequestException as e:
    print("签到请求失败：", e)
