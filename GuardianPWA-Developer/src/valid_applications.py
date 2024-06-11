import json


def check_applications(applications, origin):
    for application in applications:
        if "platform" in application:
            if application["platform"] not in [
                "chrome_web_store",
                "play",
                "chromeos_play",
                "webapp",
                "windows",
                "f-droid",
                "amazon",
            ]:
                return False
            if ["url"] in application:
                if (
                    "https" in application["url"]
                    and application["platform"] != "webapp"
                ):
                    return False
                if "https" in application["url"]:
                    if origin not in application["url"]:
                        return False
    return True


def main(filename, origin):
    origin = origin.replace(".json", "").replace("_", ".")
    if filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            allowed = False
            for key, value in data.items():
                if key == "prefer_related_application":
                    if value:
                        allowed = True
            if allowed:
                for key, value in data.items():
                    if key == "related_application":
                        if not check_applications(value, origin):
                            print(f"Invalid applications value: {value} for {filename}")
