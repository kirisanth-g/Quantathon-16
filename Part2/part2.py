import qparser
import math

stock_data = qparser.create_stocks()
get_date = qparser.t_to_date
log = math.log
coeff = qparser.create_coeffs()
N = len(stock_data[get_date(0)])
T = len(stock_data.keys())

def RCO(t, j):
	return stock_data[get_date(t)][j].so/stock_data[get_date(t-1)][j].sc-1

def ROC(t, j):
    return stock_data[get_date(t)][j].sc/stock_data[get_date(t)][j].so-1

def ROO(t, j):
    return stock_data[get_date(t)][j].so/stock_data[get_date(t-1)][j].so-1

def RVP(t, j):
    return (1/(4*log(2)))* ((log(stock_data[get_date(t)][j].sh) - 
        log(stock_data[get_date(t)][j].sl))**2)

def RCC(t, j):
    return stock_data[get_date(t)][j].sc/stock_data[get_date(t-1)][j].sc-1

def AvrRCC(t):
    total = 0
    for stock in stock_data[get_date(t)]:
        total += stock.sc
    return total / N

def Avg(t, j, f):
    total = 0
    count = 0
    for day in range(max(1, t-199), t):
        total += f(day, j)
        count += 1
    return total / count

def AvrTVL(t, j):
    return Avg(t, j, lambda day, j: stock_data[get_date(day)][j].tvl)

def AvrRCO(t, j):
    return Avg(t, j, RCO)

def AvrROC(t, j):
    return Avg(t, j, ROC)

def AvrROO(t, j):
    return Avg(t, j, ROO)

def AvrRVP(t, j):
    return Avg(t, j, RVP)


# def W1(t,j):
#     return -(1/N)*(RCC(t-1, j) - AvrRCC(t-1))



# def RP1(t):
#     sum1 = 0
#     sum2 = 0
#     for j in range(len(stock_data[get_date(t)])):
#         sum1 += W1(t, j)*RCC(t, j)
#         sum2 += abs(W1(t, j))

#     return sum1 / sum2



# def CumR1(t):
#     product = 1
#     for i in range(3,t):
#         product *= 1 + RP1(t)

#     return math.log(product)


# def num41(t):
#     total = 0
#     for j in range(len(stock_data[get_date(t)])):
#         total += abs(W1(t, j))

#     return total / N

# def num51(t):
#     sum1 = 0
#     sum2 = 0
#     for j in range(len(stock_data[get_date(t)])):
#         sum1 += W1(t, j)
#         sum2 += abs(W1(t, j))

#     return sum1 / sum2

