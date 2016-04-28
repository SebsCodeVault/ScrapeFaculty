from bs4 import BeautifulSoup #scrape library
import urllib.request #url library
import csv #csv writing


######Thoughts: We always want: Name, Position, Website, Email, Office, Phone, Picture
### Constants.
url = "http://mitsloan.mit.edu/faculty-and-research/faculty-directory/"
home = "C:/Data/scrapeFaculty"
outputDir = "C:/Data/scrapeFaculty/mitsloan.csv"
tagLvl_0 = ['div', 'div']
tagClassLvl_0 = ['left-column', 'right-column']
tagLvl_1 = ['a', 'span']
tagClassLvl_1 = ['', '']

### Create the Soup Object.
response = urllib.request.urlopen(url)
#print(response.info())
html = response.read()
response.close()
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

### Save to .csv.
outputFile = open(outputDir, 'w', newline='')
outputWriter = csv.writer(outputFile)

### Get tags.
lvl_00 = soup.find_all(tagLvl_0[0], {'class' : tagClassLvl_0[0]})
lvl_01 = soup.find_all(tagLvl_0[1], {'class' : tagClassLvl_0[1]})
for i in range(0, len(lvl_00)):
	lvl10 = lvl_00[i].find_all(tagLvl_1[0], {'class': tagClassLvl_1[0]})
	lvl11 = lvl_01[i].find_all(tagLvl_1[1], {'class': tagClassLvl_1[1]})
	for j in range(0, len(lvl10)):
		print("Name: {0}, Title: {1}, Website: http://mitsloan.mit.edu{2}".format(lvl10[j].getText(), lvl11[j].getText(), lvl10[j]['href']))
		outputWriter.writerow([lvl10[j].getText(), lvl11[j].getText(), "http://mitsloan.mit.edu" + lvl10[j]['href']])
outputFile.close()

### Scrape Personal websites
#example: http://mitsloan.mit.edu/faculty-and-research/faculty-directory/detail/?id=9051

'div' 'alignleft  wrapText'
'img' 'alignleft' ['src']
'uk' 'contact-info'