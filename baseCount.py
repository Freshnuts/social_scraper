import os
import sys

count_result = []

# baseCount save
user = 'Alliedesports'

curl_name = "curl -s -A 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1' 'https://socialblade.com/twitch/user/" + user + "/realtime' | grep 'realtime-username-twitch' | cut -d '>' -f2 | cut -d '<' -f1"

        # User Count
curl_count = "curl -s -A 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1' 'https://socialblade.com/twitch/user/" + user + "/realtime' | grep 'rawCount' | cut -d '>' -f2 | cut -d '<' -f1"

# Scraper for Name
username_result = os.popen(curl_name).read()
print username_result

# Scraper for Number
count_result = os.popen(curl_count).read()
print count_result[i]
