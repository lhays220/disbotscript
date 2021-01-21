import discord
import mcpi as minecraft
import subprocess
import os
from subprocess import Popen
import mcstatus
from discord.ext import commands
from pynput.keyboard import Key, Controller
from pynput.mouse import Button




client = commands.Bot(command_prefix = '!')
keyboard = Controller()

@client.event
async def on_ready():
    print('ready')
@client.command()
async def start(ctx):
    subprocess.Popen(['java', '-jar', 'server.jar'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True,
                     cwd='C:\mcserver')

    await ctx.send('starting')
@client.command()
async def stop(ctx):

    keyboard.type('stop')
    keyboard.press(Key.enter)
    await ctx.send('stopping')
async def cmd(ctx):
    await ctx.send('hi')


















client.run('ODAxMTIzMzY5NzA1NjY4NjI4.YAcGRw.5kGyIsX5LyTufz5mCFSqeY56-rs')
