from pypresence import Presence
import time
import json


with open("config.json") as f:
    config = json.load(f)
    
Id = config.get("client_id", None)

if Id == "None":
    clientId = input("> Enter ID of your App:")
    with open("config.json", "w") as f:
        config["client_id"] = clientId
        json.dump(config, f, indent=2)
else:
    clientId = config.get("client_id", None)
    print("[+] Id from last run loaded!")

RPC = Presence(clientId)

RPC.connect()

state = config.get("state", None)
if state == "None":
    state = input("> Enter message to be displayed:")
    with open("config.json", "w") as f:
        config["state"] = state
        json.dump(config, f, indent=2)
else:
    state = config.get("state", None)
    print("[+] Message loaded from last run!")

icon = config.get("icon", None)
if icon == "None":
    icon = input("> Enter image (icon) to be displayed:")
    with open("config.json", "w") as f:
        config["icon"] = icon
        json.dump(config, f, indent=2)
else:
    icon = config.get("icon", None)
    print("[+] Icon loaded from last run!")

button_lbl = config.get("button_lbl", None)
if button_lbl == "None":
    button_lbl = input("> Enter button text to be displayed:")
    with open("config.json", "w") as f:
        config["button_lbl"] = button_lbl
        json.dump(config, f, indent=2)
else:
    button_lbl = config.get("button_lbl", None)
    print("[+] Button text loaded from last run!")

button_url = config.get("button_url", None)
if button_url == "None":
    button_url = input("> Enter button URL to be used:")
    with open("config.json", "w") as f:
        config["button_url"] = button_url
        json.dump(config, f, indent=2)
else:
    button_url = config.get("button_url", None)
    print("[+] Button URL loaded from last run!")

RPC.update(
    state = state,
    large_image = icon,
    buttons=[{"label": button_lbl, "url": button_url}]
)
print("[+] RPC updated")

while True:
    time.sleep(60)
    