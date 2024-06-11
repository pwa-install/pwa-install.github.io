import json


def check_orientation(orientation):
    valid_set = {
        "any",
        "natural",
        "landscape",
        "portrait",
        "portrait-primary",
        "portrait-secondary",
        "landscape-primary",
        "landscape-secondary",
    }
    if orientation not in valid_set:
        return False
    return True


def main(filename):
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "orientation":
                    if not check_orientation(value):
                        print(
                            f"Invalid orientation value: {value} for {filename}, change to any instead"
                        )
