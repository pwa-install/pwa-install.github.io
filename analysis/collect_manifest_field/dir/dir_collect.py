from collections import defaultdict

inputfolder = "../../manifest_separate/"
outputfolder = "invalid.txt"
inputfile = "dir.txt"
mp = defaultdict(int)
with open(inputfolder + inputfile, "r") as file:
    for line in file:
        key, val = line.split(",")
        val = val.strip()
        mp[val] += 1
print(mp)
