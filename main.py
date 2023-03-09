import requests
import simplejson as json
import time

url = ""
headers = {"Content-Type": "application/json", "User-Agent": "MyBot/1.0"}

filename = "logs.txt"
file = open(filename, "r")
file.seek(0, 2)  # move file pointer to end of file

while True:
    line = file.readline()
    if not line:
        time.sleep(0.1) 
        continue

    try:
        # process new chat line here
        if line.strip()[0] != '<' or ('has' is line.strip() == False):
            continue

        data = {"content": line.strip()}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 204:
            print(f"{line.strip()} sent successfully.")
        else:
            print(f"{line.strip()} failed to send.")
    except:
        print('ERROR OCCURED')