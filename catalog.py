import os
from datetime import datetime

def FindBetween(s, first, last):
	try:
		start = s.index(first) + len(first)
		end = s.index(last, start)
		return s[start:end]
	except ValueError:
		return ""

def Create():
	date = datetime.now().strftime('%m/%d/%Y')
	dirs = os.listdir("Book")
	pages = []
	for d in dirs:
		if "html" in d and d != "index.html":
			pages.append(d)

	catalog = '''<html>\n<head>\n
	<title>Faerber Cookbook</title>\n
	<link rel="stylesheet" type="text/css" href="../Data/css/style.css">
	</head>\n<body>\n
	<img src="../Data/img/logo.png" width="100px"><br>
	<ul>
	'''

	for p in pages:
		rec = open("Book/" + p, "r").read()
		title = FindBetween(rec, "<title>", "</title>")
		catalog += "<li><a href='" + p + "'>" + title + "</a></li>\n"

	catalog += "</ul><br>" + date + "</body></html>"

	path = "Book/index.html"
	file = open(path, "w")
	file.write(catalog)
	print("Written catalog to " + path + "...")