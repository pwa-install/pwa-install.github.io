input_file = "https_files.txt"
output_file = "phishing_urls.txt"
with open(input_file, "r") as file:
    with open(output_file, "w") as out:
        for line in file:
            arr = line.split(", ")
            url = arr[0]
            val = "".join(arr[1:])
            if url not in val:
                out.write(line)
