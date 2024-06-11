import json


def check_scope(scope, origin):
    # check if tehre is no relative path
    if ".." in scope:
        return False
    if "https" in scope and origin not in scope:
        return False
    return True


def main(filename, origin):
    origin = origin.replace(".json", "").replace("_", ".")
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "scope":
                    if not check_scope(value, origin):
                        print(f"Invalid scope value: {value} for {filename}")
