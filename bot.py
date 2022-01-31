#!/usr/bin/env python3
# -*- coding:utf-8 -*
import os
import datetime
import time
import sqlite3
import discord
from discord.ext import tasks
from discord.ext import commands
from moodle_api import login, logout, get_upcoming_tasks_as_text, get_upcoming_tasks, from_dict_to_set
from db import db_init
from scheduler import read_schedule, check_schedule, add_schedule, remove_schedule


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
    db_init()
    check_every_ten_min.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command()
async def help(ctx):
    print("[+] help command called")
    await ctx.send("** Kyutech moodle bot **\n`list` :  show moodle check schedule list\n`add` :  add time to the check schedule list\ne.g.  add 8:00\n`remove` : remove time from the schedule list\n`fetch` : fetch task list from moodle")


@bot.command()
async def list(ctx):
    print("[+] list command called")
    schedules = read_schedule('./schedule.txt')
    if schedules is None:
        await ctx.send("There is no schedules")
        return

    message = '\n'.join(schedules)
    await ctx.send("** Notice Schedule List **")
    await ctx.send(message)


@bot.command()
async def add(ctx, arg):
    print("[+] add command called")
    if add_schedule('./schedule.txt', arg):
        await ctx.send("Add {} to the schedule list".format(arg))
        await list(ctx)
    else:
        await ctx.send("{} is invalid value !".format(arg))


@bot.command()
async def remove(ctx, arg):
    print("[+] remove command called")
    if remove_schedule('./schedule.txt', arg):
        await ctx.send("Remove {} from the schedule list".format(arg))
        await list(ctx)
    else:
        await ctx.send("{} is invalid value !".format(arg))


@bot.command()
async def fetch(ctx):
    print("[+] fetch command called")
    await ctx.send("fetching from moodle...")
    await check_moodle()



@bot.command()
async def test(ctx):
    print("[+] test command called")
    await ctx.send("Knock knock!\nWho's there?\nHawaii.\nHawaii? who?\nI just said, how are you?\n")


@bot.command()
async def secret(ctx):
    await ctx.send("Wow, did you read the source code?(or guessing?)\nIf you have a great idea, please contribute this bot.\n")


@tasks.loop(minutes=10)
async def check_every_ten_min():
    if check_schedule('./schedule.txt'):
        await check_moodle()
    else:
        return
    

async def check_moodle():
    """ Check moodle tasks page and send it"""
    login(MOODLE_ID, MOODLE_PASSWORD)
    tasks = get_upcoming_tasks_as_text()
    logout()
    ch = bot.get_channel(CHANNEL_ID)
    await ch.send(tasks)


bot.run(TOKEN)
