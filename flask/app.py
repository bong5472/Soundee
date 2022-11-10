
from flask import Flask, render_template, request
from PIL import Image
from imgcheck import *
from colorcheck import *

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/output',methods=['GET','POST'])
def output():
    img_file = request.files["file"]
    result1, result2 = imgchecking(img_file)
    search_word = color_check(result1) + ', ' + color_check(result2) + ', ' + 'playlist'
    print(search_word)
    return render_template('output.html')



# 파이썬 명령어로 실행할 수 있음
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)