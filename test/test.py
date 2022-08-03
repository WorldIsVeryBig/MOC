# -*- coding: UTF-8 -*-
import cv2
from PIL import Image,ImageFont,ImageDraw


base_img = "base_img.png"
warning_icon = "warning.png"
trapezoid_frame = "trapezoid_frame.png"
inside_of_frame = "現場監測畫面"
black_font = (20, 20, 20)
blue_font = (20, 20, 255)
red_font = (255, 20, 20)

class Create_Img():
    def __init__(self):
        self.country = "雲林縣" #
        self.target = "北港朝天宮" #
        self.contact_person = "陳泓嶧" 
        self.temp = "30.5" #
        self.hum = "42.3" #
        self.wind_speed = "50" #
        self.amc = "43.1" #
        self.target_img = "image.jpg"
        self.output_img = "output.png"
        self.warn_title = "彩繪即將乾縮損毀"
        self.content = "Test"
        self.warn_area = "毀壞區域為：(L3, W3), (L9, W1)"

    def get_info(self):
        result = {
            "country":self.country,
            "target":self.target,
            "contact_person":self.contact_person,
            "temp":self.temp,
            "hum":self.hum,
            "wind_speed":self.wind_speed,
            "amc":self.amc,
            "target_img":self.target_img,
            "output_img":self.output_img,
            "warn_message":self.warn_title,
            "content":self.content,
            "warn_area":self.warn_area
        }
        return result

    def create_result_img(self):
        data = self.get_info()
        img_top = 85
        img_left = 30
        image = cv2.imread(base_img)
        target = cv2.imread(data['target_img'])
        target = cv2.resize(target, (810,330))
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

    def draw_icon_on_img(self):
        data = self.get_info()
        logo = cv2.imread(warning_icon)
        image = cv2.imread(data['output_img'])
        logo_size_map ={
            "frame":(210, 30),
            "W3":(50, 50),
            "W2":(35, 35),
            "W1":(20, 20)}
        
    def draw_result_img(self):
        self.create_result_img()
        self.write_text_on_image(inside_of_frame, (340,87), 23, black_font)
        self.write_text_on_image(self.target, (75, 17), 23, black_font)
        self.write_text_on_image(self.country, (360, 20), 13, black_font)
        self.write_text_on_image(self.contact_person, (400, 40), 13, black_font)
        self.write_text_on_image(self.temp, (925, 60), 15, blue_font)
        self.write_text_on_image(self.hum, (1045, 60), 15, blue_font)
        self.write_text_on_image(self.wind_speed, (925, 100), 15, blue_font)
        self.write_text_on_image(self.amc, (970, 137), 15, blue_font)
        self.write_text_on_image(self.warn_title, (880, 218), 15, red_font)
        self.write_text_on_image(self.warn_area, (880, 240), 15, red_font)
        self.write_text_on_image(self.content, (880, 260), 13, black_font), 

test = Create_Img()
test.draw_result_img()