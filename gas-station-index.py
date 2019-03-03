class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    minIndex = 0 
    def canCompleteCircuit(self, A, B):
        if len(A) != len(B)
            return -1
        for i in range(len(A)):
            A= A[i:]+A[:i]
            B= B[i:]+B[:i]
            if self.travelAgain(A,B):
                self.minIndex = i    
                continue
            else:
                break
        else:
            return -1
        # print(self.minIndex,'hi')
        return self.minIndex
    
    def travelAgain(self,A,B):
        noOfUnitsRequiredToTravel = 0
        totalGasInBike = 0
        for i in range(len(A)):
            noOfUnitsRequiredToTravel = B[i]
            totalGasInBike += A[i]
            if noOfUnitsRequiredToTravel>totalGasInBike:
                break
            else:
                totalGasInBike -= noOfUnitsRequiredToTravel
        else:
            return 0
        return 1  
