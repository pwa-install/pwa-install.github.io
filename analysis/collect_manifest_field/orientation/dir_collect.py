from collections import defaultdict

inputfolder = "../../manifest_separate/"
outputfolder = "invalid.txt"
inputfile = "orientation.txt"
output = "output.txt"
output = open(output, "w")
mp = defaultdict(int)
st = set(
    [
        "any",
        "natural",
        "landscape",
        "portrait",
        "portrait-primary",
        "portrait-secondary",
        "landscape-primary",
        "landscape-secondary",
    ]
)
cnt = 0
with open(inputfolder + inputfile, "r") as file:
    for line in file:
        cnt += 1
        key, val = line.split(",")
        val = val.strip()
        if val not in st:
            output.write(line)
        mp[val] += 1
print(mp)
print(cnt)
