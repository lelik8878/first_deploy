import random
import time

import requests

random_num = random.randint(1, 100)

def send_data_json_to_django(url, pyload):
    random_num = random.randint(1, 100)
    while True:
        time.sleep(5)
        pyload['number'] = random_num
        response = requests.post(url, json=pyload)
        print(response.text)

if __name__ == '__main__':

    send_data_json_to_django('http://127.0.0.1:8000/send_data/', pyload={'id': 1})
