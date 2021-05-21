import requests

SHEETY_ENDPOINT = "https://api.sheety.co/dca6ac72c87dc84251d90fc67ef39e87/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    'iataCode': city['iataCode']
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)






