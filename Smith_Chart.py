from random import randint
from math import *
from tkinter import *

def sign(x):
    if x>0:
        return 1
    if x<0:
        return -1
    if x==0:
        return 0
    return None

def RGB(r, g, b):
    r = min(max(0, r), 1)
    g = min(max(0, g), 1)
    b = min(max(0, b), 1)
    rgb = (int(255*r),int(255*g),int(255*b))
    return "#%02x%02x%02x" % rgb

def colorwheel(angle):
    R=(angle)%360
    if R>180:
        R=360-R
    R=120-R
    G=(angle-120)%360
    if G>180:
        G=360-G
    G=120-G
    B=(angle+120)%360
    if B>180:
        B=360-B
    B=120-B

    R*=2
    G*=2
    B*=2
    R/=120
    G/=120
    B/=120

    return RGB(R, G, B)

class Imaginary:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
    def __neg__(self):
        return Imaginary(-self.Re, -self.Im)
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Imaginary(self.Re+other, self.Im)
        return Imaginary(self.Re+other.Re, self.Im+other.Im)
    def __radd__(self, other):
        return self+other
    def __sub__(self, other):
        return self+(-other)
    def __rsub__(self, other):
        return (-self)+other
    def __mul__(self, other):
        return Imaginary((self.Re*other.Re)-(self.Im*other.Im),
                         (self.Re*other.Im)+(self.Im*other.Re))
    def inverse(self):
        try:
            if self.Re**2+self.Im**2 == 0:
                return Imaginary(float(inf), float(inf))
        except OverflowError:
            return Imaginary(0, 0)
        return Imaginary(self.Re/(self.Re**2+self.Im**2),
                         -1*self.Im/(self.Re**2+self.Im**2))
    def __truediv__(self, other):
        if other.Re==0 and other.Im==0:
            return Imaginary(float(inf), float(inf))
        return self*other.inverse()

root = Tk()
root.title("Smith Chart")
root.geometry("1280x720")
canvas = Canvas(bg="white", width=1280, height=720)
canvas.pack(anchor=CENTER, expand=1)
image = PhotoImage(width=1280,height=720)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle
def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs.pop("end") - kwargs["start"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle_arc = _create_circle_arc

x0=1280//2
y0=720//2
R=300
G=Imaginary(0, 0)
Z=Imaginary(0, 0)
d=0.01

#круги+арки через проверку пикселя
for x in range(x0-R, x0+R):
    for y in range(y0-R, y0+R):
        G=Imaginary((y-y0)/R,(x-x0)/R)
        Z=(1+G)/(1-G)
        Gr=Imaginary((y-y0)/R,(x-x0+1)/R)
        Zr=(1+Gr)/(1-Gr)
        Gu=Imaginary((y-y0+1)/R,(x-x0)/R)
        Zu=(1+Gu)/(1-Gu)
        Re_coef=2
        Im_coef=2
        if Z.Re >= 0 and Z.Re!=float(inf) and Z.Im!=float(inf) and Zr.Re!=float(inf) and Zr.Im!=float(inf) and Zu.Re!=float(inf) and Zu.Im!=float(inf):
            if (int(Z.Re*Re_coef)+int(Z.Im*Im_coef))%2 != (int(Zr.Re*Re_coef)+int(Zr.Im*Im_coef))%2 or (int(Z.Re*Re_coef)+int(Z.Im*Im_coef))%2 != (int(Zu.Re*Re_coef)+int(Zu.Im*Im_coef))%2:
                image.put('black',(x, y))
        if sign(Z.Re)!=sign(Zr.Re) or sign(Z.Im)!=sign(Zr.Im) or sign(Z.Re)!=sign(Zu.Re) or sign(Z.Im)!=sign(Zu.Im):
            image.put('black',(x, y))

mouse_x=0
mouse_y=0
def callback(e):
    global mouse_x
    global mouse_y
    mouse_x = e.x
    mouse_y = e.y
    G=Imaginary((mouse_y-y0)/R,(mouse_x-x0)/R)
    Z=(1+G)/(1-G)
    ll.config(text="Z.Re: "+str(round(Z.Re,3))+", Z.Im: "+str(round(Z.Im,3)))
    ll.place(x=mouse_x, y=mouse_y, anchor='sw')

ll = Label(root, text="")
canvas.bind('<Motion>', callback)
canvas.create_image(0, 0, image = image, anchor=NW)
root.mainloop()

