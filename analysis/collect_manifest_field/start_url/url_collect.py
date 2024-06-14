from collections import defaultdict

inputfolder = "../../manifest_separate/"
inputfile = "start_url.txt"
line_count = 0
one_name_with_multiple_urls = "one_name_with_multiple_urls.txt"
https_url = "https_url.txt"
data = "data.txt"
track = "track.txt"
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
                    arr = line.split(",")
                    val = "".join(arr[1:])
                    if "https" in val:
                        url1 = arr[0]
                        if url1 not in val:
                            out_empty.write(line)
                    # check if number is in the val
                    tmp = val.split("/")
                    if (
                        any(char.isdigit() for char in tmp[-1])
                        and "=1" not in tmp[-1]
                        and "=a2hs" not in tmp[-1]
                        and "%" not in tmp[-1]
                        and "?" in tmp[-1]
                    ):
                        track.write(line)
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
