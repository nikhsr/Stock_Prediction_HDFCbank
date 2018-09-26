import math
class LinearRegression:
    def mean(self,x):
        meanx=0
        for i in x:
            meanx=(meanx+i)
        mean_xx=meanx/len(x)
        return mean_xx

    def Mul_xy(self,x,y):
        self.xy=list()
        self.xx=list()
        self.yy=list()
        co=0
        for i in x:
            xy1=i*y[co]
            co=co+1
            self.xy.append(xy1)
            xx1=i*i
            self.xx.append(xx1)
        for j in y:
            yy1=j*j
            self.yy.append(yy1)
        return self.xy,self.xx,self.yy

    def deviation_x_y(self,x,y):
        self.s1=list()
        self.s2=list()
        m1=self.mean(x)
        m2=self.mean(y)
        for k in x:
            d1=k-m1
            self.s1.append(d1)
        for l in y:
            d2=l-m2
            self.s2.append(d2)
        return self.s1,self.s2

    def deviation_xy(self):
        self.dev=list()
        c=0
        for a1 in self.s1:
            d=a1*self.s2[c]
            c=c+1
            self.dev.append(d)
        return self.dev

    def deviation_xx(self):
        self.s12=list()
        for a1 in self.s1:
            a2=a1*a1
            self.s12.append(a2)
        return self.s12

    def slope(self,x,y):
        self.deviation_x_y(x, y)
        self.deviation_xx()
        self.deviation_xy()
        Slope=sum(self.dev)/sum(self.s12)
        return Slope

    def intercept(self,x,y):
        m1=self.mean(x)
        m2=self.mean(y)
        slop=self.slope(x,y)
        intercept=m2-(slop*m1)
        return intercept

    def coefficient(self,x,y):
        self.Mul_xy(x,y)
        cor=((len(x)*sum(self.xy))-(sum(x)*sum(y)))/(math.sqrt(((len(x)*sum(self.xx))-(sum(x)*sum(x)))*((len(y)*sum(self.yy))-(sum(y)*sum(y)))))
        return cor

    def predict(self,x,y,x1):
        predict=self.intercept(x,y)+self.slope(x,y)*x1
        return predict

    def predict1(self,x,y):
        self.pre=list()
        global pred
        for i in  x:
            predict1=self.intercept(x,y)+self.slope(x,y)*i
            self.pre.append(predict1)
        return self.pre

    def residual(self,x,y,x1):
        self.count=0
        self.count1=0
        for i in x:
            if(i==x1):
                #self.count=self.count+1
                self.y1=y[self.count]
            else :
                self.count1=self.count1+1
                #self.y2=y[self.count1]
            self.residual=self.y1-self.predict1(x,y)
            return self.residual

    def residual1(self,x,y,x1):
        self.count2=0
        self.count3=0
        for i in x:
            if(i==x1):
                self.count2=self.count2+1
                self.y1=y[self.count2]
            else :
                self.count3=self.count3+1
                self.y2=y[self.count3]
        residual1=self.y2-self.predict1(x,y)
        return residual1