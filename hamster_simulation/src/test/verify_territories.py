#! /usr/bin/python3



import os

import territory.parser


for file in os.listdir("../resources/territories"):
    if file.endswith(".ter"):
        print(f"[TEST] - Try parsing <{file}>")
        try:
            ter = territory.parser.Parser().parse(f"../resources/territories/{file}")
        except Exception as e:
            print(f"[TEST] - FAILED >>> {e}")
            continue
        print("[TEST] - Success")
    else:
        print(f"[WARNING] - Skipping <{file}> for having incorrect file extension")
