import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, "html.parser")
#print(soup.prettify())

# Step 3: HTML Tree traversal
title = soup.title
#print(title)

paras = soup.find_all("p")
#print(paras)

anchors = soup.find_all("a")
#print(anchors)

#print(soup.find("p")) # Get first element in the HTML page
#print(soup.find("p")["class"])

#print(soup.find_all("p", class_="text-base")) # Get all the elements with class text-base

#print(soup.find("p").get_text())

# Get all the links on the page
all_links = set()
for link in anchors:
    #print(link.get("href"))
    if(link!="#"):
        all_links.add("https://codewithharry.com"+link.get("href"))
#print(all_links)


# Comments
markup = "<p><!--this is a comment --></p>"
soup2 = BeautifulSoup(markup)
#print(type(soup2.p.string))


navbarSupportedContent = soup.find(id="__next")
#print(navbarSupportedContent)
# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator

#for elem in navbarSupportedContent.contents:
#    print(elem)

#for item in navbarSupportedContent.strings:
#    print(item)
#print("\n")
#for item in navbarSupportedContent.stripped_strings:
#    print(item)

#print(navbarSupportedContent.parent)
print(navbarSupportedContent.parents)

for item in navbarSupportedContent.parents:
    print(item.name)