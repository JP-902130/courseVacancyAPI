from bs4 import BeautifulSoup
import requests
import mechanizeFuncs

beautifulSoupObj = mechanizeFuncs.getCourseForm("MATH", 135)


# releventRows = beautifulSoupObj.find("table").findAll("tr")[
#     2].findAll("tr")[1:]

text1 = beautifulSoupObj.find_all('td', recursive=True)
filtered = filter(lambda obj: obj.string == 'LEC 001 ', text1)
allTR = list(filtered)[0].parent.parent.find_all("tr")[1:]

allSections = []
for tr in allTR:
    section = []
    allTD = tr.find_all("td")
    for each in allTD:
        if each.string:
            section.append(each.string.strip())
    allSections.append(section)

for section in allSections:
    print(section)
# for row in releventRows:
#     allTDs = row.findAll("td")
#     strings = []
#     for td in allTDs:
#         if td.string:
#             strings.append(td.string.strip())
#     print(strings)
