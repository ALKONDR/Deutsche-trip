# # API now is not working

# import json
# from flask import abort, request, Flask
# import requests

# api_key = json.load(open('../secret.json'))['skyscanner']

# post_form = {
# 	'apiKey' : api_key,
# 	'country' : 'UK',
# 	'currency' : 'EUR',
#     'locale': 'en-GB',
#     'originplace' : 'SIN-sky',
#     'destinationplace': 'KUL-sky',
#     'outbounddate': '2017-03-28',
#     'inbounddate' : '2016-03-30',
#     'adults' : 1
# }

# response = requests.post('http://partners.api.skyscanner.net/apiservices/pricing/v1.0', data = post_form)

# print(response.json())