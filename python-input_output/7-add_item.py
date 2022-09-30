#!/usr/bin/python3
'''adds all argument'''


import json
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
lists = []

try:
    lists = load(filename)
except:
    pass
for i in range(1, len(sys.argv)):
    lists.append(sys.argv[i])
save(lists, filename)
