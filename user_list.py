import os
import sys

users = ['leekbeats', 'djksoundz', '4djfly', 'fullblastradio', 'mikecmusic', 'djjazzabella', 'chaotic060', 'fps_shaka', 'Thebausffs', 'elwind']
baseCount = [1,2,3,4,5,6,7,8,9,10]
newCount = [1,2,3,4,5,6,7,8,9,10]
newFollowers = [1,2,3,4,5,6,7,8,9,10]


# Grab Users & Initial Base Count
for i in range(0,10):

    # This part not needed, for debugging.
    # curl_name = "curl -s -A 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1' 'https://socialblade.com/twitch/user/" + users[i] + "/realtime' | grep 'realtime-username-twitch' | cut -d '>' -f2 | cut -d '<' -f1"

    # username_result = os.popen(curl_name).read()
    # print username_result

    count_result = os.popen(curl_count).read()
