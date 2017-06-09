import numpy as np
import matplotlib.pyplot as plt

def evaluate(w1,w2,w0,x0,x1,x2):

    return w1*x1+w2*x2+w0*x0


def main():
#-------------------scatter용
    w1_x1=[0.1,6.8,-3.5,2.0,4.1,3.1,-0.8,0.9,5.0,3.9]
    w1_x2=[1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0]
    w3_x1=[-3.0,0.5,2.9,-0.1,-4.0,-1.3,-3.4,-4.1,-5.1,1.9 ]
    w3_x2=[-2.9,8.7,2.1,5.2,2.2,3.7,6.2,3.4,1.6,5.1 ]


    for k in range(0,10):
        plt.scatter(w1_x1[k],w1_x2[k],c='r')
        plt.scatter(w3_x1[k],w3_x2[k],c='b')


#----------초기화
    x1=[0.1,6.8,-3.5,2.0,4.1,3.1,-0.8,0.9,5.0,3.9,1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0]
    x2=[1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0,-2.9,8.7,2.1,5.2,2.2,3.7,6.2,3.4,1.6,5.1]

    w1=0
    w2=0
    w0=0
    l=0.005
    x0=-1
    th=0.0002
    b=0.1
    k=0
    y=[]
    y1=0
    y2=0
    count=0

#-------------------오류들 검출
    for i in range(0,20):
            if evaluate(w1,w2,w0,x0,x1[i],x2[i])-b<0:
                y.append((x1[i],x2[i]))

#-------------------실행
    while 1:

        k=((k+1) % len(y))-1
        y=[]
        for i in range(0,20): #오류들 검출
            if evaluate(w1,w2,w0,x0,x1[i],x2[i])-b<0:
                y.append((x1[i],x2[i]))

        if abs(l*(b-evaluate(w1,w2,w0,x0,y[k][0],y[k][1]))*y[k][0])<th and abs(l*(b-evaluate(w1,w2,w0,x0,y[k][0],y[k][1]))*y[k][1])<th and abs(l*(b-evaluate(w1,w2,w0,x0,y[k][0],y[k][1]))*x0)<th:
            break

        w1=w1+l*(b-evaluate(w1,w2,w0,x0,y[k][0],y[k][1]))*y[k][0]
        w2=w2+l*(b-evaluate(w1,w2,w0,x0,y[k][0],y[k][1]))*y[k][1]
        w0=w0+l*(b-evaluate(w1,w2,w0,x0,y[k][0],y[k][1]))*x0
        k=k+1
        count+=1
        print("-------",count,"번---------------")
        print("w1= ",w1,"w2= ",w2,"w0= ",w0)

#-----------------그래프

    a=np.linspace(-7.8,9,100)
    plt.plot(a,((w1*a)-w0)/w2)
    plt.show()
if __name__=='__main__':
    main()