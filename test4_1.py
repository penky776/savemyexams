import requests
from bs4 import BeautifulSoup

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
    if "-" in row and row != "3. Co-ordinate geometry":
        topic_labels.append(row)

print(topic_labels)