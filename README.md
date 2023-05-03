# GeccoBot

this Discord bot is for anyone using stable diffusion image generation. 

It can pull images from a specified directory, rename them via index (0.png, 1.png, 2.png) and post them in the discord chat.

The commands are:

!hi (Hello!) : Ping command to test if the bot is working

!commandlist : prints a list of available commands

!pull : command to iterate over files in source directory (defined in a variable in the code) and move them to bot directory "images" folder

!prepare : command to rename all images in the "images" folder in the bot directory by index in preparation of !imagedump

!imagedump : command to post all images in the "images" folder in the bot directory, then rename them with timestamp and move to the "uploaded" folder

!imageget : command to post a single image from the "images" folder in the bot directory, syntax: !imageget <index> 

!go : command to execute all three main functions in one go, pull, prepare and imagedump


These functions allow access to the generated files on the go by pulling them into the chat and then to your mobile device. 


If you find yourself using this bot regularly, consider buying me a coffee - or a golden house, or gecco food, idc. 

enjoy
