import requests,re
from bs4 import BeautifulSoup

res=requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence')

soup = BeautifulSoup(res.text,"html.parser")

title=soup.select('title')
paragraph=soup.select('p')

i=0
content=''

print(title[0].getText())

while(i<len(paragraph)):
    content=content+paragraph[i].getText()
    i+=1


pattern=re.compile('\.')

content=pattern.sub(".\\n\\n-->",content)

print(content)
