from main import covidpg
import time

def main():
    index = 1
    while True:
        covidpg(index)
        index+=1
        time_wait = 60
        time.sleep(time_wait*1440)
main()