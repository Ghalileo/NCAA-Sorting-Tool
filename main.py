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

# Access to Json Data
f = open('CA.json')
s = open ('TX.json')

# Covert json to python readible
cali = json.load(f)
texas = json.load(s)

<<<<<<< HEAD
# Creates file to post response data 
with open ('res.csv', 'w', newline="") as tex:
# Creates headers for CSV file
    fieldnames = ["TXHOME", "TXAWAY", "TXLOCATION", "UCLAHOME","UCLAAWAY","UCLALOCATION"]
# Posts CSV file to header
=======
cali_df = pd.read_json('CA.json')
tex_df = pd.read_json('TX.json')

with open ('sample.csv', 'w', newline="") as tex:
    fieldnames = ["TXHOME", "TXAWAY","UCLAHOME","UCLAAWAY"]
>>>>>>> 2ca3ff18e85a594086769f2618f2c3f8a527ce31
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