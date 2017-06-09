import random
import matplotlib.pyplot as plt
import numpy as np
def evaluate(w1,w2,w0,x0,x1,x2):

    return w1*x1+w2*x2+w0*x0
#---init-----
def main():
    w1_x1=[0.1,6.8,-3.5,2.0,4.1,3.1,-0.8,0.9,5.0,3.9]
    w1_x2=[1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0]
    w2_x1=[7.1,-1.4,4.5,6.3,4.2,1.4,2.4,2.5,8.4,4.1 ]
    w2_x2=[ 4.2,-4.3,0.0,1.6,1.9,-3.2,-4.0,-6.1,3.7,-2.2 ]
    x1=[0.1,6.8,-3.5,2.0,4.1,3.1,-0.8,0.9,5.0,3.9,7.1,-1.4,4.5,6.3,4.2,1.4,2.4,2.5,8.4,4.1]
    x2=[1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0,4.2,-4.3,0.0,1.6,1.9,-3.2,-4.0,-6.1,3.7,-2.2]

    for k in range(0,10):
        plt.scatter(w1_x1[k],w1_x2[k],c='r')
        plt.scatter(w2_x1[k],w2_x2[k],c='b')

    w1=0.4
    w2=0.3
    w0=0.1
    l=0.0005
    x0=-1
    th=0.00051
    flag=1
    #for i in range(0,100):
    while 1:
        y1=0
        y2=0
        for i in range(0,20):
            net=evaluate (w1,w2,w0,x0,x1[i],x2[i])

            if net>0:
                y1+=x1[i]
                y2+=x2[i]
                flag=0

        print("flag=",flag)
        #if abs(l*y1)*y1<th and abs(l*y2)*y2<th and abs(l*x0)*<th:
        if flag==1:
           break

        w1=w1+l*y1
        w2=w2+l*y2
        w0=w0+l*x0
        print(w1,w2,w0)


    a=np.linspace(-3,8,100)
    plt.plot(a,((-w1*a)-w0)/w2)
    plt.show()

if __name__=='__main__':
    main()
