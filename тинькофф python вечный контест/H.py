import math
X,Y=map(float,input().split())
crd=list(map(float,input().split()))
x0,y0=crd[0],crd[1]
scale=math.sqrt(((crd[0]-crd[4])**2+(crd[1]-crd[5])**2)/(X**2+Y**2))
alpha=math.atan2(crd[3]-crd[1], crd[2]-crd[0])

#x_=x0+x*scale*cos(alpha)-y*scale*sin(alpha)
#y_=y0+x*scale*sin(alpha)+y*scale*cos(alpha)
#x_=x
#y_=y

x=(x0*(1-scale*math.cos(alpha))-y0*scale*math.sin(alpha))/((scale*math.sin(alpha))**2+(1-scale*math.cos(alpha))**2)
y=(y0+x*scale*math.sin(alpha))/(1-scale*math.cos(alpha))
print(x, y)
