import json

st = set()
with open("lang_val.txt", "r") as file:
    for line in file:
        st.add(line.strip())


def check_lang(dir):
    valid_set = st
    if dir not in valid_set:
        return False
    return True


def main(filename):
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "lang":
                    if not check_lang(value):
                        print(f"Invalid lang value: {value} for {filename}")
