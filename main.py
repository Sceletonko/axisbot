import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
WELCOME_GIF_URL = os.getenv('WELCOME_GIF_URL')

# --- Bot Setup ---

# Define intents
intents = discord.Intents.default()
intents.members = True  # Required for on_member_join
intents.message_content = True # Required for reading message content

# Initialize bot with intents
bot = commands.Bot(command_prefix="/", intents=intents)

# --- Events ---

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name} ({bot.user.id})')
    try:
        # Sync slash commands
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(f"Failed to sync commands: {e}")
    logger.info("AxisBot is ready!")

@bot.event
async def on_member_join(member):
    logger.info(f'{member.name} joined the server.')
    try:
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            embed = discord.Embed(
                title=f"Welcome to the server, {member.name}!",
                description="We're thrilled to have you join our Esport community! Get ready for some epic gaming!",
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            if WELCOME_GIF_URL:
                embed.set_image(url=WELCOME_GIF_URL)
            embed.set_footer(text=f"Member #{len(member.guild.members)}")

            await channel.send(embed=embed)
            logger.info(f'Sent welcome message for {member.name} in channel {WELCOME_CHANNEL_ID}')
        else:
            logger.warning(f'Welcome channel with ID {WELCOME_CHANNEL_ID} not found.')
    except Exception as e:
        logger.error(f'Error sending welcome message for {member.name}: {e}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, that command does not exist.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the necessary permissions to use this command.")
    else:
        logger.error(f"An error occurred: {error}")
        await ctx.send(f"An unexpected error occurred: {error}")

# --- Commands ---

@bot.tree.command(name="ping", description="Responds with Pong!")
async def ping(interaction: discord.Interaction):
    """Responds with Pong!"""
    logger.info(f'Received ping command from {interaction.user.name}')
    await interaction.response.send_message("Pong!")


# --- Error Handling & Graceful Shutdown ---

def run_bot():
    if not DISCORD_TOKEN:
        logger.error("DISCORD_TOKEN environment variable not set. Please set it in your .env file.")
        return
    if not WELCOME_CHANNEL_ID:
        logger.error("WELCOME_CHANNEL_ID environment variable not set. Please set it in your .env file.")
        return
    if not WELCOME_GIF_URL:
        logger.warning("WELCOME_GIF_URL environment variable not set. Welcome message will not include a GIF.")

    try:
        bot.run(DISCORD_TOKEN)
    except discord.LoginFailure:
        logger.error("Login failed. Please check your DISCORD_TOKEN.")
    except Exception as e:
        logger.error(f"Bot encountered a critical error: {e}")

if __name__ == "__main__":
    run_bot()
