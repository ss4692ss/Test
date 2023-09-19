import json
import os
import pandas
import requests
import time


if not os.path.exists("json_file"):
	os.mkdir("json_file")

access_point = "https://api.github.com"


f = open("Token", "r")
Token = f.read()
f.close()

id_list = pandas.read_csv("seed.csv")
id_list = id_list['IDS']

github_session = requests.Session()
github_session.auth = ("ss4692ss", Token)

response_text = github_session.get(access_point + "/rate_limit").text
print(json.loads(response_text))


for user_id in id_list:
	file_name = "json_file/" + user_id + ".json"
	if os.path.exists(file_name):
			print("File_exists:", user_id)
	else:
		try:
			


			print(user_id)

			response_text = github_session.get(access_point + "/users/" + user_id).text

			json_text = json.loads(response_text)

			f = open(file_name + ".temp", "w")
			f.write(json.dumps(json_text))
			f.close()

			os.rename(file_name + ".temp", file_name)
		    
		except Exception as e:
		      		print(e)

		time.sleep(5)












