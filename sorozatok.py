from datetime import datetime

#feladat 1

datacards = []

with open("lista.txt", "r") as file:
    content = file.read().splitlines()
    rows = len(content)
    datacardsum = int(rows / 5)
    for x in range(datacardsum):
        x = x*5
        datacards.append({"date": content[x-5], "name": content[x-4], "episode number": content[x-3], "playtime": content[x-2], "seen it": content[x-1]})

       
#feladat 2

print("2. feladat")

counter = 0

for datacard in datacards:
    if datacard["date"] != "NI":
        counter = counter + 1

print(str(counter) + " epizódnak ismert a megjelenési dátuma")

#feladat 3

print("3. feladat")

seenit = 0

for datacard in datacards:
    if datacard["seen it"] == "1":
        seenit = seenit + 1

print(round((seenit/datacardsum)*100,2), "%-át látta hősünk a sorozatoknak")

#feladat 4

print("4. feladat")

elapsed = 0

for datacard in datacards:
    if datacard["seen it"] == "1":
        elapsed = int(datacard["playtime"]) + elapsed

day = elapsed//1440
hour = (elapsed%1440)//60
min = elapsed%60

#hour = (elapsed//60) - (day * 24)
#min = elapsed - (hour * 60) - (day * 1440)

print("Hősünk összesen " , day, " nap " , hour, " óra és " , min, " perc ideig nézett sorozatot")

#feladat 5

print("5. feladat")
dateinraw = input("Adjon meg egy dátumot! Dátum=")

def date_fromstring(datestring):
    datelist = datestring.split(".")
    dateint = int(datelist[0]+datelist[1]+datelist[2])
    return dateint


for datacard in datacards:
    if datacard["date"] != "NI":
        if date_fromstring(datacard["date"]) <= date_fromstring(dateinraw) and datacard["seen it"] == "0":
            print(datacard["episode number"] + "\t" + datacard["name"])

"""
#datein = datetime.strptime(dateinraw, '%Y.%m.%d')
for datacard in datacards:
    if datacard["date"] != "NI":
        datadate = datetime.strptime(datacard["date"], '%Y.%m.%d')
        if  datadate <= datein and datacard["seen it"] == "0":
            print(datacard["episode number"] + "\t" + datacard["name"])
"""

#feladat 6

def hetnapja(ev, ho, nap:int):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
    hetnap = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]
    return hetnap

#feladat 7
"""
print("7. feladat")
dayname = input("Adja meg a hét egy napját (például cs)! Nap= ")

serialname=[]

for datacard in datacards:
    if datacard["date"] != "NI":
        evhonap = datacard["date"].split(".")
        weekday = hetnapja(int(evhonap[0]), int(evhonap[1]), int(evhonap[2]))
        if weekday == dayname:
            serialname.append(datacard["name"])

serialname = set(serialname)

for serial in serialname:
    print(serial)

#feladat 8

serials = []

for datacard in datacards:
    serials.append(datacard["name"])

serials = set(serials)

lines = []

for serial in serials:
    episodes = 0
    playtime = 0
    for datacard in datacards:
        if datacard["name"]==serial:
            episodes = episodes + 1
            playtime = int(datacard["playtime"]) + playtime
    lines.append((str(serial) + " " + str(playtime) + " " + str(episodes) + "\n"))

with open("summa.txt", "w") as wf:
    content = ""
    for line in lines:
        content = content + line
    wf.write(content)
"""