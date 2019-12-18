#!/bin/bash
outpart=`curl "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=$@&type=video&key=AIzaSyCSqOqZJXTlu2DJ8s1ngQfHrtR4enhvhH0" | jq '.items[].id.videoId'`
printf "$outpart"