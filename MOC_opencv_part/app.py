# -*- coding: UTF-8 -*-
import cv2
from PIL import Image,ImageFont,ImageDraw


base_img = "base_img.png"
target_img = "image.jpg"
warning_icon = "warning.png"
trapezoid_frame = "trapezoid_frame.png"
output_img = "output.png"

inside_of_frame = "現場監測畫面"
target = "北港朝天宮"
county = "雲林縣"
contact_person = "陳泓嶧"
temperature = "30.5"
humidity = "42.3"
wind_speed = "50"
amc = "43.1"
warn_title = "彩繪即將乾縮損毀"
warn_content = "測試"
warn_area = "毀壞區域為：(L3, W3), (L9, W1)"

def draw_text_on_the_base_img(img_name, put_text, position, font_size, font_color):
    # 在程式內開啟原圖
    image = Image.open(img_name).convert("RGBA")
    # 新增 RGB 格式底圖
    txt = Image.new('RGBA', image.size)
    # 設定字型、文字大小與文字透明度
    font = ImageFont.truetype("STHeiti Light.ttc", font_size)
    # 用底圖新增 ImageDraw 物件
    draw = ImageDraw.Draw(txt)    
    # 輸入文字
    draw.text(position, put_text, font=font, fill=font_color)
    # 結合底圖與文字
    combined = Image.alpha_composite(image, txt)    
    # 儲存圖片結果
    combined.save("output.png")

def covering_target_img_on_the_base_img(img_name, target_name, position, target_size):
    # 讀取原圖與 target
    target = cv2.imread(target_name)
    image = cv2.imread(img_name)
    # 調整 target 的形狀
    target = cv2.resize(target, target_size)
    # 將 target 形狀存成三個變數
    h_target, w_target, d_target = target.shape
    # 設定 target 在原圖上的座標
    top_ = position[0]
    left_ = position[1]
    bottom_ = top_ + h_target
    right_ = left_ + w_target
    # 用 target 覆蓋原圖
    image[top_:bottom_, left_:right_] = target
    # 儲存圖片
    cv2.imwrite("output.png", image)

def draw_watermark_on_the_base_img(img_name, logo_name, position, logo_size):
    # 讀取原圖與 Logo
    logo = cv2.imread(logo_name)
    image = cv2.imread(img_name)
    # 設定 Logo 大小
    if logo_size == "frame":
        logo_size = (210, 30)
    elif logo_size == "W3":
        logo_size = (50,50)
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

# Setting parameter and using function
# 在底圖上疊標的圖
covering_target_img_on_the_base_img(base_img, target_img, (85, 30), (810, 330))
# 在標的圖上疊梯形框
draw_watermark_on_the_base_img(output_img, trapezoid_frame, "frame", "frame")
# # 在標的圖上疊警示圖
draw_watermark_on_the_base_img(output_img, warning_icon, "L1", "W3")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "L2", "W3")
# 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "L3", "W3")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "L4", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "L5", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "L6", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "L7", "W1")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "L8", "W1")
# 在標的圖上疊警示圖
draw_watermark_on_the_base_img(output_img, warning_icon, "L9", "W1")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M1", "W3")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M2", "W3")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M3", "W3")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M4", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M5", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M6", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M7", "W1")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M8", "W1")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "M9", "W1")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R1", "W3")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R2", "W3")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R3", "W3")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R4", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R5", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R6", "W2")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R7", "W1")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R8", "W1")
# # 在標的圖上疊警示圖
# draw_watermark_on_the_base_img(output_img, warning_icon, "R9", "W1")
# 梯形框文字
draw_text_on_the_base_img(output_img, inside_of_frame, (340, 87), 23, (20, 20, 20))
# 標的文字
draw_text_on_the_base_img(output_img, target, (75, 17), 30, (20, 20, 20))
# 縣市文字
draw_text_on_the_base_img(output_img, county, (360, 20), 13, (20, 20, 20))
# 緊急聯絡人文字
draw_text_on_the_base_img(output_img, contact_person, (400, 40), 13, (20, 20, 20))
# 溫度文字
draw_text_on_the_base_img(output_img, temperature, (925, 60), 15, (20, 20, 255))
# 濕度文字
draw_text_on_the_base_img(output_img, humidity, (1045, 60), 15, (20, 20, 255))
# 風速文字
draw_text_on_the_base_img(output_img, wind_speed, (925, 100), 15, (20, 20, 255))
# 含水率文字
draw_text_on_the_base_img(output_img, amc, (970, 137), 15, (20, 20, 255))
# 紅字警告
draw_text_on_the_base_img(output_img, warn_title, (880, 218), 15, (255, 20, 20))
# 毀壞區域
draw_text_on_the_base_img(output_img, warn_area, (880, 240), 15, (255, 20, 20))
# 警告說明
draw_text_on_the_base_img(output_img, warn_content, (880, 260), 13, (20, 20, 20))
