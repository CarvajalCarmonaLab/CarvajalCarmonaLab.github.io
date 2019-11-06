import xml.etree.ElementTree as ET

tree = ET.parse('luispublications.txt')
root = tree.getroot()

o = open('pubsformatted.txt','w+')

for child in root:
	article = child.find('MedlineCitation').find('Article')
	journal = article.find('Journal')
	jname = journal.find('ISOAbbreviation').text
	title = article.find('ArticleTitle').text
	date = journal.find('JournalIssue').find('PubDate')
	if date.find('Month') != None or date.find('Year') != None:
		if date.find('Month') != None and date.find('Year') != None:
			pubdate = date.find('Month').text+" "+date.find('Year').text+" - "
		elif date.find('Month') != None:
			pubdate = date.find('Month').text+" - "
		elif date.find('Year') != None:
			pubdate = date.find('Year').text+" - "
	else:
		pubdate = " "
	for pid in child.find('PubmedData').find('ArticleIdList'):
		if pid.attrib['IdType'] == 'pubmed':
			pm_id = pid.text
		else:
			pm_id = ""
	o.write("<br>\n")
	o.write("<p>"+pubdate+ jname + "</p>\n")
	o.write("<a href=\"http://www.ncbi.nlm.nih.gov/pubmed/"+pm_id+"\">"+title+"</a>")
	o.write("\n")
