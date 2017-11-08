# coding=utf-8
import urllib2
import json

from basic import Basic


class Material(object):
    """
    上传图文
    """
    def add_new(self, accessToken, news):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = urllib2.urlopen(postUrl, news)
        print urlResp.read()


if __name__ == "__main__":
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    news = (
        {
            "articles":
                [
                    {
                        "title": "test",
                        "thumb_media_id": "X2UMe5WdDJSS2AS6BQkhTw9raS0pBdpv8wMZ9NnEzns",
                        "author": "vickey",
                        "digest": "",
                        "show_cover_pic": 1,
                        "content": "<p><img data-s=\"300,640\" data-type=\"jpeg\" data-src=\"http://mmbiz.qpic.cn/mmbiz/iaK7BytM0QFPLhxfSMhOHlZd2Q5cw3YibKVf4dgNpLHXdUkvl65NBSMU71rFfOEKF3ucmXuwAQbNdiaaS3441d5rg/0?wx_fmt=jpeg\" data-ratio=\"0.748653500897666\" data-w=\"\"  /><br  /><img data-s=\"300,640\" data-type=\"jpeg\" data-src=\"http://mmbiz.qpic.cn/mmbiz/iaK7BytM0QFPLhxfSMhOHlZd2Q5cw3YibKiaibdNgh0ibgOXAuz9phrGjYFBUKlyTBcrv5WE5zic08FUcz5ODXCHEykQ/0?wx_fmt=jpeg\" data-ratio=\"0.748653500897666\" data-w=\"\"  /><br  /></p>",
                        "content_source_url": "",
                    }
                ]
        })

    # type(news) dict
    # news["articles"][0]["title"] = u"测试".encode("utf-8")
    # print news["articles"][0]["title"]
    news = json.dumps(news, ensure_ascii=False)
    myMaterial.add_new(accessToken, news)
