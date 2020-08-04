from turtle import *
import time

def sketch():
    speed(1500)
    bgcolor('black')
    r,g,b = 255,0,0
    for i in range(255*2):
        colormode(255)
        if i<255//3:
            g+=3
        elif i<255*2//3:
            r-=3
        elif i<255:
            b+=3
        elif i<255*4//3:
            g-=3
        elif i<255*5//3:
            r+=3
        elif i<255*6//3:
            b -=3
        else:
            continue
        fd(50+i)
        rt(91)
        pencolor(r,g,b)

if __name__ == "__main__":
    try:
        sketch()
    except KeyboardInterrupt:
        print('this is working')
        sketch()
