from collections import defaultdict
import json

inputfolder = "../../manifest_separate/"
inputfile = "related_applications.txt"
line_count = 0

mp = defaultdict(list)
mismatch = "mismatch.txt"
with open(inputfolder + inputfile, "r") as file:
    with open(mismatch, "w") as out:
        for line in file:
            if "," not in line:
                continue
            line_count += 1
            arr = line.strip().split(", ")
            domain = arr[0]
            domain_list = domain.split(".")
            for val in arr[1:]:
                if "url" in val and "https" in val:
                    found = False
                    for d in domain_list:
                        if d in val:
                            found = True
                            break
                    if not found:
                        out.write(line)
                        break
                    if found:
                        break

    print(line_count)
