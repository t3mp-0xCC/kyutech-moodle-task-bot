#!/usr/bin/env python3
import discord
""" import from moodle_api.py """
from moodle_api import login, get_upcoming_tasks_as_text, get_upcoming_tasks, from_dict_to_set

TOKEN = '*** PASTE YOUR DISCORD BOT TOKEN HERE ***'
moodle_id = '*** PASTE YOUR MOODLE ID HERE ***'
moodle_passwd = '*** PASTE YOUR MOODLE PASSWORD HERE ***'

client = discord.Client()
