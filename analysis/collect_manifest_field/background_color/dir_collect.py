from collections import defaultdict

inputfolder = "../../manifest_separate/"
outputfolder = "invalid.txt"
inputfile = "background_color.txt"
cnt = 0
with open(inputfolder + inputfile, "r") as file:
    with open(outputfolder, "w") as out:
        for line in file:
            cnt += 1
            arr = line.strip().split(",")
            key = arr[0]
            val = "".join(arr[1:])
            val = val.replace(" ", "").strip()
            # check if val is color #RRGGBB
            if len(val) != 7 or (len(val) > 0 and val[0] != "#"):
                out.write(f"{key}, {val}\n")
print(cnt)
