import json


def check_start_url(start_url, origin):
    # check if tehre is no relative path
    if ".." in start_url:
        return False
    if "https" in start_url and origin not in start_url:
        return False
    # check tracking
    if "?id=" in start_url:
        return False
    return True


def main(filename, origin):
    origin = origin.replace(".json", "").replace("_", ".")
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "start_url":
                    if not check_start_url(value, origin):
                        print(f"Invalid start_url value: {value} for {filename}")
