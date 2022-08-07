# -*- coding: UTF-8 -*-
import cv2
from PIL import Image, ImageFont, ImageDraw
import pandas as pd

base_img = "base_img.png"
warning_icon = "warning.png"
trapezoid_frame = "trapezoid_frame.png"
inside_of_frame = "現場監測畫面"
black_font = (20, 20, 20)
blue_font = (20, 20, 255)
red_font = (255, 20, 20)


class Create_Img():

    def __init__(self, time, interface, tempo_name):
        df = pd.read_csv("./data/no_index_test_LSTM_15_北港朝天宮綜合氣象站(10min).csv")
        self.interface = interface
        self.time = time
        self.country = "雲林縣"  #
        self.target = tempo_name  #
        self.contact_person = "陳泓嶧"
        self.temp = str(df.loc[df['LocalTime'] == time]['Temp']).split("   ")[1].split('\n')[0]
        # self.temp = str(df.loc[df['LocalTime'] == time]['Temp']).split("    ")
        print(self.temp)  #
        self.hum = str(df.loc[df['LocalTime'] == time]['Hum']).split("   ")[1].split('\n')[0]  #
        # self.hum = str(df.loc[df['LocalTime'] == time]['Hum'])
        self.wind_speed = str(df.loc[df['LocalTime'] == time]['WindSpeed']).split("   ")[1].split('\n')[0]  #
        # self.wind_speed = str(df.loc[df['LocalTime'] == time]['WindSpeed'])
        self.amc = "43.1"  #
        self.target_img = tempo_name + '.jpg'
        self.output_img = "output.png"
        self.warn_title = "彩繪即將乾縮損毀"
        self.content = "Test"
        self.warn_area = "毀壞區域為：(L3, W3), (L9, W1)"

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
        data = self.get_info()
        img_top = 85
        img_left = 30
        image = cv2.imread(base_img)
        target = cv2.imread(data['target_img'])
        target = cv2.resize(target, (810, 330))
        target_l, target_w, target_h = target.shape
        img_bottom = img_top + target_l
        img_right = img_left + target_w
        image[img_top:img_bottom, img_left:img_right] = target
        cv2.imwrite(data['output_img'], image)

    def write_text_on_image(self, content, position, font_size, font_color):
        data = self.get_info()
        image = Image.open(data['output_img']).convert("RGBA")
        text_conf = Image.new('RGBA', image.size)
        font = ImageFont.truetype("STHeiti Light.ttc", font_size)
        draw = ImageDraw.Draw(text_conf)
        draw.text(position, content, font=font, fill=font_color)
        text_combined = Image.alpha_composite(image, text_conf)
        text_combined.save(data['output_img'])

    def draw_watermark_on_the_base_img(img_name, logo_name, position, logo_size):
        # 讀取原圖與 Logo
        logo = cv2.imread(logo_name)
        image = cv2.imread(img_name)
        # 設定 Logo 大小
        if logo_size == "frame":
            logo_size = (210, 30)
        elif logo_size == "W3":
            logo_size = (50, 50)
        elif logo_size == "W2":
            logo_size = (35, 35)
        elif logo_size == "W1":
            logo_size = (20, 20)
        # 調整 Logo 的形狀
        logo = cv2.resize(logo, logo_size)
        # 將 Logo 形狀存成三個變數
        h_logo, w_logo, d_logo = logo.shape
        # 設定 Logo 對應位置
        if position == "frame":
            position = (85, 305)
        else:
            if position[1] == "1":
                p0 = 190
            elif position[1] == "2":
                p0 = 250
            elif position[1] == "4":
                p0 = 210
            elif position[1] == "5":
                p0 = 260
            elif position[1] == "7":
                p0 = 230
            elif position[1] == "8":
                p0 = 270
            elif position[1] in ["3", "6", "9"]:
                p0 = 310
            if position[0] == "L" and int(position[1]) <= 3:
                p1 = 120
            elif position[0] == "L" and int(position[1]) <= 6:
                p1 = 180
            elif position[0] == "L" and int(position[1]) <= 9:
                p1 = 240
            elif position[0] == "M":
                p1 = 400
            elif position[0] == "R" and int(position[1]) <= 3:
                p1 = 680
            elif position[0] == "R" and int(position[1]) <= 6:
                p1 = 620
            elif position[0] == "R" and int(position[1]) <= 9:
                p1 = 560
            position = (p0, p1)
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
        self.create_result_img()
        self.write_text_on_image(inside_of_frame, (340, 87), 23, black_font)
        self.write_text_on_image(self.target, (75, 27), 23, black_font)
        self.write_text_on_image(self.country, (360, 25), 13, black_font)
        self.write_text_on_image(self.contact_person, (400, 43), 13, black_font)     
        print(self.temp)
        self.write_text_on_image(self.temp, (925, 60), 15, blue_font)
        print(self.hum)
        self.write_text_on_image(self.hum, (1045, 60), 15, blue_font)
        print(self.wind_speed)
        self.write_text_on_image(self.wind_speed, (925, 100), 15, blue_font)
        self.write_text_on_image(self.amc, (970, 137), 15, blue_font)
        self.write_text_on_image(self.warn_title, (880, 218), 15, red_font)
        self.write_text_on_image(self.warn_area, (880, 240), 15, red_font)
        self.write_text_on_image(self.content, (880, 260), 13, black_font)

# test = Create_Img()
# test.draw_result_img()
