from grs import Stock
from grs import TWTime
from grs import RealtimeStock
import time
import os

def clear():
    os.system('cls')

def show_company_stock_info(stock_number):
    realtime_stock = RealtimeStock(stock_number)
    dic_stock = realtime_stock.real
    print "Company Name:" +  dic_stock.get('name')
    print "Get Data Time:" + dic_stock.get('time')
    print "Up/Down:" + dic_stock.get('range')
    print "High:" + dic_stock.get('h')
    print "Low:" + dic_stock.get('l')

def show_company_stock_info_by_timeDelay(stock_number_array, delay , times):   
    for i in range(times):
        for stock_number in stock_number_array:            
            show_company_stock_info(str(stock_number))
            print "============================"
        time.sleep(delay)
        clear()


target_stock_arrar = [2498,3454]
show_company_stock_info_by_timeDelay(target_stock_arrar, 60, 60)


#print dic_stock.get('crosspic')
#stock = Stock('2498')         
#print stock.moving_average(1)   

