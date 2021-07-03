import requests
from bs4 import BeautifulSoup

cookies = {
    "_ga": "GA1.3.1651378350.1611654623",
    "sbjs_current": "typ=organic|||src=google|||mdm=organic|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
    "sbjs_current_add": "fd=2021-05-09 07:21:20|||ep=https://www.savemyexams.co.uk/notes/igcse-biology-cie-new/16-reproduction/16-1-asexual-sexual-reproduction/16-1-3-germination/|||rf=https://www.google.com/",
    "sbjs_first": "typ=organic|||src=google|||mdm=organic|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
    "sbjs_first_add": "fd=2021-01-26 09:50:01|||ep=https://www.savemyexams.co.uk/|||rf=https://www.google.com/",
    "sbjs_migrations": "1418474375998=1",
    "sbjs_udata": "vst=26|||uip=(none)|||uag=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
}

main_r = "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/"
main_r = requests.get(main_r)
request_soup = BeautifulSoup(main_r.text, 'html.parser')

table = request_soup.find_all('table')
paper4_table = table[1]
table_body = paper4_table.find('tbody')
rows = table_body.find_all('tr')

rows_text = []
for row in rows:
    row_text = row.get_text().strip()
    if row_text:
        rows_text.append(row_text)

topic_labels = []
for row in rows_text[12:]:
    if "-" in row and row != "7. Co-ordinate Geometry":
        topic_labels.append(row)

names = []
for label in topic_labels:
    name = ""
    for character in label:
        if character == "-":
            break
        elif character == "/":
            character = "-"
        else:
            name += character
    names.append(name)

numbers = []
for label in topic_labels:
    number = ""
    if label[-1] in ("1", "2", "3", "4", "5", "6"):
        number += label[-1]
    numbers.append(number)

levels = []
for label in topic_labels:
    level = ""
    if "Medium" in label:
        level += "Medium"
    elif "Hard" in label:
        level += "Hard"
    levels.append(level)

filenames = []
for name, level, number in zip(names, levels, numbers):
    filename = name + "- " + level + " " + number
    filenames.append(filename.strip())

with open('pdf_files_paper4.txt') as urls:
    for url, filename in zip(urls, filenames):
        r = requests.get(url.rstrip(), cookies=cookies)
        new_filename = filename + ".pdf"
        with open(new_filename, 'wb') as f:
            f.write(r.content)