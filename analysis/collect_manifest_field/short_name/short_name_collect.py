from collections import defaultdict

inputfolder = "../../manifest_separate/"
inputfile = "short_name.txt"
line_count = 0
one_name_with_multiple_urls = "one_name_with_multiple_urls.txt"
empty_name = "empty_name.txt"
data = "data.txt"
mp = defaultdict(list)
data = open(data, "w")
with open(inputfolder + inputfile, "r") as file:
    with open(one_name_with_multiple_urls, "w") as out:
        with open(empty_name, "w") as out_empty:
            for line in file:
                if "," not in line:
                    continue
                line_count += 1
                arr = line.split(",")
                val = "".join(arr[1:])
                if val == "":
                    out_empty.write(line)
                    continue
                val = val.strip()
                mp[val].append(arr[0])
            cur_max = 0
            mp_sorted = sorted(mp.items(), key=lambda x: len(x[1]), reverse=True)
            for k, v in mp_sorted:
                if len(v) > 1:
                    data.write(f"{k}, {len(v)}\n")
                    out.write(f"{k}, {v}\n")
            print(sum(len(v) for k, v in mp_sorted))
            print(cur_max, line_count)
