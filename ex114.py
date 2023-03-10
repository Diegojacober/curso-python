import urllib, urllib.request

try:
    site = urllib.request.urlopen('https://www.thiagoopto.online')
except urllib.error.URLError:
    print('Não foi possivel acessar o site')
else:
    print('O site o esta acessivel')
    print(site.read())