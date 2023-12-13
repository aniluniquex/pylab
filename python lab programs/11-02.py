class Bank:
    def getroi(self):
        return 12

class ICICI(Bank):
    def getroi(self):
        return 9;
 
class SBI(Bank):
    def getroi(self):
        return 7;
 
ic=ICICI()
sb=SBI()
print("ICICI Rate of Interest :",ic.getroi())
print("SBI Rate of Interest : ",sb.getroi())
