import requests
import bs4
import os

def list_links(url):
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    tbody = soup.find("tbody")
    tr = tbody.find_all("tr")
    links = []
    for i in tr:
        link = i.find("td", {"class":"link"}).find("a").get("href")
        size = i.find("td", {"class":"size"}).text
        links.append({"name":link, "size":size})
    
    return links[1:]    


def build_tree(url, num_of_spaces=0):
    current_folder = list_links(url)
    #if link is file
    for link in current_folder:
        if link["size"] != '-':
            print(num_of_spaces*"  ", link["name"], sep=None)
    #if link is folder
    for link in current_folder:
        if link["size"] == '-':
            print(num_of_spaces*"  ",link["name"], ":", sep=None)
            build_tree(url+link["name"], num_of_spaces+1)


url = "https://dl.astralinux.ru/astra/testing/orel/repository/pool/main/b/"
# for i in list_links(url):
#     print(i)
build_tree(url)
# parent_dir = os.getcwd()
# print(parent_dir)
# os.mkdir(os.path.join(parent_dir,url.split('/')[len(url.split('/'))-2]))

    



