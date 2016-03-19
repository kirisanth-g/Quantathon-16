import part2
import qparser

get_t = qparser.date_to_t

stock_data = qparser.stock_data
OUTPUT="D2.csv"

handle = open(OUTPUT, 'w')
for date in qparser.dates[1:]:
    print(date)
    handle.write(str(date) + ',')
    handle.write(str(part2.RP2(get_t(date))) + ',')
    handle.write(str(part2.CumR2(get_t(date))) + ',')
    handle.write(str(part2.num42(get_t(date))) + ',')
    handle.write(str(part2.num52(get_t(date))) + ',')
    for j in range(len(stock_data[date])):
        handle.write(str(part2.W2(get_t(date), j)))
        if j < len(stock_data[date]) - 1:
            handle.write(',')
    handle.write('\n')


handle.close()
