import requests

global_charts = 'https://spotifycharts.com/regional/global/daily/latest/download'
global_page = requests.get(global_charts)
print(global_page.content)

songs = 'regional'
area = 'global'
time = 'daily'
period = 'latest'

chart = 'https://spotifycharts.com/%s/%s/%s/%s/download' % (
    songs, area, time, period)
page = requests.get(chart)
print(page.content)
