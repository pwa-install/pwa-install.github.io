input = "data.txt"
ans = 0
with open(input, "r") as f:
    for line in f:
        arr = line.strip().split(",")

        if len(arr) > 1:
            print(arr[1])
            ans += int(arr[1].strip())
print(ans)
