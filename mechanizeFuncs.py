# Returns a beautifulSoup object
import mechanize
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
