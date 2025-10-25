import requests
import time

def tryGameStart():
    api_url_allgamedata = "https://127.0.0.1:2999/liveclientdata/allgamedata"
    waittime = 2
    max_tries = 20

    for counter in range(max_tries):
        try:
            response = requests.get(api_url_allgamedata, verify=False)
            if response.status_code == 200:
                data = response.json()['allPlayers']
                print(data)
                return True
        except requests.exceptions.RequestException as e:
            print(f"Attempt {counter + 1}/{max_tries}: {e}")

        time.sleep(waittime)

    print("Max retries reached. Exiting.")
    return False


def laningStartTip():
    prompt = "Provide 5 concise tips for the laning phase in League of Legends."
    return None

