input_file = "different_domains.txt"
output_file = open("complete_different_domains_val.txt", "w")
with open(input_file, "r") as file:
    for line in file:
        arr = line.split(",")
        key = arr[0].strip().replace("/", "")
        key_arr = key.split(".")
        found = False
        for i in key_arr[:-1]:
            if i in arr[1]:
                found = True
                break
        if not found:
            output_file.write(line)
