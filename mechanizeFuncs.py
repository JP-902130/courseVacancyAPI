import mechanize


def getCourseForm(courseName, courseID):
    url = "https://classes.uwaterloo.ca/under.html"
    pg = mechanize.Browser()
    pg.set_handle_robots(False)
    r = pg.open(url)  # open page

    pg.select_form(nr=0)
    control = pg.find_control('subject')
    control.value = [courseName]
    pg.form["cournum"] = courseID  # <input> name

    # pg.method = "POST"  # form method
    r = pg.submit()  # submitting form

    s = r.read()
    return s
