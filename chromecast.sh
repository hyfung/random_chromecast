#!/bin/bash

# This script takes in a youtube url, calls youtube-dl then cast it via VLC

IP=192.168.0.250
rm -f /tmp/cast.mp4
youtube-dl -f mp4 $1 -o /tmp/cast.mp4
vlc /tmp/cast.mp4 --sout="#chromecast{ip=192.168.0.250}" --demux-filter=demux_chromecast
