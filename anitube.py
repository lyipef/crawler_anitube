import requests
from bs4 import BeautifulSoup
import openpyxl
from twilio.rest import Client


# Credentials

account_sid = 'twiliocredentials' 

auth_token = "twiliocredentials" 

client = Client(account_sid, auth_token) 

# Url do site Anitube
url = 'https://www.anitube.site/'

response = requests.get(url)

# Caminho pelo HTML
soup = BeautifulSoup(response.text, 'html.parser')
ep_tags = soup.find('div', class_='epiSubContainer').find_all('div', class_='epiItem')

# Junta todos os ep em uma lista
ep_list  = []
for i in range(0, len(ep_tags)):
    titles = ep_tags[i].get_text().split('\n')[8]
    ep_list.append(titles)

# Transformando em strings
body_text = 'Hoje foi lançado os seguintes episódios no AniTube\n'
for eps in ep_list:
    body_text += f'{eps}\n'
body_text += 'Então quando chegar em casa aproveite <3'

print(body_text)

message = client.messages.create( 
                              from_='whatsapp:yournumber',  
                              body=body_text,      
                              to='whatsapp:twilionumber' 
                          ) 
 
print(message.sid)
