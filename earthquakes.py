import requests
import json
from bs4 import BeautifulSoup as bs4

try:
    
    r = requests.get('https://www.emsc-csem.org/#2')

    soup = bs4(r.text,features="html.parser")
    
    a=soup.find("div", {"id": "tbl_cont"})
    
    b=a.findAll(string=True)
    
    c=[i for i in b[24:-2:1]]
    d=[]
    e=[]
    z=""
    
    for i in c:

        i=i.replace("\u00a0"," ")
  
        e.append(str(i))
        if i=="\n":
            d.append(e[0:-1:1])
            e=[]
            
    d.append(e)
    
    for i in range(len(d)):
        
        a=d[i].index("earthquake")

        x = {
            "id": i+1,
            "date": d[i][a+1].split()[0],
            "time": d[i][a+1].split()[1],
            "latitude": float(d[i][-9][0:-2:1]),
            "longitude": float(d[i][-7][0:-2:1]),
            "depth": float(d[i][-5]),
            "size": float(d[i][-3]),
            "location": d[i][-2][1::],
            "attribute":"-"
        }
        
        y = json.dumps(x)
        z=z+","+y

    z="["+z[1::]+"]"
    
    f = open("demofile.json", "w")
    f.write(z)
    f.close()
    print("done")

except Exception as e:
    
    print(e)
