def maxSubarraySum(self, arr):
        # Code here
        tempsum=0
        maxsum=arr[0]
        for i in range(len(arr)):
            tempsum+=arr[i]
            maxsum=max(maxsum,tempsum)
            
            if tempsum<=0:
                tempsum=0
            
        return maxsum
