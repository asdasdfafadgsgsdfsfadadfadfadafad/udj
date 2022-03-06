# authorization: ODUyNDMxNjg4NDI0MjI2ODI2.YiHM_Q.ofuALpjvf4nBF4mYKS37YjovrSo
import time
import requests

payload = {"content": "Good morning"}
header = {
    "authorization": "ODUyNDMxNjg4NDI0MjI2ODI2.YiHM_Q.ofuALpjvf4nBF4mYKS37YjovrSo"
}


while True:
    time.sleep(5)
    requests.post(
        "https://discord.com/api/v9/channels/944016716738998312/messages",
        data=payload,
        headers=header,
    )
