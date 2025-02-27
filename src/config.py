from typing import Dict
import argparse
import csv

REQUIRED_KEYS = {"DISCORD_KEY", "OPEN_WEATHER_KEY"}


def get_api_keys(file_path="keys.csv") -> Dict[str, str]:
    parser = argparse.ArgumentParser(description="Pass API keys")
    parser.add_argument("-d", help="Discord key", type=str)
    parser.add_argument("-w", help="OpenWeather key", type=str)
    args = parser.parse_args()

    if args.d and args.w:
        return {"DISCORD_KEY": args.d, "OPEN_WEATHER_KEY": args.w}

    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            keys = {row["KEY"]: row["VALUE"] for row in reader}

            missing_keys = REQUIRED_KEYS - keys.keys()
            if missing_keys:
                raise ValueError(f"keys.csv is missing required keys: {', '.join(missing_keys)}")

            return keys

    except FileNotFoundError as e:
        raise FileNotFoundError("keys.csv was not found and no cli arguments was provided") from e
