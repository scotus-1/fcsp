from glob import glob
from os.path import basename
import toml


mods = [file for file in glob("../mods/*.toml")]

for filepath in mods:
    toml_file = toml.load(filepath)
    filename = basename(filepath).split(".")[0]

    if toml_file['side'] == "both":
        print("This is a both-sided mod: " + toml_file['name'])
    elif toml_file['side'] == "server":
        print("This is a server-sided mod: " + toml_file['name'])