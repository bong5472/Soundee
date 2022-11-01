from colorcheck import *
from imgcheck import *

src = './img3.jpg'

rgb_arr, rgb_percent = imgchecking(src)
print(rgb_arr)
point = []
for i in range(len(rgb_arr)):
    point.append([color_check(rgb_arr[i])[0],rgb_percent[i]])

search_word = point[0][0] + ', ' + point[1][0] + ', playlist'
print(search_word)