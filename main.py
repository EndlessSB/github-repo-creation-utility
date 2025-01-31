import time
import os
from arg_handler import ArgumentHandler

# define the argument handeler
handler = ArgumentHandler()

print("Welcome to the Github Repo Creation Utility Created by EndlessSB")

name = input("Enter the Repo Name --> ")
description = input("Leave blank if you dont want a description --> ")
if not description:
    yorn = input("You haven't provided a description are you sure? [y/n] --> ")
    if yorn == "n":
        exit()
visibility = input("public Or private --> ").lower()
readme = input("Add a readme? [y/n] --> ").lower()
clone = input("Clone it? [y/n] --> ").lower()
issues = input("Enable issues? --> ")
template = input("Do you want to base this off a template and if so provide a link if not leave blank --> ")
extra_args = input("Any args you wish to include which are not already include [if none leave blank] --> ")
confirm = input("Are you sure you want to continue this action? [y/n] --> ").lower()


if extra_args:
    handler.add_arg(extra_args)

if confirm == "n":
    print("Okie dokie I have canceled your current action have a nice day :)")
    exit()

if not name:
    print("You need to specify a name")
    exit()
if description:
    handler.add_arg(f"--description \"{description}\"")
if visibility == "public":
    handler.add_arg("--public")
elif visibility == "private":
    handler.add_arg("--private")
else:
    print("Not a valid visibility")
    exit()
if readme == "y":
    handler.add_arg("--add-readme")
if clone == "y":
    handler.add_arg("-c")
if issues == "y":
    handler.add_arg("--enable-issues")
elif issues == "n":
    handler.add_arg("--disable-issues")
if template:
    handler.add_arg(f"--template \"{template}\"")

args_str = ' '.join(handler.return_args())

print(f"gh repo create {name} {args_str}")
os.system(f"gh repo create {name} {args_str}")
