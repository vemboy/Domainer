import discord
from discord.ext import commands
import asyncio
import time
import aiohttp
import requests
import urllib.request
import os, requests, sys, json
import random

bot = commands.Bot(command_prefix = "=")

bot.remove_command('help')

print (discord.__version__)

input_var = ""
variable_dic = {'title_position' : "",'font_size' : "",'font_family' : ""}



@bot.command(pass_context=True)
async def add_homepage(ctx):

    def pred(m):
        return m.author == ctx.author and m.channel == ctx.channel

    async def question_ask(question, var):
        await ctx.send(question)
        input_var = await bot.wait_for('message', check=pred)
        variable_dic[var] = input_var.content

    await question_ask("What position would you want title to be in?",'title_position')
    await question_ask("Font size of title?",'font_size')
    await question_ask("Font family of title?",'font_family')

    """await ctx.send("Font size of title?")
    font_size_input = await bot.wait_for('message', check=pred)
    font_size = font_size_input.content"""

    await ctx.send(variable_dic['title_position'])







bot.run("NTE4MDY0NzQ5MzM4OTUxNzIx.DuLVFA.2h8dj1VMsGCLuFCHJSMTfNZeO4Q")
