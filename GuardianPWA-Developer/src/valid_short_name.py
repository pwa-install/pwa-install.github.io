import json

st = set()
with open("short_name_val.txt", "r") as file:
    for line in file:
        st.add(line.strip())


def check_short_name(dir):
    valid_set = st
    if dir not in valid_set:
        return False
    return True


def main(filename):
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                if key == "short_name":
                    if not check_short_name(value):
                        print(
                            f"Invalid short_name value: {value} \n for {filename}\n, someone is using this short_name already, please change to another name"
                        )
