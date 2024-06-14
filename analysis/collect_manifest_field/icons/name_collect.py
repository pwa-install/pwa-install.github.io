from collections import defaultdict

inputfolder = "../../manifest_separate/"
inputfile = "icons.txt"
line_count = 0
https_files = "https_files.txt"
empty_name = "empty_name.txt"
with open(inputfolder + inputfile, "r") as file:
    with open(https_files, "w") as out:
        with open(empty_name, "w") as out_empty:
            for line in file:
                line_count += 1
                if "," not in line:
                    continue

                arr = line.split(",")
                key = arr[0]
                val = "".join(arr[1:])
                if val == "":
                    out_empty.write(line)
                    continue
                if "https" in val:
                    url1 = arr[0]
                    out.write(f"{url1}, {val}")
print(line_count)
