import DiscordClient
from config import get_api_keys


def main():
    try:
        keys = get_api_keys()
    except Exception as e:
        print(e)
    else:
        intents = DiscordClient.discord.Intents.default()
        intents.message_content = True

        discord_client = DiscordClient.DiscordClient(
            intents=intents,
            open_weather_api_key=keys["OPEN_WEATHER_KEY"]
        )
        discord_client.run(keys["DISCORD_KEY"])


if __name__ == "__main__":
    main()
