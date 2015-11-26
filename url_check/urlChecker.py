import requests
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class URLChecker(object):
    def __init__(self, adress, arguments):
        self.adress = adress
        self.arguments = arguments
        self.page = None

    def update_page(self):
        self.page = requests.post(self.adress,params=self.arguments).text.split("\n")

    def find_row(self, field):
        if self.page:
            for row, line in enumerate(self.page):
                if field in line:
                    return row
        else:
            self.update_page()
            return self.find_row(field)

    def get_matching_row(self, matching_string, offset=0):
        if self.page:
            return self.get_row(self.find_row(matching_string)+offset)
        else:
            self.update_page()
            return self.get_matching_row(matching_string, offset)
    
    def get_row(self, row):
        if self.page:
            return strip_tags(self.page[int(row)]).strip()
                
    def get_rows(self, rows):
        if self.page:
            row_list = []
            for row in rows:
                row_list.append(self.get_row(row))
            return row_list   
