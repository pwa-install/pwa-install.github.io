import json
import os
import random
import string
import subprocess
import time

# Configuration
fields = {
    "name": ["TestName1", "TestName2", "TestName3", "Starbucks"],
    "short_name": ["Short1", "Short2", "Short3"],
    "scope": ["/fuzzy1/", "/no/", "/plus/"],
    "start_url": ["/start1/", "/start2/", "/start3/"],
    "background_color": ["#000000", "#111111", "#222222"],
    "dir": ["ltr", "rtl"],
    "id": ["ID1", "ID2", "ID3"],
    "theme_color": ["#ffffff", "#eeeeee", "#dddddd"],
    "display": ["standalone", "fullscreen", "minimal-ui"],
}

random_string_length = 10  # Length of random strings
num_random_tests = 10  # Number of random tests
sleep_duration = 600  # Sleep duration in seconds


# Generate a random string of given length
def generate_random_string(length=random_string_length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# Generate the manifest file
def generate_manifest(**kwargs):
    manifest = {
        "name": kwargs.get("name", "DefaultName"),
        "short_name": kwargs.get("short_name", "DefaultShortName"),
        "scope": kwargs.get("scope", "/fuzzy/"),
        "start_url": kwargs.get("start_url", "/fuzzy/"),
        "background_color": kwargs.get("background_color", "#000000"),
        "dir": kwargs.get("dir", "DefaultDir"),
        "id": kwargs.get("id", "DefaultID"),
        "theme_color": kwargs.get("theme_color", "#ffffff"),
        "display": kwargs.get("display", "standalone"),
        "icons": [
            {
                "src": "/fuzzy/images/pwa-icon-512.png",
                "type": "image/png",
                "sizes": "512x512",
            }
        ],
    }
    with open("manifest.json", "w") as file:
        json.dump(manifest, file, indent=2)
    print(f"Generated manifest.json with {kwargs}")


# Submit changes to GitHub
def submit2github():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Fuzz test"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to GitHub")
        time.sleep(sleep_duration)  # Sleep for the specified duration
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


# Delete the manifest file
def delete_manifest():
    if os.path.exists("manifest.json"):
        os.remove("manifest.json")
        print("Deleted manifest.json")


# Function to fuzz a specific field with given values
def fuzz_field(field_name, values):
    for value in values:
        kwargs = {field_name: value}
        generate_manifest(**kwargs)
        submit2github()
        delete_manifest()

    for _ in range(num_random_tests):
        random_value = generate_random_string()
        kwargs = {field_name: random_value}
        generate_manifest(**kwargs)
        submit2github()
        delete_manifest()


# Fuzz all fields
def fuzz_all_fields():
    for field_name, values in fields.items():
        fuzz_field(field_name, values)


if __name__ == "__main__":
    fuzz_all_fields()
