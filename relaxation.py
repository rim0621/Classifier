import random
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as lin
def evaluate(w1,w2,w0,x0,x1,x2):

    return w1*x1+w2*x2+w0*x0

def main():
    w1_x1=[0.1,6.8,-3.5,2.0,4.1,3.1,-0.8,0.9,5.0,3.9]
    w1_x2=[1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0]
    w3_x1=[-3.0,0.5,2.9,-0.1,-4.0,-1.3,-3.4,-4.1,-5.1,1.9 ]
    w3_x2=[-2.9,8.7,2.1,5.2,2.2,3.7,6.2,3.4,1.6,5.1 ]
    x1=[0.1,6.8,-3.5,2.0,4.1,3.1,-0.8,0.9,5.0,3.9,1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0]
    x2=[1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0,-2.9,8.7,2.1,5.2,2.2,3.7,6.2,3.4,1.6,5.1]


    for k in range(0,10):
        plt.scatter(w1_x1[k],w1_x2[k],c='r')
        plt.scatter(w3_x1[k],w3_x2[k],c='b')

    w1=0
    w2=0
    w0=0
    b=0.1
    #b=0.5
    l=0.4
    x0=-1
    y=[]
    y1=0
    y2=0
    flag=1
    i=0
    count=0

    while 1:
        flag=1
        y=[]

        for j in range(0,20):
            net=evaluate (w1,w2,w0,x0,x1[j],x2[j])
            if net<=b:
                y.append((x1[j],x2[j])) #오류들 집합
                flag=0

        if flag==1: #오류가없으면
            break


        for k in range(0,len(y)):
            y1=y1+y[k][0]
            y2=y2+y[k][1]

        sigma=b-evaluate(w1,w2,w0,x0,y1,y2)/pow(lin.norm((x0,y1,y2)),2)
        w1=w1+l*y1*sigma
        w2=w2+l*y2*sigma
        w0=w0+l*x0*sigma
        l-=0.0000316

        i+=1
    #-----출력 보기------
        count+=1
        print("-------",count,"번---------------")
        print("w1= ",w1,"w2= ",w2,"w0= ",w0)


        a=np.linspace(-5.5,8,10)
        plt.plot(a,((-w1*a)-w0)/w2)

    plt.show()

if __name__=='__main__':
    main()

#w1=  -3.70371032095 w2=  5.00946561126 w0=-20