from dotenv import load_dotenv
import os
import requests

from scrub import scrub
import utils

def login() -> requests.Session:
  load_dotenv()

  login_url = "https://el.etfbl.net/login/index.php"
  session = requests.Session()

  payload = {
    'username': os.getenv("USERNAME"),
    'password': os.getenv("PASSWORD"),
    'logintoken': utils.get_logintoken(session, login_url)
  }

  response = session.post(login_url, data=payload)
  
  if (response.status_code == 200):
    print("[OK] Logged in successfully.")
    return session
  else:
    print("[!] Unable to login.")
    return None