from rich.console import Console
from rich.table import Table

# Calculates what Shadowlands cooking crafting recipe is the most profitable
# Reads TSM data from addon.
# Change path to file in PATH variable, to match that file in Addons folder
# Update REALM variable to change server


PATH = "E:\Spill\World of Warcraft\_retail_\Interface\AddOns\TradeSkillMaster_AppHelper\AppData.lua"
REALM = "Draenor"
REALM_DATA_FILE="DataFile.txt"
table = Table(title="Cooking profits")

# Reads addon data
with open(PATH, "r") as f:
    x = f.readlines()
    for k in x:
        if f'"AUCTIONDB_MARKET_DATA","{REALM}"' in k:
            k = k.replace("},", "},\n")
            with open(REALM_DATA_FILE, "w+") as nf:
                nf.write(k)


# Generic bubble sort to sort prices, sorts by 5th value in list. (idx 4)
def bubble_sort(lst):
    l = len(lst)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (lst[j][4] > lst[j + 1][4]):
                _tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = _tmp
    return lst


# Find price in TSM addon data
def find_price(val):
    with open(REALM_DATA_FILE, "r") as mf:
        for i in mf.readlines():
            i = i.replace("{", "").replace("}", "").split(",")
            i.pop()
            if val in i[0]:
                return [int(x) for x in i]


# Format copper to gold, silver and copper
def format_currency(val):
    gold = val / 10000 % 100
    silver = val / 100 % 100
    copper = val % 100
    if (gold < 1):
        gold = 0
    if (silver < 1):
        silver = 0
    if (copper < 1):
        copper = 0

    return "%sg %ss" % (round(gold, 0), round(silver, 0))


# Format gold, silver and copper into just copper
def to_copper(val):
    gold = val[0]
    silver = val[1]
    copper = val[2]
    silver = silver + (gold * 100)
    copper = copper + (silver * 100)
    return copper


# Materials prices
ls = find_price("173032")  # lost_sole
sfp = find_price("173036")  # sprinefin_piranha
iria = find_price("173033")  # iridecent_amberjack
ss = find_price("179315")  # shadowy_shank
rsw = find_price("172054")  # raw_sepraphic_wing
tr = find_price("172053")  # tenebrous_ribs
ccm = find_price("179314")  # creeping_crawler_meat

# Vendor materials
sap = to_copper([4, 50, 0]) / 5  # smuggled_azerothian_produce
iav = to_copper([3, 75, 0]) / 5  # inconceivable_aged_vinegar
lwf = to_copper([3, 50, 0]) / 5  # lusterwheat_flour
rgm = to_copper([4, 25, 0]) / 5  # rich_grazer_milk
mots = to_copper([5, 0, 0]) / 5  # medley_of_transplanar_spices

# Crafts prices
spinefin_souffle = {
    'name': "Spinefin Souffle",
    'minBuy': find_price("172041")[2],
    'minBuy_F': format_currency(find_price("172041")[2]),
    'market': find_price("172041")[1],
    'market_F': format_currency(find_price("172041")[1]),
    'craftMin': (sfp[2] * 3) + (iria[2] * 3) + (sap * 4) + (
            iav * 2),
    'craftMin_F': format_currency(
        (sfp[2] * 3) + (iria[2] * 3) + (sap * 4) + (
                iav * 2)),
    'craftMarket': (sfp[1] * 3) + (iria[1] * 3) + (sap * 4) + (
            iav * 2),
    'craftMarket_F': format_currency(
        (sfp[1] * 3) + (iria[1] * 3) + (sap * 4) + (
                iav * 2))
}

iridescent_ravioli = {
    'name': "Iridescent Ravioli",
    'minBuy': find_price("172049")[2],
    'market': find_price("172049")[1],
    'minBuy_F': format_currency(find_price("172049")[2]),
    'market_F': format_currency(find_price("172049")[1]),
    'craftMin': (ls[2] * 3) + (iria[2] * 3) + (lwf * 2) + (
            iav * 1),
    'craftMin_F': format_currency(
        (ls[2] * 3) + (iria[2] * 3) + (lwf * 2) + (iav * 1)),
    'craftMarket': (ls[1] * 3) + (iria[1] * 3) + (lwf * 2) + (
            iav * 1),
    'craftMarket_F': format_currency(
        (ls[1] * 3) + (iria[1] * 3) + (lwf * 2) + (iav * 1))
}

steak_a_la_mode = {
    'name': "Steak a la Mode",
    'minBuy': find_price("172051")[2],
    'market': find_price("172051")[1],
    'minBuy_F': format_currency(find_price("172051")[2]),
    'market_F': format_currency(find_price("172051")[1]),
    'craftMin': (ss[2] * 3) + (rsw[2] * 3) + (mots * 2) + (
            iav * 2),
    'craftMin_F': format_currency((ss[2] * 3) + (rsw[2] * 3) + (mots * 2) + (
            iav * 2)),
    'craftMarket': (ss[1] * 3) + (rsw[1] * 3) + (mots * 2) + (
            iav * 2),
    'craftMarket_F': format_currency(
        (ss[1] * 3) + (rsw[1] * 3) + (mots * 2) + (
                iav * 2))
}

tenebrous_crown_roast = {
    'name': "Tenebrous Crown Roast",
    'minBuy': find_price("172045")[2],
    'market': find_price("172045")[1],
    'minBuy_F': format_currency(find_price("172045")[2]),
    'market_F': format_currency(find_price("172045")[1]),
    'craftMin': (tr[2] * 3) + (ccm[2] * 3) + (mots * 4) + (
            rgm * 2),
    'craftMin_F': format_currency(
        (tr[2] * 3) + (ccm[2] * 3) + (mots * 4) + (
                rgm * 2)),
    'craftMarket': (tr[1] * 3) + (ccm[1] * 3) + (mots * 4) + (
            rgm * 2),
    'craftMarket_F': format_currency(
        (tr[1] * 3) + (ccm[1] * 3) + (mots * 4) + (
                rgm * 2))
}

# List of crafts to make
crafts = [iridescent_ravioli, steak_a_la_mode, tenebrous_crown_roast, spinefin_souffle]
# Temporary list to store prices and profits for calculations
_p = []

# Generate temporary list to view in table in terminal
for craft in crafts:
    _p.append([craft['name'], craft['minBuy_F'], craft['market_F'], craft['craftMin_F'], format_currency(int((craft['craftMin'] - (craft['minBuy'] / 3))))])

# Sort prices
_p = bubble_sort(_p)

# Reverse sorted list so most profitable comes first
_p.reverse()

# Cols for Table
cols = ["Navn", "Min buyout","Market value", "Craft cost for 1", "Profit for 1"]
# Populate table
# - Rows
for col in cols:
    table.add_column(col)
# - Columns
for row in _p:
    table.add_row(*row)

# Write to console
console = Console()
console.print(table)
