import requests
import os
from dotenv.main import load_dotenv

# loads the .env file into the environment
load_dotenv()

day = input("Day: ")
url = "https://adventofcode.com/2022/day/8/input"
headers = {"cookie": os.getenv("ADVENTOFCODE_USER_COOKIE", "")}
r = requests.get(url, headers=headers)
if r.status_code == 200:
    with open("day8.txt", "w") as f:
        f.write(r.text)
        f.close()
