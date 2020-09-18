from lxml import html
import requests
import matplotlib.pyplot as plt


page = "https://runescape.wiki/w/Module:Exchange/Shadow_nihil_pouch/Data"
page = requests.get(page)
tree = html.fromstring(page.content)
valores = tree.xpath('/html/body/div[3]/div[2]/div[4]/div[2]/pre/text()')
print(valores)
valores = valores[0]

valores = valores.splitlines()

valores = list(map(lambda x: x.strip(), valores))
valores = list(map(lambda x: x.replace(" ", ""), valores))
valores = list(map(lambda x: x.replace("'", ""), valores))
valores = list(map(lambda x: x.replace(",", ""), valores))
valores = list(map(lambda x: x.split(":"), valores))
valores = list(filter(lambda x: len(x) > 1, valores))
valores = list(map(lambda x: int(x[1]), valores))

#print(valores)
print(max(valores))

plt.plot(valores)
plt.show()


valores2 = []
for i in range(0, len(valores)-1, 2):
    valores2.append((valores[i]+valores[i+1])/2)

plt.plot(valores2)
plt.show()