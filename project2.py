from urllib
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/List_of_Indian_people_by_net_worth'

http = urllib3.PoolManager()

r = http.request('GET', 'https://en.wikipedia.org/wiki/List_of_Indian_people_by_net_worth')

soup = BeautifulSoup(r.data, 'lxml')

print(soup.title)

print("title:" ,soup.title.string)

print(soup.a)


#print(soup.find_all('a'))
all_table = soup.find_all('table')

#print(all_table)
our_table = soup.find('table', class_= 'wikitable sortable')

#print(our_table)
table_links = our_table.find_all('a')

#print(table_links)
billionaires = []
for URL in table_links: 
   billionaires.append(URL.get('title')) 
   print(billionaires) 

   #Convert the list into a dataframe
import pandas as pd
df = pd.DataFrame(billionaires)
print(df) 

   #To save the data into an excel file
writer = pd.ExcelWriter('indian_billionaires.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='List')
writer.save()
df1= pd.read_excel('indian_billionaires.xlsx')
print(df1)
df = pd.DataFrame({'billionaires':billionaires})
df.to_csv('names.csv', index=False, encoding='utf-8')

import json
with open('json_billionaires.txt', 'wt') as outfile: 
  json.dump(billionaires, outfile)
