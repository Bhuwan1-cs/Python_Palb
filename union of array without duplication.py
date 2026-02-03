def findUnion(self, a, b):
        # code here
        arr=[]
        arr.extend(a)
        arr.extend(b)
        return list(set(arr))
