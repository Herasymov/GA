import numpy as np

#целевая функция
def func(x, l):
    res=0
    res1=[]
    for j in x:
        res=0
        for i in range(len(l)):
            res+=l[i]*(j**(len(l)-1-i))
        res1.append(res - (j+3)*np.cos(j))
    return res1

def sort(x, y):
    for i in range(len(x)):
        for j in range(len(x)-1-i):
            d=0
            for k in range(len(y[i])):
                if abs(y[j][k]) > abs(y[j+1][k]):
                    d+=1
                else:
                    d-=1
            if d>0:        
                y[j],y[j+1]=y[j+1],y[j]
                x[j+1],x[j]=x[j],x[j+1]
    return x,y

def crossover(p1, f1, n,x):
    for i in range(5):
        for j in range (i+1, 5):
            #первый кросовер среднее арифметическое/Размножение (скрещивание)
            d1=p1[i].copy()
            k=2
            for m in range(n+1):
                d1[m] = (p1[i][m] + p1[j][m]) / 2
            if d1 not in p1:
                p1.append(d1)
                f1.append(func(x,d1)) 
            #коэффициентыРазмножение (скрещивание)#2 
            while k!=n+1:
                d1=p1[i].copy()
                for m in range(k,n+1):
                    d1[m] =  p1[j][m].copy()
                
                if d1 not in p1:
                    p1.append(d1)
                    f1.append(func(x,d1)) 
                k+=1
    #негативные коэффициенты / Мутирование        
    for i in range(5):
        d1 = p1[i].copy()
        for m in range(n+1):
            d1[m] *=-1
        if d1 not in p1:
            p1.append(d1)
            f1.append(func(x,d1)) 
    #рандомные новые мутации
    for i in range(5):
        d1 = list(np.random.uniform(-100,100,[n+1]))
        if d1 not in p1:
            p1.append(d1)
            f1.append(func(x,d1)) 
    #Вычислить значение целевой функции для всех особей и селекция
    p1,f1=sort(p1,f1)
    p2=[]
    f2=[]
    #выбираем топ 10
    for i in range(5):
        p2.append(p1[i])
        f2.append(f1[i])
    return p2,f2

def generation2(n,x,m):
    p=[]
    f=[]
    it=0
    for i in range(5):
        p.append(list(np.random.uniform(-100,100,[n+1])))
        f.append(func(x,p[i]))
    p,f=sort(p, f)
    
    while it<m:
        it+=1
        p,f=crossover(p,f, n,x)
        print("подождите осталось времени до ответа: ", m-it+1)
    return(p[0])
      
        
#main
n = int(input("Ведите степень полинома: "))
ans=0
x=[-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1,1.25,1.5,1.75,2]
ans=0
m=50000
s=''
t=generation2(n,x,m)
for i in range(len(t)):
    s+=str(t[i])+"*x^"+str(len(t)-i-1)+" + "
print("Ответ:")
print(s[:-3])


