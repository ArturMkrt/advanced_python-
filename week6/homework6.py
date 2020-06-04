import json
dt = {'C':3,'B':2,'A':1}
print(json.dumps(dt,sort_keys=True,indent=4))


import json
js = sampleJson = """{ "company":{"employee":{"name":"emma","payble":{"salary":7000,"bonus":800 }}}}"""
dt = json.loads(js)
print(dt['company']['employee']['payble']['salary'])

class Vehicle:
    def __init__(self, name, engine, price):        
        self.name = name        
        self.engine = engine        
        self.price = price
        
vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
print(json.dumps(vehicle.__dict__,indent=4))
#reverse
class Vehicle:
    def __init__(self, name, engine, price):        
        self.name = name        
        self.engine = engine        
        self.price = price        
def reverse_to_object(j):
    return Vehicle(j['name'],j['engine'],j['price'])
data = json.loads('{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}',object_hook=reverse_to_object)
print(data)



import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
#5
for elem in root.iter('genre'):
    print(elem.tag,elem.attrib)
#6
elemDict = {}
for elem in root.iter():
    elemDict[elem.tag] = True
tags = list(elemDict.keys())
print(tags)
#7
for elem in root.findall('.//movie/[year="1992"]'):
    print(elem.attrib)
#8
for elem in root.findall('.//movie/format/[@multiple="Yes"]/..'):
    print(elem.attrib)
#9
movie = root.find('.//movie/[@title="Back 2 the Future"]')
movie.set('title','Back to the Future')
tree.write('movies.xml')

#10
import re
import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
for form in root.findall("./genre/decade/movie/format"):
    if form.attrib['multiple'] == 'False':
        form.set('multiple','No')
for form in root.findall("./genre/decade/movie/format"):
    match = re.search(',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')
tree.write("movies.xml")
#11
import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()

for genre in root.findall("./genre"):
    a = []
    x = {}
    for decade in genre.findall('./decade'):
        yearsINT = int(decade.attrib['years'][0:4])
        x[yearsINT] = decade
        for movie in decade.findall("./movie"): 
            year = movie.find("year")
            if int(year.text)-yearsINT>=10:
                a.append(movie)
                decade.remove(movie)

    for movie in a:
        temp  = (int(movie.find('./year').text[:-1])*10)
        if temp in x:
            x[temp].append(movie)
        else:
            new_decade = ET.SubElement(genre,"decade")
            new_decade.append(movie)
            new_decade.attrib["years"] = "{}s".format(temp)
            x[temp] = new_decade
tree.write("new.xml")