from datetime import datetime

import pymysql
import requests
import json
import time
import SQLtool

res = SQLtool.GetTopic()
url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/fetch_dynamics?"
offset = 0
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/86.0.4240.198 Safari/537.36"}


def GetOneTopic(a):
    offset = 0
    obj = datetime.now()
    while True:
        time.sleep(0.5)
        param = {
            "topic_name": a,
            "offset": offset,
            "sortby": 2,
            "platform": "h5"
        }
        r = requests.get(url, headers=header, params=param)
        delecious = json.loads(r.text)
        offset = delecious["data"]["offset"]
        if "cards" not in delecious["data"] :
            break;
        for card in delecious["data"]["cards"]:
            verydecsious = json.loads(card["card"])

            if "first_frame" not in verydecsious:
                topic = ''
                if 'topic_info' not in card["display"]:
                    break;
                for to in card["display"]["topic_info"]["topic_details"]:
                    topic += to["topic_name"] + ","
                    if len(topic) > 100:
                        break
                if "item" in verydecsious:
                    if "pictures" in verydecsious["item"]:
                        for th in verydecsious["item"]["pictures"]:
                            try:
                                SQLtool.addPic(th["img_src"], topic, obj.strftime("%Y-%m-%d %H:%M:%S"),
                                                verydecsious["user"]["name"],
                                                verydecsious["item"]["upload_time"], card["desc"]["like"])
                            except pymysql.err.IntegrityError:
                                print("已有")
        if delecious["data"]["has_more"] == 0:
            break;



Topic = SQLtool.GetTopic()
for topic in Topic:
    GetOneTopic(topic[1])
