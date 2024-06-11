import json


def check_shortcuts(shortcuts, origin):
    for shortcut in shortcuts:
        if "url" in shortcut:
            if ".." in shortcut["url"]:
                return False
            if "https" in shortcut["url"]:
                if origin not in shortcut["url"]:
                    return False
    return True


def main(filename, origin):
    origin = origin.replace(".json", "").replace("_", ".")
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "shortcuts":
                    if not check_shortcuts(value, origin):
                        print(f"Invalid shortcuts value: {value} for {filename}")
