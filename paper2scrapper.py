import requests
from bs4 import BeautifulSoup
import re

test_url = "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/sets-venn-diagrams-2-paper-2-hard-model-answers/"

# main_r_headers = {
#     "__stripe_mid": "ee9603d8-d9fc-4bf0-ba2a-b87cf1de24a8b9e6eb",
#     "_ga": "GA1.3.1651378350.1611654623",
#     "catAccCookies": "1",
#     "cp_style_906285": "true",
#     "cppro-ft": "true",
#     "fakesessid": "4bd99ad3957342ccb8bd90ad154d35cd",
#     "PHPSESSID": "k5feo8knu8v7ocurbulofd3gl8",
#     "sbjs_current": "typ=organic|||src=google|||mdm=organic|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
#     "sbjs_current_add": "fd=2021-05-09 07:21:20|||ep=https://www.savemyexams.co.uk/notes/igcse-biology-cie-new/16-reproduction/16-1-asexual-sexual-reproduction/16-1-3-germination/|||rf=https://www.google.com/",
#     "sbjs_first": "typ=organic|||src=google|||mdm=organic|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
#     "sbjs_first_add": "fd=2021-01-26 09:50:01|||ep=https://www.savemyexams.co.uk/|||rf=https://www.google.com/",
#     "sbjs_migrations": "1418474375998=1",
#     "sbjs_session": "pgs=1|||cpg=https://www.savemyexams.co.uk/members-login/?redirect=%2F",
#     "sbjs_udata": "vst=26|||uip=(none)|||uag=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
#     "sme_device_id": "601f9d952c233",
#     "wordpress_logged_in_fd8c7acb24ecaebf5c0e679b61b296b9": "18a3e8a495c8cd8ca0f776232ad21a58bcd9d2bea022b449bc06093f464ed56f",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
# }
# using these params appears as a security bypass attempt

# -------------------loop through the main urls------------------------------


main_r = "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/"
main_r = requests.get(main_r)
request_soup = BeautifulSoup(main_r.text, 'html.parser')

table = request_soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

rows_text = []
for row in rows:
    row_text = row.get_text().strip()
    if row_text:
        rows_text.append(row_text)

# pattern : Using Algebra - Easy 3 - https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/using-algebra-3-paper-2-easy-model-answers/
#pattern : name + paper_number + "-paper-2-" + level_of_difficulty + "-model-answers"

topic_labels = []
for row in rows_text[12:]:
    if "-" in row and row != "3. Co-ordinate geometry":
        # finds all the topics from which to download the ms pdf from
        topic_labels.append(row)

numbers = []
for label in topic_labels:
    number = ""
    if label[-1] in ("1", "2", "3", "4", "5", "6"):
        number += label[-1]
    numbers.append(number)  # get the paper number

levels = []
for label in topic_labels:
    level = ""
    if "Hard" in label:
        level += "hard"
    elif "Easy" in label:
        level += "easy"
    levels.append(level)  # is the paper hard or easy

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
    names.append(name)  # find the name in the relevant format

model_answer_urls = []
for name, level, number in zip(names, levels, numbers):
    url_part = ""
    full_url = ""
    url_part += name + number + "-paper-2-" + level + "-model-answers/"
    full_url += "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/" + url_part
    model_answer_urls.append(full_url)  # generating full url

with open('model_answer_urls.txt', 'w') as f:
    for item in model_answer_urls:
        f.write("%s\n" % item)

# url_part = names[0] + numbers[0] + "-paper-2-" + levels[0] + "-model-answers/"
# full_url = "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/" + url_part
# print(full_url)                                     #testing if the url-generating works as intended

# ------------------------------------------------------------------------------------------------------
# geturl_cookies = {
#     "_fbp": "fb.2.1622708580477.670640383",
#     "_ga": "GA1.3.1886808930.1622708581",
#     "_gcl_au": "1.1.711692685.1622708576",
#     "sbjs_current": "typ=organic|||src=google|||mdm=organic|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
#     "sbjs_current_add": "fd=2021-03-12 10:03:40|||ep=https://www.savemyexams.co.uk/igcse-physics-cie-new/revision-notes/|||rf=https://www.google.com/",
#     "sbjs_first": "typ=organic|||src=google|||mdm=organic|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
#     "sbjs_first_add": "fd=2021-01-26 09:50:01|||ep=https://www.savemyexams.co.uk/|||rf=https://www.google.com/",
#     "sbjs_migrations": "1418474375998=1",
#     "sbjs_session": "pgs=1|||cpg=https://www.savemyexams.co.uk/members-login/",
#     "sbjs_udata": "vst=12|||uip=(none)|||uag=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
# }

# cookies = {
#     "catAccCookies": "1",
#     "cp_style_906285": "true",

# }

# --------------------get url for pdf file---------------------------

# geturl_r = requests.get(test_url)
# geturl_soup = BeautifulSoup(geturl_r.text, 'html.parser')

# filename = "2A-Model-Answers"
# tag = geturl_soup.find_all(href=re.compile(filename))
# if not tag:
#     filename = "2B-Model-Answers"
#     tag = geturl_soup.find_all(href=re.compile(filename))

# url = tag[0]['href']
# url_list = []
# url_list.append(url)

# print(url_list)
# ---------------------------------------------------------------------

# with open('test.pdf', 'wb') as f:
#     f.write(r.content)
