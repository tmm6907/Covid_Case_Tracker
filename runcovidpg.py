from main import covidpg
import time

def main():
    index = 0
    while True:
        covidpg(index)
        time_wait = 60
        time.sleep(time_wait*1440)