from collections import defaultdict

inputfolder = "../../manifest_separate/"
inputfile = "shortcuts.txt"
line_count = 0
one_name_with_multiple_urls = "one_name_with_multiple_urls.txt"
https_url = "https_url.txt"
data = "data.txt"
track = "parent_orgin.txt"
mp = defaultdict(list)
data = open(data, "w")
with open(inputfolder + inputfile, "r") as file:
    with open(one_name_with_multiple_urls, "w") as out:
        with open(https_url, "w") as out_empty:
            with open(track, "w") as track:
                for line in file:
                    if "," not in line:
                        continue
                    line_count += 1
                    arr = line.split("}]")
                    for i in arr:
                        if "../" in i:
                            track.write(line)
                print(line_count)
