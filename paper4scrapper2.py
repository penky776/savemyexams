import requests
from bs4 import BeautifulSoup
import re

# r_cookies = {
#     "_fbp": "fb.2.1622708580477.670640383",
#     "_ga": "GA1.3.1886808930.1622708581",
#     "_gcl_au": "1.1.711692685.1622708576",
#     "_gid": "GA1.3.418448575.1623571837",
#     "_seg_uid": "ba464ea75e95bb96ba183d2f94eaf0d8",
#     "_seg_uid_6186": "ba464ea75e95bb96ba183d2f94eaf0d8",
#     "_seg_visitor_6186": '{"referrer":null}',
#     "catAccCookies": "1",
#     "cid": "1886808930.1622708581",
#     "cp_style_906285": "true",
#     "cppro-ft": "true",
#     "fakesessid": "204e3d39ca978c9b2d577e71002e6276",
#     "MSopened": "fc4d616c229dc12d755cd699e7efea3e00274e2f",
#     "MSopened.810ff74e11230d54c2e168e900da1220bab8c032": "true",
#     "MSopened.fc4d616c229dc12d755cd699e7efea3e00274e2f": "true",
#     "Pastease.passive.activated.sinQ2k2xyiNQ18z": "0",
#     "Pastease.passive.chance.sinQ2k2xyiNQ18z": "chance39.5",
#     "Pastease.pro_active.activated.E9RVBqiRuMfq70H": "1",
#     "Pastease.pro_active.activated.sinQ2k2xyiNQ18z": "1",
#     "Pastease.pro_active.chance.E9RVBqiRuMfq70H": "chance42.0",
#     "Pastease.pro_active.chance.sinQ2k2xyiNQ18z": "chance23.3",
#     "PHPSESSID": "c3lbm5r9u7nupb61os07molark",
#     "sbjs_current": "typ=typein|||src=(direct)|||mdm=(none)|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
#     "sbjs_current_add": "fd=2021-06-03 08:22:53|||ep=https://www.savemyexams.co.uk/|||rf=(none)",
#     "sbjs_first": "typ=typein|||src=(direct)|||mdm=(none)|||cmp=(none)|||cnt=(none)|||id=(none)|||trm=(none)|||mtke=(none)",
#     "sbjs_first_add": "fd=2021-06-03 08:22:53|||ep=https://www.savemyexams.co.uk/|||rf=(none)",
#     "sbjs_migrations": "1418474375998=1",
#     "sbjs_session": "pgs=2|||cpg=https://www.savemyexams.co.uk/members-login/?redirect=%2Fcie-igcse-maths-new%2Ftopic-questions%2F",
#     "sbjs_udata": "vst=17|||uip=(none)|||uag=Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
#     "sme_device_id": "60c07b9a6d32d",
#     "sucuri_cloudproxy_uuid_0f6ea8682": "d0a538ef09a9230dc499ed2cb7de850e",
#     "wordpress_logged_in_fd8c7acb24ecaebf5c0e679b61b296b9": "Balgish|1624891408|y4L8benMLaAYH9V4Y2qm9Q3qJtFYHld2w4cGAKdj8WP|061c9fb2d0189544f060dcd126e3892a5272e67809f5ccfa60db4af946451cf0"
# }

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

# url_list = []
# with open('model_answer_urls_paper4.txt') as model:
#     for line in model:
#         r = requests.get(line.strip(), cookies=r_cookies)
#         soup = BeautifulSoup(r.text, 'html.parser')

#         filename = "4A-Model-Answers"

#         tags = soup.find_all(href=re.compile(filename))

#         if not tags:
#             filename = "4B-Model-Answers"
#             tags = soup.find_all(href=re.compile(filename))

#         for tag in tags:
#             url = tag['href']
#             url_list.append(url)

# with open('pdf_files_paper4', 'w') as f:
#     for item in url_list:
#         f.write("%s\n" % item)

with open('model_answer_urls_paper4.txt') as model:
    for line in model:
        r = requests.get(line.rstrip(), cookies=r_cookies)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        filename = "4A-Medium-Model-Answers"

        tags = soup.find_all(href=re.compile(filename))

        if not tags:
            filename = "4B-Hard-Model-Answers"
            tags = soup.find_all(href=re.compile(filename))

        if not tags:
            f = open("pdf_files_paper4.txt", "a")
            f.write("something went wrong\n")
            f.close()
        else:
            url = tags[0]['href']
            
            f = open("pdf_files_paper4.txt", "a")
            f.write(url + "\n")
            f.close()