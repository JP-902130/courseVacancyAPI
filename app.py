from flask import Flask, request, jsonify
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import tools
import mechanizeFuncs
import os
executor = ThreadPoolExecutor(2)

app = Flask(__name__)


@app.route('/')
def f():
    return "main page"


@app.route('/getAvailability', methods=['GET'])
def run_jobs():
    courseName = request.args.get('courseName')
    courseCode = request.args.get('courseCode')
    try:
        if(request.method == 'GET'):

            courseObj = mechanizeFuncs.getCourseSections(
                courseName, int(courseCode))
            hasSeat = tools.hasSeats(courseObj)
            data = {
                "course": courseName+courseCode,
                "hasSpot": hasSeat,

            }
            return jsonify(data)
    except:
        data = {
            "course": courseName+courseCode,
            "hasSpot": False,
        }
        return jsonify(data)


# def some_long_task1(course, code):
#     try:
#         courseObj = mechanizeFuncs.getCourseSections(course, int(code))
#         hasSeat = tools.hasSeats(courseObj)
#         print(hasSeat)
#     except Exception as e:
#         print("Your course choice is not available next semester")
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
