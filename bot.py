#!/usr/bin/env python3
from discord.ext import tasks
import discord
# import from moodle_api.py
from moodle_api import login, get_upcoming_tasks_as_text, get_upcoming_tasks, from_dict_to_set


TOKEN = '*** PASTE YOUR DISCORD BOT TOKEN HERE ***'
CHANNEL_ID = '*** PASTE CHANNEL_ID ***'
MOODLE_ID = '*** PASTE YOUR MOODLE ID HERE ***'
MOODLE_PASSWORD = '*** PASTE YOUR MOODLE PASSWORD HERE ***'


client = discord.Client()
channel_sent = None

@tasks.loop(minutes=180)
async def check_moodle():
    """ Check moodle tasks page """
    login(MOODLE_ID, MOODLE_PASSWORD)
    tasks = get_upcoming_tasks()
    await channel_sent.send(tasks)

@client.event
async def on_ready():
    global channel_sent
    channel_sent = client.get_channel(CHANNEL_ID)
    check_moodle.start()

client.run(TOKEN)
