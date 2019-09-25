# Testing Suite

TestingSuite.py contains the class for the testing suite

## The Testing Suite is used to test your Python function with a list of expected inputs and outputs

## How to use: 
Initialize an object from the Testing Suite class, using a list of Inputs and Answers
> InputSet = ["abfcj","abaflmnoa","zyma", None]

> AnsSet = ["abf","aflmno","yz",None]

> Test1 = TestingSuite(InputSet,AnsSet)

Then use the function "beginTest" with your function
> def Function(x):

>     return x + "Something"

> Test1.beginTest(Function)

You will get the results as output.
