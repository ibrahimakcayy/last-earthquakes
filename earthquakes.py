import requests
import json


def details(detail_ids):
    
    rd = requests.get(f'https://www.emsc-csem.org/Earthquake/earthquake.php?id={detail_ids}')

    ad= rd.text.split('<table cellpadding="0" cellspacing="0" border="0" style="margin-top:5px; font-size:11px;">')[1].split('</table>')[0].split('</tr>')[-2]

    bd=ad.split('<tr><td class="point">Distances</td><td>')[1].split('<br />')

    return bd[1].replace("\n","")


try:
    
    r = requests.get('https://www.emsc-csem.org/Earthquake/world/?view=1')

    a= r.text.split('<tbody id="tbody">')[1].split('</tbody>')[0].split('</tr>')[0:-1:1]

    b=""
    date=""
    latitude=""
    longitude=""
    depth=""
    mag=""
    location=""
    last_updt=""
    ids=0
    z=""

    for i in a:
        
        b=i.split('</td>')

        date= b[3].split('</a>')[0].split('>')[-1].replace("&#160;"," ")

        ids=int(b[0].split()[1].split("id=")[1].replace('"',""))
        
        num_lat=b[4].split('<td class="tabev1">')[1].replace("&nbsp;"," ")
        text_lat=b[5].split('<td class="tabev2">')[1].replace("&nbsp;","")
        latitude=num_lat+text_lat

        num_lon=b[6].split('<td class="tabev1">')[1].replace("&nbsp;"," ")
        text_lon=b[7].split('<td class="tabev2">')[1].replace("&nbsp;","")
        longitude=num_lon+text_lon
        
        depth=b[8].split('<td class="tabev3">')[1]+" KM"

        mag=b[10].split('<td class="tabev2">')[1]+" "+b[9].split('>')[1].replace(" ","").upper()

        location=b[11].split('&#160;')[1]

        last_updt=b[12].split('>')[1]
        
        x = {
                "id": ids,
                "date": date.split()[0],
                "time": date.split()[1],
                "latitude": latitude,
                "longitude": longitude,
                "depth": depth,
                "size": mag,
                "location": location,
                "detail": details(str(ids))
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
