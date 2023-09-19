import json
import pandas
import os



if not os.path.exists("parse_file"):
	os.mkdir("parse_file")

dataset = pandas.DataFrame()

json_file_name = "json_file/emilk.json"

f = open(json_file_name, "r")
json_data = json.load(f)
f.close()

# print(json_data)

ghid = json_data['login']
gh_number_id = json_data['id']
# plan_name = json_data['plan']['name']
updated_at = json_data['updated_at']
followers = json_data['followers']

print(ghid)

print(gh_number_id)

# print(plan_name)

print(updated_at)
print(followers)