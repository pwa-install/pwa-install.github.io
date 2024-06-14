from collections import defaultdict

inputfolder = "../../manifest_separate/"
outputfolder = "invalid.txt"
inputfile = "display.txt"
mp = defaultdict(int)
correct = ["fullscreen", "standalone", "minimal-ui"]
cnt = 0
error_dict = defaultdict(int)
error_file = open(outputfolder, "w")
with open(inputfolder + inputfile, "r") as file:
    for line in file:
        cnt += 1
        key, val = line.split(",")
        val = val.strip()
        if val not in correct:
            error_file.write(f"{key}, {val}\n")
            error_dict[val] += 1
        mp[val] += 1
# print(mp)
# print(cnt)
print(error_dict)
