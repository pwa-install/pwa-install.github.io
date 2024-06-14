from collections import defaultdict

inputfolder = "../../manifest_separate/"
outputfolder = "invalid_color.txt"
inputfile = "background_color.txt"
color_dict = defaultdict(int)
with open(inputfolder + inputfile, "r") as file:
    with open(outputfolder, "w") as out:
        for line in file:
            arr = line.strip().split(",")
            key = "".join(arr[1:]).replace(" ", "").strip()
            value = color_dict[key] + 1 if key in color_dict else 1
            # check if val is color #RRGGBB
            if len(key) != 7 or (len(key) > 0 and key[0] != "#"):
                out.write(f"{key}, {value}\n")
            else:
                color_dict[key] = value
output_file = "background_color.txt"
# sort color_dict by value
color_dict = dict(sorted(color_dict.items(), key=lambda item: item[1], reverse=True))
with open(output_file, "w") as file:
    for key, val in color_dict.items():
        file.write(f"{key}, {val}\n")
