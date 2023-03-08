import requests
import simplejson as json
import time

url = "https://discord.com/api/webhooks/1082850421409845399/zCw3hMaHh0itrouprwVZ9bk8Jeyj8qUOuAZe7opfgo-PVLda6DSgLunZTJlF7aZk5YYx"
headers = {"Content-Type": "application/json", "User-Agent": "MyBot/1.0"}

filename = "logs.txt"
file = open(filename, "r")
file.seek(0, 2)  # move file pointer to end of file

while True:
    line = file.readline()
    if not line:
        time.sleep(0.1)  # wait for new lines
        continue
    # process new chat line here
    data = {"content": line.strip()}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print(f"{line.strip()} sent successfully.")
    else:
        print(f"{line.strip()} failed to send.")