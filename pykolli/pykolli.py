import urllib.request
import json

POST_URL ="http://147.14.240.50/wsp/rest-services/ntt-service-rest/api/shipment.json?id={}&locale=en&consumerId=eb3fea65-34a0-4e10-ab0e-1f42139a72fc"

class KolliId(object):
    def __init__(self, kolliid):
        with urllib.request.urlopen(POST_URL.format(kolliid)) as url:
            if url.code == 200:
                self.response = url.read()
                self.data = json.loads(self.response.decode())['TrackingInformationResponse']['shipments'][0]
    
    def print_data(self):
        print(json.dumps(self.data, indent=4, ensure_ascii=False))

    def print_formated(self):
        print('Package from: {}'.format(self.get_from_name()))
        print('Status: {}'.format(self.get_status_body()))
        print('Latest event: {}'.format(self.get_event_string()))
    
    def get_item_data(self, field, item=0):
        return self.data['items'][item][field]
    
    def get_events(self):
        return self.get_item_data('events')

    def get_event(self, number=-1):
        return self.get_events()[number]

    def get_status(self):
        return self.data['statusText']

    def get_from(self):
        return self.data['consignor']

    def get_from_name(self):
        return self.get_from()['name']

    def get_status_body(self):
        try:
            body = self.get_status()['estimatedTimeOfArrival']
        except KeyError:
            body = self.get_status()['body']
        return body

    def get_event_string(self, number=-1):
        event = self.get_event(number)
        time = event['eventTime']
        place = event['location']['displayName']
        description = event['eventDescription']
        return '{} {} {}'.format(time, place, description)
