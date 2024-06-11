import json


def check_icons(icons, origin):
    for icon in icons:
        if "src" in icon:
            if icon["src"].startswith("https://") and origin not in icon["src"]:
                return False
    return True


def main(filename, origin):
    origin = origin.replace(".json", "").replace("_", ".")
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "icons":
                    if not check_icons(value, origin):
                        print(f"Invalid icons value: {value} for {filename}")
