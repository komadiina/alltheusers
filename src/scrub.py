import requests
import time

from bs4 import BeautifulSoup as bs
import signal
import json
import codecs
import sys
import datetime

users = []
def signal_saveusers(signal, frame):
  with codecs.open(
    f'./saved/users_{datetime.datetime.now()}.json'.replace(' ', '_'), 
    'w', 
    'utf-16') as f:
    json.dump(users, f, ensure_ascii=False, indent=4)
    
  print(f"Saved {len(users)} users, exiting...")
  sys.exit(0)
  
signal.signal(signal.SIGINT, signal_saveusers)

def scrub(session: requests.Session, start_id: int = 0, user_limit: int = 99_999, delay: float = 3.0) -> list:
  users.clear()
  baseUrl = "https://el.etfbl.net/user/profile.php?id="
  
  for id in range(start_id, user_limit):
    time.sleep(delay)
    
    reqUrl = f"{baseUrl}{id}"
    response = session.get(reqUrl)
    
    print(f"GET: {reqUrl}, STATUS: {response.status_code}")
    
    if response.status_code == 200:
      if response.text.find("Ovaj korisnički nalog je obrisan") != -1 or response.text.find("Neispravan korisnik") != -1:
        continue
      else:
        print(f"User found: {id}")
        
        soup = bs(response.text, 'html.parser')
        divs = soup.find_all('div', class_='page-header-headings')
        
        for div in divs:
          h1_elems = div.find_all('h1')
          for h1 in h1_elems:
            users.append({'id': id, 'name': h1.text})
  
  return users