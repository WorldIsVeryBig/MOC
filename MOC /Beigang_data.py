import pandas as pd
import math


def csv_data():
    # 讀取csv資料
    df = pd.read_csv("./data/朝天宮三官殿Data/北港朝天宮三官殿神桌下Data.csv")
    # 將csv資料裡 LocalTime 欄位變成list
    time_data = df['資料時間'].tolist()
    # 包成 data 回傳
    data = {
        "Time": [time_data[i]+" - "+time_data[i+1] for i in range(len(time_data)-1)]
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
            data = dict()
            df1 = pd.read_csv("./data/朝天宮三川殿Data/北港朝天宮三川殿中脊楹Data.csv")
            df2 = pd.read_csv("./data/朝天宮三川殿Data/北港朝天宮三川殿正門彎枋Data.csv")
            df3 = pd.read_csv("./data/朝天宮三川殿Data/北港朝天宮三川殿虎門大楣Data.csv")
            df4 = pd.read_csv("./data/朝天宮三川殿Data/北港朝天宮三川殿龍門大楣Data.csv")
            location_data = [('interface2_B', df1), ('interface1_B', df2), ('interface2_A', df3), ('interface2_C', df4)]

            for i in range(len(location_data)):
                value = location_data[i][1]
                data.update({
                    location_data[i][0]: AH_calc(str(value.loc[value['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                                str(value.loc[value['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())
                })
            return data
        case '北港朝天宮 - 觀音殿':
            data = dict()
            df1 = pd.read_csv("./data/朝天宮觀音殿Data/北港朝天宮觀音殿虎邊大通Data.csv")
            df2 = pd.read_csv("./data/朝天宮觀音殿Data/北港朝天宮觀音殿神桌下Data.csv")
            df3 = pd.read_csv("./data/朝天宮觀音殿Data/北港朝天宮觀音殿龍邊中脊楹Data.csv")
            location_data = [('interface2_A', df1), ('interface3_H', df2), ('interface2_C', df3)]

            for i in range(len(location_data)):
                value = location_data[i][1]
                data.update({
                    location_data[i][0]: AH_calc(str(value.loc[value['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                                str(value.loc[value['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())
                })
            return data
        case '北港朝天宮 - 主殿':
            data = dict()
            df1 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿前神桌下Data.csv")
            df2 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿壽樑Data.csv")
            df3 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿藻井圓坯Data.csv")
            df4 = pd.read_csv("./data/朝天宮正殿Data/北港朝天宮正殿藻井Data.csv")
            location_data = [('interface3_H', df1), ('interface1_B', df2), ('interface2_B', df3), ('interface2_H', df4)]

            for i in range(len(location_data)):
                value = location_data[i][1]
                data.update({
                    location_data[i][0]: AH_calc(str(value.loc[value['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                                str(value.loc[value['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())
                })
            return data
        case '北港朝天宮 - 三官殿':
            data = dict()
            df1 = pd.read_csv("./data/朝天宮三官殿Data/北港朝天宮三官殿虎邊大通Data.csv")
            df2 = pd.read_csv("./data/朝天宮三官殿Data/北港朝天宮三官殿神桌下Data.csv")
            df3 = pd.read_csv("./data/朝天宮三官殿Data/北港朝天宮三官殿龍邊中脊楹Data.csv")
            location_data = [('interface2_A', df1), ('interface3_H', df2), ('interface2_F', df3)]

            for i in range(len(location_data)):
                value = location_data[i][1]
                data.update({
                    location_data[i][0]: AH_calc(str(value.loc[value['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                                str(value.loc[value['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())
                })
            return data
        case '北港朝天宮 - 文昌殿':
            data = dict()
            df1 = pd.read_csv("./data/朝天宮文昌殿Data/北港朝天宮文昌殿虎邊中脊楹Data.csv")
            df2 = pd.read_csv("./data/朝天宮文昌殿Data/北港朝天宮文昌殿神桌下Data.csv")
            df3 = pd.read_csv("./data/朝天宮文昌殿Data/北港朝天宮文昌殿龍邊大通Data.csv")
            location_data = [('interface2_D', df1), ('interface3_H', df2), ('interface2_C', df3)]

            for i in range(len(location_data)):
                value = location_data[i][1]
                data.update({
                    location_data[i][0]: AH_calc(str(value.loc[value['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                                str(value.loc[value['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())
                })
            return data
        case '鹿港龍山寺 - 正殿':
            data = dict()
            df1 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿中脊楹Data.csv")
            df2 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿虎邊大通Data.csv")
            df3 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿後虎門員光Data.csv")
            df4 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿後龍門員光Data.csv")
            df5 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿龍邊大通Data.csv")
            df6 = pd.read_csv("./data/龍山寺正殿Data/鹿港龍山寺正殿觀音前神桌下Data.csv")
            location_data = [('interface2_B', df1), ('interface2_A', df2), ('interface3_A', df3), 
                            ('interface3_C', df4), ('interface2_C', df5), ('interface3_H', df6)]

            for i in range(len(location_data)):
                value = location_data[i][1]
                data.update({
                    location_data[i][0]: AH_calc(str(value.loc[value['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                                str(value.loc[value['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())
                })
            return data
        case '鹿港龍山寺 - 後殿':
            data = dict()
            df1 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿外虎邊卷棚彎枋Data.csv")
            df2 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿外虎邊壽樑Data.csv")
            df3 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿虎邊中脊楹Data.csv")
            df4 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿虎邊束木Data.csv")
            df5 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿阿彌陀佛神桌下Data.csv")
            df6 = pd.read_csv("./data/龍山寺後殿Data/鹿港龍山寺後殿龍邊束木Data.csv")

            location_data = [('interface2_B', df1), ('interface2_A', df2), ('interface3_A', df3), 
                            ('interface3_C', df4), ('interface2_C', df5), ('interface3_H', df6)]
            for i in range(len(location_data)):
                value = location_data[i][1]
                data.update({
                    location_data[i][0]: AH_calc(str(value.loc[value['資料時間'] == time]['溫度(°C)']).split("   ")[1].split("\n")[0].strip(), 
                                                str(value.loc[value['資料時間'] == time]['相對濕度(%)']).split("   ")[1].split("\n")[0].strip())
                })
            return data
