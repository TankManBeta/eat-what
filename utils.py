# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/1 22:10
"""
import json


def load_json_file(filepath):
    with open(filepath, encoding='utf8') as f:
        data = json.load(f)
        return data


def save_json_file(filepath, my_dict):
    json_str = json.dumps(my_dict, indent=4)
    with open(filepath, 'w', encoding="utf8") as f:
        f.write(json_str)
