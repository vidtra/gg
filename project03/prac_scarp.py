import requests
from bs4 import BeautifulSoup


url = "https://clist.by/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

req = data.text
soup = BeautifulSoup(req, 'html.parser')

contests = soup.find_all('div', {'class': ['contest', 'row']})
for contest in contests:
    start_time = contest.select_one('.start-time')
    duration = contest.select_one('.duration')
    time_left = contest.select_one('.timeleft')
    event = contest.select_one('.contest_title')
    if not start_time:
        continue
    start_time = start_time.text.strip()
    duration = duration.text.strip()
    time_left = time_left.text.strip()
    event = event.text.strip()
    print(start_time)
    print(duration)
    print(time_left)
    print(event)