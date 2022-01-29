import os
import csv
import requests
from bs4 import BeautifulSoup
from save import save_to_file

os.system("clear")
alba_url = "http://www.alba.co.kr"



job_list = []


def extract_company(link, name):
  result = requests.get(link)
  soup = BeautifulSoup(result.text, "html.parser")
  main = soup.find('div', {'id': 'NormalInfo'}).find('table')
  jobs = main.find('tbody').find_all('tr', {'class': ''})
  for job in jobs:
    job_list.append(extract_attribute(job))
  print(job_list)
  return {
    'name': name,
    'jobs': job_list
  }

def extract_attribute(html):
  job = []
  if (html.find('td', {'class': 'local'}) is None or html.find('td', {'class': 'title'}) is None or
  html.find('td', {'class': 'data'}) is None or
  html.find('td', {'class': 'pay'}) is None or
  html.find('td', {'class': 'regDate'}) is None):
    pass
  else: 
    try:
      place = html.find('td', {'class': 'local'}).get_text(strip=True).replace('&nbsp;', ' ')
      job.append(place)
    except AttributeError:
      job.append('')
    try:
      title = html.find('td', {'class': 'title'}).find('a').find('span', {"class": "company"}).get_text(strip=True)
      job.append(title)
    except AttributeError:
      job.append('')
    try:
      time = html.find('td', {'class': 'data'}).find('span', {"class": "time"}).get_text(strip=True)
      job.append(time)
    except AttributeError:
      job.append('')
    try:
      hour = html.find('td', {'class': 'pay'}).find('span', {'class': 'payIcon'}).get_text()
      amount = html.find('td', {'class': 'pay'}).find('span', {'class': 'number'}).get_text()
      job.append(hour+amount)
    except AttributeError:
      job.append('')
    try:
      post_time = html.find('td', {'class': 'regDate'}).get_text()
      job.append(post_time)
    except AttributeError:
      job.append('')
  return job


def main_work():
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  main = soup.find('div', {'id': 'MainSuperBrand'}).find('ul', {'class': 'goodsBox'})
  companies = main.find_all('li')
  for company in companies:
    anchor = company.find('a')
    # link = anchor.get('href')
    # URL = f"{alba_url}{link}"
    if anchor.find('span', {'class': 'company'}): 
      link = anchor.get('href')
      name = anchor.find('span', {'class': 'company'}).get_text()
      print(link) 
      print(name)
      one_company = extract_company(link, name)
      save_to_file(one_company)
    else:
      pass
    # passdown(link)

main_work()














# result = requests.get(alba_url)
# soup = BeautifulSoup(result.text, "html.parser")
# main = soup.find('ul', {'class': 'goodsBox'})
# companies = main.find_all('li')
# for company in companies:
#   anchor = company.find('a')
#   link = anchor.get('href')
#   URL = f"{alba_url}{link}"
#   print(URL)
#   if anchor.find('span'): 
#     name = anchor.find('span', {'class': 'company'}).get_text()
#     print(name)
#   else:
#     pass
  # passdown(link)