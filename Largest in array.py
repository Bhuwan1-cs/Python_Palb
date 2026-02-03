 def largest(self, arr):
        # code here
        lar=arr[0]
        for i in range (len(arr)):
            if lar<arr[i]:
                lar=arr[i]
                
        return lar
