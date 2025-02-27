import discord
import OpenWeatherClient


class DiscordClient(discord.Client):
    def __init__(self, intents, open_weather_api_key):
        super().__init__(intents=intents)
        self.__open_weather_client = OpenWeatherClient.OpenWeatherClient(open_weather_api_key)

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower().startswith("weather in "):
            location = message.content[len("weather in "):].strip()

            weather_data = self.__open_weather_client.fetch(location)
            if not weather_data:
                await message.channel.send(f'Failed to fetch weather data for "{location}"')
                return

            embed = discord.Embed(
                title=f"🌤️ Weather in {weather_data['name']}, {weather_data['country']}",
                description=f"*{weather_data['description'].capitalize()}*",
                color=discord.Color.blue()
            )

            embed.add_field(name=f"🌡️ Temperature",
                            value=f"{weather_data['temp']}°C\n"
                                  f"(Feels like {weather_data['feels_like']}°C)",
                            inline=True)

            embed.add_field(name="💧 Humidity",
                            value=f"{weather_data['humidity']}%",
                            inline=True)

            embed.add_field(name="🌬️ Wind",
                            value=f"{weather_data['wind_speed']} m/s\n"
                                  f"Direction: {weather_data['wind_deg']}°",
                            inline=True)

            embed.add_field(name="🕶️ Visibility",
                            value=f"{weather_data['visibility']} meters",
                            inline=True)

            embed.add_field(name="☁️ Clouds",
                            value=f"{weather_data['cloudiness']}% coverage",
                            inline=True)

            embed.add_field(name="📊 Pressure",
                            value=f"{weather_data['pressure']} hPa",
                            inline=True)

            embed.set_footer(text=f"Timezone: UTC{weather_data['timezone'] // 3600:+d}")

            await message.channel.send(embed=embed)
