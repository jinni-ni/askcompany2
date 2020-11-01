import requests
TOKEN = '4e4546ab8b1aed987025758115d5311ffdd96bd5'

headers = {
    'Authorization' : f'Token {TOKEN}',
}

res = requests.get('http://localhost:8000/post/1', headers=headers)

print(res.json())
