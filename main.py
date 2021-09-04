
import time

import urllib3
import certifi
import json
import random

from nltk.corpus import words

theList = words.words()

random.shuffle(theList)

url = 'https://api.mojang.com/users/profiles/minecraft/'
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

count = 0
lowerThan = 8

time.sleep(600)

for word in theList:

    count += 1

    if len(word) > lowerThan - 1:
        continue
    if len(word) < 3:
        continue

    word = word.strip(' ').strip('\n')
    word = word.lower()

    try:
        r = http.request('GET', url + word)
    except urllib3.exceptions.SSLError as e:
        print(str(e))
        exit(0)

    try:
        r_data = json.loads(r.data.decode('utf-8'))
    except Exception as e:
        r_data = ""

    if not r_data:
        print("OG Username: " + word)

    if count > 599:
        count = 0
        time.sleep(600)




