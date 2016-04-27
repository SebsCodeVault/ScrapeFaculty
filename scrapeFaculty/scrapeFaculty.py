from bs4 import BeautifulSoup
import urllib.request

### Constants.
url = "http://mitsloan.mit.edu/faculty-and-research/faculty-directory/"
home = "C:/Data/scrapeFaculty"
tagLvl_0 = ['div', 'div']
tagClassLvl_0 = ['left-column', 'right-column']
tagLvl_1 = ['a', 'span']
tagClassLvl_1 = []

### Create the Soup Object.
response = urllib.request.urlopen(url)
#print(response.info())
html = response.read()
response.close()
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

### Get tags
for i in range(0, len(tagLvl_0)):
    resultsLvl_0 = soup.find_all(tagLvl_0[i], {'class' : tagClassLvl_0[i]})
    for j in range(0, len(resultsLvl_0)):
        print("i is: {0}, j is: {1}".format( i, j))
        resultsLvl_1 = resultsLvl_0[j].find_all(tagLvl_1[i])
            #, {'class' : tagClassLvl_1[i]})
        print(resultsLvl_1)

#<div class="left-column"> : <a>
#<div class="right-column">: <a>