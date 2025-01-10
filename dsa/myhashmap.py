class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(self.size) ]

    def _hash(self,key):
        return key % self.size
    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = [key,value]
                return
            
        bucket.append([key,value])
        print(self.buckets)
        
            
            
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self._hash(key)
        bucket = self.buckets[index]
                      
        for (k,v) in bucket:
            
            if k == key:
                return v
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
            

obj = MyHashMap()
obj.put(1,2)
param_2 = obj.get(1)
obj.put(3,4)
obj.put(1003,1004)
