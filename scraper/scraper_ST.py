from bs4 import BeautifulSoup
import urllib3

url = 'https://www.straitstimes.com/singapore/consumer/some-disgruntled-diners-fake-vaccination-certificates-in-first-week-of-dining-in'
http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data, 'html.parser')
bucket = ''
for item in soup.findAll('div', attrs={'class': 'odd field-item'}):
    for p in item.findAll('p'):
        bucket += p.text
        bucket += ' '
print(bucket)
