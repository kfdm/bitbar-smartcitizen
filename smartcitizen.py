#!/usr/local/bin/python3
import configparser
import logging
import os
import pathlib
import sys

import requests

if "BitBar" in os.environ:
    logging.basicConfig(level=logging.WARNING)
    sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf8")
else:
    logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

CONFIG_FILE = pathlib.Path.home() / ".bitbarrc"

config = configparser.ConfigParser()
if CONFIG_FILE.exists():
    with CONFIG_FILE.open() as fp:
        config.read_file(fp)


def main():
    print("SC")
    print("---")
    print("RELOAD | refresh=true")

    for device, url in config.items("smartcitizen"):
        print("---")
        result = requests.get(url)
        result.raise_for_status()
        data = result.json()
        print("{name} - {description} | href=https://smartcitizen.me/kits/{id}".format(**data))
        for sensor in data["data"].get("sensors", []):
            print("{value} {unit} ({description})".format(**sensor))


if __name__ == "__main__":
    main()
