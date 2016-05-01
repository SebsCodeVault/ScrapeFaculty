#!python3

from bs4 import BeautifulSoup #scrape library
import urllib.request #url library
import csv #csv writing
from datetime import date #for dates
import json #for json configs
import sys #for console interaction

######Thoughts: We always want: Name, Position, Website, Email, Office, Phone, Picture
### Constants.
'''
school = "mitsloan"
url = "http://mitsloan.mit.edu/faculty-and-research/faculty-directory/"
home = "C:/Data/scrapeFaculty"

tagLvl_0 = ['div', 'div']
tagClassLvl_0 = ['left-column', 'right-column']
tagLvl_1 = ['a', 'span']
tagClassLvl_1 = ['', '']
'''

if len(sys.argv) != 2:
    print('Usage: scrapeFaculty.py config')
    sys.exit()

configPath = sys.argv[1] #sys.argv[0] is the program, i.e. scrapeFaculty.py
#Load the config
configFile = open("C:/github/scrapeFaculty/scrapeFaculty/configs/test.json")
with open(configPath) as jsonFile:
	config = json.load(jsonFile)

### Initialize variables
school = config['school']
url = config['url']
home = config['home']
tagLvl_0 = config['tagLvl_0']
tagClassLvl_0 = config['tagClassLvl_0']
tagLvl_1 = config['tagLvl_1']
tagClassLvl_1 = config['tagClassLvl_1']

personalTagLvl_0 = config['personalTagLvl_0']
personalTagClass_0 = config['personalTagClass_0']
personalTagLvl_1 = config['personalTagLvl_1']
personalTagClass_1 = config['personalTagClass_1']

### Constants.
today = date.today()
outputPath = "C:/Data/scrapeFaculty/{0}_{1}.csv".format(school, today.strftime("%Y_%m_%d"))

def fetchUrl(url):
	### Create the Soup Object.
	response = urllib.request.urlopen(url)
	#print(response.info())
	html = response.read()
	response.close()
	return BeautifulSoup(html, 'html.parser')
	#print(soup.prettify())

### Fetch url.
print("Fetching {0} data.".format(school))
soup = fetchUrl(url)

### Create output file.
outputFile = open(outputPath, 'w', newline='')
outputWriter = csv.writer(outputFile)


### Get tags.
lvl_00 = soup.find_all(tagLvl_0[0], {'class' : tagClassLvl_0[0]})
lvl_01 = soup.find_all(tagLvl_0[1], {'class' : tagClassLvl_0[1]})
for i in range(0, len(lvl_00)):
	lvl10 = lvl_00[i].find_all(tagLvl_1[0], {'class': tagClassLvl_1[0]})
	lvl11 = lvl_01[i].find_all(tagLvl_1[1], {'class': tagClassLvl_1[1]})
	for j in range(0, len(lvl10)):
		name = lvl10[j].getText()
		title = lvl11[j].getText()
		personalUrl = "http://mitsloan.mit.edu" + lvl10[j]['href']
		print("Name: {0}, Title: {1}, Website: {2}".format(name, title, personalUrl))
		### Call personalUrl Scraper
		print("Fetching personal Url for {0}.".format(Name))
		personalUrlScraper(personalUrl)
		outputWriter.writerow(name, title, personalUrl)
outputFile.close()
print("Finished writing {0} data.".format(school))

### Scrape Personal websites
#example: http://mitsloan.mit.edu/faculty-and-research/faculty-directory/detail/?id=9051


#Example: 
# html_doc: http://mitsloan.mit.edu/faculty-and-research/faculty-directory/
# tagList:	[div class="alphabetical-section" id="A", [div class="left column", [a]], ]
def htmlScraper(html_doc, tagList, tagAttList):
	if (len(tagList != len(tagAttList))):
		raise DimError('the tag and tag attribute lists must have the same length.')
	if (len(tagList) == 0):
		raise NullError('There has to be at least one tag.')

	### Base Case: just one tag
	if (len(tagList) == 1):
		#return 
		result = html_doc.find_all(tagList[0], {'class': tagAttList[0]})
		return result
	else:
		for i in range(0, len(tagList)):
			html_docs = html_doc.find_all(tagList[i], {tagAttList[i]})
			for html_doc in html_docs:
				UrlScraper(html_doc, tagList[1:], tagAtt[1:])

