from urllib import response
import requests
import time
import json
import pandas as pd
from decouple import config
import csv
import openpyxl
from openpyxl.styles import Font, Color
# API_key = config("THE_API_KEY")
# url = 'https://api.sportsdata.io/v3/cbb/scores/json/Games/2022?key={API_key}'

# col = pd.read_csv("data.csv")

# teams = list(col.columns)

# print(teams)

# Access to Json Data Files
f = open('CA.json')
s = open ('TX.json')

# Covert json to python readible
cali = json.load(f)
texas = json.load(s)

cali_df = pd.read_json('CA.json')
tex_df = pd.read_json('TX.json')

data_df = pd.read_csv('res.csv')

tmp=[]
counter=0
for i,tx_home in enumerate(data_df['TXHOME'].to_list()):
    print('new first loop',i,len(tmp))
    if tx_home != 'TX':
        j=0
        for j,ucla in enumerate(data_df['UCLAAWAY'].to_list()):
         #   print(j)
            if tx_home==ucla:
                counter+=1
                print(f'inner append {counter}')
                tmp.append(tx_home)
                print('Found a match',tx_home, ucla,'Away Team index',j,'Home Team index',i)
                break
            elif j == len(data_df['UCLAAWAY'].to_list())-1:
                tmp.append('')
                print('no match')
    else:
        tmp.append('')



workbook = openpyxl.load_workbook('test.xlsx')
worksheet = workbook['Sheet1']
tmp1=data_df['TXHOME_TO_UCLAAWAY_HITS'].to_list()
tmp2=data_df['TXAWAY_TO_UCLAAWAY_HITS'].to_list()
tmp3=data_df['TXAWAY_TO_UCLAHOME_HITS'].to_list()
tmp4=data_df['TXHOME_TO_UCLAHOME_HITS'].to_list()
cnt=0
for a,b,c,d in zip(tmp1,tmp2,tmp3,tmp4):
    print(a,b,c,d)
    if a != '':
        print('fuckin',a)
        col = 'A'
        row = cnt+2
        row = str(row)
        val = a
        placement=col+row
        worksheet[placement]=val
        worksheet[placement].font = Font(color='FF0000',bold=True)

        
    if b != '':
        print('fuckin',b)
        col = 'B'
        row = cnt+2
        row = str(row)
        val = b
        placement=col+row
        worksheet[placement]=val
        worksheet[placement].font = Font(color='FF0000',bold=True)

        
    if c != '':
        print('fuckin',c)
        col = 'C'
        row = cnt+2
        row = str(row)
        val = c
        placement=col+row
        worksheet[placement]=val
        worksheet[placement].font = Font(color='FF0000',bold=True)

        
    if d != '':
        print('fuckin',d)
        col='D'
        row = cnt+2
        row = str(row)
        val = d
        placement=col+row
        worksheet[placement]=val
        worksheet[placement].font = Font(color='FF0000',bold=True)
    
    cnt+=1
workbook.save(filename='font_test2.xlsx')      


tmp=[]
for row in worksheet['TXAWAY_TO_UCLAHOME_HITS']:
    print(row)
counter=0
for i,tx_home in enumerate(data_df['TXHOME'].to_list()):
    print('new first loop',i,len(tmp))
    if tx_home != 'TX':
        j=0
        for j,ucla in enumerate(data_df['UCLAHOME'].to_list()):
         #   print(j)
            if tx_home==ucla:
                counter+=1
                print(f'inner append {counter}')
                tmp.append(tx_home)
                print('Found a match',tx_home, ucla,'Away Team index',j,'Home Team index',i)
                break
            elif j == len(data_df['UCLAAWAY'].to_list())-1:
                tmp.append('')
                print('no match')
    else:
        tmp.append('')

data_df['TXHOME_TO_UCLAHOME_HITS']=tmp

data_df.to_excel('test.xlsx',index=False)




with open ('sample.csv', 'w', newline="") as tex:
    fieldnames = ["TXHOME", "TXAWAY","UCLAHOME","UCLAAWAY"]
    writer = csv.DictWriter(tex, fieldnames=fieldnames)
# Initiates function
    writer.writeheader()
# For loop to prepare the data from JSON to post to CSV file
    for i, j in zip(texas, cali):
# Writes data to CSV
        writer.writerow({'TXHOME': i['HomeTeam'], 'TXAWAY': i['AwayTeam'], 'TXLOCATION': str(i['Stadium']['City']),'UCLAHOME': j['HomeTeam'], 'UCLAAWAY': j['AwayTeam'], 'UCLALOCATION': str(j["Stadium"]["City"])})
        # if i["HomeTeam"] == j["HomeTeam"] or i["HomeTeam"] == j["AwayTeam"]:
        #    with open('Matches.txt', 'a') as match:
        #     match.write(i) and match.write("\t Matches \n")
        # else: 
        #     print("no matches")


# file_path = str(input('Enter File Path: '))
# domain_CSV = pandas.read_csv((file_path))

# Urls = domain_CSV['Teams'].tolist()

# for i in range (url=url):
#     parameters = {'apikey': API_key, 'resource': i}
#     response = requests.get(url)
#     json_response = json.loads(response.text)
#     if json_response['HomeTeam'] == "TX":
#         with open('Matches.txt', 'a') as match:
#             match.write(i) and match.write("\t Matches \n")
#     else:
#         with open ('Nothing.txt', 'a') as Nothing:
#             Nothing.write(i) and Nothing.write("\t No Matches \n")

#     time.sleep(20)

# response = requests.get(url)
# print(response.json())