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
variable_dic_hp = {'hp_title_position' : "",'hp_font_size' : "",'hp_font_family' : "", 'hp_background_color' : "", 'hp_font_color' : "", 'hp_margin_left' : "", 'hp_margin_right' : "", 'hp_margin_top' : ""}
variable_dic_ap = {'ap_height' : "", 'ap_title_font-family': "", 'ap_text_font-family': "", 'ap_no_1' : "", 'ap_no_2' : "", 'ap_no_3' : "", 'ap_no_4' : ""}

HTML_1 = """<!DOCTYPE html>

            <html>
            <body>"""

HTML_2 = """
            </body>
            </html>"""

CSS_1 = "<style>"
CSS_2 = "</style>"

@bot.command(pass_context=True)
async def add_homepage(ctx):

    def pred(m):
        return m.author == ctx.author and m.channel == ctx.channel

    async def question_ask_hp(question, var):
        await ctx.send(question)
        input_var = await bot.wait_for('message', check=pred)
        variable_dic_hp[var] = input_var.content

    await question_ask_hp("What position would you want title to be in?",'hp_title_position')
    if(variable_dic_hp[hp_title_position] == "right" or variable_dic_hp[hp_title_position] == "Right"):
        variable_dic_hp[hp_margin_right] = "10%"
        variable_dic_hp[hp_margin_top] = "5%"
    elif(variable_dic_hp[hp_title_position] == "left" or variable_dic_hp[hp_title_position] == "Left"):
        variable_dic_hp[hp_margin_left] = "10%"
        variable_dic_hp[hp_margin_top] = "5%"
    else:
        variable_dic_hp[hp_margin_right] = "0%"
        variable_dic_hp[hp_margin_top] = "0%"

    await question_ask_hp("Font size of title?",'hp_font_size')
    await question_ask_hp("Font family of title?",'hp_font_family')
    await question_ask_hp("Color of title?",'hp_font_color')
    await question_ask_hp("Background color of homepage?",'hp_background_color')





@bot.command(pass_context=True)
async def add_aboutpage(ctx, quantity: int = None):

    if(quantity > 4 or quantity < 0):
        await ctx.send("Please enter a number between 1-4")
        return


    def pred(m):
        return m.author == ctx.author and m.channel == ctx.channel

    async def question_ask_ap(question, var):
        await ctx.send(question)
        input_var = await bot.wait_for('message', check=pred)
        variable_dic_ap[var] = input_var.content

    await question_ask_ap("What should the height be?", "ap_height")
    await question_ask_ap("What should the title font-family be?", "ap_title_font-family")
    await question_ask_ap("What should the text font-family's be?", "ap_text_font-family")
    for x in range(quantity):
        while(quantity > x):
            await question_ask_ap("What should the title name be for about_page_number: " + str(x + 1), "ap_no_" + str(x + 1))
            x = x + 1
        break

    await ctx.send("You're gonna have to edit the text's yourelf :)")









bot.run("NTE4MDY0NzQ5MzM4OTUxNzIx.DuLVFA.2h8dj1VMsGCLuFCHJSMTfNZeO4Q")
