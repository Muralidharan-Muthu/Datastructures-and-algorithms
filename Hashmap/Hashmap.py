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

# SEPERATE CHAINING COLLISION HANDLING  in this class
class HashMapCollisionHandled(HashMap):
    
    def __init__(self):
        # get variables from the parent class HashMap
        super().__init__()
        self.Array = [[] for x in range(self.MAX)]
    
    # overriding the method for collision handling (seperate chaining)
    def __setitem__(self, key, value):
        h = self.getHash(key)
        found = False
        for index,element in enumerate(self.Array[h]):
            if (len(element) == 2) and (element[1] == key):
                found = True
                self.Array[h][index] = (key,value)
        if not found:
            self.Array[h].append((key,value))

    # overriding the method for collision handling (seperate chaining)
    def __getitem__(self, key):
        h = self.getHash(key)
        for element in self.Array[h]:
            if element[0] == key:
                return element[1]
    
    # overriding the method to delete the (key,value) in the array
    def __delitem__(self, key):
        h = self.getHash(key)
        for index,element in enumerate(self.Array[h]):
            if element[0] == key:
                del self.Array[h][index]
    
    # overriding the method to show all the element in 2D array
    def show(self):
        for element in self.Array:
            print(element)
        
        
if __name__ == "__main__":
    # HashMap class instance
    HM = HashMap()

    # set (key,value) to HashMap
    HM.add("Apple",49)
    HM.add("Banana",52)
    HM['Orange'] = 35
    HM['Strawberry'] = 46

    # get value from HashMap by using the key
    print(HM['Apple'])
    print(HM['Orange'])

    # Deleting value using key
    del HM['Apple']

    # show full array
    HM.show()
    
    print("----------------------------------------------------")
    # HashMapCollisionHandled class instance

    HMCH = HashMapCollisionHandled()

    # set (Key,value) pair
    HMCH["Carrot"] = 30
    HMCH["Raddish"] = 50
    HMCH["Brinjal"] = 40
    HMCH["Potato"] = 70
    HMCH["Tomato"] = 60
    HMCH["Optato"] = 20

    # get value using key
    print(HMCH["Brinjal"])
    print(HMCH["Potato"])

    # delete value using key
    del HMCH["Potato"]

    # show full array
    HMCH.show()