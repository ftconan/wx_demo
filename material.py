# coding=utf-8
import urllib2
import json
import poster.encode

from poster.streaminghttp import register_openers
from basic import Basic


class Material(object):
    def __init__(self):
        register_openers()

    def add_news(self, accessToken, news):
        """
        上传图文
        """
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = urllib2.urlopen(postUrl, news)
        print urlResp.read()

    def upload(self, accessToken, filePath, mediaType):
        """
        上传图片
        :param accessToken:
        :param filePath:
        :param mediaType:
        :return:
        """
        openFile = open(filePath, "rb")
        fileName = "hello"
        param = {"media": openFile, "fileName": fileName}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (accessToken, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        print urlResp.read()

    def get(self, accessToken, mediaId):
        """
        下载图片
        :param accessToken:
        :param mediaId:
        :return:
        """
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/get_material?access_token=%s" % accessToken
        postData = "{ \"media_id\": \"%s\" }" % mediaId
        urlResp = urllib2.urlopen(postUrl, postData)
        headers = urlResp.info().__dict__['headers']
        if ("Content-Type: application/json\r\n" in headers) or ("Content-Type: text/plain\r\n" in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            # 素材的二进制
            buffer = urlResp.read()
            medidaFile = file("test_media.jpg", "wb")
            medidaFile.write(buffer)
            print "get successful"

    def delete(self, accessToken, mediaId):
        """
        删除
        :param self:
        :param accessToken:
        :param mediaId:
        :return:
        """
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/del_material?access_token=%s" % accessToken
        postData = "{ \"media_id\": \"%s\" }" % mediaId
        urlResp = urllib2.urlopen(postUrl, postData)
        print urlResp.read()

    def batch_get(self, accessToken, mediaType, offset=0, count=20):
        """
        获取素材列表
        :param self:
        :param accessToken:
        :param mediaType:
        :param offset:
        :param count:
        :return:
        """
        postUrl = ("https://api.weixin.qq.com/cgi-bin/material"
                   "/batchget_material?access_token=%s" % accessToken)
        postData = ("{ \"type\": \"%s\", \"offset\": %d, \"count\": %d }"
                    % (mediaType, offset, count))
        urlResp = urllib2.urlopen(postUrl, postData)
        print urlResp.read()


if __name__ == "__main__":
    # add_new
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
    print news["articles"][0]["title"]
    news = json.dumps(news, ensure_ascii=False)
    myMaterial.add_news(accessToken, news)

    # batch_get
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    mediaType = "news"
    myMaterial.batch_get(accessToken, mediaType)
