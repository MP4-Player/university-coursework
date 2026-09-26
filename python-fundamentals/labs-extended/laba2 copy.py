class CompClass:
    n_count=0
    def __init__(self,nomberes,date,BMO,FIO,PS):
        CompClass.n_count+=1
        self.n=CompClass.n_count
        self.nomberes=nomberes
        self.date=date
        self.BMO=BMO
        self.FIO=FIO
        self.PS=PS

class Construktor:
    n_count=0
    def __init__(self,nomberesing):
        Construktor.n_count+=1
        self.n=Construktor.n_count
        self.nomberesing=nomberesing


class Corpus:
    global poisk
    poisk=[]
    def corpusing(cor):
        poisk.append(cor)
    def Vivod(n):
        print(n.nomberesing)
    def Corpus():
        nomberesinggg=input("ввидите число  ")
        for n in poisk:
            if n.nomberesing==nomberesinggg:
                Corpus.Vivod(n)


class Collect:#создать несколго классов колект чтобы было можно  искать по корпусам
    global baze
    baze=[]
    def CozdatColect(vvod):
        baze.append(vvod)
    def Vivod(info):
        print(info.n,info.nomberes,info.date,info.BMO,info.FIO,info.PS)
    def Date():
        dat=input("ввидите число  ")
        for info in baze:
            if info.date==dat:
                Collect.Vivod(info)
    def Name():
        name=input("ввидите familiy  ")
        for info in baze:
            if info.FIO==name:
                Collect.Vivod(info)

a1=Construktor("4")
Corpus.corpusing

a=CompClass("317","22.02","ВМО11","Шипилова","проверить_лабу")
Collect.CozdatColect(a)
s=CompClass("317","22.02","ВМО12","Шипилова","проверить_лабу",)
Collect.CozdatColect(s)
d=CompClass("317","23.02","ВМО13","Шипилова","провести_лабу")
Collect.CozdatColect(d)
f=CompClass("292","3.03","ВМО11","Ельчинкова","дз")
Collect.CozdatColect(f)
g=CompClass("292","3.04","ВМО11","Ельчинкова","проверить_дз")
Collect.CozdatColect(g)
h=CompClass("292","3.03","ВМО13","Шипилова","дз")
Collect.CozdatColect(h)
j=CompClass("292","3.03","ВМО12","Ельчинкова","дз")
Collect.CozdatColect(j)
k=CompClass("134","3.07","ВМО11","Ельчинкова","кр")
Collect.CozdatColect(k)
l=CompClass("134","3.07","ВМО11","Шипилова","кр")
Collect.CozdatColect(l)
for info in baze or n in poisk:
    Collect.Vivod(info) or Corpus.Vivod(n)
poisk=input('Поиск по дате -1 или по преподователю -2  ')
while poisk!=0:
    if poisk=='1':
        Collect.Date()
    elif poisk=='2':
        Collect.Name()
    elif poisk=='3':
        Construktor.Corpus()
    else:
        print('без - попробуй , 0 всё перезапустит  ')
    poisk=input('Поиск по дате -1 или по преподователю -2  ')
        

    
    
