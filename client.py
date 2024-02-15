import requests
import time 

def get_message():
    while True:
        time.sleep(2)
        message = requests.get("http://127.0.0.1:5000")
        print(message.content)


if __name__ == "__main__":
    get_message()