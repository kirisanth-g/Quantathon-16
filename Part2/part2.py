import qparser
import math

stock_data = qparser.create_stocks()
get_date = qparser.t_to_date
log = math.log
coeff = qparser.create_coeffs()
N = len(stock_data[get_date(0)])
T = len(stock_data.keys())

def RCO(t, j):
    #close-to-open return on stock j
	return stock_data[get_date(t)][j].so/stock_data[get_date(t-1)][j].sc-1

def ROC(t, j):
    #open-to-close return
    return stock_data[get_date(t)][j].sc/stock_data[get_date(t)][j].so-1

def ROO(t, j):
    #open-to-open return for each stock
    return stock_data[get_date(t)][j].so/stock_data[get_date(t-1)][j].so-1

def RVP(t, j):
    #range-based proxy for variance on day t
    return (1/(4*log(2)))* ((log(stock_data[get_date(t)][j].sh) - 
        log(stock_data[get_date(t)][j].sl))**2)

def RCC(t, j):
    #daily close-to-close return for stock j
    return stock_data[get_date(t)][j].sc/stock_data[get_date(t-1)][j].sc-1

def AvrRCC(t):
    #average daily close-to-close return
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
    if count == 0:
        return f(t, j)
    return total / count

def Avg2(t, f):
    total = 0
    count = 0
    for j in range(len(stock_data[get_date(t)])):
        total += f(t, j)
        count += 1
    return total / count

def TVL(t, j):
    #trading volume
    return stock_data[get_date(t)][j].tvl

def AvrTVL(t, j):
    #average trading volume
    return Avg(t, j, lambda day, j: stock_data[get_date(day)][j].tvl)

def AvrRCO(t):
    #average close-to-open return on stock j
    return Avg2(t, RCO)

def AvrROC(t):
    #average open-to-close return
    return Avg2(t, ROC)

def AvrROO(t):
    #average open-to-open return
    return Avg2(t, ROO)

def AvrRVP(t, j):
    #average range-based proxy for variance
    return Avg(t, j, RVP)


def W2(t, j):
    #portfolio weights
    a = RCC(t-1, j)
    b = AvrRCC(t-1)
    c = ROO(t, j)
    d = AvrROO(t)
    e = ROC(t-1, j)
    f = AvrROC(t-1)
    g = RCO(t, j)
    h = AvrRCO(t)
    i = TVL(t-1,j)
    j = AvrTVL(t-1,j)
    
    return coeff['a1']*(a - b)/N + coeff['a2']*(c - d)/N + \
            coeff['a3']*(e - f)/N + coeff['a4']*(g - h)/N + \
            coeff['a5']*(i / j)*(a - b) / N + \
            coeff['a6']*(i / j)*(c - d) / N + \
            coeff['a7']*(i / j)*(e - f) / N + \
            coeff['a8']*(i / j)*(g - h) / N + \
            coeff['a9']*(i / j)*(a - b) / N + \
            coeff['a10']*(i / j)*(c - d) / N + \
            coeff['a11']*(i / j)*(e - f) / N + \
            coeff['a12']*(i / j)*(g - h) / N



def RP2(t):
    sum1 = 0
    sum2 = 0
    for j in range(len(stock_data[get_date(t)])):
        sum1 += W2(t, j)*RCC(t, j)
        sum2 += abs(W2(t, j))
    return sum1 / sum2


def CumR2(t):
    product = 1
    for i in range(3,t):
        product *= 1 + RP2(t)
    return math.log(product)

def num42(t):
    total = 0
    for j in range(len(stock_data[get_date(t)])):
        total += abs(W2(t, j))
    return total / N

def num52(t):
    sum1 = 0
    sum2 = 0
    for j in range(len(stock_data[get_date(t)])):
        sum1 += W2(t, j)
        sum2 += abs(W2(t, j))
    return sum1 / sum2

