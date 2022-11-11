import requests
import re
from bs4 import BeautifulSoup as bs
site = requests.get('https://startuptalky.com/patna-startups/')
soup = bs(site.content,features="lxml")
content = soup.find('article', attrs = {'class':'tag-collections'})
titles = []
for row in content.findAll('h2'):
    titles.append(row.text.strip())
info = []
for row in content.findAll('h4'):
    row = row.text.strip()
    row = row.split(":")
    if len(row) > 1:
        founder = row[1].replace("Year Founded","").strip()
        year = re.findall(r'\d+', row[2])[0]
        type = row[3].strip()
        info.append({"founder":founder,"type":type,"year":year})

titles.remove(titles[0])
titles.remove(titles[-1])
data = dict (zip(titles, info))
print(data)

