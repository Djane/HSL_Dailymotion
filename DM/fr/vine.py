#! /usr/bin/python3

import requests
import json

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=2270400,RESOLUTION=1280x720')

json_url = "http://hls-live-linear-fs.cdn01.net/aVJtTnlBRE40SWpONU1tTWpOMk54VTJZbFoyTTVRMk41TWpaMUFqTmpOVFp4QXpZNGdUTW1oSE1fNDI3MjQyNzI3MV9LS0dQSUdZVFNFTUE/LiveChannels/stream_22405/stream_info.php"
response = requests.get(json_url)
data = response.json()
primary_url = data.get("primary")
new_string = primary_url.replace("playlist", "LiveChannels/stream_22405")
print(new_string)
