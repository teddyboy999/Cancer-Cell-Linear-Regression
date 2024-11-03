# main

# Imports
# Import the helper.py file with all the math functions
import helper

if (__name__ == "__main__"):
	# Testing The Linear Regression Model

	# user input for values to test
	strValues = str(input("Insert comma separated values: "))
	helper.multipleLinearRegression('cancer.csv', strValues)

