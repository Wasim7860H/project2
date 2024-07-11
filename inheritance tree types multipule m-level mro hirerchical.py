#MULTI LEVEL INHERITANCE IN PYTHON
class Father:
    def showF(self):
        print("Father class Method")
class Son(Father):
    def ShowS(srlf):
        print("Som Class Method")
class GrnadSon(Son):
    def ShowG(self):
        print("GrandSon Class Method")
g = GrnadSon()
g.ShowG()
g.ShowS()
g.showF()
# MULTILEVEL INHERITANCE WITH COSTRUCTOR
print()
class Parent1:
    def __init__(self):
        print("Parent One Class Constructor")
    def ShowP1(self):
        print("Parent Class Method")
class Parent2(Parent1):
    def __init__(self):
        super().__init__()
        print("Parent Two Class Constructor")
    def showP2(self):
        print("Parent Tow Class Method")
class Parent3(Parent2):
    def __init__(self):
        super().__init__()
        print("Parent Tree Class Constrctor")
    def showP3(self):
        print("Parent Class Method")
p = Parent3()
p.ShowP1()
p.showP2()
p.showP3()
print()
#HIERARCHICAL INHERITANCE IN PYTHON
class Father1:
    def showF(self):
        print("Father One Class Method")
class Son1(Father1):
    def showS(self):
        print("Son One Class Method")
class Daughter(Father1):
    def showD(self):
        print("Daughter Class Method")
H = Daughter()
H.showD()
H.showF()
print()
# hierarchial inheritance with constructor
class Father1:
    def __init__(self):
        print("Father One Class Constructot")
    def showF(self):
        print("Father One Class Method")
class Son1(Father1):
    def __init__(self):
        super().__init__()
        print("Son One Class Constructot")
    def showS(self):
        print("Son One Class Method")
class Daughter(Father1):
    def __init__(self):
        super().__init__()
        print("Daugther Class Constructot")
    def showD(self):
        print("Daughter Class Method")
l1 = Daughter()
print()
#MULTIPULE IN HEHARITANCE IN PYTHON
class Father:
    def ShowF2(self):
        print("Fater Class Method")
class Mother:
    def showM(self):
        print("Mother Class Method")
class Son(Father, Mother):
    def showS(self):
        print("Son Class Method")
w = Son()
w.showS()
w.showM()
w.ShowF2()
print()
# MULTIPULE IN HERITANCE WITH COSTRUCTIOR
print("MULTIPULE IN HERITANCE WITH CONSTRUCTOR")
class Father:
    def __init__(self):
        super().__init__()
        print("Father Class Constructor")
    def ShowF2(self):
        print("Fater Class Method")
class Mother:
    def __init__(self):
        super().__init__()
        print("Mothor Class Constructor")
    def showM(self):
        print("Mother Class Method")
class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Son class Constructor")
    def showS(self):
        print("Son Class Method")
q = Son()
