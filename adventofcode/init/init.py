import requests
import os
from dotenv.main import load_dotenv

# loads the .env file into the environment
load_dotenv()
url_year = "2022"


def fetch_input(day: str, new_file_name: str):
    url_day = day[1] if day[0] == "0" else day
    url = f"https://adventofcode.com/{url_year}/day/{url_day}/input"
    headers = {"cookie": os.getenv("ADVENTOFCODE_USER_COOKIE", "")}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        with open(f"../{url_year}/{new_file_name}.txt", "x") as f:
            f.write(r.text)
            f.close()
            print(f"Success: day{new_file_name}.txt created.")
    else:
        print("Error: Cannot fetch input.")


def generate_new_file_name(day: str) -> str:
    if len(day) == 1:
        day = "0" + day

    return "day" + day


def load_template() -> list[str]:
    with open("template.py", "r") as f:
        template = f.read().splitlines()
        f.close()
    return template


def change_name(template: list[str], new_file_name: str):
    target_index = template.index('with open("change_name.txt", "r") as f:')
    template[target_index] = f'with open("{new_file_name}.txt", "r") as f:'


def create_new_file(template: list[str], new_file_name: str):
    try:
        with open(f"../{url_year}/{new_file_name}.py", "x") as f:
            for line in template:
                f.write(line + "\n")
            f.close()
        print(f"Success: {new_file_name}.py created.")
    except FileExistsError:
        print(f"Error: {new_file_name}.py already exists.")


def main():
    day = input("Day: ")
    new_file_name = generate_new_file_name(day)
    fetch_input(day, new_file_name)
    template = load_template()
    change_name(template, new_file_name)
    create_new_file(template, new_file_name)


if __name__ == "__main__":
    main()
