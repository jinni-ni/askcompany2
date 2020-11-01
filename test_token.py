import requests
#TOKEN = '4e4546ab8b1aed987025758115d5311ffdd96bd5'
JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImtpbXNqIiwiZXhwIjoxNjA0MjM3MDE4LCJlbWFpbCI6IiJ9.Ses7NOZfj4uQZ4SxjbPFIiHHvmJSX7LPev6_Na3WIok'



headers = {
    #'Authorization' : f'Token {TOKEN}', # Token 인증
    'Authorization' : f'JWT {JWT_TOKEN}', # JWT 인증
}
# eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImtpbXNqIiwiZXhwIjoxNjA0MjM2NjQxLCJlbWFpbCI6IiJ9

res = requests.get('http://localhost:8000/post/1', headers=headers)

print(res.json())
