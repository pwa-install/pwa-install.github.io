import json


def check_display(display):
    valid_set = {"fullscreen", "standalone", "minimal-ui", "browser"}
    if display not in valid_set:
        return False
    return True


def main(filename):
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "display":
                    if not check_display(value):
                        print(
                            f"Invalid display value: {value} for {filename}, change to minimal-ui instead"
                        )
