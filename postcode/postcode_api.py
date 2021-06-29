import requests

class ValidPostcodeChecker:
    def __init__(self, postcode):
        self.api_requests(postcode)
        self.postcode = postcode

    def api_requests(self, postcode):
        url = "https://api.postcodes.io/postcodes/" + postcode
        response = requests.get(url)

        if response:
            print("success")
            response_dict = response.json()['result']
            print("Country: {}".format(response_dict['country']))
            print("region: {}".format(response_dict ['region']))
            print("longitude: {}".format(response_dict['longitude']))
            print("latitude: {}".format(response_dict['latitude']))
            print("admin_district: {}".format(response_dict['admin_district']))
        else:
            print("failed test!!")
            print("Postcode Invalid")


    def full_info(self):
        url = "https://api.postcodes.io/postcodes/" + self.postcode
        response = requests.get(url).json()['result']

        for key in response:
            print("{} : {}".format(key, response[key]))




