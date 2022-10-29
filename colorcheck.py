#color check
import pandas as pd

mood = pd.read_csv('./mood.csv',encoding='euc-kr')

def color_check(target_color):
    t_red,t_green,t_blue = target_color
    t_mood = ''
    color_dist = 700
    for i in range(len(mood)):
        print('check==',i)
        dist = ((t_red - mood.iloc[i][0])**2 + (t_green - mood.iloc[i][1])**2 + (t_blue - mood.iloc[i][2])**2)**(1/2)
        if color_dist > dist:
           print('change : ',i)
           color_dist = dist
           t_mood = mood.iloc[i][5]
    return t_mood, color_dist 
    
print(color_check([255,10,152]))
    
    
    