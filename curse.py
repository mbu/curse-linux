#!/usr/bin/python

#source: http://forum.ubuntuusers.de/topic/curse-client-fuer-linux-nicht-world-of-warcraf/

import urllib2
import csv
import os
from zipfile import ZipFile
from bs4 import BeautifulSoup
from time import sleep

def getFile(url):
    response = urllib2.urlopen(url)
    data = response.read()
    filename = url.split('/')[-1]
    with open(filename, 'wb') as zipped:
        zipped.write(data)
    zipped = ZipFile(filename)
    zipped.extractall('./Interface/AddOns/')
    updated.append(filename)
    os.remove(filename)
    return filename

addons = []
updated = []

with open('addons.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        addons.append(row)

for i in range(len(addons)):
    sleep(1)
    request = urllib2.Request(addons[i][0] + '/download', headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'})
    response = urllib2.urlopen(request)
    html = response.read()

    soup = BeautifulSoup(html)
    for link in soup.findAll('a'):
        zipfile = link.get('data-href')
        if zipfile != None:
            if len(addons[i]) == 1:
                version = getFile(zipfile)
                if len(addons[i]) == 2:
                    addons[i][1] = version
                else: addons[i].append(version)
            elif zipfile.split('/')[-1] != addons[i][1]:
                version = getFile(zipfile)
                if len(addons[i]) == 2:
                    addons[i][1] = version
                else: addons[i].append(version)

with open('addons.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for i in range(len(addons)):
        csvwriter.writerow(addons[i])

if len(updated) == 0:
    message = 'All Addons upto date'
else:
    message = 'Following Addons were updated:'
    for element in updated:
        message = message + '\n' + element
print message;
