import pandas as pd
import numpy as np
import bs4
import requests
from bs4 import BeautifulSoup
from time import time, sleep
import tickers
from os import system, name


def clear():
	___ = system('clear')



class bcolors:
    GREEN = '\033[92m' #GREEN
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


def getStockData(ticker):
	up = True
	r = requests.get(f"https://finance.yahoo.com/quote/{ticker}/")
	soup = bs4.BeautifulSoup(r.text, "lxml")
	price = soup.find('span', {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
	try:
		soup.find('span', {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"})
		percentChange = soup.find('span', {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"}).text
		up = False 
		#__, percentChange = percentChange.split('', 1)
	except:
		percentChange = soup.find('span', {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"}).text
		#__, percentChange = percentChange.split('', 1)
		up = True

	return price, percentChange, up


def getCryptoData(name):
	up = True
	r = requests.get(f"https://coinmarketcap.com/currencies/{name}/")
	soup = bs4.BeautifulSoup(r.text, "lxml")
	ticker = soup.find('small', {"class": "nameSymbol"}).text
	price = soup.find('div', {"class": "imn55z-0 hCqbVS price"}).find('div').text
	price = price.replace('$', '')
	price = price.replace(',', '')
	try:
		soup.find('span', {"class": "icon-Caret-down"})
		percentChange = soup.find('span', {"class": "sc-15yy2pl-0 feeyND"}).text
		up = False
	except:
		percentChange = soup.find('span', {"class": "sc-15yy2pl-0 gEePkg"}).text
		up = True
	amountChange = soup.find('div', {"class": "sc-16r8icm-0 fmPyWa"}).find('table').find('tbody').find_all('tr')[1].find('td').find('span').text
	amountChange = amountChange.replace('$', '')
	amountChange = amountChange.replace(',', '')
	amountChange = round(float(amountChange), 2)
	return ticker, price, percentChange, amountChange, up


def loading():
	print("[     ]", end='\r')
	sleep(24 - time() % 24)
	print("[=    ]", end='\r')
	sleep(24 - time() % 24)
	print("[==   ]", end='\r')
	sleep(24 - time() % 24)
	print("[===  ]", end='\r')
	sleep(24 - time() % 24)
	print("[==== ]", end='\r')
	sleep(24 - time() % 24)
  

lastValues = {}
for i in tickers.stockTickers:
    lastValues[i] = 0
for i in tickers.cryptoNames:
    lastValues[i] = 0

greenOrRed = 'GREEN'
boolin = True
while boolin == True:
	clear()
	print("STOCKS:")

	for ticker in tickers.stockTickers:

		price, percentChange, up = getStockData(ticker)

		if up == True:
			greenOrRed = bcolors.GREEN
		else:
			greenOrRed = bcolors.RED

		print(f"{ticker}: ${price}" + f"     {greenOrRed}⬤{bcolors.RESET} " + f"{percentChange}")
		lastValues.update({ticker: price})

	print("\nCRYPTO:")
	for name in tickers.cryptoNames:

		ticker, price, percentChange, amountChange, up = getCryptoData(name)

		if up == True:
			greenOrRed = bcolors.GREEN
		else:
			greenOrRed = bcolors.RED

		print(f"{ticker}: ${price}" + f"     {greenOrRed}⬤{bcolors.RESET} " + f"{amountChange}  "     + f"({percentChange})")
		lastValues.update({name: price})

	loading()



