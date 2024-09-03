# GeccoBot

this Discord bot is for anyone using stable diffusion image generation. 

It can pull images from a specified directory, rename them via index (0.png, 1.png, 2.png) and post them in the discord chat.


 https://discord.com/developers/applications portal 

1. To set it up, create a bot on the [Discord Developer Portal](https://discord.com/developers/applications) 
2. Click on "New Application" and give your application a name.
3. In the left sidebar, click on "Bot" and then "Add Bot" on the right.
4. Under the bot's username, you'll see a "Token" section. Click "Copy" to copy your bot token.
5. Paste this token into your `.env` file as described in the installation steps.
6. In the left sidebar, click on "OAuth2" and then "URL Generator".
7. In the "Scopes" section, check "bot".
8. In the "Bot Permissions" section, check "Send Messages" and "Attach Files".
9. Copy the generated URL at the bottom of the page.
10. Open this URL in a new tab and select the server you want to add the bot to.

Remember to keep your bot token secret and never share it publicly.

open the .env file and replace the "your-bot-token-here" string with your actual bot token. 

open the bot.py and specify the directory you want to pull images from by replacing "YOUR/FILE/DIRECTORY/TO/PULL/IMAGES/FROM" with your local output folder from SD (or any other images directory containing .png files)

to run the file, you need the following python packages:

nextcord, install with 'pip install nextcord'
dotenv, install with 'pip install python-dotenv'


save the files, and you're good to go. 


The bot comes with the following commands:


!hi (Hello!) : Ping command to test if the bot is working

!commandlist : prints a list of available commands

!pull : command to iterate over files in source directory (defined in a variable in the code) and move them to bot directory "images" folder

!prepare : command to rename all images in the "images" folder in the bot directory by index in preparation of !imagedump

!imagedump : command to post all images in the "images" folder in the bot directory, then rename them with timestamp and move to the "uploaded" folder

!imageget : command to post a single image from the "images" folder in the bot directory, syntax: !imageget <index> 

!go : command to execute all three main functions in one go, pull, prepare and imagedump


These functions allow access to the generated files on the go by pulling them into the chat and then to your mobile device. 


If you find yourself using this bot regularly, consider buying me a coffee - or a golden house, or gecco food, idc. 
https://www.buymeacoffee.com/cybersnacc

enjoy

- shoutout and credit to Max Teaches Tech for getting me started on Discord bots. If you struggle to activate the bot on your server, be sure to check out his Youtube Channel! https://www.youtube.com/@MaxTeachesTech
