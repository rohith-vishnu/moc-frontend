import urllib.request
page = urllib.request.urlopen('http://hiscore.runescape.com/index_lite.ws?player=zezima')
print(page.read())