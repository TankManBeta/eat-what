# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/29 17:28
"""
from flask import Flask, render_template, request
from datetime import datetime
import random
from utils import load_json_file, save_json_file

# create app
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def home_page():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        # lucky number for shuffle
        random_times = 3
        # optional list for lunch and dinner
        lunch_food_list = ["馄饨", "泡面", "红油面皮", "粥", "汉堡", "炒饭"]
        dinner_food_list = ["炒米粉", "咖喱饭", "馄饨", "麻辣烫", "汉堡", "便当饭", "花椒鱼", "减肥餐", "烧烤", "擂椒饭",
                            "泰熙家", "梅菜扣肉饼"]

        # load some existing data
        default_dict = load_json_file('./data.json')

        # decide whether to rewrite json file
        # get day
        now_day = datetime.now().day
        dict_day = default_dict["day"]
        # initiate every day at first time
        if now_day != dict_day:
            # generate lunch option and dinner option randomly
            for i in range(0, random_times):
                random.shuffle(lunch_food_list)
                random.shuffle(dinner_food_list)
            lunch_option = lunch_food_list[2]
            dinner_option = dinner_food_list[2]
            # construct new content for data.json
            new_dict = {
                "day": now_day,
                "lunch_option": lunch_option,
                "dinner_option": dinner_option
            }
            # save new dict to json file
            save_json_file('./data.json', new_dict)

        # not first time
        else:
            lunch_option = default_dict["lunch_option"]
            dinner_option = default_dict["dinner_option"]

        # get hour
        now_hour = datetime.now().hour
        # recommend lunch
        if now_hour < 14:
            if lunch_option == "粥":
                return f"臭宝今天午餐喝{lunch_option}！"
            else:
                return f"臭宝今天午餐吃{lunch_option}！"
        # recommend dinner
        else:
            return f"臭宝今天晚餐吃{dinner_option}！"


if __name__ == "__main__":
    app.run(port=5555)
