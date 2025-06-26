from bs4 import BeautifulSoup
import requests

# Categories to search for news
categories = ['national','sports','business','technology','world','entertainment']
header = {'User-Agent':'Mozilla/5.0'}

all_headlines=[]

for category in categories:
    url = f"https://inshorts.com/en/read/{category}"
    response = requests.get(url,headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('span',itemprop='headline')
    all_headlines.extend([h1.get_text(strip=True) for h1 in headlines])

# Writing the headlines from all_headlines to headlines.txt 

with open("headlines.txt","w",encoding="utf-8") as file:
    for idx,headline in enumerate(all_headlines):
        file.write(f"{idx+1}. {headline}\n")

print(f"Saved {len(all_headlines)} to headlines.txt")