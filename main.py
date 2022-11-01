from colorcheck import *
from imgcheck import *

src = './cafe.jpg'

rgb_arr, rgb_percent = imgchecking(src)
print(rgb_arr)
point = []
for i in range(len(rgb_arr)):
    point.append([color_check(rgb_arr[i])[0],rgb_percent[i]])
print(point[:2])