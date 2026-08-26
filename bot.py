import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def join(ctx):
    """Make the bot join your current voice channel."""
    if not ctx.author.voice:
        await ctx.send("You need to be in a voice channel first.")
        return

    channel = ctx.author.voice.channel

    if ctx.voice_client:
        await ctx.voice_client.move_to(channel)
    else:
        await channel.connect()

    await ctx.send(f"Joined **{channel.name}** 🔊")


@bot.command()
async def leave(ctx):
    """Make the bot leave the voice channel."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Left the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel.")


TOKEN = os.getenv("MTU0MjE1NzQzNDE5NjQ1OTU2MA.GithmA.GQPW4A_58GS5tj4ZeMNhPtdAgIHcadBjHowj7E")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN environment variable is missing.")

bot.run("MTU0MjE1NzQzNDE5NjQ1OTU2MA.GithmA.GQPW4A_58GS5tj4ZeMNhPtdAgIHcadBjHowj7E")