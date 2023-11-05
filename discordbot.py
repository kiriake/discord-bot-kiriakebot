from discord.ext import commands
import os
import traceback
import subprocess


bot = commands.Bot(command_prefix='/')
cmd = "aws ssm get-parameter --name discord-bot-kiriakebot --with-decryption --query 'Parameter.Value' --output text"
token = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True).communicate()[0].decode('utf-8').strip()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, 'original', error)
    error_msg = ''.join(traceback.TracebackExcetion.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
