import requests

#imgURL = "https://fackel.oeaw.ac.at/php/getPage.php?keyString=02-037_n0002&type=img&"
# alternative is to get it from archive.org

prefix = ['01-001', '02-037', '03-037', '04-100', '05-135', '06-159', '07-179']

for volume in prefix:
    for i in range(1, 40): # estimate <= 40 pages or less, not checked
        imgURL = "https://fackel.oeaw.ac.at/php/getPage.php?keyString=%s_n00%s&type=img&"%(volume, ('%02d' % i))
        print(imgURL)
        
        img_data = requests.get(imgURL).content
        with open('fackel-%s_n00%s.jpg'% (volume, '%02d' %i), 'wb') as handler:
            handler.write(img_data)
    
