#!/usr/bin/python3
"""
a script that adds all arguments to a Python list
and then save them to a file
"""
import json
import os.pathx


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
js_list = []

if os.path.exists(filename):
    js_list = load_from_json_file(filename)

save_to_json_file("add_item.json",js_list)
