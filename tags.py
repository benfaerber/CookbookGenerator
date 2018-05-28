def Bold(t):
	return "<b>" + t + "</b>"

def ListElement(t):
	return "<li>" + t + "</li>\n"

def Header(t, size):
	return "<h" + str(size) + ">" + t + "</h" + str(size) + ">\n"

def Break():
	return "\n<br>\n"