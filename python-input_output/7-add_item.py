#!/usr/bin/python3
'''comments'''


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list_a = []

for arg in range(1, len(sys.argv)):
    list_a.append(sys.argv[arg])

save_to_json_file(list_a, "add_item.json")
