import requests
import re
from bs4 import BeautifulSoup
import urllib
import webbrowser

data = raw_input("Enter the name of the book and the format: ")
stringobject = 'https://www.google.co.in/search?q='+data
req  = requests.get(stringobject)


soup = BeautifulSoup(req.text)

#f=open('frankensteing web scrap.txt','w')
#f.write(str(soup))
#f.close()
#pattern = '<cite>.*</cite>'
#m = re.match(pattern, str(soup))
new = 2
m = soup.findAll('cite')
firsttime = True
for link in m:
	data = link.get_text()
	gate = re.match('.*.pdf',data)
	
	if gate!="none":
		 try:
			 if(firsttime == True):
	               		 webbrowser.open_new(data)
				 firsttime = False
			 else:
				webbrowser.open_new_tab(data)
              		 print "Webpage opened: "+data
       		 except:
        		  print "some error. system crashed"
	

print '\n\nFUNCTION COMPLETE'
