import requests
from bs4 import BeautifulSoup
import argparse

#get url
parser = argparse.ArgumentParser(description = 'Code Scraper for javatpoint')
parser.add_argument('url', type = str, help = 'javatpoint url where the code has to be scrapped')
args = parser.parse_args()



#request stuff
url = args.url
r = requests.get(url)

#parse to html
get = BeautifulSoup(r.text,"html.parser")

#grab things
sitename = get.find(property="og:site_name")
titlecontent = get.find(property='og:title')
Codecontent = get.findAll(True,class_='codeblock')

#tranfer content
tname = titlecontent['content']
sname = sitename['content']

#comment lines for files
ftname = "<!--"+titlecontent['content']+"-->\n"
fsname =  "<!--"+sitename['content']+"-->\n"

#file writing portion
fname = tname + ".html"
fdo = open(fname,"w+")
fdo.write(fsname)
fdo.write(ftname)
for item in Codecontent:
    if item != '':
        if Codecontent.index(item) == 0:
            itemx = "<!--"+str(item.find('textarea').contents[0])+"-->\n"
            fdo.write("<!--Syntax-->\n")
            fdo.write(str(itemx))
        else:
            fdo.write('<!--Code-->\n\n')
            for i in range(len(item.find('textarea').contents)):
                if len(str(item.find('textarea').contents[i])) > 4:
                    fdo.write(str(item.find('textarea').contents[i]))
fdo.close()
