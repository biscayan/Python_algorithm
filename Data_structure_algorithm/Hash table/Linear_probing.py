class Linear_probing:

    def __init__(self,size):
        self.size=size
        self.keys=[None]*self.size
        self.values=[None]*self.size

    def hash(self,key):
        
        #if key is integer
        if isinstance(key,int)==True:
            return key%self.size

        #if key is character
        if key.isalpha()==True:
            sum=0
            for string in range(len(key)):
                sum+=ord(key[string]) #based on ASCII code
            return sum%self.size

    def put(self,key,data):

        index=self.hash(key)

        while self.keys[index]!=None:
            if self.keys[index]==key:
                self.values[index]==data
                return

            index=(index+1)%self.size

        self.keys[index]=key
        self.values[index]=data

    def get(self,key):

        index=self.hash(key)

        while self.keys[index]!=None:
            if self.keys[index]==key:
                return self.values[index]
            
            index=(index+1)%self.size
        
        #if key is not in the table
        return None

        