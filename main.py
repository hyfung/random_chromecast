#!/usr/bin/python3

import random
import subprocess
import os
import argparse
import signal

current_video = None

def on_sigint():
    os('pkill vlc')
    delete_video(current_video)
    exit()

def choose_video(directory) -> str:
    """
    Takes in a directory, spits a random video with its full path
    """
    if not directory.endswith('/'):
        directory += '/'

    files = [file for file in os.listdir(directory) if file.endswith('.mp4')]
    
    if files == []:
        # No video available
        exit()
    
    return directory + random.choice(files)

def cast_video(path) -> None:
    """
    Takes in the full path to the video, invoke chromecast via VLC via os.system()
    """
    global current_video
    current_video = path
    print('[*] Casting %s' % path)
    cmd = 'cvlc %s --sout="#chromecast{ip=192.168.0.250}" --rate %.2f --demux-filter=demux_chromecast --play-and-exit' % (args['rate'], path)
    os.system(cmd)

def delete_video(path) -> str:
    """
    Takes in the full path to video, delete it
    """
    print('[*] Deleting ' + path)
    os.remove(path.strip('\''))

def main():
    """
    This is the entrypoint, depending on the options passed to argparse it will go
    either one shot or repeatedly
    """
    signal.signal(signal.SIGINT, on_sigint)

    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dir", help="Full path to the folder", type=str,
                    default='/mnt/Media/Youtube/Play-n-delete')
    ap.add_argument("-r", "--repeat", help="", action='store_true', default=False)
    ap.add_argument("-s", "--speed", help="Playback speed", type=float, default=1.0)
    args = vars(ap.parse_args())

    directory = args['dir']
    

    while True:
        file = choose_video(directory)
        cast_video(repr(file))
        delete_video(repr(file))
        
        if not args['repeat']:
            exit()
    
if __name__ == '__main__':
    main()
