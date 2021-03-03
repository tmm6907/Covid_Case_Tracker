from main import covidpg
import time

def main():
    index = 1 #keeps track of log number
    while True:
        covidpg(index)
        index+=1
        time_wait = 60
        time.sleep(time_wait*1440) #runs once a day
main()