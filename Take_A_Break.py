import webbrowser
import time

total_breaks = 3
break_count = 0

print ("This program started on " + time.ctime())
hours_waiting = input("How many hours do you want to wait?")
while hours_waiting.isalpha() == True:
    hours_waiting = input("How many hours do you want to wait?")
else:
    while break_count < total_breaks:
        time.sleep(int(hours_waiting)*60*60)
        webbrowser.open("https://www.youtube.com/watch?v=i7IWbinVA4k")
        break_count = break_count + 1
