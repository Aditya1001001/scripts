import requests

url = "https://google-search3.p.rapidapi.com/api/v1/search"

querystring = {"get_total":"false","country":"US","language":"lang_en","max_results":"100","uule":"w%2BCAIQICIbSG91c3RvbixUZXhhcyxVbml0ZWQgU3RhdGVz","q":"site%3A rapidapi.com %22apigeek%22"}

headers = {
    'x-rapidapi-host': "google-search3.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)