date, close, high, low = '', '', '', ''
dict_date, dict_ticker = {}, {}
ticker = 0
summ = 0
list_ma_1, list_ma_2 = [], []

with open('EURUSD_210101_210120 (3).txt', 'r') as file:
    ma_1 = int(input('Введите период МА 1 - '))
    ma_2 = int(input('Введите период МА 2 - '))
    for line in file.readlines(): # проход по строчкам
        date = line.split(',')[2] + '-' + line.split(',')[3][:2] + ':' + line.split(',')[3][2:4] # дата
        print(date)
        close = line.split(',')[-1].strip('\n') # закрытие свечи
        high = line.split(',')[-3] # макс цена свечи
        low = line.split(',')[-2] # мин цена свечи
        print(close)
        dict_date.update({date: [close, high, low, ticker]}) # добавление в словарь (доступ по дате) данных
        dict_ticker.update({ticker: [close, high, low, date]}) # тоже самое, только доступ по тикеру свечи
        list_ma_1.append(float(close))
        if len(list_ma_1) > ma_1:
            list_ma_1.remove(list_ma_1[0])
        print('MA1 - ',  ma_1, ' - ', sum(list_ma_1)/int(ma_1))
        list_ma_2.append(float(close))
        if len(list_ma_2) > ma_2:
            list_ma_2.remove(list_ma_2[0])
        print('Ma2 - ', ma_2, ' - ', sum(list_ma_2) / int(ma_2), '\n', '\n')
        ticker = ticker + 1

input_date = input('Введите дату и время - ')
print(dict_date[input_date])
ma_1 = int(input('Введите период МА 1 - '))
ma_2 = int(input('Введите период МА 2 - '))
ticker_ma = dict_date[input_date][-1]
for i in range(ma_1):
    ticker_ma = ticker_ma - 1
    summ = summ + float(dict_ticker[ticker_ma][0])
    print(dict_ticker[ticker_ma])
print(summ/ma_1)

