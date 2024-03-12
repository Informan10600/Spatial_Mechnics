import numpy as np
#Defining matrices
#original position/point 1 of object
Point_1 = np.array([[-8.96],
                    [7.50],
                    [6.62],
                    [1]], dtype= float)

#final position/point 5 of object
Point_5 = np.array([[-10.94],
                    [-5.32],
                    [0.85],
                    [1.]], dtype= float)

#Translation Matrix that maps point 1 onto point 2
matrix_A = np.array ([[1,0,0,0],
                      [0,1,0,0],
                      [0,0,1,10.56],
                      [0,0,0,1]], dtype= float)

#Translation Matrix that maps point 2 onto point 3
matrix_B = np.array ([[1,0,0,-2.86],
                      [0,1,0,-11.47],
                      [0,0,1,0.02],
                      [0,0,0,1]], dtype= float)

#Translation Matrix that maps point 3 onto point 4
matrix_C = np.array ([[1,0,0,0.02],
                      [0,1,0,-2.02],
                      [0,0,1,-8.26],
                      [0,0,0,1]], dtype= float)

#Translation Matrix that maps point 4 onto point 5
matrix_D = np.array ([[1,0,0,0.86],
                      [0,1,0,0.67],
                      [0,0,1,-8.09],
                      [0,0,0,1]], dtype= float)

#Calculating the combined matrix transformation
Comb_T = matrix_D @ (matrix_C @ (matrix_B @matrix_A))
print(Comb_T)
