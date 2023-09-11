import hashlib as hl
import json
from os.path import exists
from os import mkdir
import re

classes = []
classes_index = -1

# Read the names in and separate them into different classes
# Entries are put first name then last name
with open("names.txt", "r") as file:
    for name in file:
        # Determine when a new class starts and adjust existing class list accordingly
        if "#" in (proc := name.strip()):
            classes.append([])
            classes_index += 1

        # Skip over empty lines
        elif proc == "":
            continue

        # Enter processed names into correct class
        classes[classes_index].append(" ".join(proc.split(", ")[::-1]))

# Outputting results
path = ""
for num, entry in enumerate(classes):
    # Create key value pairs with names as key and sha256 encoded values as value
    res = dict(zip(entry[1::], [hl.sha256("paws".join(name.split(" ")).strip().encode()).hexdigest() for name in entry]))

    # Check if the 'outputs' directory exists
    if not exists("outputs"):
        mkdir("outputs")

    # Finally write to separate files for organization
    with open(f"outputs/validation_{entry[0][2::]}.json", "w") as out:
        json.dump(res, out, indent=4)

