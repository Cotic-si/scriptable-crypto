import requests
from bs4 import BeautifulSoup
import os
import json
import datetime

cryptos_url = 'https://finance.yahoo.com/losers/'
cryptos_response = requests.get(cryptos_url)
cryptos_page = BeautifulSoup(cryptos_response.text, 'html.parser')
cryptos_table = cryptos_page.find('tbody')
crypto_rows = cryptos_table.find_all('tr')

result_json_content = {}
result_json_content['timestamp'] = datetime.datetime.now().strftime('%c')
result_json_content['cryptos'] = []

for crypto_row in crypto_rows:
  cells = crypto_row.find_all('td')
  ticker = cells[0].find('a').string
  name = cells[1].text
  change = cells[4].find('span').string
  result_json_content['cryptos'].append({
    'ticker': ticker,
    'name': name,
    'change': change
  })

cryptos_json_filename = 'docs/result.json'
if os.path.exists(cryptos_json_filename):
  os.remove(cryptos_json_filename)

with open(cryptos_json_filename, 'a') as cryptos_json_file:
  json.dump(result_json_content, cryptos_json_file)
