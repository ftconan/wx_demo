# coding=utf-8
from basic import Basic
import urllib2
import poster.encode
from poster.streaminghttp import register_openers
import json


class Media(object):
    def __init__(self):
        register_openers()

    def upload(self, accessToken, filePath, mediaType):
        """
        上传图片
        :param accessToken:
        :param filePath:
        :param mediaType:
        :return:
        """
        openFile = open(filePath, "rb")
        param = {"media": openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
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
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib2.urlopen(postUrl)

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


if __name__ == "__main__":
    # upload
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = "D:/code/mpGuide/media/test.jpg"
    mediaType = "image"
    myMedia.upload(accessToken, filePath, mediaType)

    # get
    myMedia = Media()
    accessToken = Basic().get_access_token()
    mediaId = "2ZsPnDj9XIQlGfws31MUfR5Iuz-rcn7F6LkX3NRCsw7nDpg2268e-dbGB67WWM-N"
    myMedia.get(accessToken, mediaId)
