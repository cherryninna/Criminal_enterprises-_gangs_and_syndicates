import requests
from bs4 import BeautifulSoup
import json
import spacy
import uuid

nlp = spacy.load('en_core_web_sm')

url = 'https://en.wikipedia.org/wiki/List_of_criminal_enterprises,_gangs,_and_syndicates'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all <li> elements that correspond to certain conditions
li_elements = soup.find_all('li')
li_elements = [li for li in li_elements if '</li>' in str(li) and str(li).count('<li>') == 1 and not li.find_parent('div', {'aria-labelledby': 'Scams_and_confidence_tricks'}) and not li.find_parent('div', {'id': 'catlinks'}) and not li.find_parent('div', {'style': 'padding:0 0.25em'})]

# Find all <a> elements within the selected <li> elements that have a href starting with "/wiki/"
links = []
for li in li_elements:
    link = li.find('a', href=True)
    if link and link['href'].startswith('/wiki/') and ('id' not in li.attrs or li['id'].startswith('cite_ref')):
        if link not in links:
            links.append(link)

# Create a list of dictionaries containing name and additional attributes
values = []
for link in links:
    if '</a>' in str(link.parent) and str(link.parent).count('<li>') == 1 and 'title' in link.attrs and link.text:
        if link.text == 'Crime family':
            break
        if len(link.text.strip()) > 0:
            link_response = requests.get('https://en.wikipedia.org' + link['href'])
            link_soup = BeautifulSoup(link_response.content, 'html.parser')

            # Find all <th> and <td> elements with the specified scope and class values
            th_elements = link_soup.find_all('th', {'scope': 'row', 'class': 'infobox-label'})
            td_elements = link_soup.find_all('td', {'class': 'infobox-data'})

            # Exclude elements whose only known attribute is name
            if len(th_elements) > 0:
                # Create a dictionary
                info_dict = {'name': link.text, 'metadata': {}, 'uuid': str(uuid.uuid4())} # Generate a UUID and convert it to a string of hex digits
                
                for i in range(len(th_elements)):
                    th = th_elements[i].text.strip()
                    td = td_elements[i].text.strip()
                
                    # Remove escape characters
                    escape_characters = ['\"', '\n', '\\']
                    for char in escape_characters:
                        td = td.replace(char, " ")
                
                    # Remove references from strings
                    if "[" in th:
                        th = th[:th.index("[")]
                    if "[" in td:
                        td = td[:td.index("[")]
                       
                    # Filter out empty attributes
                    if len(td) > 0:
                        info_dict['metadata'][th] = td                               

                # Append the dictionary to the list of values
                values.append(info_dict)

# Create a dictionary containing cluster information
data = {'authors': ['Nina Janeva', 'Zainab Guennoun'], 'category': 'Criminals', 'description':'Enterprises, gangs, mafias and criminal syndicates involved in organized crime', 'name':'Criminal enterprises, gangs and syndicates', 'source': 'Wikipedia', 'type': 'organized crime', 'uuid': '1d13407c-d73d-47db-b17e-c248214a3088', 'values': values, 'version': 1}

# Generate a JSON file
with open('../clusters/criminals.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent = 4, ensure_ascii=False)
