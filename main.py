from rich.console import Console
from rich.table import Table

VALS = ["itemString", "marketValue", "minBuyout", "historical", "numAuctions"]
table = Table(title="Cooking profits")
with open("E:\Spill\World of Warcraft\_retail_\Interface\AddOns\TradeSkillMaster_AppHelper\AppData.lua", "r") as f:
    x = f.readlines()
    for k in x:
        if '"AUCTIONDB_MARKET_DATA","Draenor"' in k:
            k = k.replace("},", "},\n")
            with open("nydata.txt", "w+") as nf:
                nf.write(k)


def bubble_sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                _tmp = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = _tmp
    return sub_li


def findPrice(val):
    with open("nydata.txt", "r") as mf:
        for i in mf.readlines():
            i = i.replace("{", "").replace("}", "").split(",")
            i.pop()
            if val in i[0]:
                return [int(x) for x in i]


def format_gold(val):
    gold = val / 10000 % 100
    silver = val / 100 % 100
    copper = val % 100
    if (gold <= 1):
        gold = 0
    if (silver <= 1):
        silver = 0
    if (copper <= 1):
        copper = 0

    return "%sg %ss %sc" % (round(gold, 0), round(silver, 0), round(copper, 0))


def to_copper(val):
    gold = val[0]
    silver = val[1]
    copper = val[2]
    silver = silver + (gold * 100)
    copper = copper + (silver * 100)
    return copper


# Materials prices
ls = findPrice("173032")
sfp = findPrice("173036")
iria = findPrice("173033")
ss = findPrice("179315")
rsw = findPrice("172054")
tr = findPrice("172053")
ccm = findPrice("179314")

# Vendor materials
sap = to_copper([4, 50, 0]) / 5
iav = to_copper([3, 75, 0]) / 5
lwf = to_copper([3, 50, 0]) / 5
rgm = to_copper([4, 25, 0]) / 5
mots = to_copper([5, 0, 0]) / 5

# Crafts prices
spinsouf = {
    'name': "Spinefin Souffle",
    'minBuy': findPrice("172041")[2],
    'minBuy_F': format_gold(findPrice("172041")[2]),
    'market': findPrice("172041")[1],
    'market_F': format_gold(findPrice("172041")[1]),
    'craftMin': (sfp[2] * 3) + (iria[2] * 3) + (sap * 4) + (
            iav * 2),
    'craftMin_F': format_gold(
        (sfp[2] * 3) + (iria[2] * 3) + (sap * 4) + (
                iav * 2)),
    'craftMarket': (sfp[1] * 3) + (iria[1] * 3) + (sap * 4) + (
            iav * 2),
    'craftMarket_F': format_gold(
        (sfp[1] * 3) + (iria[1] * 3) + (sap * 4) + (
                iav * 2))
}

ir = {
    'name': "Iridescent_Ravioli",
    'minBuy': findPrice("172049")[2],
    'market': findPrice("172049")[1],
    'minBuy_F': format_gold(findPrice("172049")[2]),
    'market_F': format_gold(findPrice("172049")[1]),
    'craftMin': (ls[2] * 3) + (iria[2] * 3) + (lwf * 2) + (
            iav * 1),
    'craftMin_F': format_gold(
        (ls[2] * 3) + (iria[2] * 3) + (lwf * 2) + (iav * 1)),
    'craftMarket': (ls[1] * 3) + (iria[1] * 3) + (lwf * 2) + (
            iav * 1),
    'craftMarket_F': format_gold(
        (ls[1] * 3) + (iria[1] * 3) + (lwf * 2) + (iav * 1))
}

salam = {
    'name': "Steak_a_la_Mode",
    'minBuy': findPrice("172051")[2],
    'market': findPrice("172051")[1],
    'minBuy_F': format_gold(findPrice("172051")[2]),
    'market_F': format_gold(findPrice("172051")[1]),
    'craftMin': (ss[2] * 3) + (rsw[2] * 3) + (mots * 2) + (
            iav * 2),
    'craftMin_F': format_gold((ss[2] * 3) + (rsw[2] * 3) + (mots * 2) + (
            iav * 2)),
    'craftMarket': (ss[1] * 3) + (rsw[1] * 3) + (mots * 2) + (
            iav * 2),
    'craftMarket_F': format_gold(
        (ss[1] * 3) + (rsw[1] * 3) + (mots * 2) + (
                iav * 2))
}

tcr = {
    'name': "Tenebrous_Crown_Roast",
    'minBuy': findPrice("172045")[2],
    'market': findPrice("172045")[1],
    'minBuy_F': format_gold(findPrice("172045")[2]),
    'market_F': format_gold(findPrice("172045")[1]),
    'craftMin': (tr[2] * 3) + (ccm[2] * 3) + (mots * 4) + (
            rgm * 2),
    'craftMin_F': format_gold(
        (tr[2] * 3) + (ccm[2] * 3) + (mots * 4) + (
                rgm * 2)),
    'craftMarket': (tr[1] * 3) + (ccm[1] * 3) + (mots * 4) + (
            rgm * 2),
    'craftMarket_F': format_gold(
        (tr[1] * 3) + (ccm[1] * 3) + (mots * 4) + (
                rgm * 2))
}

_c = [ir, salam, tcr, spinsouf]
_p = []
for l in _c:
    _p.append([l['name'], format_gold(int(l['craftMin'] * 3) - int(l['minBuy']))])

max = max([_p[0][1], _p[1][1], _p[2][1], _p[3][1]])

_p = bubble_sort(_p)
_p.reverse()

cols = ["Navn", "Profit for 1"]
for col in cols:
    table.add_column(col)

for row in _p:
    table.add_row(*row, style='bright_green')

console = Console()
console.print(table)
