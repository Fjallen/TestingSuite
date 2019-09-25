from TestingSuite import TestingSuite
import time
# Initialize the Sets
testset = ["abfcj","abaflmnoa","zyma", None]
ansset = ["abf","aflmno","yz",None]

# Initialize the Question1
Question1 = TestingSuite(testset,ansset)

#Your Function Goes Here
# def func(x):
#    return 0

Question1.beginTest(func)
# Wait for 10 seconds to let you read the result
time.sleep(10)
