from bs4 import BeautifulSoup as bs
import requests

def get_logintoken(session: requests.Session, url: str) -> str:
  response = session.get(url)
  soup = bs(response.text, 'html.parser')
  return soup.find('input', attrs={'name': 'logintoken'})['value']

def clamp(num, lower_limit, upper_limit):
  if (num < lower_limit):
    return lower_limit
  elif (num > upper_limit):
    return upper_limit
  
  return num
    