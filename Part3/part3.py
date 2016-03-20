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
    return stock_data[get_date(t)][j].tvl

def AvrTVL(t, j):
    return Avg(t, j, lambda day, j: stock_data[get_date(day)][j].tvl)

def AvrRCO(t):
    return Avg2(t, RCO)

def AvrROC(t):
    return Avg2(t, ROC)

def AvrROO(t):
    return Avg2(t, ROO)

def AvrRVP(t, j):
    return Avg(t, j, RVP)


def W2(t, j):
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

def W3(t, j):
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
    
    return coeff['b1']*(a - b)/N + coeff['b2']*(c - d)/N + \
            coeff['b3']*(e - f)/N + coeff['b4']*(g - h)/N + \
            coeff['b5']*(i / j)*(a - b) / N + \
            coeff['b6']*(i / j)*(c - d) / N + \
            coeff['b7']*(i / j)*(e - f) / N + \
            coeff['b8']*(i / j)*(g - h) / N + \
            coeff['b9']*(i / j)*(a - b) / N + \
            coeff['b10']*(i / j)*(c - d) / N + \
            coeff['b11']*(i / j)*(e - f) / N + \
            coeff['b12']*(i / j)*(g - h) / N


def FILL3(t, j):
    return 1 if W3(t, j)*stock_data[get_date(t)][j].ind >= 0 else 0

def RP3(t):
    total1 = 0
    total2 = 0
    for j in range(len(stock_data[get_date(t)])):
        total1 += FILL3(t, j)*W3(t, j)*ROC(t, j)
        total2 += abs(FILL3(t, j)*W3(t, j))

    if total2 == 0:
        return 0

    return total1 / total2

def CumR3(t):
    product = 1
    for i in range(3,t):
        product *= 1 + RP3(t)
    return math.log(product)

def num43(t):
    total = 0
    for j in range(len(stock_data[get_date(t)])):
        total += abs(FILL3(t, j)*W3(t, j))

    return total / N


def num53(t):
    total1 = 0
    total2 = 0
    for j in range(len(stock_data[get_date(t)])):
        total1 += FILL3(t, j)*W3(t, j)
        total2 += abs(FILL3(t, j)*W3(t, j))

    return total1 / total2




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

