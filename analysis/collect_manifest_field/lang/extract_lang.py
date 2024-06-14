def main():
    input_file = "lang_registry.txt"
    output_file = open("lang_val.txt", "w")
    st = set()
    with open(input_file, "r") as file:
        for line in file:
            if "Subtag:" in line:
                st.add(line.split(":")[1].strip())
                output_file.write(line.strip().replace("Subtag: ", "") + "\n")
            if "Tag:" in line:
                st.add(line.split(":")[1].strip())
                output_file.write(line.strip().replace("Tag: ", "") + "\n")
    return st


main()
