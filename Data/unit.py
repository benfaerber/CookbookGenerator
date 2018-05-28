from __future__ import division
from datetime import datetime
print("Recipe Creator")

def Inp(question):
	return raw_input(question)

isMetric = False

imperial = [
	["teaspoon", "tsp"],
	["tablespoon", "tbsp"],
	["cup", "c"],
	["pint", "pt"],
	["quart", "qt"],
	["gallon", "gal"],
	["ounce", "oz"],
	["pound", "lb", "#"]
]

metric = [
	["milliliter", "ml", "milli"],
	["liter", "l"],
	["gram", "g"],
	["kilogram", "kg", "kilo"]
]

def GetUnit(unit):
	unit = unit.lower()
	unit = unit.replace(".", "")
	if unit[-1:] == "s":
		unit = unit[:-1]

	arr = metric if isMetric else imperial
	for row in arr:
		for col in row:
			if col == unit:
				return row[0]

def Convert(value, unit):
	num = 0
	if "/" in value:
		v = value.split("/")
		num = float(v[0]) / float(v[1])
	else:
		num = float(value)

	if unit == "cup":
		return str(num * 240)

	if unit == "milliliter":
		return str(num / 240)

'''
date = datetime.now().strftime('%m/%d/%Y')
title = Inp("Title: ")

print("Input ingredients, type / to finish")
rawIng = []
i = ""
while i != "/":
	i = Inp("")
	if "grams" in i or "ml" in i:
		isMetric = True

	if i != "/":
		rawIng.append(i)
'''

file = open("recipe.html", "w")
recipe = ""

rawIng = ["1 tbsp Salt", "2 cups sugar", "4 gallons water"]
recipe += "<script>\n"
for ing in rawIng:
	words = ing.split(" ")
	unit = words[1]
	n = GetUnit(unit)
	if n != "":
		unit = n
		Convert(words[0], words[1])
	words[1] = unit

	hold = ""
	for w in words:
		hold += w + " "
	hold = hold[:-1]