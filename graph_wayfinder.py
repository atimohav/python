from tkinter import *
from math import *

maxN=10
N=4
orientation=0
ortxt=['Граф неориентированый', 'Граф ориентированый']
A=0
B=3
matrix = [[0] * maxN for i in range(maxN)]
matrix_d = [0] * maxN
labN = [[0] * maxN for i in range(maxN)]
entM = [[0] * maxN for i in range(maxN)]
paths=[]
bestpaths=[]
pathsbtn=[]
r=20
x0=200
y0=200


def task(a, b, deep, gone, l, N):
    if deep==0:
        paths.clear()
    if a>maxN or b>maxN:
        return inf
    gone[a]=deep+1
    if a==b:
        paths.append(gone+[l])
        return 0
        
    minl=inf
    for i in range(N):
        if matrix[i][a]!=0 and gone[i]==0:
            j=matrix[i][a]+task(i, b, deep+1, gone[0:N], l+matrix[i][a], N)
            if minl>j:
                minl=j
            elif minl==j:
                pass
    return minl

def ore(event):
    global orientation, matrix
    orientation=1-orientation
    event.widget['text']=ortxt[orientation]
    if orientation==0:
        for i in range(maxN):
            for j in range(i):
                if matrix[i][j]!=matrix[j][i]:
                    matrix[i][j],matrix[j][i]=0,0
                    entM[i][j]['text'],entM[j][i]['text']='0','0'
    update()

def pathe(event):
    k_=-1*(event.widget['wraplength']+1)
    drawcan(len(bestpaths[k_])-2, k_)
            
def btne(event):
    event.widget['text']=1-int(event.widget['text'])
    if orientation==0:
        for i in range(maxN):
            for j in range(maxN):
                if entM[i][j]['text']!=entM[j][i]['text']:
                    entM[i][j]['text']=event.widget['text']
                    entM[j][i]['text']=event.widget['text']
            
    for i in range(maxN):
        for j in range(maxN):
            matrix[i][j]=int(entM[i][j]['text'])
    
    update()
            

#####################################################################################################################
def drawcan(N, selectedpath):
    sc=0.85
    p=0.4
    can.create_rectangle(0, 0, 2*x0, 2*y0, fill='white', outline='white')
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==1:
                fill_='grey'
                if selectedpath!=-1:
                    if abs(paths[bestpaths[selectedpath][N+1]][i]-paths[bestpaths[selectedpath][N+1]][j])==1 and paths[bestpaths[selectedpath][N+1]][i]!=0 and paths[bestpaths[selectedpath][N+1]][j]!=0:
                        fill_='red'
                x1,y1,x2,y2=x0+x0*sc*cos(i*2*pi/N), y0+y0*sc*sin(i*2*pi/N), x0+x0*sc*cos(j*2*pi/N), y0+y0*sc*sin(j*2*pi/N)
                x1,y1,x2,y2=x1+r*(x2-x1)/((x1-x2)**2+(y1-y2)**2)**0.5,y1+r*(y2-y1)/((x1-x2)**2+(y1-y2)**2)**0.5,x2-r*(x2-x1)/((x1-x2)**2+(y1-y2)**2)**0.5,y2-r*(y2-y1)/((x1-x2)**2+(y1-y2)**2)**0.5
                if matrix[i][j]==matrix[j][i]:
                    can.create_line(x1,y1,x2,y2, fill=fill_)
                else:
                    can.create_line(x2,y2,x1,y1, fill=fill_, arrow=LAST)
    for i in range(N):
        can.create_oval(x0+x0*sc*cos(i*2*pi/N)-r, y0+y0*sc*sin(i*2*pi/N)-r, x0+x0*sc*cos(i*2*pi/N)+r, y0+y0*sc*sin(i*2*pi/N)+r, fill='white', outline='black')
        can.create_text(x0+x0*sc*cos(i*2*pi/N), y0+y0*sc*sin(i*2*pi/N),
              text='v'+str(i+1),
              justify=CENTER, font="Verdana 14")
    can.update()
    

#####################################################################################################################
def update():
    N=int(entN.get())
    if N>maxN:
        entN.delete(0, END)
        entN.insert(0, maxN)
        N=maxN
    
    for i in range(maxN):
        labN[0][i].grid_forget()
        labN[1][i].grid_forget()
        for j in range(maxN):
            entM[i][j].grid_forget()
            
    for i in range(N):
        labN[0][i].grid(row=i+4, column=0)
        labN[1][i].grid(row=3, column=i+1)
        for j in range(N):
            entM[i][j].grid(row=j+4, column=i+1)
    
    A=int(entA.get())-1
    B=int(entB.get())-1


    bestpaths.clear()
    res=task(A, B, 0, [0] * N, 0, N)
    if res==inf:
        txt='Пути из A в B (из v'+str(A+1)+' в v'+str(B+1)+') не существует.'
    else:
        txt='Длина кратчайшего пути из A в B (из v'+str(A+1)+' в v'+str(B+1)+') = '+str(res)+'\nКратчайшие пути из A в B:'
        l=0
        for i in paths:
            if i[N]==res:
                bestpaths.append([0]*(N+2))
                bestpaths[-1][N+1]=l
                for j in range(N):
                    for k in range(N):
                        if i[k]-1==j:
                            bestpaths[-1][j]=k+1
                            #txt+='v'+str(k+1)
                            if k==B:
                                #txt+='\n'
                                bestpaths[-1][N]=j+1
                            else:
                                pass
                                #txt+='-'
            l+=1
            
    for i in pathsbtn:
        i.grid_forget()
    pathsbtn.clear()
    k=0
    for i in bestpaths:
        btntxt=''
        for j in range(i[N]):
            btntxt+='v'+str(i[j])
            if j!=i[N]-1:
                btntxt+='-'
        pathsbtn.append(Button(root, text=btntxt))
        pathsbtn[-1]['wraplength']=-k-1
        pathsbtn[-1].bind('<Button-1>', pathe)
        pathsbtn[-1].grid(row=maxN+5+k,column=maxN+1)
        k+=1

    labres.config(text=txt)
    drawcan(N, -1)
    root.update()
##############################################################################
root = Tk()
root.title('Поиск путей в графе')
root.geometry('1280x720')
#root.attributes('-fullscreen', True)

header = Frame(root)
btn = Button(header, text='Обновить')
btn.config(command=update)
btn.pack(side=LEFT)
entO = Button(header, text = ortxt[orientation])
entO.bind('<Button-1>', ore)
entO.pack(side=RIGHT)
header.grid(row=0, columnspan = maxN)

entN = Entry(root)
entN.insert(0, N)
entN.grid(row=1, columnspan = maxN)


for i in range(maxN):
    labN[0][i]=Label(root, text='v'+str(i+1), fg='blue', width=0)
    labN[1][i]=Label(root, text='v'+str(i+1), fg='blue', width=0)
    for j in range(maxN):
        if i==j:
            entM[i][j]=Label(root, width=0, text='0')
        else:
            entM[i][j]=Button(root, width=0)
            entM[i][j].bind('<Button-1>', btne)
            entM[i][j].config(text=str(matrix[j][i]))

for i in range(N):
    labN[0][i].grid(row=i+4, column=0)
    labN[1][i].grid(row=3, column=i+1)
    for j in range(N):
        entM[i][j].grid(row=j+4, column=i+1)
            

can = Canvas(root, width=2*x0, height=2*y0)

frameAB=Frame(root)
frameAB.grid(row=maxN+4, column=0, rowspan=maxN, columnspan=maxN)
labA=Label(frameAB,text='A:')
entA=Entry(frameAB, width=5)
entA.insert(0, A+1)

labB=Label(frameAB,text='B:')
entB=Entry(frameAB, width=5)
entB.insert(0, B+1)

labres=Label(root, text='', bg='white')

can.grid(row=0, column=maxN+1, columnspan = maxN, rowspan = maxN+4)
labA.grid(row=0, column=0)
entA.grid(row=0, column=1)
labB.grid(row=1, column=0)
entB.grid(row=1, column=1)
labres.grid(row=maxN+4, column=maxN+1)

update()
root.mainloop()
