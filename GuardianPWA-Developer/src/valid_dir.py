import json


def check_dir(dir):
    valid_set = {"ltr", "rtl", "auto"}
    if dir not in valid_set:
        return False
    return True


def main(filename):
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "dir":
                    if not check_dir(value):
                        print(
                            f"Invalid dir value: {value} for {filename}, change to auto instead"
                        )
