Discord Weather Bot
===================

A lightweight Discord bot that fetches and displays current weather information using the OpenWeatherMap API. The bot
listens for messages in a Discord channel and responds with an embedded message containing detailed weather data when
prompted.

<div align="center">
  <img src="./img/img1.png" width="400">
</div>

* * * * *

Table of Contents
-----------------

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

* * * * *

Overview
--------

This project is a simple yet effective Discord bot that provides real-time weather information. By integrating with the
OpenWeatherMap API, the bot retrieves data such as temperature, humidity, wind conditions, and more, and then formats
the data into a rich embed message for a better user experience on Discord.

* * * * *

Features
--------

- **Discord Integration:** Connects to Discord via the Discord API.
- **Weather Data Retrieval:** Uses the OpenWeatherMap API to fetch up-to-date weather information.
- **Interactive Messaging:** Listens for commands starting with `weather in` to trigger weather lookups.
- **Embedded Responses:** Displays weather details in a visually appealing embedded message.
- **Flexible Configuration:** Supports configuration through CLI arguments or a CSV file (`keys.csv`).

* * * * *

Project Structure
-----------------

- **main.py:**
  Initializes the bot by loading API keys from config.py, setting up the required Discord intents, and starting the bot
  with the provided Discord token.

- **discord.py:**
  Defines the DiscordClient class, which extends discord.Client. It listens for messages and, upon detecting a command (
  e.g., "weather in London"), fetches weather data using the OpenWeatherClient.

- **openweather.py:**
  Implements the OpenWeatherClient class that sends HTTP requests to the OpenWeatherMap API. It processes the response
  data into a structured format suitable for the Discord embed.

- **config.py:**
  Manages API key retrieval. Keys can be provided as command-line arguments or through a CSV file (keys.csv). The file
  must contain the required keys: DISCORD_KEY and OPEN_WEATHER_KEY.

* * * * *

Installation
-----------------

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/weather-discord-bot.git
   cd weather-discord-bot
   ```
2. Create and Activate a Virtual Environment (Optional but Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install Required Packages:
   ```bash
   pip install discord requests
   ```

* * * * *

Configuration
-----------------

The bot requires two API keys:

- **Discord Bot Token:** For connecting to Discord.
- **OpenWeatherMap API Key:** For fetching weather data.

Configuration
API Keys

The bot requires two API keys:

- **Discord Bot Token: For connecting to Discord.
- **OpenWeatherMap API Key: For fetching weather data.

You can provide these keys in two ways:

1. Command-Line Arguments:
   Run the bot with the -d and -w flags:
   ```bash
   python main.py -d YOUR_DISCORD_TOKEN -w YOUR_OPENWEATHER_KEY
   ```
2. CSV File (keys.csv):
   Create a keys.csv file in the project root with the following format:
   ```bash
   KEY,VALUE
   DISCORD_KEY,YourDiscordToken
   OPEN_WEATHER_KEY,YourOpenWeatherAPIKey
   ```

   Then simply run:
   ```bash
   python main.py
   ```

If the keys are missing or not provided correctly, the application will raise an appropriate error.

* * * * *

Usage
-----------------

Once the bot is running, invite it to your Discord server. In any text channel where the bot has access, you can type:

```bash
weather in <location>
```

For example:

```bash
weather in New York
```

The bot will respond with an embedded message displaying current weather information for the specified location.

* * * * *

Contributing
-----------------

Please open an issue or submit a pull request for any improvements or bug fixes.

* * * * *

License
-----------------

This project is licensed under the MIT License. See the LICENSE file for details.