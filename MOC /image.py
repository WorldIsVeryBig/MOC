# -*- coding: UTF-8 -*-
import posix
import cv2
from PIL import Image, ImageFont, ImageDraw
import pandas as pd

init_root = './data/init_photo/'
base_img = init_root + "base_img.png"
warning_icon = init_root + "warning.png"
trapezoid_frame = init_root + "trapezoid_frame.png"
inside_of_frame = "現場監測畫面"
black_font = (20, 20, 20)
blue_font = (20, 20, 255)
red_font = (255, 20, 20)


class Create_Img():

    def __init__(self, time, interface, tempo_name):
        df = pd.read_csv("./data/no_index_test_LSTM_15_北港朝天宮綜合氣象站(2020).csv")
        self.interface = interface
        self.time = time
        self.country = "雲林縣"  #
        self.target = tempo_name  #
        self.contact_person = "陳泓嶧"
        self.temp = str(df.loc[df['LocalTime'] == time]['Temp']).split("   ")[1].split('\n')[0]
        self.hum = str(df.loc[df['LocalTime'] == time]['Hum']).split("   ")[1].split('\n')[0]  #
        self.wind_speed = str(df.loc[df['LocalTime'] == time]['WindSpeed']).split("   ")[1].split('\n')[0]  #
        self.amc = "43.1"  #
        self.target_img = './data/Photo/' + tempo_name + '.jpg'
        self.output_img = "output.png"
        self.warn_title = "彩繪即將乾縮損毀"
#         self.content = "區域: 左前上"
#         self.warn_area = """毀損區塊座標:
# [ N: 928.5 ~ 3796.1,
#   E: -15454.1 ~ -11165.9,
#   Z: 3315 ~ 4536 ]"""
#         self.content = "區域: 左中上"
#         self.warn_area = """毀損區塊座標:
# [ N: 928.5 ~ 3796.1,
# E: -5363 ~ -8135.7,
# Z: 3315 ~ 4536 ]"""
        self.content = "區域: 左後上"
        self.warn_area = """毀損區塊座標:
[ N: -5363.3 ~ -8135.7,
E: -2593.9 ~ -6979.9,
Z: 3315 ~ 4536 ]"""

    def get_info(self):
        result = {
            "country": self.country,
            "target": self.target,
            "contact_person": self.contact_person,
            "temp": self.temp,
            "hum": self.hum,
            "wind_speed": self.wind_speed,
            "amc": self.amc,
            "target_img": self.target_img,
            "output_img": self.output_img,
            "warn_message": self.warn_title,
            "content": self.content,
            "warn_area": self.warn_area
        }
        return result

    def create_result_img(self):
        # 取得傳入資料
        data = self.get_info()
        img_top = 85
        img_left = 30
        # 讀取底圖
        image = cv2.imread(base_img)
        target = cv2.imread(data['target_img'])
        # 調整target的形狀
        target = cv2.resize(target, (810, 330))
        target_l, target_w, target_h = target.shape
        # 設定 target 在原圖上的座標
        img_bottom = img_top + target_l
        img_right = img_left + target_w
        # 用 target 覆蓋原圖
        image[img_top:img_bottom, img_left:img_right] = target
        # 儲存圖片
        cv2.imwrite(data['output_img'], image)

    def write_text_on_image(self, content, position, font_size, font_color):
        # 取得傳入資料
        data = self.get_info()
        # 開啟目標圖片
        image = Image.open(data['output_img']).convert("RGBA")
        # 新增 RGB 格式底圖
        text_conf = Image.new('RGBA', image.size)
        # 設定字型、文字大小與文字透明度
        font = ImageFont.truetype("STHeiti Light.ttc", font_size)
        # 用底圖新增 ImageDraw 物件
        draw = ImageDraw.Draw(text_conf)
        # 輸入文字
        draw.text(position, content, font=font, fill=font_color)
        # 結合底圖與文字
        text_combined = Image.alpha_composite(image, text_conf)
        # 儲存圖片結果
        text_combined.save(data['output_img'])

    def draw_watermark_on_the_base_img(img_name, logo_name, position, logo_size):
        # 讀取原圖與 Logo
        logo = cv2.imread(logo_name)
        image = cv2.imread(img_name)
        # 設定 Logo 大小
        logo_size_map = {
            "frame": (210, 30),
            "W3": (50, 50),
            "W2": (35, 35),
            "W1": (20, 20)}
        logo_size = logo_size_map.get(logo_size)
        # 調整 Logo 的形狀
        logo = cv2.resize(logo, logo_size)
        # 將 Logo 形狀存成三個變數
        h_logo, w_logo, d_logo = logo.shape
        # 設定 Logo 對應位置
        position_map = {
            "frame": (85, 305),
            "L1": (190, 100),
            "L2": (250, 100),
            "L3": (310, 100),
            "M1": (155, 395),
            "M2": (265, 395),
            "M3": (350, 395),
            "R1": (190, 700),
            "R2": (250, 700),
            "R3": (310, 700),
            "L4": (210, 180),
            "L5": (260, 180),
            "L6": (310, 180),
            "M4": (195, 400),
            "M5": (275, 400),
            "M6": (335, 400),
            "R4": (220, 620),
            "R5": (270, 620),
            "R6": (320, 625),
            "L7": (240, 240),
            "L8": (280, 240),
            "L9": (320, 240),
            "M7": (220, 410),
            "M8": (275, 410),
            "M9": (335, 410),
            "R7": (240, 585),
            "R8": (280, 585),
            "R9": (320, 585)}
        position = position_map.get(position)

        # 設定 Logo 在原圖上的座標
        top_ = position[0]
        left_ = position[1]
        bottom_ = top_ + h_logo
        right_ = left_ + w_logo

        # 劃定原圖與 Logo 相對應的座標
        destination = image[top_:bottom_, left_:right_]

        # 轉成浮水印
        result = cv2.addWeighted(destination, 1, logo, 1, 0)

        # 用 Logo 覆蓋原圖
        image[top_:bottom_, left_:right_] = result

        # 儲存圖片
        cv2.imwrite("output.png", image)

    def draw_result_img(self):
        # 創建底圖
        self.create_result_img()
        # 繪製現場監測畫面
        self.write_text_on_image(inside_of_frame, (340, 87), 23, black_font)
        # 繪製目標名稱
        self.write_text_on_image(self.target, (75, 27), 23, black_font)
        # 繪製縣市名稱
        self.write_text_on_image(self.country, (360, 25), 13, black_font)
        # 繪製聯絡人名稱
        self.write_text_on_image(self.contact_person, (400, 43), 13, black_font)
        # 繪製溫度
        self.write_text_on_image(self.temp, (925, 60), 15, blue_font)
        # 繪製濕度
        self.write_text_on_image(self.hum, (1045, 60), 15, blue_font)
        # 繪製風速
        self.write_text_on_image(self.wind_speed, (925, 100), 15, blue_font)
        # 繪製平衡含水率
        self.write_text_on_image(self.amc, (970, 137), 15, blue_font)
        # 繪製警告標題
        self.write_text_on_image(self.warn_title, (880, 218), 15, red_font)
        # 繪製毀壞警告區域
        self.write_text_on_image(self.warn_area, (880, 240), 15, red_font)
        # 繪製內容
        self.write_text_on_image(self.content, (880, 320), 16, red_font)
