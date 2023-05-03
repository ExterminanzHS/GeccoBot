import json
import os
import nextcord
import time
import shutil

from nextcord.ext import commands
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file, in this case, the bot-token.

bot = commands.Bot(command_prefix="!")

source_dir = "YOUR/FILE/DIRECTORY/TO/PULL/IMAGES/FROM"

# !hi command to ping the bot and receive an answer.
@bot.command(name="hi")
async def send_message(ctx):
    """Send a greeting message"""
    await ctx.send('Hello!')

# !imageget command to post a single image from the "images" folder in the bot directory by index 
@bot.command()
async def imageget(ctx, index: int):
    """Parameters:
       index (int): The index of the image to get
       Syntax:       !imagedump <index>
    """
    filename = f"{index}.png"
    image_path = os.path.join(os.getcwd(), "images", filename)

    try:
        with open(image_path, "rb") as file:
            picture = nextcord.File(file)
            await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send(f"Image with index {index} not found.")

# !imagedump command to post all images in the "images" folder in the bot directory, then rename them with timestamp and move to the "uploaded" folder
@bot.command(name='imagedump')
async def imagedump(ctx):
    images_path = 'images/'
    uploaded_path = 'images/uploaded/'
    timestamp = str(int(time.time()))
    for filename in os.listdir(images_path):
        if filename.endswith('.png'):
            image_path = os.path.join(images_path, filename)
            new_filename = timestamp + '_' + filename
            uploaded_path_with_filename = os.path.join(uploaded_path, new_filename)
            os.rename(image_path, uploaded_path_with_filename)
            with open(uploaded_path_with_filename, 'rb') as f:
                file = nextcord.File(f)
                await ctx.send(file=file)

# !prepare command to rename all images in the "images" folder in the bot directory by index in preparation of !imagedump
@bot.command(name='prepare')
async def prepare_images(ctx):
    count = 0
    for file_name in os.listdir('images'):
        if file_name.endswith('.png'):
            src = os.path.join('images', file_name)
            dst = os.path.join('images', f'{count}.png')
            os.rename(src, dst)
            count += 1
    await ctx.send(f"Renamed {count} images")

# !pull command to iterate over files in source directory (specified above) and move them to images folder
@bot.command()
async def pull(ctx):
    for file_name in os.listdir(source_dir):
        if file_name.endswith(".png"):
            shutil.copy(os.path.join(source_dir, file_name), "images")
    await ctx.send("Images pulled successfully!")

# !commandlist command to print a list of available commands 
@bot.command(name='commandlist')
async def command_list(ctx):
    """Lists all available commands."""
    commands = [f'!{command.name}' for command in bot.commands if command.name != 'help']
    command_list = '\n'.join(commands)
    await ctx.send(f'Here are the available commands:\n{command_list}')

# !go command to execute all three main functions in one go, pull, prepare and imagedump
@bot.command(name='go')
async def go(ctx):
    await ctx.invoke(bot.get_command('pull'))
    await ctx.invoke(bot.get_command('prepare'))
    await ctx.invoke(bot.get_command('imagedump'))
    await ctx.send('Images updated and dumped.')

# 'image' definition
@bot.group()
async def image(ctx):
    """Group of commands related to images"""
    pass

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    
if __name__ == '__main__':
    bot.run(os.getenv("BOT_TOKEN"))