import requests

api_url_allgamedata = "https://127.0.0.1:2999/liveclientdata/allgamedata"

respone = requests.get(api_url_allgamedata, verify=False)
data = respone.json()['allPlayers']
print(data)