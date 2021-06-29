

# import requests
#
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/")
#
# if check_response_postcode.status_code == 200:
#     print("postcode is valid")
#     print("Status code: {}" .format(check_response_postcode.status_code))
#
# else:
#     print("OOps something went wrong")
#
#
# import requests
#
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/nw24pn")
# if check_response_postcode:                             # Functionality is abstracted
#     print("Success")
# else:
#     print("unavailable")
#
#


import requests

check_response_postcode = requests.get("https://api.postcodes.io/postcodes/nw24pn")

# print(type(check_response_postcode.headers))




response_dict = check_response_postcode.json()["result"]

for key in response_dict.keys():
    print(f"The name if the key is {key} and the value inside the key is {response_dict[key]}")


postcode = input("Enter a postcode?")

url ="https://api.postcodes.io/postcodes/" + postcode

response = requests.get(url)

if response:
    print("success")

while True:
    postcode = input("Enter a postcode?")
    url = "https://api.postcodes.io/postcodes/" + postcode
    if response:
        print("success")
    else:
