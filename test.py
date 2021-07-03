import requests
from bs4 import BeautifulSoup
import re

r_cookies = {
    "__stripe_mid": "ee9603d8-d9fc-4bf0-ba2a-b87cf1de24a8b9e6eb",
    "_ga": "GA1.3.1651378350.1611654623",
    "catAccCookies": "1",
    "cppro-ft": "true",
    "fakesessid": "05a4e59dbc79f0e58a275a62ce51f0e0",
    "PHPSESSID": "db7od7ciobp2d1uqqfivj6p0n9",
    "sbjs_current": "typ=organic|||src=google|||mdm=organic|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
    "sbjs_current_add": "fd=2021-05-09 07:21:20|||ep=https://www.savemyexams.co.uk/notes/igcse-biology-cie-new/16-reproduction/16-1-asexual-sexual-reproduction/16-1-3-germination/|||rf=https://www.google.com/",
    "sbjs_first": "typ=organic|||src=google|||mdm=organic|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
    "sbjs_first_add": "fd=2021-01-26 09:50:01|||ep=https://www.savemyexams.co.uk/|||rf=https://www.google.com/",
    "sbjs_migrations": "1418474375998=1",
    "sbjs_udata": "vst=26|||uip=(none)|||uag=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "sme_device_id": "601f9d952c233",
    "wordpress_logged_in_fd8c7acb24ecaebf5c0e679b61b296b9": "Balgish|1626350556|jvd6MlQzymh4I4TXpy6zgjKrtbV0z9WMuWYQL2UStz9|1ee630a1b66cfa91839edee0f8e45854dd005dd10fd52a55ccdcadff760c1fc6"
}

test_url = "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/using-a-calculator-2-paper-2-easy-model-answers/"
# test_url = "https://www.savemyexams.co.uk/cie-igcse-maths-new/topic-questions/bounds-2-paper-2-easy-model-answers/"
geturl_r = requests.get(test_url, cookies=r_cookies)
geturl_soup = BeautifulSoup(geturl_r.text, 'html.parser')

filename = "2A-Model-Answers"
tag = geturl_soup.find_all(href=re.compile(filename))
if not tag:
    filename = "2B-Model-Answers"
    tag = geturl_soup.find_all(href=re.compile(filename))
else:
    filename = "Answers"
    tag = geturl_soup.find_all(href=re.compile(filename))
print(tag)
# url = tag[0]['href']
# url_list = []
# url_list.append(url)

# print(url_list)