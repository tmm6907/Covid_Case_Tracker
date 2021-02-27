from main import covidpg
import time

def main():
    while True:
        covidpg()
        time_wait = 60
        time.sleep(time_wait*1440)