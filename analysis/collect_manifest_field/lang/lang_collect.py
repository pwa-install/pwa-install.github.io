import extract_lang
from collections import defaultdict

inputfolder = "../../manifest_separate/"
st = extract_lang.main()
print(len(st))
inputfile = "lang.txt"
outputfile = "invalid_lang.txt"
mp = defaultdict(int)
invalid = 0
valid = 0
cnt = 0
with open(inputfolder + inputfile, "r") as file:
    with open(outputfile, "w") as out:
        for line in file:
            cnt += 1
            if "," not in line:
                continue
            arr = line.split(",")
            val = "".join(arr[1:])
            val = val.strip()
            mp[val] += 1
            if val not in st:
                invalid += 1
                out.write(line)
            if val in st:
                valid += 1
print(invalid, valid, cnt)
