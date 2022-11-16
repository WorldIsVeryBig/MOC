# -*- coding: UTF-8 -*-
import cv2
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import math


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
        df1 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿壽樑Data.csv")
        df2 = pd.read_csv("./Total_Data/2022 data 北港朝天宮.csv")
        self.interface = interface
        self.time = time
        self.country = "雲林縣"  #
        self.target = tempo_name  #
        self.contact_person = "陳泓嶧"
        self.temp = (str(df1.loc[df1['資料時間'] == time]['溫度(°C)']).split("   ")[1].split('\n')[0].strip())
        self.hum = str(df1.loc[df1['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split('\n')[0]  #
        self.wind_speed = str(df2.loc[df2['LocalTime'] == time]['WindSpeed']).split("   ")[1].split('\n')[0]  #
        if self.temp == 'NaN':
            Pw_Pa = 'Nan'
        else:
            Tk = float(self.temp) + 273.15
            sida = 1 - (Tk / 647.096)
            exp = (math.exp((647.096 * (-7.85951783 * sida + 1.84408259 * sida ** 1.5 - 11.7866497 * sida ** 3 + 22.6807411 * sida ** 3.5 - 
                  15.9618719 * sida ** 4 + 1.80122502 * sida ** 7.5))/Tk))
            Pws_hPa = 220640 * exp
            Pw_Pa = (float(self.hum) / 100) * Pws_hPa * 100
            Ah = str(round(float(2.169 * Pw_Pa / Tk), 2))
        self.amc = Ah  #
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
        font = ImageFont.truetype("./NotoSansCJKtc-hinted/NotoSansCJKtc-DemiLight.otf", font_size, encoding='utf-8')
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
            "L1": (170, 190),
            "L2": (230, 190),
            "L3": (295, 190),
            "L4": (210, 260),
            "L5": (255, 260),
            "L6": (300, 260),
            "L7": (230, 305),
            "L8": (265, 305),
            "L9": (300, 305),
            "M1": (170, 410),
            "M2": (230, 410),
            "M3": (295, 410),
            "M4": (210, 415),
            "M5": (255, 415),
            "M6": (300, 415),
            "M7": (230, 425),
            "M8": (265, 425),
            "M9": (300, 425),
            "R1": (170, 620),
            "R2": (230, 620),
            "R3": (295, 620),
            "R4": (210, 560),
            "R5": (255, 560),
            "R6": (300, 560),
            "R7": (230, 540),
            "R8": (265, 540),
            "R9": (300, 540)}
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
        self.write_text_on_image(self.target, (75, 20), 23, black_font)
        # 繪製縣市名稱
        self.write_text_on_image(self.country, (360, 20), 13, black_font)
        # 繪製聯絡人名稱
        self.write_text_on_image(self.contact_person, (400, 37), 13, black_font)
        # 繪製溫度
        self.write_text_on_image(self.temp, (925, 54), 15, blue_font)
        # 繪製濕度
        self.write_text_on_image(self.hum, (1045, 54), 15, blue_font)
        # 繪製風速
        self.write_text_on_image(self.wind_speed, (925, 93), 15, blue_font)
        # 繪製絕對濕度
        self.write_text_on_image(self.amc, (960, 130), 15, blue_font)
        # 繪製警告標題
        self.write_text_on_image(self.warn_title, (880, 218), 15, red_font)
        # 繪製毀壞警告區域
        # self.write_text_on_image(self.warn_area, (880, 240), 15, red_font)
        # # 繪製內容
        # self.write_text_on_image(self.content, (880, 320), 16, red_font)
