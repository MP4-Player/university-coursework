import matplotlib.pyplot as plt
import numpy

class LTHMVJ:
    def __init__(self,a,s,d,h,k):
        self.x=numpy.arange(a,s)
        self.xl=numpy.arange(d)
        self.xr=numpy.arange(h)
        self.y=numpy.arange(a,s)
        self.yl=numpy.arange(d)
        self.yr=numpy.arange(h)
        self.e=numpy.arange(k)
        self.f=(((self.x-self.xl+((((self.x-self.xl)**2)+self.e**2)**0.5))*(self.xr-self.x+((((self.xr-self.x)**2)+self.e**2)**0.5)))/4*(((((self.x-self.xl)**2)+self.e**2))*(((self.xr-self.x)**2)+self.e**2))**0.5)*(((((self.y-self.yl+((((self.y-self.yl)**2)+self.e**2)**0.5))*(self.yr-self.y)+((((self.yr-self.y)**2)+(self.e)**2)**0.5)))/4*(((((self.y-self.yl)**2)+(self.e)**2))*(((self.yr-self.y)**2)+(self.e**2))**0.5)))                          
        ax=plt.axes(projection="3d")
        ax.plt3D(self.x,self.y,self.f)

    def draw(self):
        fig=plt.figure()
        #ax=fig.add_subplot(111)
        plt.plot(self.x,self.xl,self.xr,self.y,self.yl,self.yr,self.e,self.f)
        plt.show()
        pass
a1=5.0
s1=10.0
d1=5.0
h1=6.0
k1=5.0

paint=LTHMVJ(a1 , s1 , d1 , h1 , k1 )
paint.draw()

