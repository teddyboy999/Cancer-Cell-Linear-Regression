# Helper Module
# Has Math functions such as variance(X), Standard Deviation(X), etc.

# Testing Method
def printHello():
    print("hello world!")


'''
Define the following functions:
'''


'''
* transpose(matrixA) finds the transpose of the argument matrix 
* and returns it.
'''
def transpose(matrixA:list)->list:
    if (matrixA == []):
        return []

    m:int = len(matrixA)
    n:int = len(matrixA[0])

    # Make Empty Transpose
    transpose:list = [[0 for y in range(0,m)] for x in range(0,n)]

    # Build Transpose Matrix
    for i in range(0, m):
        for j in range(0, n):
            transpose[j][i] = matrixA[i][j]

    # Testing
    print(transpose)

    return transpose

'''
Testing
listA:list = [[1, 2],
              [3,4],
              [5,6]]
transpose(listA)
'''



'''
mean finds the mean/average value of a
given list of floating point values and returns the average as a float.
'''
def mean(arrX:list)->float:
    fMean = 0
    fSum = 0
    nNum = 0

    for fElement in arrX:
        fSum += fElement
        nNum += 1

    fMean = fSum / nNum
    return fMean


'''
varianceFun finds the 
summation of (xi - avgX) ^ 2 and returns it as a float value.
'''
def variance(arrX:list)->float:
    fSum = 0
    fMean = mean(arrX)

    for fElement in arrX:
        fSum += (fElement - fMean) ** 2

    return fSum


'''
covarianceFun finds the summation of (yi - avgY) * (xi - avgX) 
from the arrays arrX and arrY respectively and returns it as a float value.
'''
def covariance(arrX:list, arrY:list)->float:
    fSum = 0
    fMeanX = mean(arrX)
    fMeanY = mean(arrY)

    if (len(arrX) != len(arrY)):
        return -1
    else:
        nLen = len(arrX)

    for nIndex in range(0, nLen):
        fElementX = arrX[nIndex]
        fElementY = arrY[nIndex]
        fSum += (fElementX - fMeanX) * (fElementY - fMeanY)

    return fSum


'''
coefficientsFunc(matrixA: list)-> list is a function that creates 
and returns a list of correlation coefficients of rxy. 

r^2 = SSR/SST = total sum of squares due to regression / total sum of squares

SST = SSR + SSE (Sum of Squares due to Error)

def coefficientsFunc(matrixA):
    print()

'''

# Multiple Linear Regression Model
import pandas as pd
import numpy as np
from IPython.display import display

# Global Variables
arrX = []
arrY = []
database = None
def multipleLinearRegression(strCSV:str, strValues:str):
    dataset = pd.read_csv(strCSV) # read the csv file. This will make a 2d matrix

    # x = everything in the dataset except the column "diagnosis(1=m, 0=b)"
    x = dataset.drop(columns = ["diagnosis(1=m, 0=b)"])

    #x = remove the first row as it is the names of the columns
    x = x.drop([0,0])

    #make an array of all 1s sized the number of rows (we already excluded first col)
    onesArr = np.ones(x.shape[0])

    #insert array of ones in the beginning of x
    x.insert(0, '', onesArr, True)

    #y = only the first col as this is what we are aiming to achieve
    y = dataset["diagnosis(1=m, 0=b)"]

    #y = remove the first row as it is the names of the columns
    y = y.drop([0,0])

    #size of whole arr
    #print(x.shape)
    #print(x)

    #x transposed
    Xt = x.transpose()
    #print(Xt.shape)

    #transposed x multiplied with x
    XtX = Xt.__matmul__(x)
    #print(XtX.shape)

    #transposed x multiplied with y
    XtY = Xt.__matmul__(y)
    #print(XtY.shape)

    #inverse of transposed x
    XtXinv = np.linalg.inv(XtX)
    #print(XtXinv.shape)

    #regression coeffecient for multiple regression
    beta = XtY.__matmul__(XtXinv)
    #print(beta.shape)

    #print(beta)

    #user input for values to test
    # strValues = str(input("Insert comma separated values: "))

    #converting the string into an array of flats, separated by ', ' as the delimiter
    arr = np.fromstring(strValues, dtype=float, sep=', ')
    print()
    #print(arr)

    #final result is the first regression coeffecient + the summation of (beta[n] * arr[n]), where n is above 1
    #the np.multiply will multiply each respective element and combine to 1 arr i.e. a[1] = b[1] * c[1]
    #the np.sum adds all elements of array
    tempArr = np.multiply(beta[1:], arr[1:])
    mlr = beta[0] + np.sum(tempArr)

    print("Final = ", mlr)



    # Testing the Graph Function
    sumArray = beta[1:] + np.multiply(beta[1:], arr[1:])
    graph(arr[1:], sumArray)



# Graphing the Linear Regression Model
import matplotlib.pyplot as plt
def graph(X, Y):
    #dataset.plot(kind = "scatter", x = "Parameters", y = "Predicted", title = "Cancer Cell Multiple Regression")

    plt.plot(X, Y)
    plt.show()

    # Testing
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
