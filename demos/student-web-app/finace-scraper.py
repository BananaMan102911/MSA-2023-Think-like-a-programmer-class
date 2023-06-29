import requests
import time
from bs4 import BeautifulSoup

def export_data(list_of_stocks):
    export_file = open("stock.csv", "w")
    #write a header row in the csv file
    header_row = ""
    for key in list_of_stocks[0]:
        header_row += key+","
    export_file.write(f"{header_row}\n")

    #loop through list of stocks
    for stock in list_of_stocks:
        stock_record = ""        
        #write stock indicators to the file
        for indicator, value in stock.items():
            stock_record += value + ","
        #write record to file
        export_file.write(f"{stock_record}\n")
    
    export_file.close()
    
    return

def main():
    list_of_stock_dictionaries = []
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    
    symbols_list = ["GOOGL", "IBM", "SBUX", "AMC", "NFLX", "TSLA", "BA"]
   
    for symbol in symbols_list:
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'
        
        #request the page
        response = requests.get(url, headers = headers)

        #parse html and create a baeutifulsoup object
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Requesting data for {symbol} stock")
        
        stock_dictionary = {}

        counter = 1
        #loop through the cell in the table
        for cell in soup.find_all('td'):
            #odd iterations are keys. Set key on odd number iterations
            if counter % 2 != 0:
                
                key = cell.text
            else:
                #enter key, value in to the dictionary on even iterations
                stock_dictionary[key] = cell.text
                
            #increment counter
            counter += 1
        list_of_stock_dictionaries.append(stock_dictionary)
        #time.sleep(2)
    
    export_data(list_of_stock_dictionaries)


main()
