import bs4
import requests as r

### SET UP VARIABLES ###
url = 'https://en.wikipedia.org/wiki/List_of_busiest_airports_by_passenger_traffic'
req = r.get(url)
data = req.text
soup = bs4.BeautifulSoup(data,"html.parser")
code_list = []

### PARSING ###
# get table
all_table_elements = soup.find_all('table')
# open file for writing
with open('codes.txt', 'w') as outfile:
    #loop through, find tr elements, and get 5th index (IATA codes)
    for table_elements in all_table_elements[0:7]:
        for e in table_elements.find_all('tr')[1:]:
            if e is not None and len(e) > 0:
                airport = e.find_all('td')[1].text.lstrip().encode("utf-8")
                code = e.find_all('td')[4].text.split("/")[0].encode("utf-8")
                if code not in code_list:
                    code_list.append(code)
                    outfile.write(code+"\n")
                    #print airport + " | " + code