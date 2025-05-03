
class HashMap:
    def __init__(self):
        self.MAX = 50 # array size
        self.Array = [None for x in range(self.MAX)]

    # By using this method to get the hash value for the Key
    def getHash(self, key: str):
        h = 0
        for char in key:
            h += ord(char)
        return (h % 10)
    
    def add(self,key: str,value: int):
        # Got the index value for our main value to store
        h = self.getHash(key)
        self.Array[h] = value

    # This method is mainly used to get the value for a key
    def get(self,key):
        # by taking the key. It will provide the value 
        index = self.getHash(key)
        return self.Array[index]
        
    def __setitem__(self,key: str,value: int):
        # Got the index value for our main value to store
        h = self.getHash(key)
        self.Array[h] = value

    # This method is mainly used to get the value for a key
    def __getitem__(self,key):
        # by taking the key. It will provide the value 
        index = self.getHash(key)
        return self.Array[index]
    
    def __delitem__(self,key):
        index = self.getHash(key)
        self.Array[index] = None
     
    def show(self):
        print(self.Array)

    # lets see collisions in the next video



if __name__ == "__main__":
    HM = HashMap()
    HM.add("Apple",49)
    HM.add("Banana",52)
    print(HM.get("Apple"))

    # lets use the __getitem__() and __setitem__() without specifing the method name
    HM['Orange'] = 35
    HM['Strawberry'] = 46

    print(HM['Apple'])
    print(HM['Orange'])
    HM.show()

    del HM['Apple']
    
    HM.show()
 
 



