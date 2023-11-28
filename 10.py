class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next 
    def getData(self):
        return self.data
    def setData(self,data):
        self.data=data
    def getNextData(self):
        return self.next
    def setNextData(self,Node):
        self.next=Node
        
class LinkedList:
    def __init__(self,head=None):
        self.head=head 
        self.size=0
    def getSize(self):
        return self.size
    def addNode(self,data):
        node=Node(data,self.head)
        self.head=data
        self.size+=1
        return True
   
                
        return False
    def findNode(self,value):
        cur=self.head 
        while cur:
            if(cur.getData()==value):
                return True
            else:
                cur=cur.getNextData()
        return False
    def printLL(self):
        cur=self.head 
        while cur:
            print(cur.data)
            cur=cur.getNextdata()
myList=LinkedList()
print("inserting values into LinkedList")
print(myList.addNode(100))
print(myList.addNode(200))
print(myList.addNode(300))
print("removing value from list is 200")

myList.printLL()
print("value is 300 found is",myList.findNode(300))
        