from flask import Flask
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import mechanizeFuncs
executor = ThreadPoolExecutor(2)

app = Flask(__name__)


@app.route('/jobs')
def run_jobs():
    executor.submit(some_long_task1)
    return 'Two jobs were launched in background!'


def some_long_task1():
    courseLists = mechanizeFuncs.getCourseSections("MATH", 135)
    sleep(5)
    print(courseLists)


if __name__ == '__main__':
    app.run()
