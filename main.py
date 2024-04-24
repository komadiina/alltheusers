import sys
import requests

sys.path.insert(0, './src')
from login import login
from scrub import scrub
import utils

if __name__ == '__main__':
  session: requests.Session = login()
  
  if session != None:
    start = int(input("Starting user id (default = 1): "))
    end = int(input("Final user id (default = 99999): "))
    delay = float(input("Request delay (default/minimum = 1.0): "))
    
    utils.clamp(delay, 1.0, 60.0)
    active_users = scrub(session, start, end, delay)
    
    for (id, fullname) in active_users:
      print(f"[{fullname}] - {id}")
  else:
    exit(0x0F)