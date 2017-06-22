import requests
from bs4 import BeautifulSoup


#username = input('enter github username - ')
url = "https://github.com/RavicharanN"
sauce = requests.get(url)    
soup = BeautifulSoup(sauce.content,'html.parser')     # lxml is a parser
#print(soup)

repoNo = int(soup.find('span',class_='Counter').text)
n1 = repoNo

url2 = url + "?tab=repositories"
sauce = requests.get(url2)   
soup = BeautifulSoup(url2,'html.parser')
#print(soup)

arr = [0]
tags = soup.find_all('a', itemprop="name codeRepository")
for tag in tags:
    if tag.text!="":
        arr.append((tag.text).lstrip())

k=2
while(len(arr)<=n1):
    url3 = url + "?page="+str(k)+"&tab=repositories"
    k+=1
    sauce = requests.get(url3)    
    soup = BeautifulSoup(sauce.content,'html.parser')
    tags = soup.find_all('a', itemprop="name codeRepository")
    for tag in tags:
        if tag.text!="":
            arr.append((tag.text).lstrip())

for i in range(1,len(arr)):
    h1 = str(i) + ".  "+str(arr[i])
    print(h1) 
