input_file = "data.txt"
output_file = "short_name_val.txt"

with open(input_file, "r") as file:
    with open(output_file, "w") as out:
        for line in file:
            arr = line.split(", ")
            name = arr[0]
            out.write(name + "\n")
