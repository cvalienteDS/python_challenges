from datetime import datetime

def weekly_aggregation(ts):
    dict_output = {}
    for i, date_str in enumerate(ts):
        date = datetime.strptime(date_str, '%Y-%m-%d')
        if i == 0:
            starting_date = date
        weeks_from_starting = (date - starting_date).days //7
        try:
            dict_output[weeks_from_starting].append(date)
        except KeyError:
            dict_output[weeks_from_starting] = [date]
    list_output = [[datetime.strftime(date, format='%Y-%m-%d') for date in value] for value in dict_output.values()]
    return list_output


ts = [
    '2019-01-01',
    '2019-01-02',
    '2019-01-08',
    '2019-02-01',
    '2019-02-02',
    '2019-02-05',
]
print(weekly_aggregation(ts))