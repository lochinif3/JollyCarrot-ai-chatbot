import requests
from bs4 import BeautifulSoup

def get_rabbit_traits_info():
    url = 'https://www.theeducatedrabbit.com/rabbit-personalities.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    if page.status_code == 200:
        target = "Rabbit personalities are as varied as ours."
        for paragraph in soup.find_all('p'):
            if target in paragraph.text:
                return paragraph.text.strip()
        return "The specific paragraph was not found."
    else:
        return f"Whoops! Sorry, I'm a bit lost in this cyberspace right now. But I'll bounce back in no time :) : {page.status_code}"
