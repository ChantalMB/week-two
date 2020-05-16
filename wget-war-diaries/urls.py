# empty varible for url string
urls = '';

# file io
f = open('urls.txt','w')

# range x - 1
for x in range(8029, 8110):
    urls = 'http://data2.collectionscanada.ca/e/e061/e00151%d.jpg\n' % (x)
    f.write(urls)
f.close
