# priceWatcher
 Stock and Crypto Price Tracker on Terminal


<img width="326" alt="Screen Shot 2021-09-07 at 12 51 45 PM" src="https://user-images.githubusercontent.com/13202373/132382923-953eaf23-44a1-49fc-9cfe-2e2667ae6384.png">


HOW TO UPDATE STOCK/CRYPTO LIST:
1. Go into "tickers.py"
2. Add any stocks you want to the stockTickers list
3. Add any crypto you want to the cryptoNames list
4. Enjoy :)



HOW TO TURN THIS INTO A DESKTOP APP ON MAC:

1. Create a shell script with the following: (MAKE SURE YOU HAE THE RIGHT LOCATION FOR THE FILE THAT YOU ARE CD ing TO)
-----------------------------

#!/bin/sh

cd ~/Desktop/priceWatcher



python priceWatcher.py

-----------------------------

2. Save this as priceWatcher.command (you can use another name but make sure to do the .command ending)

3. Go into your terminal type: chmod u+x priceWatcher.command

ALL SET!

(optional)
4. To change the icon: right click/copy an image --> right click command script --> more info --> click icon in top left --> paste --> run

Icon I Use:
![image](https://user-images.githubusercontent.com/13202373/132383020-1ff6bf86-9644-41ae-94f3-36a93fac6e33.png)
