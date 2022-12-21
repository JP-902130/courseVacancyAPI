from flask import Flask
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import tools
import mechanizeFuncs
executor = ThreadPoolExecutor(2)

app = Flask(__name__)


@app.route('/jobs')
def run_jobs():

    while True:
        executor.submit(some_long_task1(input("course"), input("code")))
        isquit = input("quit?")
        if isquit == 'q':
            break
    return 'running'


def some_long_task1(course, code):
    try:
        courseObj = mechanizeFuncs.getCourseSections(course, int(code))
        hasSeat = tools.hasSeats(courseObj)
        print(hasSeat)
    except Exception as e:
        print("Your course choice is not available next semester")


if __name__ == '__main__':
    app.run()
