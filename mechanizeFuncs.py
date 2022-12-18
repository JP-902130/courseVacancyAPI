# Returns a beautifulSoup object
import mechanize
import re
from bs4 import BeautifulSoup


def getCourseForm(courseName, courseID):
    url = "https://classes.uwaterloo.ca/under.html"
    pg = mechanize.Browser()
    pg.set_handle_robots(False)
    r = pg.open(url)
    pg.select_form(nr=0)
    control = pg.find_control('subject')
    control.value = [courseName]
    pg.form["cournum"] = str(courseID)
    r = pg.submit()
    soup = BeautifulSoup(r, "lxml")
    return soup


def getCourseSections(courseName, courseID):
    beautifulSoupObj = getCourseForm("MATH", 135)

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

    filtered = filter(lambda lst: re.search("^[0-9]", lst[0]), allSections)
    allSections = list(filtered)
    return allSections
