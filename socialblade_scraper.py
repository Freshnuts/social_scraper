from openpyxl import Workbook
import time
import os
import sys

workbook = Workbook()
sheet = workbook.active

users = ['Gaules', 'bystaxx', 'NICKMERCS', 'pokimane', 'asmongold', 'maximum']
baseCount = [1,2,3,4,5,6]
newCount = [1,2,3,4,5,6]
newFollowers = [1,2,3,4,5,6]


# Base user count - Doesn't change, runs 1 time.
for k in range(0,6):

    # NEED TO: Use import json instead
    baseCurl_count = "curl -H 'query: " + users[k] + "' -H 'history: default' -H 'clientid: [CLIENT ID HERE]' -H 'token: [TOKEN GOES HERE]' -X GET https://matrix.sbapis.com/b/twitch/statistics | grep followers | cut -d ':' -f30 | tr -d [:alpha:] | tr -d [:punct:]"

    baseCount_result = os.popen(baseCurl_count).read()
    baseCount[k] = int(baseCount_result)


# newCount - Changes everytime there is a new subscriber
while True:
    for i in range(0,6):

        # NEED TO: Use import json instead
        curl_count = "curl -H 'query: " + users[i] + "' -H 'history: default' -H 'clientid: [CLIENT ID HERE]' -H 'token: [TOKEN GOES HERE]' -X GET https://matrix.sbapis.com/b/twitch/statistics | grep followers | cut -d ':' -f30 | tr -d [:alpha:] | tr -d [:punct:]"

        # newCount - baseCount = newFollowers
        count_result = os.popen(curl_count).read()
        newCount[i] = int(count_result)
        newFollowers[i] = newCount[i] - baseCount[i]

    for n in range(0,6):
        print users[n]
        print 'baseCount', baseCount[n]
        print 'newCount', newCount[n]
        print 'NewFollowers', newFollowers[n]

        if n == 0:
            sheet['A1'] = users[n]
            sheet['A2'] = baseCount[n]
            sheet['A3'] = newCount[n]

        if n == 1:
            sheet['B1'] = users[n]
            sheet['B2'] = baseCount[n]
            sheet['B3'] = newCount[n]

        if n == 2:
            sheet['C1'] = users[n]
            sheet['C2'] = baseCount[n]
            sheet['C3'] = newCount[n]


        if n == 3:
            sheet['D1'] = users[n]
            sheet['D2'] = baseCount[n]
            sheet['D3'] = newCount[n]


        if n == 4:
            sheet['E1'] = users[n]
            sheet['E2'] = baseCount[n]
            sheet['E3'] = newCount[n]

        if n == 5:
            sheet['F1'] = users[n]
            sheet['F2'] = baseCount[n]
            sheet['F3'] = newCount[n]

        if n == 6:
            sheet['G1'] = users[n]
            sheet['G2'] = baseCount[n]
            sheet['G3'] = newCount[n]

        workbook.save(filename='follower_count.xlsx')

    time.sleep(10)
    # break;
