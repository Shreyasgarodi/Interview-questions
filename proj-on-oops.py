class bank:
    roi=0.5
    bname='sbi'
    bceo='saswat'
    def _init_(self,name,bal):
        self.name=name
        self.bal=bal
        self.tran=[]
        self.tran+=[('inital amount: ',self.bal)]
    def deposit(self,amt):
        self.bal+=amt
        self.tran+=[('deposit of '+str(amt)+' balance= '+str(self.bal))]
    def withdraw(self,amt):
        if self.bal>=amt:
            self.bal-=amt
            self.tran+=[('withdraw of '+str(amt)+' balance= '+str(self.bal))]
        else:
            raise ValueError('insaficient balance')
    def transa(self):
        for i in self.tran:
            print(i)
    def roit(self):
        pa=(self.bal)*(self.roi)
        self.bal+=pa
        self.tran+=[('intrest applied '+str(pa)+' balance= '+str(self.bal))]
ac1=bank('nitin',10000)
ac2=bank('mohan',20000)
