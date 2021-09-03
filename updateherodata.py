import urllib.request as req
import bs4
import json

urls = "https://docs.google.com/spreadsheets/d/14uJKxlri8FxYd_3MatRKeog9oqNSd-48zUTmqu3rEjc/htmlview#"
request = req.Request(urls, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")
hero_data = root.find("div", id="1091616240").find_all("tr" , style="height: 20px")
with open("herodata.json", "w",encoding="utf8") as file:   
    jsonstring ='{'
    for sheet in range(13,232):                     #update here
        hero = hero_data[sheet].find_all("td")      #https://docs.google.com/spreadsheets/d/14uJKxlri8FxYd_3MatRKeog9oqNSd-48zUTmqu3rEjc/htmlview#
        jsonstring = jsonstring + '"'+ hero[3].text +'":{\n'
        jsonstring = jsonstring + '"攻擊力":'+hero[4].text+',\n'
        jsonstring = jsonstring + '"生命力":'+hero[5].text+',\n'
        jsonstring = jsonstring + '"防禦力":'+hero[6].text+',\n'
        jsonstring = jsonstring + '"速度":'+hero[7].text+',\n'
        jsonstring = jsonstring + '"暴擊":'+hero[8].text+',\n'
        jsonstring = jsonstring + '"暴傷":'+hero[9].text+',\n'
        jsonstring = jsonstring + '"效命":'+hero[11].text+',\n'
        jsonstring = jsonstring + '"效抗":'+hero[12].text+'\n}'
        if sheet !=231 :
            jsonstring += ',\n'
        else:
            jsonstring += '\n}'
    jsonstring = json.loads(jsonstring)
    json.dump(jsonstring, file,indent = 2,ensure_ascii = False)         #indent=縮排幾字元, ensure_ascii = 顯示中文
file.close()
