# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from image import *
from Beigang_data import *


def get_info(event):
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
    # 繪製目標圖
    result.draw_result_img()

    # 繪製警告標誌
    if interface_combobox.get() == 'Interface 1':
        Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L1", "W3")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L2", "W3")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L3", "W3")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M1", "W3")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M2", "W3")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M3", "W3")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R1", "W3")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R2", "W3")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R3", "W3")
    elif interface_combobox.get() == 'Interface 2':
        Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L4", "W2")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L5", "W2")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L6", "W2")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M4", "W2")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M5", "W2")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M6", "W2")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R4", "W2")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R5", "W2")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R6", "W2")
    else:
        Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L7", "W1")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L8", "W1")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "L9", "W1")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M7", "W1")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M8", "W1")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "M9", "W1")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R7", "W1")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R8", "W1")
        # Create_Img.draw_watermark_on_the_base_img('output.png', warning_icon, "R9", "W1")

    # 設置預設圖片
    photo = tk.PhotoImage(file="output.png")
    imgLabel = tk.Label(root, image=photo)
    imgLabel.place(x=24, y=125)

    return data

# 設置主畫面
root = tk.Tk()
root.title('test window')
root.geometry('1200x600')
# 設置畫布
canvas = tk.Canvas(root, width=1250, height=600)
canvas.pack()
# 取得時間資料
data = csv_data()

# 設置時間下拉條
# time_combobox_list = ['2018/05/26 13:30:00 - 2018/05/26 13:40:00']
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
tempo_name_combobox_list = ['北港朝天宮 - 三川殿', '北港朝天宮 - 觀音殿', '北港朝天宮 - 主殿', '北港朝天宮 - 三宮殿', '北港朝天宮 - 文昌殿']
tempo_name_combobox = ttk.Combobox(root, state='readonly')
tempo_name_combobox.bind("<<ComboboxSelected>>", get_info)
tempo_name_combobox['value'] = tempo_name_combobox_list
tempo_name_combobox.place(x=24, y=20)
tempo_name_combobox.current(0)

# 繪製矩形框
canvas.create_rectangle(22, 123, 1179, 567, width=3)

# 設置預設圖
photo = tk.PhotoImage(file="output.png")
imgLabel = tk.Label(root, image=photo)
imgLabel.place(x=24, y=125)

root.mainloop()
