# Helper Module
# Has Math functions such as variance(X), Standard Deviation(X), etc.

# Testing Method
def printHello():
	print("hello world!")


'''
Define the following functions:
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
def covariance(arrX, arrY):
	print()


'''
coefficientsFunc(matrixA: list)-> list is a function that creates 
and returns a list of correlation coefficients of rxy. 

r^2 = SSR/SST = total sum of squares due to regression / total sum of squares

SST = SSR + SSE (Sum of Squares due to Error)
'''
def coefficientsFunc(matrixA):
	print()