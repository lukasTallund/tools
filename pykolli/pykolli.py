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
        self.update_id()

    def update_id(self,kolliid=None):
        if not kolliid:
            kolliid = self.kolliid
        self.page = requests.post(POST_URL, data=self.params).text
        self.bs_object = BeautifulSoup(self.page)
    
    def get_div_tag_value(self, tag_name):     
        div_results = self.bs_object.find_all("div", class_=tag_name)
        if div_results:
            return div_results[0].string
    
    def get_table_row(self, row_number):
        table_results =  self.bs_object.find_all("table")
        if table_results:
            table = table_results[0]
            return table.find_all("tr")[row_number]

    def get_table_item(self, row, position):
        if row:
            if len(row.find_all("td"))>position:
                return row.find_all("td")[position].string

    def get_time(self, row):
        return self.get_table_item(row, 0)

    def get_place(self, row):
        return self.get_table_item(row, 1)

    def get_last_time(self):
        return self.get_time(self.get_table_row(1))
    
    def get_last_place(self):
        return self.get_place(self.get_table_row(1))
    
    def get_last_update(self):
        return "{}: {}".format(self.get_last_time(), self.get_last_place())
    
