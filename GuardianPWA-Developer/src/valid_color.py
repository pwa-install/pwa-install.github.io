import json
import re


def check_color(color):
    valid_pattern = r"^#[0-9a-fA-F]{6}$"
    if not re.match(valid_pattern, color):
        return False
    return True


def main(filename):
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "theme_color":
                    if not check_color(value):
                        print(f"Invalid theme_color value: {value} for {filename}")
                if key == "background_color":
                    if not check_color(value):
                        print(f"Invalid background_color value: {value} for {filename}")
