import part1
import qparser

get_t = qparser.date_to_t

stock_data = qparser.stock_data
OUTPUT="D1.csv"

handle = open(OUTPUT, 'w')
for date in qparser.dates[1:]:
    print(date)
    handle.write(str(date) + ',')
    handle.write(str(part1.RP1(get_t(date))) + ',')
    handle.write(str(part1.CumR1(get_t(date))) + ',')
    handle.write(str(part1.num41(get_t(date))) + ',')
    handle.write(str(part1.num51(get_t(date))) + ',')
    for j in range(len(stock_data[date])):
        handle.write(str(part1.W1(get_t(date), j)))
        if j < len(stock_data[date]) - 1:
            handle.write(',')
    handle.write('\n')


handle.close()
