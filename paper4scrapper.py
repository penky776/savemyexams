import requests
from bs4 import BeautifulSoup
import re

main_r = "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/#tab-f60582be5ab1628eabc"
main_r = requests.get(main_r)
request_soup = BeautifulSoup(main_r.text, 'html.parser')

table = request_soup.find('table', {'id': 'tablepress-807'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')

rows_text = []
for row in rows:
    row_text = row.get_text().strip()
    if row_text:
        rows_text.append(row_text)

topic_labels = []
for row in rows_text[11:]:
    if "-" in row and row != "7. Co-ordinate Geometry":
        # finds all the topics from which to download the ms pdf from
        topic_labels.append(row)

numbers = []
for label in topic_labels:
    number = ""
    if label[-1] in ("1", "2", "3", "4", "5", "6"):
        number += label[-1]
    numbers.append(number)

levels = []
for label in topic_labels:
    level = ""
    if "Hard" in label:
        level += "hard"
    elif "Easy" in label:
        level += "easy"
    elif "Medium" in label:
        level += "medium"
    levels.append(level)

names = []
for label in topic_labels:
    name = ""
    for character in label:
        if character == " ":
            name += "-"
        elif character == "-":
            break
        elif character == "&":
            continue
        else:
            name += character.lower()
    names.append(name)

model_answer_urls = []
for name, level, number in zip(names, levels, numbers):
    url_part = ""
    full_url = ""
    url_part += name + number + "-paper-4-" + level + "-model-answers/"
    full_url += "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/" + url_part
    model_answer_urls.append(full_url)

with open('model_answer_urls_paper4.txt', 'w') as f:
    for item in model_answer_urls:
        f.write("%s\n" % item)
