from pandas_datareader import data, wb
def Adj_Close(tickers,start,end,path):
    #Download Data
    data_comp=data.DataReader(tickers,'yahoo',start,end)
    data_comp_Close=data_comp['Adj Close']
    data_comp_Close.to_csv(path)
##Input
tickers_L=[]
n=int(input('Please enter The number of the companies you want to download them Data:'))
for i in range(n):
    tick=input("input symbol:")
    tickers_L.append(tick)
start_time=input("Input the date you want start download data un format Y-M-D: ")
end_time=input("Input the date you want end download data un format Y-M-D: ")
path=input("Input where you want save the data:")
Adj_Close(tickers_L,start_time,end_time,path)