
import subprocess

def convert480p(path):
    target = path + '_480p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(path, target)
    subprocess.run(cmd, shell = True, cwd = 'c:/Users/Alex/AlexTestApi2/AlexTestApi2/mysite/media/videos')