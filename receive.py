# coding=utf-8
import xml.etree.ElementTree as ET


def parse_xml(web_data):
    """
    解析xml
    :param web_data:
    :return:
    """
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.finde("MsgType").text
    if msg_type == "event":
        event_type = xmlData.find("Event").text
        if event_type == "CLICK":
            return Click(xmlData)
        # elif event_type in ('subscribe', 'unsubscribe'):
            # return Subscribe(xmlData)
        # elif event_type == 'VIEW':
            # return View(xmlData)
        # elif event_type == 'LOCATION':
            # return LocationEvent(xmlData)
        # elif event_type == 'SCAN':
            # return Scan(xmlData)
    elif msg_type == "text":
        return TextMsg(xmlData)
    elif msg_type == "image":
        return ImageMsg(xmlData)


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find("ToUserName").text
        self.FromUserName = xmlData.find("FromUserName").text
        self.CreateTime = xmlData.find("CreateTime").text
        self. MsgType = xmlData.find("MsgType").text
        self.MsgId = xmlData.find('MsgId').text


class TextMsg(Msg):
    """
    文本处理
    """
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find("Content").text.encode("utf-8")


class ImageMsg(Msg):
    """
    图片处理
    """
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find("PicUrl").text
        self.MediaId = xmlData.find('MediaId').text


class EventMsg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.Event = xmlData.find('Event').text


class Click(EventMsg):
    def __init__(self, xmlData):
        EventMsg.__init__(self, xmlData)
        self.Eventkey = xmlData.find('EventKey').text
