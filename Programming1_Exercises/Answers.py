#Exercicio 3.1
'''
A=int(input('numerador:'))
B=int(input('denominador:'))
print(A,'/',B,'=',int(A/B),'+',A%B,'/',B)
'''

#Exercicio 4.1
def area_triangulo(a,b,c):
    '''a,b,c lados do triângulo'''
    import math
    s=a+b+c/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

#Exercicio 4.4
def bissexto(n):
    if n%4==0 and not(n%100==0 and n%400!=0):
        return True
    else:
        return False

#Exercicio 4.5
def bissexto_tab(a,b):
    '''tabela de bissextos ou não de ano "a" a "b"'''
    while a<=b:
        if bissexto(a):
            print(a,'é bissexto')
            a=a+1
        else:
            print (a,'não é bissexto')
            a=a+1


#Exercicio 4.6
def algarismos(n):
    a=0
    while int(n)>0:
        n=int(n/10)
        a+=1
    return a


#Exercicio 4.7 a) e c)
def mindiv(n):
    import math
    a=1
    while True:
        a+=1
        if a==math.sqrt(n):
            return n
        if n%a==0:
            return a

#b)
def primo(n):
    a=mindiv(n)
    if a==n:
        return True
    else:
        return False

#Exercicio 4.8
def leibniz(k):
    a=0
    for i in range(k+1):
        a=a+((-1)**i)/(2*i+1)
    return 4*a

#Exercicio 4.9 a)
def soma2dados(k):
    import random
    c=0
    a=random.randint(1,6)
    b=random.randint(1,6)
    for i in range(50000):
        if a+b==k:
            c+=1
        a=random.randint(1,6)
        b=random.randint(1,6)
    return c/50000

#b)
def soma2dados_t():
    for i in range(2,13):
        print('Frequência da soma ser',i,'é:',soma2dados(i))


#Exercicio 5.1
def triangular(n):
    a=n
    for i in range(1,n+1):
        if a==0:
            return True
        elif a<=0:
            return False
        else:
            a=a-i


#Exercicio 5.2
def raiz(q,n):
    a=q/2
    for i in range(n):
        a=1/2*(a+q/a)
    return a

#Exercicio 5.3
def raiz_eps(q, epsilon):
    n=1
    a=raiz(q,n-1)
    b=raiz(q,n)
    while abs(a-b)>epsilon:
        a=b
        n+=1
        b=raiz(q,n)
    return b

#Exercicio 5.4
def binom(n,k):
    a=1
    b=1
    c=1
    for i in range(1,n+1):
        a=a*i
    for i in range(1,k+1):
        b=b*i
    for i in range(1,n-k+1):
        c=c*i
    return int(a/(b*c))

#Exercicio 5.5
def apenas_letras(txt):
    for i in txt:
        if not ('a'<=i<='z' or 'A'<=i<='Z'):
            return False
    return True

#Exercicio 5.6
def filtra_letras(txt):
    x=''
    for i in txt:
        if 'a'<=i<='z' or 'A'<=i<='Z':
            x=x+i
    return x

#Exercicio 5.7
def inversa(txt):
    x=''
    for i in range(len(txt)):
        x=x+txt[len(txt)-1-i]
    return x

#Exercicio 5.8 e 5.9
def palindromo(txt):
    txt=txt.lower()
    txt=filtra_letras(txt)
    if inversa(txt)==txt:
        return True
    else:
        return False

#Exercicio 5.10
def rem_espacos(txt):
    x=''
    for i in range(len(txt)):
        if txt[i]==' ' and txt[(i+1)%len(txt)]==' ':
            txt=txt[:i]+' '+txt[i+1:]
    return txt
    
#Exercicio 5.11
def vinegere(chave,mensagem):
    c=[]
    chave=chave.lower()
    for i in range(len(chave)):
        c=c+[ord(chave[i])-97]
    c=c*len(mensagem)
    a=''
    for i in range(len(mensagem)):
        if 'a'<=mensagem[i]<='z':
            a=a+chr(((ord(mensagem[i])-97)+int(c[i]))%26+97)
        elif 'A'<=mensagem[i]<='Z':
            a=a+chr(((ord(mensagem[i])-65)+int(c[i]))%26+65)
        else:
            a=a+mensagem[i]
    return a


#Exercicio 6.1
def forte(passwd):
    c=len(passwd)
    ma=0
    mi=0
    a=0
    for i in passwd:
        if 'a'<=i<='z':
            mi+=1
        if 'A'<=i<='Z':
            ma+=1
        if '0'<=i<='9':
            a+=1
    if (c>=8 and mi!=0 and ma!=0 and a!=0):
        return True
    else:
        return False

#Exercicio 6.2
def dup_vogais(txt):
    a=''
    for i in txt:
        if ('a'==i or 'e'==i or 'i'==i or 'o'==i or 'u'==i
            or 'A'==i or 'E'==i or 'I'==i or 'O'==i or 'U'==i):
            a=a+2*i
        else:
            a=a+i
    return a

#Exercicio 6.3 a)
def divisores(n):
    a=[]
    import math
    for i in range(1,int(n/2)+1):
        if n%i==0:
            a=a+[i]
    return a

#b)
def perfeito(n):
    a=divisores(n)
    b=sum(a)
    if b==n:
        return True
    else:
        return False


#Exercicio 6.4
def ocorrencias(txt,c):
    a=[]
    for i in range(len(txt)):
        if txt[i]==c:
            a=a+[i]
    return a

#Exercicio 6.5
def repetidos(lista):
    for i in range(len(lista)):
        if lista[i] in lista[i+1:]:
            return True
    else:
        return False


#Exercicio 6.6
def palavras(txt):
    a=''
    for i in range(len(txt)):
        if not ('a'<=txt[i]<='z' or 'A'<=txt[i]<='Z' or txt[i]==' '):
            a=a
        else:
            a=a+txt[i]
    return a.split()
            

#Exercicio 6.8
def pascal(n):
    l1=[1]
    l2=[1,1]
    if n==1:
        return l2
    elif n==0:
        return l1
    else:
        for i in range(n-1):
            l1=[1]
            for j in range(len(l2)-1):
                l1.append(l2[j]+l2[j+1])
            l1.append(1)
            l2=l1
        return l1
        
#Exercicio 6.9
def aniv(n):
    b=0
    import random
    for i in range(5000):
        a=[]
        for x in range(n):
            a.append(random.randint(1,365))
            if a[x] in a[:x]:
                b+=1
                break
    return b/5000

#Exercicio 7.1
def tab_log(x):
    import math
    for i in range(1,x+1):
        print('log(%02d)=%6f' % (i,math.log(i)))

#Exercicio 7.2
def tab_doispot(n):
    for i in range(n+1):
        print('2^%2d =%10d' %(i,2**i))

#Exercicio 7.3
def tempo(t):
    horas=int(t/60/60)
    minutos=int(t/60)%60
    segundos=t-horas*60*60-minutos*60
    return '%02d:%02d:%02d' % (horas,minutos,segundos)

#Exercicio 7.4
def media_arit(xs):
    x=0
    for i in range(len(xs)):
        x=x+xs[i]
    return x/len(xs)

#Exercicio 7.5
def media_geom(xs):
    x=1
    for i in range(len(xs)):
        x=x*x[i]
    return x**(1/len(xs))

#Exercicio 7.6
def desvio_padrao(xs):
    media=media_arit(xs)
    a=0
    for i in range(len(xs)):
        a=a+(xs[i]-media)**2
    return ((1/(len(xs)-1))*a)**(1/2)


#Exercicio 7.7
def prod_interno(xs,ys):
    a=0
    for i in range(len(xs)):
        a=a+xs[i]*ys[i]
    return a

#Exercicio 7.8
def intervalo(xs,a,b):
    a=xs[a:b+1]
    return len(a)

#Exercicio 7.9
def magico(A):
    sc=0
    sl=0
    sd1=0
    sd2=0
    for i in range(len(A)):
        sd1=sd1+A[i][i]
        sd2=sd2+A[i][len(A)-1-i]
        sl=sl+A[0][i]
        sc=sc+A[i][0]
    if sl==sc==sd1==sd2:
        x=sd1
        for i in range(len(A)):
            sl=0
            sc=0
            for j in range(len(A)):
                sl=sl+A[i][j]   #soma da linha "i"
                sc=sc+A[j][i]   #soma da coluna "i"
            if sl!=x or sc!=x:
                return False
    if not(sl==sc==sd1==sd2):
        return False
    return True
    
        
#Exercicio 8.1
def fatorial(n):
    if n==0:
        return 1
    if n<0:
        raise ValueError('Número tem de ser positivo')
    if type(n)==float:
        raise TypeError('Numero tem de ser natural')
    else:
        return n*fatorial(n-1)

        
    
#Exercicio 8.2
def media(xs):
    if type(xs)!=list:
        raise TypeError('Tem de ser uma lista')
    if xs==[]:
        raise ValueError('Não pode ser uma lista vazia')
    else:
        return sum(xs)/len(xs)

#Exercicio 8.3
def longa(file):
    f=open(file,'r')
    b=''
    c=0
    while True:
        a=(f.readline()).replace(',','')
        g=a.split()
        if a=='':
            break
        else:
            for i in g:
                if len(i)>c:
                    c=len(i)
                    b=i
    return b

#Exercicio 8.4
def collatz(n):
    a=0
    while n!=1 and n!=0:
        a+=1
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    return a
        
    
#Exercicio 8.5
def collatz_texto(n):
    f=open('collatz.txt','w')
    for i in range(1,n+1):
        f.write('%04d %04d \n' %(i,collatz(i)))

#Exercicio 8.6
def anagramas(txt1,txt2):
    txt1=txt1.lower()
    txt2=txt2.lower()
    a={}
    b={}
    for i in txt1:
        if 'a'<=i<='z':
            a[i]=1+a.get(i,0)
    for i in txt2:
        if 'a'<=i<='z':
            b[i]=1+b.get(i,0)
    if a==b:
        return True
    else:
        return False

#Exercicio 8.7
def morse(txt):
    codigo={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
            'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
            'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
            'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
            'Y':'-.--','Z':'--..'}
    txt=txt.upper()
    a=''
    for i in txt:
        if 'A'<=i<='Z':
            a=a+codigo[i]+' '
        else:
            a=a+i
    return a
        
#Exercicio 8.8
def certas_p(chave,tentativa):
    a=0
    for i in range(len(chave)):
        if tentativa[i]==chave[i]:
            a+=1
    return a

def certas(chave, tentativa):
    if len(chave)!=len(tentativa):
        raise ValueError('Chave e tentativa tem de ter o mesmo numero de caracteres')
    a={}
    b={}
    c=0
    for i in range(len(chave)):
        b[chave[i]]=1+b.get(chave[i],0)
        a[tentativa[i]]=1+a.get(tentativa[i],0)
    for i in a.keys():
        c=c+min(a[i],b.get(i,0))
    return c  



def pontua(chave,tentativa):
    cc=certas_p(chave,tentativa)
    c=certas(chave,tentativa)
    return (cc,c-cc)
    
#Exercicio 9.1
def mdc(a,b):
    if b==0:
        return a
    else:
        return mdc(b, a%b)

#Exercicio 9.2
def coprimos(n):
    a=[]
    for i in range(n):
        if mdc(i,n)==1:
            a=a+[i]
    return a


#Exercicio 9.3
def binom1(n,k):
    if k==n or k==0:
        return 1
    else:
        return binom1(n-1,k-1)+binom(n-1,k)
        
#Exercicio 9.4
def ack(m,n):
    if m==0:
        return n+1
    if m>0 and n==0:
        return ack(m-1,1)
    else:
        return ack(m-1,ack(m,n-1))

#Exercicio 9.5
def palindromo1(txt):
    if len(txt)<=1:
        return True
    else:
        if txt[0]==txt[-1]:
            txt=txt[1:len(txt)-1]
            return palindromo1(txt)
        else:return False

#Exercicio 9.6
def koch(n,side):
    import turtle
    if n==0:
        turtle.forward(side)
    else:
        for i in [60,-120,60,0]:
            koch(n-1,side/3)
            turtle.left(i)
        
def floco(n,side):
    import turtle
    for i in [120,120,120]:
        koch(n,side)
        turtle.right(i)

#Exercicio 9.7
def draw_tree(n,size,angle,ratio,thick):
    import turtle
    turtle.pensize(thick)
    turtle.pencolor('brown')
    if n==0:
        turtle.pencolor('green')
    turtle.forward(size*ratio)
    if n>0:
        (x,y)=turtle.position()
        head=turtle.heading()
        turtle.left(angle)
        draw_tree(n-1,(1-ratio)*size,angle,ratio,0.8*thick)
        turtle.penup()
        turtle.goto(x,y)
        turtle.setheading(head)
        turtle.pendown()
        turtle.right(angle)
        draw_tree(n-1,(1-ratio)*size,angle,ratio,0.8*thick)
        
    





    

