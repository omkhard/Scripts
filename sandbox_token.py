import requests
import json
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
USER = "devnetuser"
PASS = "Cisco123!"
requests.packages.urllib3.disable_warnings()
postreq = requests.post(url,auth=(USER,PASS))
token  = json.loads(postreq.text)['Token']
print(token)