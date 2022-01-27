#!/usr/bin/env python3
from discord.ext import tasks
import discord
# import from moodle_api.py
from moodle_api import login, logout, get_upcoming_tasks_as_text, get_upcoming_tasks, from_dict_to_set


TOKEN = '*** PASTE YOUR DISCORD BOT TOKEN HERE ***'
CHANNEL_ID = 0000000000000000000# dummy, change me !
MOODLE_ID = '*** PASTE YOUR MOODLE ID HERE ***'
MOODLE_PASSWORD = '*** PASTE YOUR MOODLE PASSWORD HERE ***'


client = discord.Client()
ch = client.get_channel(CHANNEL_ID)

@tasks.loop(minutes=180)# 3 hours
async def check_moodle():
    """ Check moodle tasks page """
    login(MOODLE_ID, MOODLE_PASSWORD)
    tasks = get_upcoming_tasks_as_text()
    logout()
    await ch.send(tasks)

@client.event
async def on_ready():
    print("[+] Discord bot started !")
    await ch.send("moodle bot started !")
    check_moodle.start()

client.run(TOKEN)
