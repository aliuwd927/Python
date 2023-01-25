import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,rain,showers'
response = requests.get(url)
response_code = response.status_code
data = response.json()

if response_code == 200:
    for details in data:
        print(details)
else:
    print('error')
