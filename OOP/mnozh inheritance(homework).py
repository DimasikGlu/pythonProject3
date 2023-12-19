"""1"""
class Xerocopy():
    def __init__(self,nameModel,nameDoc,copyQuanity,copyLimit):
        self.nameModel = nameModel
        self.nameDoc = nameDoc
        self.copyQuanity = copyQuanity
        self.copyLimit = copyLimit
    def Copy(self):
        delta = self.copyLimit - self.copyQuanity
        if delta <= 0:
            print(f"You have not color for copy doc quanity: {delta}!")
            self.copyLimit = delta
        else: print(f"Model {self.nameModel} copy doc {self.nameDoc} in quanity {self.copyQuanity}.You have a limit copy doc {delta}")
        self.copyLimit = delta
    def addLists(self,addList):
        self.addLists = addList
        print(f"You have before list: {self.copyLimit}, but after refill: {self.copyLimit+self.addLists}")
        self.copyLimit = self.copyLimit + self.addLists

test1 = Xerocopy('Samsung','Failik',5,6)
# test1.Copy()
# test1.addLists(5)


class Printer():
    def __init__(self,nameModel,nameDoc,printQuanity,printLimit):
        self.nameModel = nameModel
        self.nameDoc = nameDoc
        self.printQuanity = printQuanity
        self.printLimit = printLimit
    def printColored(self):
        self.printLimit = self.printLimit - self.printQuanity
        print(f"Model{self.nameModel} printed document {self.nameDoc} in color "
              f"in quanity {self.printQuanity}. Print limit is {self.printLimit} list")
    def printBlacked(self):
        delta_black = self.printLimit - self.printQuanity
        if delta_black >0:
            print(f"Model{self.nameModel} printed document {self.nameDoc} in black color"
              f"quanity print {self.printQuanity}. Print limit is {delta_black} list")
        else: print(f"limit is over!")
    def addLists(self,addLists):
        self.addLists = addLists
        print(f"You have before list: {self.printLimit}, but after refill: {self.printLimit + self.addLists}")
        self.printLimit = self.printLimit + self.addLists

"""3"""

class LGTech(Xerocopy,Printer):
    def __init__(self,nameModel,nameDoc,copyQuanity,copyLimit,printQuanity,printLimit):
        super().__init__(nameModel,nameDoc,copyQuanity,copyLimit)
        Printer.__init__(self,nameModel,nameDoc,printQuanity,printLimit)
    def getLG(self):
        print()


test3 = LGTech("bb",'vv',5,200)
test3.printBlacked()


