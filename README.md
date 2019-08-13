# Minecraft Achievement Merger

*Developed for* [Sky Factory 4](https://www.curseforge.com/minecraft/modpacks/skyfactory-4), *untested with* Prestige *mode*.

## Why

You started playing *Sky Factory 4* locally, then decided to move your world to a dedicated server to play with your friends, and after a few hours you realized that during the migration you or your friends now have 2 different sets of achievements, both incomplete. This tiny tool fixes that issue.

## How

The tiny `merger.py` takes a JSON file (from `./world/advancements`) as the oldest input and complements the achievement data with the other provided, newer file. The result is then created as a third data file that can be used to replace the one in the server (or in a local world).

## Usage

Simply download the script, edit the file names and run it with python 3.