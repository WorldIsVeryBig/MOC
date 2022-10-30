import pandas as pd
import math


def csv_data():
    # 讀取csv資料
    df = pd.read_csv("./data/朝天宮三官殿Data/北港朝天宮三官殿神桌下Data.csv")
    # 將變數time設成 list
    time = list()
    # 將csv資料裡 LocalTime 欄位變成list
    time_data = df['資料時間'].tolist()
    # 將 LocalTime 裡的資料傳入 Time 變數裡
    time = [time_data[i]+" - "+time_data[i+1] for i in range(len(time_data)-1)]
    # 包成 data 回傳
    data = {
        "Time": time
    }
    return data

def AH_calc(temp, hum):
    Tk = float(temp) + 273.15
    sida = 1 - (Tk / 647.096)
    exp = (math.exp((647.096 * (-7.85951783 * sida + 1.84408259 * sida ** 1.5 - 11.7866497 * sida ** 3 + 22.6807411 * sida ** 3.5 - 
            15.9618719 * sida ** 4 + 1.80122502 * sida ** 7.5))/Tk))
    Pws_hPa = 220640 * exp
    Pw_Pa = (float(hum) / 100) * Pws_hPa * 100
    Ah = str(round(float(2.169 * Pw_Pa / Tk), 2))
    return Ah

def alert_point_data(tempo_name, time):
    match tempo_name:
        case '北港朝天宮 - 三川殿':
            df1 = pd.read_csv("./data/朝天宮三川殿Data/北港朝天宮三川殿中脊楹Data.csv")
            df2 = pd.read_csv("./data/朝天宮三川殿Data/北港朝天宮三川殿正門彎枋Data.csv")
            df3 = pd.read_csv("./data/朝天宮三川殿Data/北港朝天宮三川殿虎門大楣Data.csv")
            df4 = pd.read_csv("./data/朝天宮三川殿Data/北港朝天宮三川殿龍門大楣Data.csv")

            data = {
                "interface2_B": AH_calc(str(df1.loc[df1['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df1.loc[df1['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 中上
                "interface1_B": AH_calc(str(df2.loc[df2['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df2.loc[df2['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 1 中上
                "interface2_A": AH_calc(str(df3.loc[df3['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df3.loc[df3['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 左上
                "interface2_C": AH_calc(str(df4.loc[df4['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df4.loc[df4['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())  #interface 2 右上
            }
            return data
        case '北港朝天宮 - 觀音殿':
            df1 = pd.read_csv("./data/朝天宮觀音殿Data/北港朝天宮觀音殿虎邊大通Data.csv")
            df2 = pd.read_csv("./data/朝天宮觀音殿Data/北港朝天宮觀音殿神桌下Data.csv")
            df3 = pd.read_csv("./data/朝天宮觀音殿Data/北港朝天宮觀音殿龍邊中脊楹Data.csv")

            data = {
                "interface2_A": AH_calc(str(df1.loc[df1['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df1.loc[df1['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 左上
                "interface3_H": AH_calc(str(df2.loc[df2['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df2.loc[df2['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 3 中下
                "interface2_C": AH_calc(str(df3.loc[df3['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df3.loc[df3['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())  #interface 2 右上
            }
            return data
        case '北港朝天宮 - 主殿':
            df1 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿前神桌下Data.csv")
            df2 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿壽樑Data.csv")
            df3 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿藻井圓坯Data.csv")
            df4 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿藻井Data.csv")

            data = {
                "interface3_H": AH_calc(str(df1.loc[df1['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df1.loc[df1['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 3 中下
                "interface1_B": AH_calc(str(df2.loc[df2['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df2.loc[df2['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 1 中上
                "interface2_B": AH_calc(str(df3.loc[df3['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df3.loc[df3['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 中上
                "interface2_H": AH_calc(str(df4.loc[df4['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df4.loc[df4['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())  #interface 2 中下
            }
            return data
        case '北港朝天宮 - 三官殿':
            df1 = pd.read_csv("./data/朝天宮三官殿Data/北港朝天宮三官殿虎邊大通Data.csv")
            df2 = pd.read_csv("./data/朝天宮三官殿Data/北港朝天宮三官殿神桌下Data.csv")
            df3 = pd.read_csv("./data/朝天宮三官殿Data/北港朝天宮三官殿龍邊中脊楹Data.csv")

            data = {
                "interface2_A": AH_calc(str(df1.loc[df1['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df1.loc[df1['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 左上 
                "interface3_H": AH_calc(str(df2.loc[df2['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df2.loc[df2['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 3 中下
                "interface2_F": AH_calc(str(df3.loc[df3['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df3.loc[df3['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())  #interface 2 右中
            }
            return data
        case '北港朝天宮 - 文昌殿':
            df1 = pd.read_csv("./data/朝天宮文昌殿Data/北港朝天宮文昌殿虎邊中脊楹Data.csv")
            df2 = pd.read_csv("./data/朝天宮文昌殿Data/北港朝天宮文昌殿神桌下Data.csv")
            df3 = pd.read_csv("./data/朝天宮文昌殿Data/北港朝天宮文昌殿龍邊大通Data.csv")

            data = {
                "interface2_D": AH_calc(str(df1.loc[df1['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df1.loc[df1['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 左中
                "interface3_H": AH_calc(str(df2.loc[df2['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df2.loc[df2['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 3 中下
                "interface2_C": AH_calc(str(df3.loc[df3['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df3.loc[df3['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())  #interface 2 右上
            }
            return data
        case '鹿港龍山寺 - 正殿':
            df1 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿中脊楹Data.csv")
            df2 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿虎邊大通Data.csv")
            df3 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿後虎門員光Data.csv")
            df4 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿後龍門員光Data.csv")
            df5 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿龍邊大通Data.csv")
            df6 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿觀音前神桌下Data.csv")

            data = {
                "interface2_B": AH_calc(str(df1.loc[df1['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df1.loc[df1['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 左中
                "interface2_A": AH_calc(str(df2.loc[df2['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df2.loc[df2['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 左上
                "interface3_A": AH_calc(str(df3.loc[df3['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df3.loc[df3['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()),  #interface 3 左上
                "interface3_C": AH_calc(str(df4.loc[df4['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df4.loc[df4['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 3 右上
                "interface2_C": AH_calc(str(df5.loc[df5['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df5.loc[df5['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 2 右上
                "interface3_H": AH_calc(str(df6.loc[df6['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df6.loc[df6['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())  #interface 3 中下
            }
            return data
        case '鹿港龍山寺 - 後殿':
            df1 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿外虎邊卷棚彎枋Data.csv")
            df2 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿外虎邊壽樑Data.csv")
            df3 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿虎邊中脊楹Data.csv")
            df4 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿虎邊束木Data.csv")
            df5 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿阿彌陀佛神桌下Data.csv")
            df6 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿龍邊束木Data.csv")

            data = {
                "interface1_A": AH_calc(str(df1.loc[df1['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df1.loc[df1['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 1 左上
                "interface1_B": AH_calc(str(df2.loc[df2['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df2.loc[df2['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 1 中上
                "interface2_A": AH_calc(str(df3.loc[df3['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df3.loc[df3['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()),  #interface 2 左上
                "interface3_C": AH_calc(str(df4.loc[df4['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df4.loc[df4['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 3 左上
                "interface3_H": AH_calc(str(df5.loc[df5['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df5.loc[df5['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip()), #interface 3 中下
                "interface3_C": AH_calc(str(df6.loc[df6['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                        str(df6.loc[df6['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())  #interface 3 右上
            }
            return data
