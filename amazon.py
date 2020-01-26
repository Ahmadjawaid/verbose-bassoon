# Demo product - hydroflask

import requests

global_charts = 'https://www.amazon.com/s?k=Hydro+Flask+Standard+Mouth+Water+Bottle%2C+Flex+Cap&ref=nb_sb_noss_2'
global_page = requests.get(global_charts)
print(global_page.content)
