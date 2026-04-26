# AxisBot

AxisBot is a Discord bot designed for Esport servers, focusing on providing a welcoming experience for new members.

## Features

- **Welcome Message**: Sends a customizable embedded welcome message to new members, featuring their profile picture and a relevant GIF.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/axisbot.git
    cd axisbot
    ```

2.  **Create a `.env` file**: 
    Copy the `.env.example` file and rename it to `.env`. Then, populate it with your bot's token:
    ```
    DISCORD_TOKEN=your_token_here
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the bot**:
    ```bash
    python main.py
    ```

## Environment Variables

-   `DISCORD_TOKEN`: Your Discord bot token. You can get this from the [Discord Developer Portal](https://discord.com/developers/applications).

## Inviting the Bot

To invite AxisBot to your server, you will need the `client_id` of your bot. Go to the [Discord Developer Portal](https://discord.com/developers/applications), select your bot, and navigate to the OAuth2 -> URL Generator section.

Select the following scopes:
- `bot`
- `applications.commands`

And the following bot permissions:
- `Send Messages`
- `Embed Links`

Generate the URL and use it to invite the bot to your server.
