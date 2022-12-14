import time
import requests
import bs4
import os
import status

class Memory:
    def __init__(self):
        self.byteSize = 0
    def add(self, size):
        if "KiB" in size:
            self.byteSize += float(float(size[0:-4])*1024**1) 
        elif "MiB" in size:
            self.byteSize += float(float(size[0:-4])*1024**2)
        elif "GiB" in size:
            self.byteSize += float(float(size[0:-4])*1024**3)
        elif "TiB" in size:
            self.byteSize += float(float(size[0:-4])*1024**4)
        else:
            self.byteSize += float(float(size[0:-2]))
    def __str__(self) -> str:
        if self.byteSize/1024**3 > 1024:
            return str(round(self.byteSize/1024**4, 3))+" TiB"
        if self.byteSize/1024**2 > 1024:
            return str(round(self.byteSize/1024**3, 3))+" GiB"
        if self.byteSize/1024**1 > 1024:
            return str(round(self.byteSize/1024**2, 3))+" MiB"
        if self.byteSize/1024**0 > 1024:
            return str(round(self.byteSize/1024**1, 3))+" KiB"
        return str(self.byteSize)+" B"

size = Memory()

def list_links(url):
    try:
        result = requests.get(url, timeout=1)
    except:
        while not requests.get(url):
            result = requests.get(url)
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



def calc_size(url, num_of_spaces=0):
    current_folder = list_links(url)
    for link in current_folder:
        if link["size"] != '-':
            status.status_print(num_of_spaces*"  ", link["name"], link["size"], size=size, sep=None)
            size.add(link["size"])
    for link in current_folder:
        if link["size"] == '-':
            status.status_print(num_of_spaces*"  ",link["name"], ":", size=size, sep=None)
            calc_size(url+link["name"], num_of_spaces+1)
    status.status_print(size=size, sep=None)
    
if __name__ == '__main__':
    url = "https://dl.astralinux.ru/astra/testing/orel/repository/pool/smb-heimdal/t/"
    calc_size(url)
    print(size)
    print(status.last_status)
