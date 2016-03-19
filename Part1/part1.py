import qparser
import math

get_date = qparser.t_to_date
stock_data = qparser.stock_data
N = len(stock_data[get_date(0)])
T = len(stock_data.keys())


def RCC(t, j):
	return stock_data[get_date(t)][j].sc/stock_data[get_date(t-1)][j].sc-1

def AvrRCC(t):
    total = 0
    for stock in stock_data[get_date(t)]:
        total += stock.sc
    return total / N

def W1(t,j):
    return -(1/N)*(RCC(t-1, j) - AvrRCC(t-1))



def RP1(t):
    sum1 = 0
    sum2 = 0
    for j in range(len(stock_data[get_date(t)])):
        sum1 += W1(t, j)*RCC(t, j)
        sum2 += abs(W1(t, j))

    return sum1 / sum2



def CumR1(t):
    product = 1
    for i in range(3,t):
        product *= 1 + RP1(t)

    return math.log(product)


def num41(t):
    total = 0
    for j in range(len(stock_data[get_date(t)])):
        total += abs(W1(t, j))

    return total / N

def num51(t):
    sum1 = 0
    sum2 = 0
    for j in range(len(stock_data[get_date(t)])):
        sum1 += W1(t, j)
        sum2 += abs(W1(t, j))

    return sum1 / sum2

