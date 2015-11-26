import requests
from bs4 import BeautifulSoup

POST_URL = "http://www.posten.se/tracktrace/TrackConsignments_do.jsp" 
POST_PARAM_DICT = {"trackntraceAction" : "saveSearch", "lang":"GB", "consignmentId": ""}

class KolliId(object):
    def __init__(self, kolliid):
        self.kolliid = kolliid
        self.bs_object = None
        self.page = None 
        self.params = POST_PARAM_DICT
        self.params["consignmentId"] = self.kolliid

    def update_id(self,kolliid=None):
        if not kolliid:
            kolliid = self.kolliid
        self.page = requests.post(POST_URL, data=self.params).text
        self.bs_object = BeautifulSoup(self.page)
    def get_tag_value(self, tag_name):     
        return self.bs_object.find_all("div", class_=tag_name)[0].string
