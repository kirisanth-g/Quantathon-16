import part3
import qparser

get_t = qparser.date_to_t

stock_data = qparser.stock_data
OUTPUT="D3.csv"

handle = open(OUTPUT, 'w')
for date in qparser.dates[1:]:
    print(date)
    handle.write(str(date) + ',')
    handle.write(str(part3.RP3(get_t(date))) + ',')
    handle.write(str(part3.CumR3(get_t(date))) + ',')
    handle.write(str(part3.num43(get_t(date))) + ',')
    handle.write(str(part3.num53(get_t(date))) + ',')
    for j in range(len(stock_data[date])):
        handle.write(str(part3.W3(get_t(date), j)))
        if j < len(stock_data[date]) - 1:
            handle.write(',')
    handle.write('\n')


handle.close()
