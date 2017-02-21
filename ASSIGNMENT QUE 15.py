#QUESTION
"""
Write a Python function to create the HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> 'Python' add_tags('b', 'Python Tutorial') -> 'Python Tutorial '
"""

#FUNCTION TO CREATE CUSTOME TAGS

def add_tags(tag, content, closingtag):
	return( "  <%s><%s><%s>" %(tag, content, closingtag))

#---------------------------------------------------------

print("<!DOCTYPE html>\n<html>\n <body>\n")

#*********OUR CREATED TAGS ARE HERE**************

print(add_tags("i", "Your Sample Code Here", "i"))
print(add_tags("b", "SOMETHING ELSE HERE ", "b"))

#----CLOSING TAG FOR HTML OPTIONAL---------

print(" </body>\n</html>")
