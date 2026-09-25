import requests as rq
import pytest
import re
import sys
from datetime import date
from datetime import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
def streamtext(txt: str, delay: float =0.015):
  for char in txt:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()
  return ""


def dat():
 while True:
   dt=input(streamtext("Please input the date of which you'd like to start the price from in the YYYY-MM-DD form or press enter to do today's date")).strip()

   if not dt:
    dt=date.today()
    dt2=date.today()
   else:
        dt2=input(streamtext("Please input the date of which you'd like to end the price at in the YYYY-MM-DD form or press enter to end at today's date")).strip()
        if not dt2:
          dt2=date.today()
   today=date.today()
   datecheck=datetime.strptime(dt,r"%Y-%m-%d").date()
   datecheck2=datetime.strptime(dt2,r"%Y-%m-%d").date()
   if datecheck > today or datecheck2 > today:
     streamtext("Invalid date")
     continue 


   match=re.fullmatch("(1[0-9][0-9][0-9]|20[0-9][0-9])-(0?[1-9]|1[0-2])-(0?[1-9]|1[0-9]|2[0-9]|3[0-1])",str(dt))
   match2=re.fullmatch("(1[0-9][0-9][0-9]|20[0-9][0-9])-(0?[1-9]|1[0-2])-(0?[1-9]|1[0-9]|2[0-9]|3[0-1])",str(dt2))

   if not match or not match2:
    streamtext("Invalid Format")
    continue
   else:
     return dt,dt2

def plotcurr(X,dt,dt2,curr):
  plt.clf()
  plt.close("all")
  perDayPrices=[]
  for dict in X:
   perDayPrices.append(float(dict["rate"]))
  dailyDate=pd.date_range(start=f"{dt}",periods=len(perDayPrices),freq="D")
  plt.plot(dailyDate,perDayPrices)
  plt.xlabel("Date")
  plt.ylabel("Price")
  plt.title(f"Price of 1 USD in {curr} from {dt} to {dt2}")
  plt.savefig("Graph.png")
  streamtext("Saved as Graph.png!")

def plotgold(X,dt,dt2):
  plt.clf()
  plt.close("all")
  PerDayPrices=[]
  for dict in X:
    PerDayPrices.append(float(dict["rate"])/31.1035)
  dailyDate=pd.date_range(start=f"{dt}",periods=len(PerDayPrices),freq="D")
  plt.plot(dailyDate,PerDayPrices)
  plt.xlabel("Date")
  plt.ylabel("Price per Gram")
  plt.title(f"Gold Price per gram from {dt} to {dt2}")
  plt.savefig("Graph.png", dpi=300)
  streamtext("Saved as Graph.png!")

try:
  r=(rq.get(f"https://api.frankfurter.dev/v2/rates?base=USD")).json()
except rq.exceptions.ConnectionError:
  streamtext("No Internet Connection")
  sys.exit()
rates=[]
for dict in r:
  rates.append(dict["base"])
  break
for dict in r:
  rates.append(dict["quote"])




def main():
    (streamtext("====================================================================================",0.001))
    (streamtext("Welcome to the Currency Converter and Viewer. (Made by ZiadFazbear aka zodda1999-bit on Github) To View or Exchange, please choose:"))
    (streamtext("====================================================================================",0.001))
    choices = ["1","2","3"]
    while True:
     x=input(streamtext("1 ) Price of USD in different currencies over time \n2 ) Currency Conversion \n3 ) Gold Price Index")).strip()
     if x not in choices:
        print("Not a choice!")
     else:
      choicelist={"1":valueviewer,"2":converter,"3":gold}
      choicelist[f'{x}']()
      choice=input(streamtext("Would you like to exit?\n1 ) Yes\n2 ) No"))
      if choice=="2":
        continue
      else:
        streamtext("Goodbye!")
        sys.exit()


def valueviewer():
   plt.clf()
   plt.close("all")
   while True:
     while True:
      cur= input(streamtext("Please Type in your currency using the currency code. I.e: AED, EGP, EUR, etc.....")).upper()
      if cur not in rates:
       (streamtext("Not A Valid Currency"))
       continue
      else:
         dt1,dt2=dat()
         r=(rq.get(f"https://api.frankfurter.dev/v2/rates?base=USD&quotes={cur}&from={dt1}&to={dt2}")).json()
         if dt1==dt2:
           for dict in r:
             price=dict['rate']
           streamtext(f"The Price of 1 USD on {dt1} is {price} {cur}.")
         else:
          plotcurr(r,dt1,dt2,cur)
         break
     break




def converter():
  while True:
   cur1=input(streamtext("Please enter the currency you want to exchange in the three letter form i.e USD, AED, EGP, etc...")).upper().strip()
   if cur1 not in rates:
    streamtext("Invalid Currency")
    continue
   else:
    while True:
     try:
      cur1n=float(input(streamtext(f"Please enter the amount of {cur1}:")))
      if cur1n<0:
            raise ValueError("Number cannot be negative")
     except (TypeError, ValueError):
      streamtext("Not a number!")
      continue
     else:
        while True:
         cur2= input(streamtext("Please input the wanted currency in country code, I.e USD, EGP, AED, etc... ")).upper().strip()
         if cur2 not in rates:
           streamtext("Invalid Currency")
           continue
         else:
           r=(rq.get(f"https://api.frankfurter.dev/v2/rates?base={cur1}&quotes={cur2}")).json() #how much of cur 2 makes cur1? rates is the amount of cur2 needed to get one cur1
           for dict in r:
            price=dict["rate"]
           outprice=cur1n*float(price)
           streamtext(f"{cur1n} {cur1} will give you {outprice:.2f} {cur2}")
           return outprice,cur1n,price
           break
        break
    break

def gold():

  g=(rq.get(f"https://api.frankfurter.dev/v2/rates?base=USD")).json()
  suppcur=["USD"]
  for dicts in g:
    suppcur.append(dicts["quote"])
  while True:
    targetcurr=input(streamtext("Please input your target currency in the three letter form i.e USD, EGP, AED, etc..")).upper().strip()
    if targetcurr not in suppcur:
     streamtext("Invalid Currency")
     continue
    else:
     break
  dt,dt2=dat()
  while True:
   g=(rq.get(f"https://api.frankfurter.dev/v2/rates?base=XAU&quotes={targetcurr}&from={dt}&to={dt2}")).json()
   if dt==dt2:
    for dict in g:
     gprice=dict['rate']
     streamtext(f"Gold price on {dict['date']} is {gprice} {targetcurr} per troy ounce of 24k gold and {(float(gprice)/31.1035):.2f} {targetcurr} per gram of 24k gold")
   else:
     while True:
      choice=input(streamtext(f"Would you like to show a plot or see the direct daily values from {dt} to {dt2}?\n1 ) Plot\n2 ) Direct daily values"))
      if choice=="1":
       plotgold(g,dt,dt2)
      elif choice=="2":
       for dict in g:
        gprice=dict['rate'] #per troy ounce
        streamtext(f"Gold price on {dict['date']} is {gprice} {targetcurr} per troy ounce of 24k gold and {(float(gprice)/31.1035):.2f} {targetcurr} per gram of 24k gold",delay=0.00001)
      else:
        print("Not a choice!")
        continue
      break
   break


if __name__=="__main__":
 main()
