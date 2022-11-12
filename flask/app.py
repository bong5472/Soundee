
from flask import Flask, render_template, request
from PIL import Image
from imgcheck import *
from colorcheck import *
from youtube import *
import random

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
    result1, result2, result3 = imgchecking(img_file)
    search_word1 = color_check(result1) + ' ' + color_check(result2) + ' ' + '플레이리스트'
    search_word2 = color_check(result1) + ' ' + color_check(result3) + ' ' + '플레이리스트'
    search_word3 = color_check(result2) + ' ' + color_check(result3) + ' ' + '플레이리스트'

    print(search_word1)

    youtube_result = youtube_search(search_word1) + youtube_search(search_word2) + youtube_search(search_word3)
      
    video_id = random.sample(youtube_result,3)  
    return render_template('output.html',video_id1 = video_id[0]
                                        ,video_id2 = video_id[1]
                                        ,video_id3 = video_id[2]
                                        )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)