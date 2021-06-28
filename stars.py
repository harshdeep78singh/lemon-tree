# please suggest changes if u feel something wrong
# like ,share and subscribe

import os

n=7
if n%2==0: 
    n=n+1
elif n>9:
    n=9
elif n<=3:
    n=3

def a():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n-1):
            if n-i-1==j or i==j-n+1 or (i==int(n/2) and (j>=n-i-1 and j<=i+n-1)):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr    

def b():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if (i==0 and j!=n-1) or j==0 or (i==n-1 and j!=n-1) or (i==int(n/2) and j!=n-1 ) or (j==n-1 and (i not in [int(n/2),0,n-1])):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def C():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if (i==0 and j != 0 ) or (j==0 and i != 0 and i!=n-1) or (i==n-1 and j!=0):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def d():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if (i==0 and j != n-1 ) or (j==0) or (i==n-1 and j!=n-1) or (j==n-1 and i!=n-1 and i!=0):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def e():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if i==0 or j==0 or i==n-1 or (i==int(n/2) and j<=int(n/2) ):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def f():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if i==0 or j==0  or (i==int(n/2) and j<=int(n/2) ):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def g():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n):
            if (i==0 and j != 0 and j<=n ) or (j==0 and i != 0 and i!=n-1) or (i==n-1 and j!=0 and j<=n) or (i>=int(n/2) and j==n) or (i==int(n/2) and j>n) or (i>=int(n/2) and j==2*n-1):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def h():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n+1):
            if j==0 or j==n or i==int(n/2):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def i():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if i==0 or i==n-1 or j==int(n/2):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def J():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if i==0 or (i==n-1 and j<=n/2) or j==int(n/2):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def k():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n-1):
            if j==0 or (j!=0 and n-i-2==j) or (j!=0 and i-int(n/2)+1==j):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def l():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n+1):
            if j==0 or i==n-1:
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def m():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n+2):
            if j==0 or (i==j and i<=int(n/2)+1) or (n-i+1==j and i<=int(n/2)+1) or j==n+1:
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def N():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n-1):
            if j==0 or 2*i==j or j==2*n-2 :
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def o():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if (j==0 and i!=0 and i!=n-1) or (i==0 and j!=0 and j!=n-1) or (j==n-1 and i!=n-1 and i!=0) or (i==n-1 and j!=0 and j!=n-1):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr    

def p():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if i==0 or j==0 or (j==n-1 and i<=int(n/2)) or i==int(n/2):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def q():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n):
            if (i==0 and j<=n+1) or j==0 or (i==n-1 and j<=n+1) or j==n+1 or (i>=int(n/2) and ((n+1)/2)+((i-int(n/2))*2)==j):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def r():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if i==0 or j==0 or (j==n-1 and i<=int(n/2)) or i==int(n/2) or (i-int(n/2))*2==j:
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def S():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if (i==0 and j!=0 and j!=n-1)  or (j==n-1 and i>int(n/2) and i!=n-1) or (j==0 and i<int(n/2) and i!=0) or (i==int(n/2) and j!=0 and j!=n-1) or (i==n-1 and j!=0 and j!=n-1) :
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def t():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if i==0 or j==int(n/2):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def u():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(n):
            if (j==0 and i!=n-1) or (j==n-1 and i!=n-1) or (i==n-1 and j!=0 and j!=n-1):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def v():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n):
            if i==j or i==2*n-j-2:
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def w():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n-int(n/2)):
            if (j==0 and i!=n-1) or (i==n-1 and j<n+1 and j!=0 and j!=((n+1)/2)) or (j==n+1 and i!=n-1)  or (i>=int(n/2) and j==((n+1)/2) and i!=n-1):
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def x():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n):
            if j==2*i or i==2*(n-j) :
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def ux():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n):
            if j==2*i or 2*i==2*n-j-1 :
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def ox():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n):
            if j==2*i or 2*i==2*n-j :
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def y():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n-int(n/2)):
            if (j==2*i and i<=int(n/2))  or i==2*(n-j) :
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def z():
    arr = []
    for i in range(n):
        temp= ""
        for j in range(2*n):
            if i==0 or i==n-1 or 2*i==2*n-j-1 :
                #print("*",end="")
                temp=temp+'*'
            else:
                #print(" ",end="")
                temp=temp+' '
        arr.append(temp)
    return arr

def find(a,b):
    x=0
    for i in range(b+1,len(a)):
        if(a[i]==' '):
            return x
        x=x+1
    return x


def Main():
    s="Harshdeep"
    s=s.lower()
    name={}
    sx=0
    c= os.get_terminal_size()
    c = c.columns//((n*2)+1)
    for _ in range(len(s)):
        if s[_].isalpha():
            if s[_]=='n':
                name[sx]=N()
                sx=sx+1
            elif s[_]=='s':
                name[sx]=eval("S()")
                sx=sx+1
            elif s[_]=='c':
                name[sx]=eval("C()")
                sx=sx+1
            elif s[_]=='j':
                name[sx]=eval("J()")
                sx=sx+1    
            else:   
                name[sx]=eval(s[_]+"()")
                sx=sx+1
        elif s[_]==' ':
            sp = []
            ls=find(s,_)
            for j in range(n):
                sp.append("     ")
            name[sx]=sp
            sx=sx+1
            if c-(len(name)%c)>ls:
                pass
            else:
                for ka in range(c-(len(name)%c)):
                    for ja in range(n):
                        sp.append("     ")
                    name[sx]=sp
                    sx=sx+1
        else:
            continue
    if len(name)%c==0:
        no_of_lines=int(len(name)/c)
    else:
        no_of_lines=(len(name)//c)+1
    if(len(name)%c==0):
        iteration = c
    else:
        iteration = len(name)%c
    for k in range(no_of_lines-1):
        for i in range(n):
            for j in range(c):
                print(name[(c*k)+j][i],' ',end="")
            print()
        print()

    for i in range(n):
        for j in range(iteration):
            print(name[(c*(no_of_lines-1))+j][i],' ',end="")
        print()
        

if __name__=="__main__":
    Main()
