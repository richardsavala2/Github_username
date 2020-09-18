import requests
from bs4 import BeautifulSoup

request = requests.get('https://github.com/thrillhobaby')
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "p-nickname vcard-username d-block", "itemprop": "additionalName"})
print(element.get_text())

# <span class="p-nickname vcard-username d-block" itemprop="additionalName">thrillhobaby</span>
# <span class="p-nickname vcard-username d-block" itemprop="additionalName">thrillhobaby</span>