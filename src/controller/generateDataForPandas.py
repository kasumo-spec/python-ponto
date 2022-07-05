import pandas as pd

def generate_data_for_pandas(data):
    result_dict = {}
    bank_time = 0
    for year, months in data.items():
        result_dict[year] = {}
        for month, days in months.items():
            result_dict[year][month] = {}
            for day, value in days.items():
                values = {}
                for i in range(4):
                    values['P{}'.format(i)] = value['hours'][i] if i < len(value['hours']) else None
                bank_time = bank_time + value['bank_time'] 
                hour_bank = value['bank_time'] // 60
                minute_bank = value['bank_time'] % 60
                values['Bank'] = "{}:{}".format(int(hour_bank),int(minute_bank))
                result_dict[year][month][day] = values

    hour_final = bank_time // 60
    minute_final = bank_time % 60
    timer = "{}:{}".format(int(hour_final),int(minute_final))

    return result_dict, timer