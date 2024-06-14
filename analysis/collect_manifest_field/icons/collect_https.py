import re
from collections import defaultdict

input_file = "https_files.txt"
output_file = "https_dict.txt"
dic = defaultdict(int)
dic2 = defaultdict(list)
with open(input_file, "r") as f:
    with open(output_file, "w") as out:
        for line in f:
            # find all urls start with https
            uu = line.split(",")[0]
            urls = line.split(",")[1]
            tmp = re.findall(r"https://[^\s']*", urls)
            for url in tmp:
                dic[url] += 1
                dic2[url].append(uu)
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        for key, val in dic.items():
            out.write(f"{key}, {val}\n")
dic2 = dict(sorted(dic2.items(), key=lambda item: len(item[1]), reverse=True))
output_file2 = "https_dict2.txt"
file2 = open("output_file2.txt", "w")
for key, val in dic2.items():
    file2.write(f"{key}, ")
    for v in val:
        file2.write(f"{v}, ")
    file2.write("\n")
