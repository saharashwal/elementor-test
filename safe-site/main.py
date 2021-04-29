import schedule
import requests


def sample_sites():
    requests.get('http://localhost:5000/ds1')
    requests.get('http://localhost:5000/check')

if __name__ == "__main__":
    schedule.every(30).minutes.do(sample_sites)

    while True:
        schedule.run_pending()
