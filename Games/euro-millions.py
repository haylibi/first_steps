from random import*
def Euro_Millions():
    def numbers():
        x=1
        l = []
        for i in range(1, 51):
            l.append(x)
            x+=1
        y=sample(l, 5)
        print('Numbers',y)
    def stars():
        x=1
        l = []
        for i in range(1, 13):
            l.append(x)
            x+=1
        y=sample(l, 2)
        print('Stars',y)
    numbers()
    stars()
