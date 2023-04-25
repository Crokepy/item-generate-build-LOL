# test file for creation files for investigation
import requests
import json

response = requests.get("http://ddragon.leagueoflegends.com/cdn/13.8.1/data/es_MX/item.json")
data = json.dumps(response.json(),  indent=4)


f = open("orc.json", "w")

f.write(data)
print("file write complete")

f.close()