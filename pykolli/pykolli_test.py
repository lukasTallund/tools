from pykolli import KolliId
from bs4 import BeautifulSoup

myId = KolliId("")
myId.update_id()

print(myId.get_tag_value("consignmentId"))
