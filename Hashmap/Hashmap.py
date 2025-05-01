
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
    
    def show(self):
        print(self.Array)

if __name__ == "__main__":
    HM = HashMap()
    HM.add("Apple",49)
    HM.add("Banana",52)
    HM.show()



