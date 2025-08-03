class product():


        


    def __init__(self,stak,investment,purchasing,profit):
        self.stak=stak
        self.investment=investment
        self.purchasing=purchasing
        self.profit=profit
    def apple(self):

        print("apple stak:",self.stak)
        print()
        print("apple investment:",self.investment)
        print()
        print("apple purchasing:",self.purchasing)
        print()
        print("appple profit:",self.profit)


    def orange(self):

        print("orange stak:",self.stak)
        print()
        print("orange investment:",self.investment)
        print()
        print("orange purchasing:",self.purchasing)
        print()
        print("orange profit:",self.profit)

    def mango(self):

        print("manogo stak:",self.stak)
        print()
        print("mango investment:",self.investment)
        print()
        print("mango purchasing:",self.purchasing)
        print()
        print("mango profit:",self.profit)

    def banana(self):

        print("banana stak:",self.stak)
        print()
        print("banana investment:",self.investment)
        print()
        print("banana purchasing:",self.purchasing)
        print()
        print("banana profit:",self.profit)      
        
apple=product("10kg",10000,200000,50000)
orange=product("30kg",30000,300000,30000)
mango=product("20kg",40000,800000,80000)
banana=product("50kg",90000,600000,65703)

user=input("what product name:")

if(user=="apple"):
  apple.apple()
elif(user=="mango"):
    print(mango.mango())
elif(user=="orango"):
    print(orange.orange())
elif(user=="banana"):
    print(banana.banana())
else:
    print("this product is not avaliable")


