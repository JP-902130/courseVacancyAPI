import course
import re


def hasSeats(courseObj):

    courseList = courseObj.list1
    indexOfCap = courseObj.indexOfCap
    indexOfTot = courseObj.indexOfTot

    for sec in courseList:
        print(sec)
        if re.search("^LEC", sec[1]):
            if int(sec[indexOfCap]) > int(sec[indexOfTot]):
                return True

    return False
