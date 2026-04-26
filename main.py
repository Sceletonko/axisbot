import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s: %(message)s')
logger = logging.getLogger('discord')

# Load environment variables from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Define Discord Intents
intents = discord.Intents.default()
intents.members = True  # Required to receive member join events
intents.message_content = True # Required for slash commands to interact with messages

# Initialize the bot
# Set `debug_guilds` to a list of guild IDs for faster command syncing during development.
# For production, remove `debug_guilds` to sync globally (takes up to an hour).
bot = commands.Bot(command_prefix="!", intents=intents, application_id=YOUR_APPLICATION_ID_HERE)

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user} (ID: {bot.user.id})')
    try:
        # Sync application commands (slash commands)
        # For production, consider syncing globally once and then removing this line for future runs if commands don't change often.
        # This makes sure commands are available on all guilds the bot is on.
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} command(s).")
    except Exception as e:
        logger.error(f"Failed to sync commands: {e}")

# --- Welcome Feature ---
# Configure your welcome channel ID and GIF URL here
WELCOME_CHANNEL_ID = YOUR_WELCOME_CHANNEL_ID_HERE # Replace with the actual ID of your welcome channel
WELCOME_GIF_URL = "https://example.com/your_welcome_gif.gif" # Replace with the URL of your desired GIF

@bot.event
async def on_member_join(member):
    if member.guild.id != YOUR_GUILD_ID_HERE: # OPTIONAL: Replace with your guild ID if you want to restrict to a specific guild, otherwise remove this line
        return

    welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if welcome_channel:
        embed = discord.Embed(
            title=f"Welcome to the Server, {member.name}!",
            description=f"We're thrilled to have you here at **{member.guild.name}**! Get ready for some epic gaming moments.\n\nMake sure to check out our rules and introductions channel.",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_image(url=WELCOME_GIF_URL)
        embed.set_footer(text="Enjoy your stay!")

        try:
            await welcome_channel.send(f"Hey {member.mention}!", embed=embed)
            logger.info(f"Sent welcome message to {member.name} in {welcome_channel.name}.")
        except discord.DiscordException as e:
            logger.error(f"Could not send welcome message to {member.name}: {e}")
    else:
        logger.warning(f"Welcome channel with ID {WELCOME_CHANNEL_ID} not found.")

# --- Error Handling ---
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, that command does not exist.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing a required argument. Please check the command usage.\nUsage: `{ctx.command.usage}`")
    else:
        logger.exception(f"Unhandled command error: {error}")
        await ctx.send("An unexpected error occurred.")

# --- Graceful Shutdown ---
async def shutdown(signal, loop):
    logger.info(f"Received exit signal {signal.name}...")
    await bot.close()
    logger.info("Bot gracefully shut down.")
    loop.stop()

async def main():
    # Replace YOUR_APPLICATION_ID_HERE and YOUR_WELCOME_CHANNEL_ID_HERE and YOUR_GUILD_ID_HERE (optional) 
    # with your actual application ID, welcome channel ID and guild ID before running.

    # It's recommended to put YOUR_APPLICATION_ID_HERE and YOUR_WELCOME_CHANNEL_ID_HERE 
    # and YOUR_GUILD_ID_HERE (optional) into environment variables for better security and flexibility.

    if not DISCORD_TOKEN:
        logger.error("DISCORD_TOKEN not found in environment variables. Please set it.")
        return

    # Start the bot
    try:
        await bot.start(DISCORD_TOKEN)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error(f"Bot encountered an error: {e}")

if __name__ == "__main__":
    # To run this, you need to replace YOUR_APPLICATION_ID_HERE, YOUR_WELCOME_CHANNEL_ID_HERE, and optionally YOUR_GUILD_ID_HERE.
    # For the `application_id` in `bot` initialization, you can find it in the Discord Developer Portal under your bot's General Information.
    # For `WELCOME_CHANNEL_ID`, right-click on your desired welcome channel in Discord and select 'Copy ID' (Developer Mode needs to be enabled in Discord settings).
    # For `YOUR_GUILD_ID_HERE`, right-click on your server name in Discord and select 'Copy ID'.
    import asyncio
    asyncio.run(main())
