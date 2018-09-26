import math
import LinearRegression as lr
m=lr.LinearRegression()
global count
class MultipleRegression:
    def mul_xx(self,x):       #x^2
        self.xx=list()
        for i in x:
            self.xx.append(i*i)
        return self.xx

    def mul_xy(self,x,y):    #x*y
        c=0
        self.xy=list()
        for j in x:
            xy1=j* y[c]
            c=c + 1
            self.xy.append(xy1)
        return self.xy

    def sum_xy(self,x,y):
        self.mul_xy(x,y)
        sum_xy=sum(self.xy)-((sum(x)*sum(y))/len(x))
        return sum_xy

    def dev_xx(self,x):
        m1=m.mean(x)
        self.devx=list()
        for i in x:
            dev=i-m1
            self.devx.append(dev)
        return self.devx

    def deviation_xx(self,x):
        self.dev_xx(x)
        self.devxx=list()
        for a1 in self.devx:
            a2=a1*a1
            self.devxx.append(a2)
        return self.devxx

    def sum_devxx(self,x):
        self.deviation_xx(x)
        return sum(self.devxx)

    def slope1(self,x1,x2,y):
        slope1=((self.sum_devxx(x2)*self.sum_xy(x1,y))-(self.sum_xy(x1,x2)*self.sum_xy(x2,y)))/((self.sum_devxx(x1)*self.sum_devxx(x2))-((self.sum_xy(x1,x2))**2))
        return slope1

    def slope(self,y,x1,x2):
        slope=((m.coefficient(x1,y)-(m.coefficient(x2,y)*m.coefficient(x1,x2)))/(1-(m.coefficient(x1,x2))**2))*(self.standard_dev(y)/self.standard_dev(x1))
        return slope


    def intercept(self,y,x1,x2):
        intercept=m.mean(y) - (self.slope(y,x1, x2) * m.mean(x1)) - (self.slope(y,x2,x1) * m.mean(x2))
        return intercept

    def intercept3(self,y,x1,x2,x3):
        intercept3=m.mean(y) - (self.slope(y,x1,x2) * m.mean(x1)) - (self.slope(y,x2,x3) * m.mean(x2))- (self.slope(y,x3, x1) * m.mean(x3))
        return intercept3

    def intercept2(self,y,x1,x2,x3,x4,x5,x6,x7):
        intercept2=m.mean(y)-(self.slope(y,x1,x7)*m.mean(x1))-(self.slope(y,x2,x7)*m.mean(x2))-(self.slope(y,x3,x7)*m.mean(x3))-(self.slope(y,x4,x1)*m.mean(x4))-(self.slope(y,x5,x7)*m.mean(x5))-(self.slope(y,x6,x7)*m.mean(x6))-(self.slope(y,x7,x4)*m.mean(x7))
        return intercept2

    def predict(self,y,x1,x2,x3,x4):
        predict=(self.intercept(y,x1,x2))+(self.slope(y,x1,x2)*x3)+(self.slope(y,x2,x1)*x4)
        return predict

    def standard_dev(self,x):
        std_dev=math.sqrt(self.sum_devxx(x)/(len(x)-1))
        return std_dev

    def predict1(self,y,x1,x2):
        self.pre=list()
        for i in  x1:
            for j in x2:
                #self.pred1=self.slope(y, x1, x2) * i
                self.pred2=self.intercept(y,x1,x2)+self.slope(y, x1, x2) * i+self.slope(y,x2,x1)*j
                self.pre.append(self.pred2)
        return self.pre



