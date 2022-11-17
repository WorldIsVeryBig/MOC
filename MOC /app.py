# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from image import *
from Beigang_data import *


def get_info(event):
    content_mapping = {
        "A": "左上方",
        "B": "中上方",
        "C": "右上方",
        "D": "左中方",
        "E": "正中間",
        "F": "右中方",
        "G": "左下方",
        "H": "中下方",
        "I": "右下方"
    }
    # 取得資料
    data = {
        "Time": time_combobox.get(),
        "Interface": interface_combobox.get(),
        "Tempo_name": tempo_name_combobox.get()
    }
    # 處理傳入時間
    time = data['Time'].split(" - ")[1]
    # 傳入 class 所需變數
    result = Create_Img(time=time, interface=data['Interface'], tempo_name=data['Tempo_name'])
    image_data = result.get_info()
    # 繪製目標圖
    result.draw_result_img()
    alert_data = alert_point_data(tempo_name=data['Tempo_name'], time=time)

    # 繪製警告標誌
    if interface_combobox.get() == 'Interface 1':
        content = ['左下方'] if data.get('Tempo_name') == '北港朝天宮 - 主殿' and image_data['wind_speed'] != 0 else list()
        icon_mapping = {
            "A": ("L1", "W3"), 
            "D": ("L2", "W3"),
            "G": ("L3", "W3"),
            "B": ("M1", "W3"),
            "E": ("M2", "W3"),
            "H": ("M3", "W3"),
            "C": ("R1", "W3"),
            "F": ("R2", "W3"),
            "I": ("R3", "W3")
        }
        for i in list(alert_data):
            if i.split('_')[0] != 'interface1':
                alert_data.pop(i)
        for k, v in alert_data.items():
            if float(v) < 11.5 or float(v) > 15:
                font_info = icon_mapping.get(k.split('_')[1])
                Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, font_info[0], font_info[1])
                position_info = content_mapping.get(k.split('_')[1])
                if position_info not in content:
                    content.append(position_info)
        content = "區域：{area}".format(area = content)
        result.write_text_on_image(content, (880, 240), 15, (255, 20, 20))
        if data.get('Tempo_name') == '北港朝天宮 - 主殿' and image_data['wind_speed'] != 0:
            Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, 'L3', 'W3')
    elif interface_combobox.get() == 'Interface 2':
        content = ['中上方', '正中間'] if data.get('Tempo_name') == '北港朝天宮 - 主殿' and image_data['wind_speed'] != 0 else list()
        icon_mapping = {
            "A": ("L4", "W2"), 
            "D": ("L5", "W2"),
            "G": ("L6", "W2"),
            "B": ("M4", "W2"),
            "E": ("M5", "W2"),
            "H": ("M6", "W2"),
            "C": ("R4", "W2"),
            "F": ("R5", "W2"),
            "I": ("R6", "W2")
        }
        for i in list(alert_data):
            if i.split('_')[0] != 'interface2':
                alert_data.pop(i)

        for k, v in alert_data.items():
            if float(v) < 11.5 or float(v) > 15:
                font_info = icon_mapping.get(k.split('_')[1])
                Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, font_info[0], font_info[1])
                position_info = content_mapping.get(k.split('_')[1])
                if position_info not in content:
                    content.append(position_info)
        content = "區域：{area}".format(area = content)
        result.write_text_on_image(content, (880, 240), 15, (255, 20, 20))
        if data.get('Tempo_name') == '北港朝天宮 - 主殿' and image_data['wind_speed'] != 0:
            Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, 'M4', 'W2')
            Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, 'M5', 'W2')
    else:
        content = ['右上方'] if data.get('Tempo_name') == '北港朝天宮 - 主殿' and image_data['wind_speed'] != 0 else list()
        icon_mapping = {
            "A": ("L7", "W1"), 
            "D": ("L8", "W1"),
            "G": ("L9", "W1"),
            "B": ("M7", "W1"),
            "E": ("M8", "W1"),
            "H": ("M9", "W1"),
            "C": ("R7", "W1"),
            "F": ("R8", "W1"),
            "I": ("R9", "W1")
        }
        for i in list(alert_data):
            if i.split('_')[0] != 'interface3':
                alert_data.pop(i)

        for k, v in alert_data.items():
            if float(v) < 11.5 or float(v) > 15:
                font_info = icon_mapping.get(k.split('_')[1])
                Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, font_info[0], font_info[1])
                position_info = content_mapping.get(k.split('_')[1])
                if position_info not in content:
                    content.append(position_info)
        content = "區域：{area}".format(area = content)
        result.write_text_on_image(content, (880, 240), 15, (255, 20, 20))
        if data.get('Tempo_name') == '北港朝天宮 - 主殿' and image_data['wind_speed'] != 0:
            Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, 'R7', 'W1')
    # 設置預設圖片
    photo = tk.PhotoImage(file="output.png")
    imgLabel = tk.Label(root, image=photo)
    imgLabel.place(x=24, y=125)

    return data

# 設置主畫面
root = tk.Tk()
root.title('User Window')
root.geometry('1200x600')
# 設置畫布
canvas = tk.Canvas(root, width=1250, height=600)
canvas.pack()
# 取得時間資料
data = csv_data()

# 設置時間下拉條
time_combobox_list = data['Time']
time_combobox = ttk.Combobox(root, state='readonly', width=32)
time_combobox.bind("<<ComboboxSelected>>", get_info)
time_combobox['values'] = time_combobox_list
time_combobox.place(x=870, y=20)
time_combobox.current(0)

# 設置介面下拉條
interface_combobox_list = ['Interface 1', 'Interface 2', 'Interface 3']
interface_combobox = ttk.Combobox(root, state='readonly')
interface_combobox.bind("<<ComboboxSelected>>", get_info)
interface_combobox['value'] = interface_combobox_list
interface_combobox.place(x=500, y=20)
interface_combobox.current(0)

# 設置宮殿名稱下拉條
tempo_name_combobox_list = ['北港朝天宮 - 三川殿', '北港朝天宮 - 觀音殿', '北港朝天宮 - 主殿', '北港朝天宮 - 三官殿',
                            '北港朝天宮 - 文昌殿', '鹿港龍山寺 - 正殿', '鹿港龍山寺 - 後殿']
tempo_name_combobox = ttk.Combobox(root, state='readonly')
tempo_name_combobox.bind("<<ComboboxSelected>>", get_info)
tempo_name_combobox['value'] = tempo_name_combobox_list
tempo_name_combobox.place(x=24, y=20)
tempo_name_combobox.current(2)

# 繪製矩形框
canvas.create_rectangle(22, 123, 1179, 567, width=3)

# 設置預設圖
photo = tk.PhotoImage(file="output.png")
imgLabel = tk.Label(root, image=photo)
imgLabel.place(x=24, y=125)

root.mainloop()
