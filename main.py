#!/usr/bin/python3

import random
import subprocess
import os
import argparse

def choose_video(directory):
    """
    Takes in a directory, spits a random video with its full path
    """
    files = [file for files in os.listdir(directory) if file.endswith('.mp4')]
    return directory + random.choice(files)

def cast_video(path):
    """
    Takes in the full path to the video, invoke chromecast via VLC via os.system()
    """
    pass

def delete_video(path):
    """
    Takes in the full path to video, delete it
    """
    print('deleting ' + path)
    pass

def main():
    """
    This is the entrypoint, depending on the options passed to argparse it will go
    either one shot or repeatedly
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dir", help="Full path to the folder", type=str,
                    required=True, default='/mnt/Media/Youtube')
    ap.add_argument("-r", "--repeat", help="", action='store_true', default=False)
    args = vars(ap.parse_args())

    directory = args['dir']
    if not directory.endswith('/'):
        directory += '/'

    while True:
        file = choose_video(directory)
        cast_video(repr(file))
        delete_video(repr(file))
        if not args['repeat']:
            exit()
    
if __name__ == '__main__':
    main()
