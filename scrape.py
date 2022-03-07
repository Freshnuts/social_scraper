from openpyxl import Workbook
import os
import sys

# Excel Sheet (Ugly & Inefficient)
workbook = Workbook()
sheet = workbook.active

print "Insert 10 player names: "

for i in range(0,10):
    print "Enter Username: "
    user = raw_input()

    # UserName
    curl_name = "curl -s -A 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1' 'https://socialblade.com/twitch/user/" + user + "/realtime' | grep 'realtime-username-twitch' | cut -d '>' -f2 | cut -d '<' -f1"

    # User Count
    curl_count = "curl -s -A 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1' 'https://socialblade.com/twitch/user/" + user + "/realtime' | grep 'rawCount' | cut -d '>' -f2 | cut -d '<' -f1"

    # Scraper for Name
    username_result = os.popen(curl_name).read()
    print username_result

    # Scraper for Number
    count_result = os.popen(curl_count).read()
    print count_result




    print "current user: ", i


    # (LOL UGLY)
    # NEEDTO - use arrays lists incrementation to apply dynamic functionality to cell block locations.
    if i == 0:
        sheet["A1"] = username_result
        sheet["A2"] = count_result
    if i == 1:
        sheet["B1"] = username_result
        sheet["B2"] = count_result

    if i == 2:
        sheet["C1"] = username_result
        sheet["C2"] = count_result

    if i == 3:
        sheet["D1"] = username_result
        sheet["D2"] = count_result

    if i == 4:
        sheet["E1"] = username_result
        sheet["E2"] = count_result

    if i == 5:
        sheet["F1"] = username_result
        sheet["F2"] = count_result

    if i == 6:
        sheet["G1"] = username_result
        sheet["G2"] = count_result
    
    if i == 7:
        sheet["H1"] = username_result
        sheet["H2"] = count_result

    if i == 8:
        sheet["I1"] = username_result
        sheet["I2"] = count_result

    if i == 9:
        sheet["J1"] = username_result
        sheet["J2"] = count_result

    workbook.save(filename="follower_count.xlsx")
