#!/usr/bin/env python3
import discord
from discord.ext import tasks
from discord.ext import commands
# import from moodle_api.py
from moodle_api import login, logout, get_upcoming_tasks_as_text, get_upcoming_tasks, from_dict_to_set


TOKEN = '*** PASTE YOUR DISCORD BOT TOKEN HERE ***'
CHANNEL_ID = 0000000000000000000# DUMMY, CHANGE ME !
MOODLE_ID = '*** PASTE YOUR MOODLE ID HERE ***'
MOODLE_PASSWORD = '*** PASTE YOUR MOODLE PASSWORD HERE ***'


bot = commands.Bot(command_prefix='$')
bot.remove_command('help')


@bot.event
async def on_ready():
    ch = bot.get_channel(CHANNEL_ID)
    print("[+] Discord bot started !")
    await ch.send("moodle bot started !")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command()
async def help(ctx):
    print("[+] help command called")
    await ctx.send("** Kyutech moodle bot **\n`list` : show notice schedule\n`add` : add notice schedule\nexp.   add 8:00\n`delete` : delete notice schedule\n")


@bot.command()
async def test(ctx):
    print("[+] test command called")
    await ctx.send("Knock knock!\nWho's there?\nHawaii.\nHawaii? who?\nI just said, how are you?\n")


async def check_moodle():
    """ Check moodle tasks page """
    login(MOODLE_ID, MOODLE_PASSWORD)
    tasks = get_upcoming_tasks_as_text()
    logout()
    ch = bot.get_channel(CHANNEL_ID)
    await ch.send(tasks)


bot.run(TOKEN)
