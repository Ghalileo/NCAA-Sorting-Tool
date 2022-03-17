from urllib import response
import requests
import time
import json
import pandas as pd
from decouple import config
import csv

# API_key = config("THE_API_KEY")
# url = 'https://api.sportsdata.io/v3/cbb/scores/json/Games/2022?key={API_key}'

# col = pd.read_csv("data.csv")

# teams = list(col.columns)

# print(teams)

f = open('CA.json')
s = open ('TX.json')


cali = json.load(f)
texas = json.load(s)

for i, j in zip(cali, texas ):
    with open ('USCLAHOME.csv', 'a') as cali:
        cali.write(i["HomeTeam"]) and cali.write("\n")
    with open ('USCLAAWAY.csv', 'a') as cali:
        cali.write(i["AwayTeam"]) and cali.write("\n")
    with open ('TXHOME.csv', 'a') as tex:
        tex.write(j["HomeTeam"]) and tex.write("\n")
    # with open ('TXAWAY.csv', 'a') as tex:
        # fieldnames = ["TXHOME", "TXAWAY"]
        # writer = csv.DictWriter(tex, fieldnames=fieldnames)
        # writer.writeheader()
        # writer.writerow(i["HomeTeam"])
        # tex.write(j["AwayTeam"]) and tex.write("\n")
    # with open ('UCLAID.csv', 'a') as cali:
    #     cali.write(str(i["Stadium"])) and cali.write("\n")    
    # with open ('TXID.csv', 'a') as tex:
    #     tex.write(str(j["Stadium"])) and tex.write("\n")   



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