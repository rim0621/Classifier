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

    w1=0.3
    w2=0.7
    w0=0.9
    #l=0.0001
    l=0.005
    x0=-1
    flag=1
    count=0

#------------------실행
    i=0
    while 1:
        flag=1
        while i < 20:
            net=evaluate (w1,w2,w0,x0,x1[i],x2[i])

            if net<0:
                f_net=0
            else:#오류
                f_net=1
            w1=w1+l*x1[i]*(0-f_net)
            w2=w2+l*x2[i]*(0-f_net)
            w0=w0+l*x0*(0-f_net)
            if f_net==1:
                i=0
                flag=0
            i+=1
#-----------------출력---------------
            count+=1
            print("-------",count,"번---------------")
            print("w1= ",w1,"w2= ",w2,"w0= ",w0)

        if flag==1: #오류가 없으면
            break
    a=np.linspace(-3,8,100)
    plt.plot(a,((-w1*a)-w0)/w2)



    plt.show()
if __name__=='__main__':
    main()
