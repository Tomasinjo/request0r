import requests
import datetime
import time

urls = ['https://www.domain1.com/url', 'https://www.domain2.com/url', 'https://www.domain3.com/url']

def check_urls(url):
    timestamp = datetime.datetime.now().isoformat()
    status = ''
    response_time = ''
    exception = ''
    try:
        resp = requests.get(url, timeout=10)
    except Exception as exception:
        return timestamp, url, status, response_time, exception
    status = resp.status_code
    response_time = resp.elapsed.total_seconds()
    return timestamp, url, status, response_time, exception

while True:
    for url in urls:
        timestamp, url, status, response_time, exception = check_urls(url)
        print(f'{timestamp}|{url}|{status}|{response_time}|{exception}')
    time.sleep(5)
