# API Requests

- API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.

- API requests are made via `requests.get(url)`.
- Status code `200 ` must be received to indicate successful response.
- Next the response must be processed into `json` format for data scraping.
- Data is targeted via key-value pairs.

```python
import requests

 check_response_postcode = requests.get("https://api.postcodes.io/postcodes/")

if check_response_postcode.status_code == 200:
     print("postcode is valid")
     print("Status code: {}" .format(check_response_postcode.status_code))
     response_dict = check_response_postcode.json()["result"]

    for key in response_dict.keys():
        print(f"The name if the key is {key} and the value inside the key is {response_dict[key]}")

else:
     print("OOps something went wrong")
```


## Postcode Checker

- `ValidPostcodeChecker` is a class that checks for a valid postcode and display info regarding postcode by making an API request.

```python
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

```