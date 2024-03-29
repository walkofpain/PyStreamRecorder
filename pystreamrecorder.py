import schedule
import datetime
import time
import subprocess

URL = 'https://www.twitch.tv/bratishkinoff' # stream channel link (youtube/twitch/wasd/goodgame), youtube link with "/live"
quality = 'best' # choose quality (audio_only, worst, best)

text = '''
▒█▀▀█ █░░█ ▒█▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀ █▀▀█ █▀▄▀█ ▒█▀▀█ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ 
▒█▄▄█ █▄▄█ ░▀▀▀▄▄ ░░█░░ █▄▄▀ █▀▀ █▄▄█ █░▀░█ ▒█▄▄▀ █▀▀ █░░ █░░█ █▄▄▀ █░░█ █▀▀ █▄▄▀ 
▒█░░░ ▄▄▄█ ▒█▄▄▄█ ░░▀░░ ▀░▀▀ ▀▀▀ ▀░░▀ ▀░░░▀ ▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀
'''
print(text)

def job_function():
    now = datetime.datetime.now()
    outputfile = 'stream-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'-'+str(now.hour)+'-'+str(now.minute)+'.mp4'
    
    command='streamlink ' + URL + ' '+ quality + ' -o '  + outputfile
    subprocess.call(command, shell=True)

schedule.every(2).seconds.do(job_function) 

while True:
    schedule.run_pending()
    time.sleep(0)
