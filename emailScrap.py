import re
import json

email_type = ""
occured = 1
emails = []
result_data = {}


def check_email(email):
    data = email
    store = data.split("@")
    new_array = store[0].split(".")
    if len(new_array) < 2:
        return "Non-Human"
    else:
        return "Human"


text = """Get 50% off on every purchase. contact marketing team at market@qq.com. Find all your linkedin
    contacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at market@qq.com"""
text = open("websiteData.txt", encoding="utf-8").read()
# Remove the comment from above text if you want to test output with website.txt

for eachData in text.split(" "):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)

for email in emails:
    occured = emails.count(email)
    email_type = check_email(email)
    result_data.update({email: {"Occurrence": occured, "EmailType": email_type}})

with open('result.json', 'w') as output:
    json.dump(result_data, output, sort_keys=True, indent=4, ensure_ascii=False)
    output.close()
