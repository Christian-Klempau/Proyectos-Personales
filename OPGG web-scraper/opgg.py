from lxml import html
import requests
nombres = open("opgg.csv", "r", encoding="UTF8")

jungla = []
top = []
mid = []
adc = []
support = []

for linea in nombres:
    linea = linea.strip()
    linea = linea.split(",")
    name = linea[1]
    if name.count(" ") > 1:
        name = name.replace(" ", "+")
    page = "https://las.op.gg/summoner/userName="+name
    print(page)
    page = requests.get(page)
    tree = html.fromstring(page.content)
    rank = tree.xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[2]/text()')
    print(rank)
    if rank[0].find("Unranked") != -1:
        rank = "Unranked"
    else:
        rank = rank[0]
    if linea[4] == "ADC":
        adc.append([linea[1], rank])
    elif linea[4] == "Mid":
        mid.append([linea[1], rank])
    elif linea[4] == "Support":
        support.append([linea[1], rank])
    elif linea[4] == "Jungle":
        jungla.append([linea[1], rank])
    elif linea[4] == "Top":
        top.append([linea[1], rank])

    if linea[5] == "ADC":
        adc.append([linea[1], rank])
    elif linea[5] == "Mid":
        mid.append([linea[1], rank])
    elif linea[5] == "Support":
        support.append([linea[1], rank])
    elif linea[5] == "Jungle":
        jungla.append([linea[1], rank])
    elif linea[5] == "Top":
        top.append([linea[1], rank])

    #print(rank)
print("JUNGLA")
for user in jungla:
    print(user)
print("TOP")
for user in top:
    print(user)
print("ADC")
for user in adc:
    print(user)
print("MID")
for user in mid:
    print(user)
print("SUPPORT")
for user in support:
    print(user)