import requests

url = 'http://localhost:3000/api'

i = input("what is ur name: ");
correct_payload = {'i': i}

r = requests.post(url, data=correct_payload)
print(r.text)
