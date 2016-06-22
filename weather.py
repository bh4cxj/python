#!/usr/bin/env python
# coding:utf-8
#  "now": { //实况天气
#        "cond": { //天气状况
#            "code": "100", //天气状况代码
#            "txt": "晴" //天气状况描述
#        },
#        "fl": "30", //体感温度
#        "hum": "20%", //相对湿度（%）
#        "pcpn": "0.0", //降水量（mm）
#        "pres": "1001", //气压
#        "tmp": "32", //温度
#        "vis": "10", //能见度（km）
#        "wind": { //风力风向
#            "deg": "10", //风向（360度）
#            "dir": "北风", //风向
#            "sc": "3级", //风力
#            "spd": "15" //风速（kmph）
#        }
#    },
#
#    "aqi": { //空气质量，仅限国内部分城市，国际城市无此字段
#        "city": {
#            "aqi": "30", //空气质量指数
#            "co": "0", //一氧化碳1小时平均值(ug/m³)
#            "no2": "10", //二氧化氮1小时平均值(ug/m³)
#            "o3": "94", //臭氧1小时平均值(ug/m³)
#            "pm10": "10", //PM10 1小时平均值(ug/m³)
#            "pm25": "7", //PM2.5 1小时平均值(ug/m³)
#            "qlty": "优", //空气质量类别
#            "so2": "3" //二氧化硫1小时平均值(ug/m³)
#        }
#    },
#
#
import sys
import urllib
import urllib2
import json


class getWTR():
    def __init__(self):
        self.city = 'shanghai'
        self.apikey = "xxxxxxxxxxxxxxxxxxxxxxx"

    def get_wtr(self):
        url = 'http://apis.baidu.com/heweather/weather/free?city=%s' % self.city
        req = urllib2.Request(url)
        req.add_header("apikey", self.apikey)
        resp = urllib2.urlopen(req)
        content = resp.read()
        ax = content.find('[')
        bx = content[::-1].find(']')
        self.tmp = eval(content[ax+1:][::-1][bx+1:][::-1])
#        self.data = json.loads(self.tmp)
#        self.now = json.dumps(self.data["now"], ensure_ascii=False)
#        self.aqi = json.dumps(self.data["aqi"], ensure_ascii=False, indent=4)

    def parse_wtr(self):
        dictnow = self.tmp["now"]
        dictaqi = self.tmp["aqi"]["city"]
        now = "天气：%s    温度：%s℃      降水量：%smm    体感温度：%s℃   能见度：%skm    相对湿度：%s%%   风向：%s    风力：%s    风速：%skm/h" % (dictnow["cond"]["txt"], dictnow["tmp"], dictnow["pcpn"], dictnow["fl"], dictnow["vis"], dictnow["hum"], dictnow["wind"]["dir"], dictnow["wind"]["sc"], dictnow["wind"]["spd"])
        aqi = "空气质量指数：%s    一氧化碳：%sug/m³/h     二氧化氮：%sug/m³/h     臭氧：%sug/m³/h     PM10：%sug/m³/h     PM2.5：%sug/m³/h    二氧化硫：%sug/m³/h     空气质量：%s" % (dictaqi["aqi"], dictaqi["co"], dictaqi["no2"], dictaqi["o3"], dictaqi["pm10"], dictaqi["pm25"], dictaqi["so2"], dictaqi["qlty"])
        print  now
        print aqi


if __name__ == '__main__':
    a = getWTR()
    a.get_wtr()
    a.parse_wtr()
