import urllib2, random, catalog
from datetime import datetime
from tags import *
print("Recipe Creator")

def Inp(question):
	return raw_input(question)

def FriendlyTitle(t):
	t = t.lower()
	rep = [
		[" ", "-"],
		[".", ""],
		[",", ""],
		["!", ""],
		["/", "-"]
	]
	for r in rep:
		t = t.replace(r[0], r[1])
	return t

def findBetween(s, first, last):
	try:
		start = s.index(first) + len(first)
		end = s.index(last, start)
		return s[start:end]
	except ValueError:
		return "" 

agents = open("Data/agents.txt").read().split("\n")
def RandomAgent():
    ran = random.randint(0, len(agents)-1)
    return agents[ran]

def Recipe(t, ingr, dire):
	date = datetime.now().strftime('%m/%d/%Y')
	recipe = '''<html>\n<head>\n
<title>''' + t + '''</title>\n
<link rel="stylesheet" type="text/css" href="../Data/css/style.css">
</head>\n<body>\n
<img src="../Data/img/logo.png" width="100px"><br>
'''
	recipe += Header(t, 1)

	# Ingredients list
	recipe += Bold("Ingredients") + Break()
	recipe += "<ul>\n"
	for i in ingr:
		if i == "":
			recipe += "<br>"
		else:
			recipe += ListElement(i)
	recipe += "</ul>\n\n"

	# Directions list
	recipe += Bold("Directions") + Break()
	recipe += "<ol>\n"
	for d in dire:
		recipe += ListElement(d)
	recipe += "</ol>\n"

	recipe += date + "<br><a href=\"index.html\">Home</a>\n</body>\n</html>"
	file = open("Book/" + FriendlyTitle(t) + ".html", "w")
	file.write(recipe)

title = Inp("Title or AllRecipes print URL: ")

# Manual type
print("Input ingredients, type / to finish")
rawIng = []
i = ""
while i != "/":
	i = Inp("")
	if i != "/":
		rawIng.append(i)

print("Input directions, type / to finish")
dirs = []
i = ""
while i != "/":
	i = Inp("")
	if i != "/":
		dirs.append(i)

Recipe(title, rawIng, dirs)
print("Wrote " + title + "...")
catalog.Create()