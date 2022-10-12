
import subprocess

def convert_480p(path):
    target = path + '_480p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(path, target)
    run = subprocess.run(cmd, capture_output=True)