

class Fraction:
    def __init__(self,ss,mm):
        self.s = ss
        self.m = mm

    def sum(self,k2):
        s = self.s * k2.m + self.m * k2.s
        m = self.m * k2.m
        x = Fraction(s,m)
        return x

    def mul(self,kasr_1):
        result_s = kasr_1.s * self.s
        result_m  = kasr_1.m * self.m

        x = Fraction(result_s,result_m)
        return x

    def sub(self,frac1):
        s = self.s * frac1.m - self.m * frac1.s
        m = self.m * frac1.m
        x = Fraction(s,m)
        return x        

    def div(self,frac1):
        frac1_s = self.s * frac1.m
        frac1_m = self.m * frac1.s
        return Fraction(frac1_s , frac1_m)
    
    def fraction_to_number(self):
        return  self.s / self.m 
        

    def show(self):
        print(" ")
        print(' ',self.s)
        print("-----")
        print(" ",self.m)
        print(" ")  
 


a = Fraction(2,3)
# a.show()

b = Fraction(4,3)
# b.show()

mul = b.mul(a)
# mul.show()

sum = a.sum(b)
# sum.show()

sub = a.sub(b)
# sub.show()

div = a.div(b)
# div.show()

f_to_n = Fraction(2,3)
print(f_to_n.fraction_to_number())