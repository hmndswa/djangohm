import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"       #based off django

get_response = requests.get(endpoint, json={"product_id": 123 }) #HTTP Request
#print(get_response.text) #print the raw text response
print(get_response.status_code)


#print(get_response.json()['message'])      #print the raw text response
#print(get_response.status_code)
print("Raw Text:\n", get_response.text)
  