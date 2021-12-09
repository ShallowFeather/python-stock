import requests
import time
import json
import csv
print("-----------------------------------------")
print("Search Taiwan Stock oAo")
print("Input the Year and Month like (2021/12)")
print("-----------------------------------------")

print("Input Start Date: ", end = "")
StartDate = input()
print("Input End Date: ", end = "")
EndDate = input()
print("Input No: ", end = "")
ID = input()
print("File Name: ", end = "")
FileName = input()
StartDate = StartDate.split('/')
EndDate = EndDate.split('/')

Sy = StartDate[0]
Sm = StartDate[1]
Ey = EndDate[0]
Em = EndDate[1]

if(Sy > Ey or (Sy == Ey and Sm > Em)):
    exit()

chk = (Sy == Ey)

for year in range(int(Sy), int(Ey) + 1):
    for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        if(year == int(Ey) and int(month) > int(Em)):
            exit()
        owo = False
        if(chk and month == Sm):
            chk = False
        if(chk and month != Sm):
            owo = True
        if(owo == True):
            continue
        if(len(str(month)) == 1):
            url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=" + str(year) + str(0) +str(month) + "01" + "&stockNo=" + str(ID)
        else :
            url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=" + str(year) + str(month) + "01" + "&stockNo=" + str(ID)
        response = requests.get(url)
        date = response.json()
        print(month)
        with open(FileName + ".csv", 'a') as csvfile:
            writer = csv.writer(csvfile)
            for Data in date.get('data'):
                writer.writerow(Data)
        time.sleep(5.5)

print("Finish")
