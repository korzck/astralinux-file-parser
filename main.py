import requests
import bs4
import os
import time
import size
import status
import urllib.request

memory = size.Memory()
url = "https://dl.astralinux.ru/astra/"

def download_filesys(url, folder_path, num_of_spaces=1):
    current_folder = size.list_links(url)
    for link in current_folder:
        if link["size"] != '-':
            status.status_print(num_of_spaces*"  ", link["name"], link["size"], size=memory, current_file=link["name"]+" "+link["size"], sep=None)
            memory.add(link["size"])
            if not os.path.exists(folder_path+link["name"]):
                try:
                    urllib.request.urlretrieve(url+link["name"], folder_path+link["name"])
                except:
                    pass
    for link in current_folder:
        if link["size"] == '-':
            try:
                new_folder = os.path.join(folder_path, link["name"])
                os.mkdir(new_folder)
            except:
                pass
            status.status_print(num_of_spaces*"  ",link["name"], ":", size=memory, sep=None)
            download_filesys(url+link["name"], new_folder, num_of_spaces+1)

    

parent_dir = os.getcwd()
# create base folder 
base_folder = os.path.join(parent_dir,url.split('/')[len(url.split('/'))-2]+'/')
try:
    os.mkdir(base_folder)
except:
    pass
download_filesys(url, base_folder)
status.status_print(size=memory, sep=None)
print()
print()
    




