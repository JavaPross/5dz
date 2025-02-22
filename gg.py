import requests

пп = "https://fake-json-api.mock.beeceptor.com/"
response = requests.get(пп)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Ошибка {response.status_code}")
if пп:
    print('Response OK')
else:
    print('Response Failed')
    
try:
    response = requests.get(пп, timeout=5)
    response.raise_for_status() 
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Ошибка: {e}")

