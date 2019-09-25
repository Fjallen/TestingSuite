class TestingSuite():
    # constructor
    def __init__(self,set1,set2):
        # Set of inputs
        self.testingSet = set1
        # Set of Outputs
        self.answerSet = set2
    #Start the test
    def beginTest(self,func):
        #Stores the result
        resultSet = []
        # Test the function for each input
        for item in self.testingSet:
            #Append the output
            resultSet.append(func(item))
        # If perfect
        if (resultSet == self.answerSet):
            return "Test Complete, your code is correct"
        else:
            #Otherwise, prints which ones are wrong
            for index in range(0,len(self.answerSet)):
                if (self.answerSet[index] != resultSet[index]):
                    print("index at" + str(index) + " has the wrong  result")
            return "There is something wrong in your code, see above for errors"
