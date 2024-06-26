#0. install all the requirements
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/"

#1. get the html
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
#2. parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')


#commonly used types of objects
#1 tag : title = souptitle print(title)
#2 navigabestring : print(title.string)
#3 beautifulsoup : print(soup.prettify())
#4 comment
#3. html tree traversal


