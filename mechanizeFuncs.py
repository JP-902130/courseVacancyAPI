# Returns a beautifulSoup object
import mechanize
from bs4 import BeautifulSoup
import course
import re


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
    resObj = course.course([], 0, 0)

    beautifulSoupObj = getCourseForm(courseName, courseID)

    text1 = beautifulSoupObj.find_all('td', recursive=True)

    filtered = filter(lambda obj: re.search("^LEC", str(obj.string)), text1)

    allTh = list(filtered)[0].parent.parent.find("tr").find_all("th")

    for i in range(len(allTh)):
        if allTh[i].string == "Enrl Cap":
            resObj.indexOfCap = i
            resObj.indexOfTot = i+1
            break
    filtered = filter(lambda obj: re.search("^LEC", str(obj.string)), text1)
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
    for each in allSections:
        resObj.list1.append(each)

    return resObj
