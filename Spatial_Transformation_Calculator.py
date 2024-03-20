import numpy as np

#Defining functions and constants
#Conversion contant for converting desgrees to redians
Radians = np.pi/180

#identity matrix
I_M = np.array([[1,0,0,0],
                            [0,1,0,0],
                            [0,0,1,0],
                            [0,0,0,1] ], dtype= int )

#Function for rotating along the x axis by an  angle alpha
def Rx (alpha):
    Alpha = alpha * Radians
    return np.array([   [1,0,0,0],
                        [0,np.cos(Alpha),-np.sin(Alpha),0],
                        [0,np.sin(Alpha),np.cos(Alpha),0],
                        [0,0,0,1] ], dtype = float)

#Function for rotating along the y axis by an  angle Beta
def Ry (beta):
    Beta = beta * Radians
    return np.array([   [np.cos(Beta),np.sin(Beta),0,0],
                        [0,1,0,0],
                        [-np.sin(Beta),0,np.cos(Beta),0],
                        [0,0,0,1] ], dtype = float)

#Function for rotating along the z axis by an  angle Gamma
def Rz (gamma):
    Gamma = gamma * Radians
    return np.array([   [np.cos(Gamma),-np.sin(Gamma),0,0],
                        [np.sin(Gamma),np.cos(Gamma),0,0],
                        [0,0,1,0],
                        [0,0,0,1], ], dtype = float)

#Function for rotating along the z axis by an  angle Gamma
def T (x, y, z):
    return np.array([   [1,0,0,x],
                        [0,1,0,y],
                        [0,0,1,z],
                        [0,0,0,1]],dtype= float )
#Example_1
Transformation_1 = Rx(40) @ (I_M @ T(0,7,0))
print('Homogeneous Transforamtion Matrix_1:\n')
print(Transformation_1)

#Example_2
Transformation_2 = T(4,0,0) @ (Rx(50) @ (I_M @ (T(0,0,-6) @ Ry(25))))
print('Homogeneous Transforamtion Matrix_2:\n')
print(Transformation_2)

#Example_3
Transformation_3 = T(0,5,0) @ (Rz(-60) @ (Rx(60) @ I_M))
print('Homogeneous Transforamtion Matrix_3:\n')
print(Transformation_3)