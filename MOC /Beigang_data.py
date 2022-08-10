import pandas as pd


def csv_data():
    # 讀取csv資料
    df = pd.read_csv("./data/no_index_test_LSTM_15_北港朝天宮綜合氣象站(2020).csv")
    # 將變數time設成 list
    time = list()
    # 將csv資料裡 LocalTime 欄位變成list
    time_data = df['LocalTime'].tolist()
    # 將 LocalTime 裡的資料傳入 Time 變數裡
    for i in range(len(time_data)-1):
        time.append(time_data[i]+" - "+time_data[i+1])
    # 包成 data 回傳
    data = {
        "Time": time
    }
    return data
