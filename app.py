# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/29 17:28
"""
from flask import Flask, render_template, request
from datetime import datetime
import random

# create app
app = Flask(__name__)
# food for lunch
lunch_food_list = ["馄饨", "泡面", "红油面皮", "粥", "汉堡", "炒饭"]
# food for dinner
dinner_food_list = ["炒米粉", "咖喱饭", "馄饨", "麻辣烫", "汉堡", "便当饭", "花椒鱼", "减肥餐", "烧烤", "擂椒饭",
                    "泰熙家", "梅菜扣肉饼"]
# what for lunch
lunch_option = ""
# what for dinner
dinner_option = ""


@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def home_page():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        # get hour to decide lunch or dinner
        now_hour = datetime.now().hour
        # lucky number for shuffle
        random_times = 3
        global lunch_food_list, dinner_food_list, lunch_option, dinner_option
        # recommend lunch
        if now_hour < 14:
            if not lunch_option:
                for i in range(0, random_times):
                    random.shuffle(lunch_food_list)
                lunch_option = lunch_food_list[2]
            if lunch_option == "粥":
                return f"臭宝今天午餐喝{lunch_option}！"
            else:
                return f"臭宝今天午餐吃{lunch_option}！"
        # recommend dinner
        else:
            if not dinner_option:
                for i in range(0, random_times):
                    random.shuffle(dinner_food_list)
                dinner_option = dinner_food_list[2]
            return f"臭宝今天晚餐吃{dinner_option}！"


if __name__ == "__main__":
    app.run(port=5555)
