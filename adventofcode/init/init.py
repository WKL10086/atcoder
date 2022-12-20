import requests
import os
from dotenv.main import load_dotenv

# loads the .env file into the environment
load_dotenv()


def fetch_input(day: str, new_file_name: str):
    url_var = day[1] if day[0] == "0" else day
    url = "https://adventofcode.com/2022/day/{}/input".format(url_var)
    headers = {"cookie": os.getenv("ADVENTOFCODE_USER_COOKIE", "")}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        with open("{}".format("../2022/{}.txt".format(new_file_name)), "x") as f:
            f.write(r.text)
            f.close()
            print("Success: day{}.txt created.".format(new_file_name))
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
    template[target_index] = 'with open("{}", "r") as f:'.format(new_file_name + ".txt")


def create_new_file(template: list[str], new_file_name: str):
    try:
        with open("../2022/{}.py".format(new_file_name), "x") as f:
            for line in template:
                f.write(line + "\n")
            f.close()
        print("Success: {} created.".format(new_file_name + ".py"))
    except FileExistsError:
        print("Error: {} already exists.".format(new_file_name + ".py"))


def main():
    day = input("Day: ")
    new_file_name = generate_new_file_name(day)
    fetch_input(day, new_file_name)
    template = load_template()
    change_name(template, new_file_name)
    create_new_file(template, new_file_name)


if __name__ == "__main__":
    main()
