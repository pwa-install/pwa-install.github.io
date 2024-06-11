import json


def check_id(id, origin):
    # check if tehre is no relative path
    if "https" in id and origin not in id:
        return False
    # check tracking
    if "?id=" in id:
        return False
    return True


def main(filename, origin):
    origin = origin.replace(".json", "").replace("_", ".")
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "id":
                    if not check_id(value, origin):
                        print(f"Invalid id value: {value} for {filename}")
