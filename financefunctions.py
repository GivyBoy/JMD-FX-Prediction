from datetime import date
import pandas as pd
import quantstats as qs


def get_jse_data(ticker, start_date = '2000-01-01', end_date = date.today()):
    """
    This aim of this function is to scrape stock data from the Jamaica Stock Exchange. 
    
    ticker: Enter the ticker of the stock you wish to analyze
    start_date: in the format 'yyyy-mm-dd', enter the starting date if the data you want.
    end_date: The default end date is today (yes, I coded it to be dynamic). If you want a special date, enter that date in the format 'yyy-mm-dd'.
    
    """
    
    ticker = ticker.upper() #Ensures that all the letters of the ticker are capitalized. This is to ensure that the code doesn't get any errors later on, since tickers are normally all caps.
    
    #Catches an error if the user forgets to input the start date and uses of the fault value of January 1, 2017.
    if start_date:
        start_date = pd.to_datetime(start_date, format='%Y%m%d', errors='ignore') #formats the date
    else:
        start_date = '2000-01-01'
    
    #same as above 
    if end_date:
        end_date = pd.to_datetime(end_date, format='%Y%m%d', errors='ignore') #formats the date
    else:
        end_date = date.today()
    
    data = pd.read_html(f"""https://www.jamstockex.com/market-data/download-data/price-history/{ticker}/{start_date}/{end_date}""") #The Jamaica Stock Exchange has a pattern with how they store their data. I found that pattern, as such, I'm leveraging it. This line scrapes the data from the JSE and tries to return it as a dataframe.
    
    data = data[0] #The data wasn't returned as a dataframe, instead, it was returned as an array with one element: the data. This line indexes into the array amd accesses the data.
    
    del data['Unnamed: 0'] #deletes an unnecessary row
    
    data.index = data['Date'] #assigns the "Date" column as the index
    
    del data['Date'] #deletes the row
    
    data.index = pd.to_datetime(data.index) #transforms the dates into a datetime object. Most libraries need the index to be a datetime object, so that's why this was done.
    
    for i, b in enumerate(data.columns.values):
        data.columns.values[i] = b.replace(" ($)", "").replace("  ", " ") #The titles of the columns aren't formatted properly, so these lines correct that.
        
    data = data.dropna(axis=1) #removes all the columns that don't have useful values
    
    return data #returns the datarame to the user 

####################################################################################################

def get_jse_data_daily_returns(ticker, start_date = '2000-01-01', end_date = date.today()):
    """
    This aim of this function is to scrape stock data from the Jamaica Stock Exchange. 
    
    ticker: Enter the ticker of the stock you wish to analyze
    start_date: in the format 'yyyy-mm-dd', enter the starting date if the data you want.
    end_date: The default end date is today (yes, I coded it to be dynamic). If you want a special date, enter that date in the format 'yyy-mm-dd'.
    
    """
    
    ticker = ticker.upper() #Ensures that all the letters of the ticker are capitalized. This is to ensure that the code doesn't get any errors later on, since tickers are normallt all caps.
    
    #Catches an error if the user forgets to input the start date and uses of the fault value of January 1, 2017.
    if start_date:
        start_date = pd.to_datetime(start_date, format='%Y%m%d', errors='ignore') #formats the date
    else:
        start_date = '2000-01-01'
    
    #same as above 
    if end_date:
        end_date = pd.to_datetime(end_date, format='%Y%m%d', errors='ignore') #formats the date
    else:
        end_date = date.today()
    
    data = pd.read_html(f"""https://www.jamstockex.com/market-data/download-data/price-history/{ticker}/{start_date}/{end_date}""") #The Jamaica Stock Exchange has a pattern with how they store their data. I found that pattern, as such, I'm leveraging it. This line scrapes the data from the JSE and tries to return it as a dataframe.
    
    data = data[0] #The data wasn't returned as a dataframe, instead, it was returned as an array with one element: the data. This line indexes into the array amd accesses the data.
    
    del data['Unnamed: 0'] #deletes an unnecessary row
    
    data.index = data['Date'] #assigns the "Date" column as the index
    
    del data['Date'] #deletes the row
    
    data.index = pd.to_datetime(data.index) #transforms the dates into a datetime object. Most libraries need the index to be a datetime object, so that's why this was done.
    
    for i, b in enumerate(data.columns.values):
        data.columns.values[i] = b.replace(" ($)", "").replace("  ", " ") #The titles of the columns aren't formatted properly, so these lines correct that.
        
    data = data.dropna(axis=1) #removes all the columns that don't have useful values
    
    data = data['Close Price'] 
    data = data.pct_change()
    
    return data #returns the datarame to the user 

########################################################################################

def get_stock_report(ticker, start_date = '2000-01-01', end_date = date.today()):
    """
    This aim of this function is to scrape stock data from the Jamaica Stock Exchange and then give a report on the stock's performance and visualize some key metrics about the stock: Cumulative Return, Drawdown and Daily Return. 
    
    ticker: Enter the ticker of the stock you wish to analyze
    start_date: in the format 'yyyy-mm-dd', enter the starting date if the data you want.
    end_date: The default end date is today (yes, I coded it to be dynamic). If you want a special date, enter that date in the format 'yyy-mm-dd'.
    
    """
    
    ticker = ticker.upper() #Ensures that all the letters of the ticker are capitalized. This is to ensure that the code doesn't get any errors later on, since tickers are normallt all caps.
    
    #Catches an error if the user forgets to input the start date and uses of the fault value of January 1, 2017.
    if start_date:
        start_date = pd.to_datetime(start_date, format='%Y%m%d', errors='ignore') #formats the date
    else:
        start_date = '2000-01-01'
    
    #same as above 
    if end_date:
        end_date = pd.to_datetime(end_date, format='%Y%m%d', errors='ignore') #formats the date
    else:
        end_date = date.today()
    
    data = pd.read_html(f"""https://www.jamstockex.com/market-data/download-data/price-history/{ticker}/{start_date}/{end_date}""") #The Jamaica Stock Exchange has a pattern with how they store their data. I found that pattern, as such, I'm leveraging it. This line scrapes the data from the JSE and tries to return it as a dataframe.
    
    data = data[0] #The data wasn't returned as a dataframe, instead, it was returned as an array with one element: the data. This line indexes into the array amd accesses the data.
    
    del data['Unnamed: 0'] #deletes an unnecessary row
    
    data.index = data['Date'] #assigns the "Date" column as the index
    
    del data['Date'] #deletes the row
    
    data.index = pd.to_datetime(data.index) #transforms the dates into a datetime object. Most libraries need the index to be a datetime object, so that's why this was done.
    
    for i, b in enumerate(data.columns.values):
        data.columns.values[i] = b.replace(" ($)", "").replace("  ", " ") #The titles of the columns aren't formatted properly, so these lines correct that.
        
    data = data.dropna(axis=1) #removes all the columns that don't have useful values
    
    data = data['Close Price'] 
    data = data.pct_change()
    
    return qs.reports.basic(data)

##############################################################################################

def get_stock_report_full(ticker, start_date = '2000-01-01', end_date = date.today()):
    """
    This aim of this function is to scrape stock data from the Jamaica Stock Exchange and then give a full report on the stock's performance, with the S&P500 as a benchmark.
    
    ticker: Enter the ticker of the stock you wish to analyze
    start_date: in the format 'yyyy-mm-dd', enter the starting date if the data you want.
    end_date: The default end date is today (yes, I coded it to be dynamic). If you want a special date, enter that date in the format 'yyy-mm-dd'.
    
    """
    
    ticker = ticker.upper() #Ensures that all the letters of the ticker are capitalized. This is to ensure that the code doesn't get any errors later on, since tickers are normallt all caps.
    
    #Catches an error if the user forgets to input the start date and uses of the fault value of January 1, 2017.
    if start_date:
        start_date = pd.to_datetime(start_date, format='%Y%m%d', errors='ignore') #formats the date
    else:
        start_date = '2000-01-01'
    
    #same as above 
    if end_date:
        end_date = pd.to_datetime(end_date, format='%Y%m%d', errors='ignore') #formats the date
    else:
        end_date = date.today()
    
    data = pd.read_html(f"""https://www.jamstockex.com/market-data/download-data/price-history/{ticker}/{start_date}/{end_date}""") #The Jamaica Stock Exchange has a pattern with how they store their data. I found that pattern, as such, I'm leveraging it. This line scrapes the data from the JSE and tries to return it as a dataframe.
    
    data = data[0] #The data wasn't returned as a dataframe, instead, it was returned as an array with one element: the data. This line indexes into the array amd accesses the data.
    
    del data['Unnamed: 0'] #deletes an unnecessary row
    
    data.index = data['Date'] #assigns the "Date" column as the index
    
    del data['Date'] #deletes the row
    
    data.index = pd.to_datetime(data.index) #transforms the dates into a datetime object. Most libraries need the index to be a datetime object, so that's why this was done.
    
    for i, b in enumerate(data.columns.values):
        data.columns.values[i] = b.replace(" ($)", "").replace("  ", " ") #The titles of the columns aren't formatted properly, so these lines correct that.
        
    data = data.dropna(axis=1) #removes all the columns that don't have useful values
    
    data = data['Close Price'] 
    data = data.pct_change()
    
    return qs.reports.metrics(data, benchmark='SPY', mode="full")

####################################################################################################################

def drawdown(return_series: pd.Series):
    """Takes a time series of asset returns.
       returns a DataFrame with columns for
       the wealth index, 
       the previous peaks, and 
       the percentage drawdown
    """
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    return pd.DataFrame({"Wealth": wealth_index, 
                         "Previous Peak": previous_peaks, 
                         "Drawdown": drawdowns})

####################################################################################################################

def get_fx_rates():
    
    today = date.today()
    data = pd.read_html(f'http://www.boj.org.jm/foreign_exchange/searchfx.php?iAll=1&iUSD=1&iGBP=1&iCAD=1&iEUR=1&rate=1&strFromDate=2000-01-01&strToDate={today}&Enter=')
    fx= data[3]
    
    dates = []

    for i in range(0,len(fx), 2):
        dates.append(fx.iloc[i][0])
     
    dates=dates[::-1]
    for i in range(0,len(fx), 2):
        fx = fx.drop([i], axis=0)
        
    del fx[('Date', 'Unnamed: 0_level_1')]
    
    usd_buy = list(fx[('USD', 'BUY')])[::-1]
    usd_buy = [round(float(i), 2) for i in usd_buy]

    gbp_buy = list(fx[('GBP', 'BUY')])[::-1]
    gbp_buy = [round(float(i), 2) for i in gbp_buy]

    cad_buy = list(fx[('CAD', 'BUY')])[::-1]
    cad_buy = [round(float(i), 2) for i in cad_buy]

    eur_buy = list(fx[('EUR', 'BUY')])[::-1]
    eur_buy = [round(float(i), 2) for i in eur_buy]

    usd_sell = list(fx[('USD', 'SELL')])[::-1]
    usd_sell = [round(float(i), 2) for i in usd_sell]

    gbp_sell = list(fx[('GBP', 'SELL')])[::-1]
    gbp_sell = [round(float(i), 2) for i in gbp_sell]

    cad_sell = list(fx[('CAD', 'SELL')])[::-1]
    cad_sell = [round(float(i), 2) for i in cad_sell]

    eur_sell = list(fx[('EUR', 'SELL')])[::-1]
    eur_sell = [round(float(i), 2) for i in eur_sell]
    
    
    forex = {'USD BUY': usd_buy,
             'USD SELL': usd_sell,
             'GBP BUY': gbp_buy,
             'GBP SELL': gbp_sell,
             'CAD BUY': cad_buy,
             'CAD SELL': cad_sell,
             'EUR BUY': eur_buy,
             'EUR SELL': eur_sell
          }
    
    fx_data = pd.DataFrame.from_dict(forex)
    
    fx_data.index = dates
    
    fx_data.index = pd.to_datetime(fx_data.index.values, format='%Y%m%d', errors='ignore')
    
    fx_data = fx_data.drop(index='2020-09-03')
    
    return fx_data
###################################################################################################

today = date.today()
def get_full_fx_rates():
     
    
    data = pd.read_html(f'http://www.boj.org.jm/foreign_exchange/searchfx.php?iAll=1&iUSD=1&iGBP=1&iCAD=1&iEUR=1&rate=1&high=1&volume=1&low=1&tenday=1&all=1&strFromDate=2000-01-01&strToDate={today}&Enter=')
    
    data = data[3]
    
    date = []

    for i in range(0,len(data), 6):
        date.append(data.iloc[i][0])

    date = date[::-1]
    
    usd_buy_rates = []
    usd_buy_volume = []
    usd_buy_high = []
    usd_buy_low = []
    usd_buy_10day = []

    col = 1

    for i in range(1,len(data), 6):
        usd_buy_rates.append(round(float(data.iloc[i, col]), 2))
        usd_buy_volume.append(round(float(data.iloc[i+1, col]), 2))
        usd_buy_high.append(round(float(data.iloc[i+2, col]), 2))
        usd_buy_low.append(round(float(data.iloc[i+3, col]), 2))
        usd_buy_10day.append(round(float(data.iloc[i+4, col]), 2))

    usd_buy_rates = usd_buy_rates[::-1]
    usd_buy_volume = usd_buy_volume[::-1]
    usd_buy_high = usd_buy_high[::-1]
    usd_buy_low = usd_buy_low[::-1]
    usd_buy_10day = usd_buy_10day[::-1]
    
    
    usd_buy = {'Date': date,
               'Exchange Rate':usd_buy_rates,
               'Volume Traded':usd_buy_volume,
               'High':usd_buy_high,
               'Low':usd_buy_low,
               '10 Day MA':usd_buy_10day,
    }

    usd_buy = pd.DataFrame.from_dict(usd_buy)

    usd_buy.index = pd.to_datetime(usd_buy['Date'], format='%Y%m%d', errors='ignore')
    del usd_buy['Date']
    usd_buy = usd_buy.drop(index='2020-09-03')
    
    usd_sell_rates = []
    usd_sell_volume = []
    usd_sell_high = []
    usd_sell_low = []
    usd_sell_10day = []

    col = 2

    for i in range(1,len(data), 6):
        usd_sell_rates.append(round(float(data.iloc[i, col]), 2))
        usd_sell_volume.append(round(float(data.iloc[i+1, col]), 2))
        usd_sell_high.append(round(float(data.iloc[i+2, col]), 2))
        usd_sell_low.append(round(float(data.iloc[i+3, col]), 2))
        usd_sell_10day.append(round(float(data.iloc[i+4, col]), 2))

    usd_sell_rates = usd_sell_rates[::-1]
    usd_sell_volume = usd_sell_volume[::-1]
    usd_sell_high = usd_sell_high[::-1]
    usd_sell_low = usd_sell_low[::-1]
    usd_sell_10day = usd_sell_10day[::-1]
    
    usd_sell = {'Date': date,
               'Exchange Rate':usd_sell_rates,
               'Volume Traded':usd_sell_volume,
               'High':usd_sell_high,
               'Low':usd_sell_low,
               '10 Day MA':usd_sell_10day,
    }

    usd_sell = pd.DataFrame.from_dict(usd_sell)
    usd_sell.index = pd.to_datetime(usd_sell['Date'], format='%Y%m%d', errors='ignore')
    del usd_sell['Date']
    usd_sell = usd_sell.drop(index='2020-09-03')
    
    gbp_buy_rates = []
    gbp_buy_volume = []
    gbp_buy_high = []
    gbp_buy_low = []
    gbp_buy_10day = []

    col = 3

    for i in range(1,len(data), 6):
        gbp_buy_rates.append(round(float(data.iloc[i, col]), 2))
        gbp_buy_volume.append(round(float(data.iloc[i+1, col]), 2))
        gbp_buy_high.append(round(float(data.iloc[i+2, col]), 2))
        gbp_buy_low.append(round(float(data.iloc[i+3, col]), 2))
        gbp_buy_10day.append(round(float(data.iloc[i+4, col]), 2))

    gbp_buy_rates = gbp_buy_rates[::-1]
    gbp_buy_volume = gbp_buy_volume[::-1]
    gbp_buy_high = gbp_buy_high[::-1]
    gbp_buy_low = gbp_buy_low[::-1]
    gbp_buy_10day = gbp_buy_10day[::-1]
    
    gbp_buy = {'Date': date,
               'Exchange Rate':gbp_buy_rates,
               'Volume Traded':gbp_buy_volume,
               'High':gbp_buy_high,
               'Low':gbp_buy_low,
               '10 Day MA':gbp_buy_10day,
    }

    gbp_buy = pd.DataFrame.from_dict(gbp_buy)

    gbp_buy.index = pd.to_datetime(gbp_buy['Date'], format='%Y%m%d', errors='ignore')
    del gbp_buy['Date']
    gbp_buy = gbp_buy.drop(index='2020-09-03')
    
    
    gbp_sell_rates = []
    gbp_sell_volume = []
    gbp_sell_high = []
    gbp_sell_low = []
    gbp_sell_10day = []

    col = 4

    for i in range(1,len(data), 6):
        gbp_sell_rates.append(round(float(data.iloc[i, col]), 2))
        gbp_sell_volume.append(round(float(data.iloc[i+1, col]), 2))
        gbp_sell_high.append(round(float(data.iloc[i+2, col]), 2))
        gbp_sell_low.append(round(float(data.iloc[i+3, col]), 2))
        gbp_sell_10day.append(round(float(data.iloc[i+4, col]), 2))

    gbp_sell_rates = gbp_sell_rates[::-1]
    gbp_sell_volume = gbp_sell_volume[::-1]
    gbp_sell_high = gbp_sell_high[::-1]
    gbp_sell_low = gbp_sell_low[::-1]
    gbp_sell_10day = gbp_sell_10day[::-1]
    
    gbp_sell = {'Date': date,
               'Exchange Rate':gbp_sell_rates,
               'Volume Traded':gbp_sell_volume,
               'High':gbp_sell_high,
               'Low':gbp_sell_low,
               '10 Day MA':gbp_sell_10day,
    }

    gbp_sell = pd.DataFrame.from_dict(gbp_sell)
    gbp_sell.index = pd.to_datetime(gbp_sell['Date'], format='%Y%m%d', errors='ignore')
    del gbp_sell['Date']
    gbp_sell = gbp_sell.drop(index='2020-09-03')
    
    cad_buy_rates = []
    cad_buy_volume = []
    cad_buy_high = []
    cad_buy_low = []
    cad_buy_10day = []

    col = 5

    for i in range(1,len(data), 6):
        cad_buy_rates.append(round(float(data.iloc[i, col]), 2))
        cad_buy_volume.append(round(float(data.iloc[i+1, col]), 2))
        cad_buy_high.append(round(float(data.iloc[i+2, col]), 2))
        cad_buy_low.append(round(float(data.iloc[i+3, col]), 2))
        cad_buy_10day.append(round(float(data.iloc[i+4, col]), 2))

    cad_buy_rates = cad_buy_rates[::-1]
    cad_buy_volume = cad_buy_volume[::-1]
    cad_buy_high = cad_buy_high[::-1]
    cad_buy_low = cad_buy_low[::-1]
    cad_buy_10day = cad_buy_10day[::-1]
    
    cad_buy = {'Date': date,
               'Exchange Rate':cad_buy_rates,
               'Volume Traded':cad_buy_volume,
               'High':cad_buy_high,
               'Low':cad_buy_low,
               '10 Day MA':cad_buy_10day,
    }

    cad_buy = pd.DataFrame.from_dict(cad_buy)

    cad_buy.index = pd.to_datetime(cad_buy['Date'], format='%Y%m%d', errors='ignore')
    del cad_buy['Date']
    cad_buy = cad_buy.drop(index='2020-09-03')
    
    cad_sell_rates = []
    cad_sell_volume = []
    cad_sell_high = []
    cad_sell_low = []
    cad_sell_10day = []

    col = 6

    for i in range(1,len(data), 6):
        cad_sell_rates.append(round(float(data.iloc[i, col]), 2))
        cad_sell_volume.append(round(float(data.iloc[i+1, col]), 2))
        cad_sell_high.append(round(float(data.iloc[i+2, col]), 2))
        cad_sell_low.append(round(float(data.iloc[i+3, col]), 2))
        cad_sell_10day.append(round(float(data.iloc[i+4, col]), 2))

    cad_sell_rates = cad_sell_rates[::-1]
    cad_sell_volume = cad_sell_volume[::-1]
    cad_sell_high = cad_sell_high[::-1]
    cad_sell_low = cad_sell_low[::-1]
    cad_sell_10day = cad_sell_10day[::-1]
    
    cad_sell = {'Date': date,
               'Exchange Rate':cad_sell_rates,
               'Volume Traded':cad_sell_volume,
               'High':cad_sell_high,
               'Low':cad_sell_low,
               '10 Day MA':cad_sell_10day,
    }

    cad_sell = pd.DataFrame.from_dict(cad_sell)
    cad_sell.index = pd.to_datetime(cad_sell['Date'], format='%Y%m%d', errors='ignore')
    del cad_sell['Date']
    cad_sell = cad_sell.drop(index='2020-09-03')
    
    eur_buy_rates = []
    eur_buy_volume = []
    eur_buy_high = []
    eur_buy_low = []
    eur_buy_10day = []

    col = 7

    for i in range(1,len(data), 6):
        eur_buy_rates.append(round(float(data.iloc[i, col]), 2))
        eur_buy_volume.append(round(float(data.iloc[i+1, col]), 2))
        eur_buy_high.append(round(float(data.iloc[i+2, col]), 2))
        eur_buy_low.append(round(float(data.iloc[i+3, col]), 2))
        eur_buy_10day.append(round(float(data.iloc[i+4, col]), 2))

    eur_buy_rates = eur_buy_rates[::-1]
    eur_buy_volume = eur_buy_volume[::-1]
    eur_buy_high = eur_buy_high[::-1]
    eur_buy_low = eur_buy_low[::-1]
    eur_buy_10day = eur_buy_10day[::-1]
    
    eur_buy = {'Date': date,
               'Exchange Rate':eur_buy_rates,
               'Volume Traded':eur_buy_volume,
               'High':eur_buy_high,
               'Low':eur_buy_low,
               '10 Day MA':eur_buy_10day,
    }

    eur_buy = pd.DataFrame.from_dict(eur_buy)

    eur_buy.index = pd.to_datetime(eur_buy['Date'], format='%Y%m%d', errors='ignore')
    del eur_buy['Date']
    eur_buy = eur_buy.drop(index='2020-09-03')
    
    eur_sell_rates = []
    eur_sell_volume = []
    eur_sell_high = []
    eur_sell_low = []
    eur_sell_10day = []

    col = 8

    for i in range(1,len(data), 6):
        eur_sell_rates.append(round(float(data.iloc[i, col]), 2))
        eur_sell_volume.append(round(float(data.iloc[i+1, col]), 2))
        eur_sell_high.append(round(float(data.iloc[i+2, col]), 2))
        eur_sell_low.append(round(float(data.iloc[i+3, col]), 2))
        eur_sell_10day.append(round(float(data.iloc[i+4, col]), 2))

    eur_sell_rates = eur_sell_rates[::-1]
    eur_sell_volume = eur_sell_volume[::-1]
    eur_sell_high = eur_sell_high[::-1]
    eur_sell_low = eur_sell_low[::-1]
    eur_sell_10day = eur_sell_10day[::-1]
    
    eur_sell = {'Date': date,
               'Exchange Rate':eur_sell_rates,
               'Volume Traded':eur_sell_volume,
               'High':eur_sell_high,
               'Low':eur_sell_low,
               '10 Day MA':eur_sell_10day,
    }

    eur_sell = pd.DataFrame.from_dict(eur_sell)
    eur_sell.index = pd.to_datetime(eur_sell['Date'], format='%Y%m%d', errors='ignore')
    del eur_sell['Date']
    eur_sell = eur_sell.drop(index='2020-09-03')
    
    return usd_buy, usd_sell, gbp_buy, gbp_sell, cad_buy, cad_sell, eur_buy, eur_sell

##########################################################################################################################