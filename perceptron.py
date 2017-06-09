import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import sympy as syp
def evaluate(w_vector1,w_vector2,w1_x1,w1_x2,w2_x1,w2_x2):
    w=[w_vector1,w_vector2]
    xx1=[w1_x1,w1_x2]
    xx2=[w2_x1,w2_x2]
    x1=syp.symbols('x1',integer=True)
    x2=syp.symbols('x2',integer=True)
    x=[x1,x2]
    g=np.dot(np.transpose(w),x)
    g1=np.dot(np.transpose(w),xx1)
    g2=np.dot(np.transpose(w),xx2)
    print("init weight vector = ",w)
    print("g1-g2= ",g1-g2)
    if g1-g2 >0 :
        print("g1")
    else:
        print("g2")

    g=syp.solve(g,x1)
    Boundary(g)

def Boundary(g):
   # print(g)
    x2=syp.symbols('x2',intger=True)
    x2=np.linspace(-3,8,100)
    b=-x2
    plt.plot(x2,b)


def main():

    w1_x1=[0.1,6.8,-3.5,2.0,4.1,3.1,-0.8,0.9,5.0,3.9  ]
    w1_x2=[1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0]
    w2_x1=[7.1,-1.4,4.5,6.3,4.2,1.4,2.4,2.5,8.4,4.1 ]
    w2_x2=[ 4.2,4.3,0.0,1.6,1.9,3.2,4.0,6.1,3.7,2.2 ]
    w_vector1=0.5  #random.random()
    w_vector2=0.5 #random.random()

    for i in range(0,10):
        evaluate(  w_vector1,w_vector2,w1_x1[i],w1_x2[i],w2_x1[i],w2_x2[i])
        plt.scatter(w1_x1[i],w1_x2[i],c='r')
        plt.scatter(w2_x1[i],w2_x2[i],c='b')

    plt.show()




if __name__=='__main__':
    main()
