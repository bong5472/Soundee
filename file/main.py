from colorcheck import *
from imgcheck import *
# from youtube import *

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



src = './img3.jpg'

rgb_arr, rgb_percent = imgchecking(src)
print(rgb_arr)
point = []
for i in range(len(rgb_arr)):
    point.append([color_check(rgb_arr[i])[0],rgb_percent[i]])

search_word = point[1][0] + ', ' + point[0][0] + ', ' + point[2][0] +', playlist'
print(search_word)