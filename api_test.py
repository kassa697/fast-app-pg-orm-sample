import requests
import json
from datetime import datetime

def main():
  print("start")
  url = "http://localhost:8000/contacts"
  cur_date = datetime.now().isoformat()
  body = {
    "id": 1,
    "name": "kasa",
    "email": "test@test.com",
    "url": "http://test.tset.tse",
    "gender": 2,
    "message": "this is message",
    "is_enabled": True,
    "created_at": cur_date
  }

  res = requests.post(url, json.dumps(body))
  print(res.json())

if __name__ == "__main__":
  main()