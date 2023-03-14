# DiscordRichPresence

<p align="center">
    <span style="color: #fff; font-weight: bold;">Discord RPC</span>
<span style="color: #fff; font-weight: bold;">v1.0.0</span>
</p>

This program allows you to have RP on your discord profile

# Usage

1. Download executable file [here](https://www.mediafire.com/file/4p9jld87qggyqhe/Discord_RPC.zip/file), after that unzip it.

- **IMPORTANT**: `config.json` and `bot.exe` files have to be in same folder or else program will not work!

2. Go to the [discord developer portal](https://discord.com/developers/applications), sign in, and click `New Application`. Choose any name (keep in mind tah name of that aplication is going to display like this `Playing name of your app`), click accept and create. Next go to the `Rich Presence` section and click `Add Image(s)` button (if you want to have any icon on your rich presence), select your image, upload it and rename it however you want but just make sure to remember its name. Next go to `General Information` section, there find `APPLICATION ID` and under it `Copy` button that you want to click.

3. Run the `bot.exe` witch you downloaded earlier in first step. After program asks you to input app ID just paste ID that you copied earlier using `CTRL + V` and press `ENTER`.

4. Next program will ask you to input other data, for example in next input question you want to write message to be displayed on your RP, in this input just write the name of the icon that you uploaded in discord developer portal (if you renamed you image to `icon` just write that), button text is text you want to be displayed on button and button URL is what URL that will button will lead to when clicked for example it can be invite link for an server (when you do so you will see something like image down below).

<p align="center">
  <img alt="issue" src="https://github.com/Josakko/DiscordRichPresence/blob/main/image.png?raw=true" width="500px">
</p>

5. That is it when you open your account you will see that you are playing the name of the application. When you open `bot.exe` all data that you inputted last time will be loaded automatically so you don't have to input anything (on image down below is example how Rich Presence looks on discord profile). 

<p align="left">
  <img alt="issue" src="https://github.com/Josakko/DiscordRichPresence/blob/main/screenshot.png?raw=true" width="250px">
</p>

- **IMPORTANT**: If you close terminal window that opened after you ran `bot.exe` RP will disappear from your account.

6. In case that you want to reset saved data (button URL, button text, icon exedra) just copy text down below and open `config.json` file. There replace existing text whit text you just copied. Now when you run `bot.exe` next time you will have to input data again.
 
```
  {
    "client_id": "None",
    "state": "None",
    "icon": "None",
    "button_lbl": "None",
    "button_url": "None"
  }
```

## Need Help?

If you need help contact me on my [discord server](https://discord.gg/xgET5epJE6).

## Contributors

Big thanks to all of the amazing people (only me) who have helped by contributing to this project!
