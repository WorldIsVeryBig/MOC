import pandas as pd


def csv_data():
    df = pd.read_csv("./data/LSTM_15_北港朝天宮綜合氣象站(10min).csv")
    time = list()
    time_data = df['LocalTime'].tolist()
    for i in range(len(time_data)-1):
        time.append(time_data[i]+" - "+time_data[i+1])

    data = {
        "Time": time
    }
    return data
csv_data()