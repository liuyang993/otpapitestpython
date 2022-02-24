import requests
import json

url = "https://otpapi.worldhubcom.com/api/mcotp/send"

payload = json.dumps({
  "to": "62967888001",
  "length": 4,
  "tag": "123",
  "timeout": 300
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic writeyourauthcodehere'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
