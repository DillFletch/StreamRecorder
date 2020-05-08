import os
import datetime

filename = datetime.date.today()
filename = str(filename)

print("----Livestream recorder script by sm0lman----")
link = input("Paste the link of the webpage which contains the livestream: ")
name = input("What is the streamers name?: ")
filename = filename + name
print("Getting available formats...")
os.system("youtube-dl --list-formats"+" '"+link+"'")
form = input("Which format code would you like to record?: ")
print("Beginning recording, press ctrl+c to end...")
command = "ffmpeg -i $(youtube-dl -f "+form+" -g '"+link+"'"") -c copy "+filename+".ts"
os.system(command)
