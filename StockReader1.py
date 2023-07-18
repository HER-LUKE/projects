import yfinance as yf
import pandas as pd
import datetime




def get_Time():
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%H")
    return formatted_time

def get_stock_data(symbol,period):
    stock = yf.Ticker(symbol)
    data = stock.history(period)
    return data

def get_current_price(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    current_price = info.get('currentPrice')
    return current_price, info

def get_week_data(symbol):
    period = "7d"
    stock_data = get_stock_data(symbol,period)
    Os_data = stock_data['Open'].tolist()
    Cs_data = stock_data['Close'].tolist()
    x = 0
    total_change = []
    while x < len(Os_data):
        day_Change = float(Cs_data[x]) - float(Os_data[x])
        total_change.append(day_Change)
        day = x + 1
        print('Day: ' + str(day) + ' \n Changes : ' + str(day_Change))
        x +=1
    wt_Change = sum(total_change)
    print(str(symbol) + ": Week Price Change: " + str(wt_Change))
    ## w_Change > 0 

def get_month_data(symbol):
    period = "30d"
    stock_data = get_stock_data(symbol,period)
    Os_data = stock_data['Open'].tolist()
    Cs_data = stock_data['Close'].tolist()
    x = 0
    total_change = []
    while x < len(Os_data):
        day_Change = float(Cs_data[x]) - float(Os_data[x])
        total_change.append(day_Change)
        day = x + 1
        print('Day: ' + str(day) + ' \n Changes : ' + str(day_Change))
        x +=1
    mt_Change = sum(total_change)
    print(str(symbol) + ": Month Price Change: " + str(mt_Change))
    return mt_Change, stock_data

def main():
    symbols = ["AAPL"] ##,"GOOGL", "GOOG" ]
    for symbol in symbols:
        stock_data , mtChange = get_month_data(symbol)
        current_price, info = get_current_price(symbol)
        print(str(symbol) + " " + str(stock_data))
        print("Current Price: " + str(current_price))

main()
