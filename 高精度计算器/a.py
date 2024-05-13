def qj(a):
    aa=a.split(".")
    if (len(aa)==1):
        aa+="0"
    a=aa[0]+"."+aa[1]
    while(a[0]=="0" and a[1]!="."):
        a=a[1:]
    if (len(aa)==1):
        return a
    while(a[-1]=="0" and a[-2]!="."):
        a=a[:-1]
    return a

def jf(a,b):
    if (a[0]=="-"):
        return (jif(b,a[1:]))
    if (a=="" or a=="0"):
        return qj(b)
    elif (b=="" or b=="0"):
        return qj(a)
    c=""
    d=""
    e="0"
    aa=[]
    bb=[]
    aa=a.split(".")
    bb=b.split(".")
    if (len(aa)==1):
        aa+="0"
    if (len(bb)==1):
        bb+="0"
    if (aa[0]==""):
        aa[0]="0"
    if (bb[0]==""):
        bb[0]="0"
    if len(aa[0])>len(bb[0]):
        aa[0],bb[0]=bb[0],aa[0]
    while (len(aa[0])!=len(bb[0])):
        aa[0]="0"+aa[0]
    if len(aa[1])>len(bb[1]):
        aa[1],bb[1]=bb[1],aa[1]
    while (len(aa[1])!=len(bb[1])):
        aa[1]=aa[1]+"0"
    a=aa[0]+"."+aa[1]
    b=bb[0]+"."+bb[1]
    for j in range(len (a)):
        if (a[-j-1]=="."):
            c="."+c
            continue
        d=str(int(a[-j-1])+int(b[-j-1])+int(e))
        e="0"
        if (len(d)!=1):
            e="1"
        c=d[-1]+c
    if (len(d)!=1):
        c=d[0]+c
    return qj(c)

def cf(a,b):
    if (a=="1"):
        return qj(b)
    elif (b=="1"):
        return qj(a)
    elif (a=="0" or b=="0" or a=="" or b==""):
        return 0
    if (a[0]=="-" and b[0]=="-"):
        return cf(a[1:],b[1:])
    if (a[0]=="-"):
        return ("-"+cf(a[1:],b))
    if (b[0]=="-"):
        return ("-"+cf(a,b[1:]))
    c=""
    d=""
    e="0"
    f=0
    aa=[]
    bb=[]
    aa=a.split(".")
    bb=b.split(".")
    if (len(aa)==1):
        aa+="0"
    if (len(bb)==1):
        bb+="0"
    if (aa[0]==""):
        aa[0]="0"
    if (bb[0]==""):
        bb[0]="0"
    a=aa[0]+aa[1]
    b=bb[0]+bb[1]
    f=len(aa[1])+len(bb[1])
    for j in range(len (b)):
        d="0.0"
        for k in range(int(b[-j-1])):
            d=jf(d,a)
        d=d[:-2]+"0"*j
        c=jf(d,c)
    if (c[-2]!="."):
        c+=".0"
    while (len(c)<abs(-f-3)):
        c="0"+c
    c=c[:-f-2]+"."+c[-f-2:-2]
    return qj(c)

def jif(a,b):
    if (a=="" or a=="0"):
        return("-"+qj(b))
    elif (b=="" or b=="0"):
        return qj(a)
    if (a[0]=="-" and b[0]!="-"):
        return ("-"+jf(a[1:],b))
    if (a[0]!="-" and b[0]=="-"):
        return (jf(a,b[1:]))
    if (a[0]=="-" and b[0]=="-"):
        return ("-"+jif(a[1:],b[1:]))
    c=""
    d=""
    e="0"
    e1="0"
    aa=[]
    bb=[]
    aa=a.split(".")
    bb=b.split(".")
    if (len(aa)==1):
        aa+="0"
    if (len(bb)==1):
        bb+="0"
    if (aa[0]==""):
        aa[0]="0"
    if (bb[0]==""):
        bb[0]="0"
    if (len(aa[0])>len(bb[0])):
        while (len(aa[0])>len(bb[0])):
            bb[0]="0"+bb[0]
    if (len(aa[0])<len(bb[0])):
        while (len(aa[0])<len(bb[0])):
            aa[0]="0"+aa[0]
    if (len(aa[1])>len(bb[1])):
        while (len(aa[1])>len(bb[1])):
            bb[1]+="0"
    if (len(aa[1])<len(bb[1])):
        while (len(aa[1])<len(bb[1])):
            aa[1]+="0"
    a=aa[0]+"."+aa[1]
    b=bb[0]+"."+bb[1]
    for j in range(len (a)):
        if (a[-j-1]=="."):
            c="."+c
            continue
        d=str(int(a[-j-1])-int(b[-j-1])-int(e))
        if (d[0]!="-"):
            e="0"
        if (d[0]=="-"):
            d=str(int ("1"+a[-j-1])-int(b[-j-1])-int(e))
            e="1"
        c=d[-1]+c
    if (e=="1"):
        e1="1"+"0"*len(aa[0])
        return ("-"+jif(e1,c))
    if (c[0]=="0"):
        while (c[0]=="0" and c[1]!="."):
            c=c[1:]
    return qj(c)

def chf(a,b):#200位
    if (b=="1"):
        return qj(a)
    if (a=="0"):
        return 0
    if (b=="0"):
        return "Math ERROR"
    if (a[0]=="-" and b[0]=="-"):
        return chf(a[1:],b[1:])
    if (a[0]=="-"):
        return ("-"+chf(a[1:],b))
    if (b[0]=="-"):
        return ("-"+chf(a,b[1:]))
    c=""
    d=""
    e="0"
    f="0"
    g="0"
    h="0"
    aa=[]
    bb=[]
    ee=[]
    aa=a.split(".")
    bb=b.split(".")
    if (len(aa)==1):
        aa+="0"
    if (len(bb)==1):
        bb+="0"
    if (aa[0]==""):
        aa[0]="0"
    if (bb[0]==""):
        bb[0]="0"
    if (len(bb[1])>len(aa[1])):
        while (len(bb[1])>len(aa[1])):
            aa[1]+="0"
    if (len(bb[1])<len(aa[1])):
        while (len(bb[1])<len(aa[1])):
            bb[1]+="0"
    a=aa[0]+aa[1]
    b=bb[0]+bb[1]
    if (a[-1]=="0" and b[-1]=="0"):
        while (a[-1]=="0" and b[-1]=="0"):
            a=a[:-1]
            b=b[:-1]
    for i in a:
        ee=e.split(".")
        ee[0]+=i
        g=ee[0]
        for j in range (10):
            h=str(cf(b,str(j)))
            f=str(jif(g,h))
            if (f[0]=="-"):
                f="0"
                break
            d=str(j)
        h=str(cf(b,d))
        e=str(jif(g,h))
        c+=d
    if (e=="0.0"):
        return qj(c)
    c+="."
    for i in range (201):
        ee=e.split(".")
        ee[0]+="0"
        g=ee[0]
        for j in range (10):
            h=str(cf(b,str(j)))
            f=str(jif(g,h))
            if (f[0]=="-"):
                break
            d=str(j)
        h=str(cf(b,d))
        e=str(jif(g,h))
        c+=d
        if (e=="0.0"):
            break
    if (int(c[-1])>=5 and e!="0.0"):
        c=c[:-2]+str(int(c[-2])+1)
    return qj(c)

def sz(a,e=0):
    b=[]
    c=[]
    d=""
    if (a[0]=="-" and a[1]=="("):
        a="0"+a
    if (a[0]=="-" or a[0]=="+"):
        a="0"+a
    for i in range(len(a)):
        if (a[i-1]=="(" and a[i]=="-"):
            d+=a[i]
            continue
        if a[i] in "0123456789.":
            d+=a[i]
        if a[i] in "+-*/()":
            b+=a[i]
            if (d!="" and d!="-" and d!="+"):
                c.append(d)
                d=""
    if (d!=""):
        c.append(d)
    if (e==0):
        return b
    if (e==1):
        return c

def yx(a):
    b=0
    c=[]
    for i in a:
        if (i=="("):
            b+=3
        if (i in "*/"):
            b+=2
            c.append(b)
            b-=2
        if (i in "+-"):
            b+=1
            c.append(b)
            b-=1
        if (i==")"):
            b-=3
    return c

def px(a):
    b=[0]*len(a)
    c=sorted(a,reverse=True)
    d=0
    for i in range(0,len(a)):
        d=a.index(c[i])
        a[d]=0
        b[d]=i+1
    return b

def jc(sz,ff,sx):
    sxx=0
    sxy=""
    sz1=""
    sz2=""
    daa=""
    for i in range (1,len(sx)+1):
        sxx=sx.index(i)
        sxy=ff[sxx]
        sz1=sz[sxx]
        sz2=sz[sxx+1]
        if (sz1=="Math ERROR" or sz2=="Math ERROR"):
            return "Math ERROR"
        if (sxy=="+"):
            daa=jf(sz1,sz2)
        elif (sxy=="-"):
            daa=jif(sz1,sz2)
        elif (sxy=="*"):
            daa=cf(sz1,sz2)
        elif (sxy=="/"):
            daa=chf(sz1,sz2)
        sz.pop(sxx+1)
        sz.pop(sxx)
        sz.insert(sxx,daa)
        ff.pop(sxx)
        sx.pop(sxx)
    return sz[0]
#-----------------------------------------------------------------------#
print ("计算式存放在当前文件夹中的question.txt文件夹中。")
print ("答案储存在当前文件夹中的answer.txt文件夹中。")
print ("加: + 减: - 乘: * 除: /")
print ("输入任意字符继续:")
while 1:
    try:
        input ()
        ci=open(r"question.txt","r")
        break
    except:
        print ("未找到文件，请重试！")
        continue
cii=[]
cis=[]
ciz=[]
yxx=[]
yxz=[]
daa=""
da=open("answer.txt","w")
for i in ci:
    cii+=i
    cis+=sz(i)
    ciz+=sz(i,1)
    yxx+=yx(cis)
    cis=[x for x in cis if (x!="(")]
    cis=[x for x in cis if (x!=")")]
    yxx=px (yxx)
    if (len(ciz)!=(len(cis)+1)):
        daa="Math ERROR"
        da.write(daa+"\n")
        cis=[]
        ciz=[]
        yxx=[]
        continue
    daa=jc (ciz,cis,yxx)
    da.write(daa+"\n")
    cis=[]
    ciz=[]
    yxx=[]
da.close()
