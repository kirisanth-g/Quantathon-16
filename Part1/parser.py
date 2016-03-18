INITIAL_DAY = 20000104

class Stock:
    def __init__(self, so, sh, sl, sc, tvl, ind):
        self.so = so
        self.sh = sh
        self.sl = sl
        self.sc = sc
        self.tvl = tvl
        self.ind = ind


def t_to_date(t):
    return t + INITIAL_DAY




def create_stocks(filename="in_sample_data.txt"):
    handle = open(filename, 'r')
    stock_data = {}
    for raw_line in handle:
        line = raw_line.split(",")
        stock_data[int(line[0])] = []
        for i in range(1, len(line), 6):
            stock_data[int(line[0])].append(
                Stock(
                    float(line[i].strip()), 
                    float(line[i+1].strip()),
                    float(line[i+2].strip()),
                    float(line[i+3].strip()),
                    int(line[i+4].strip()),
                    int(line[i+5].strip())))

    return stock_data
            
    
