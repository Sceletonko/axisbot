# AxisBot

AxisBot is a Discord bot designed for Esport Discord Servers to welcome new members with a custom embed message featuring their profile picture, a personalized text, and a GIF.

## Features

- **Welcome Messages**: Sends a customizable welcome embed when a new member joins the server.
- **User Profile Picture**: Displays the new member's profile picture in the welcome embed.
- **Customizable Text**: Allows for personalized welcome text.
- **GIF Integration**: Includes an animated GIF in the welcome embed.

## Setup

### 1. Create a Discord Bot Application

Follow these steps to create a Discord Bot application and obtain a token:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application".
3. Give your application a name (e.g., "AxisBot") and click "Create".
4. Navigate to the "Bot" tab on the left sidebar.
5. Click "Add Bot" and confirm.
6. Under "Privileged Gateway Intents", enable **PRESENCE INTENT**, **SERVER MEMBERS INTENT**, and **MESSAGE CONTENT INTENT**.
7. Click "Reset Token" to generate a new token (if you haven't already).
8. Copy the token. This will be your `DISCORD_TOKEN`.

### 2. Environment Variables

Create a `.env` file in the root directory of your project and add your Discord bot token:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
WELCOME_CHANNEL_ID=YOUR_WELCOME_CHANNEL_ID
WELCOME_GIF_URL=YOUR_WELCOME_GIF_URL
```

- Replace `YOUR_BOT_TOKEN_HERE` with the token you copied from the Discord Developer Portal.
- Replace `YOUR_WELCOME_CHANNEL_ID` with the ID of the channel where you want welcome messages to be sent. You can get a channel ID by right-clicking on the channel in Discord and selecting "Copy ID" (Developer Mode must be enabled in Discord settings).
- Replace `YOUR_WELCOME_GIF_URL` with the URL of the GIF you want to display in the welcome message.

### 3. Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd AxisBot
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Running the Bot

```bash
python main.py
```

### 5. Inviting the Bot to Your Server

1. Go back to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Navigate to your bot's application.
3. Go to the "OAuth2" tab, then "URL Generator".
4. Under "Scopes", select `bot` and `applications.commands`.
5. Under "Bot Permissions", select the following:
   - `View Channels`
   - `Send Messages`
   - `Embed Links`
   - `Attach Files` (if your GIF is an attachment and not a URL)
   - `Read Message History`
6. Copy the generated URL and paste it into your browser.
7. Select your server and authorize the bot.

## Render Deployment (Optional)

This project includes a `render.yaml` file for easy deployment to Render as a Background Worker.

1. Create a new 