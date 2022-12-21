from flask import Flask
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import tools
import mechanizeFuncs
executor = ThreadPoolExecutor(2)

app = Flask(__name__)


@app.route('/jobs')
def run_jobs():

    executor.submit(some_long_task1)
    return 'running'


def some_long_task1():
    try:
        courseObj = mechanizeFuncs.getCourseSections("CS", 138)
        hasSeat = tools.hasSeats(courseObj)
        print(hasSeat)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run()
