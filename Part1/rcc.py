import qparser

stock_data = qparser.create_stocks()
get_date = qparser.t_to_date

def rcc(t, j):
	return stock_data[get_date(t)][j].so/stock_data[get_date(t-1)][j].so-1