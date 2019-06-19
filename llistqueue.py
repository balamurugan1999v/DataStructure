class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def front(self,data):
        if (self.head==None):
            self.head=self.tail=Node(data)
        else:
            newnode=Node(data)
            self.tail.next=newnode
            self.tail=newnode
            newnode=None
        
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
    def rear(self):
        c=0
        abi=self.head
        while abi is not None:
            c+=1
            abi=abi.next
        if(c==0):
            return True
        else:
            temp=self.head
            temp=temp.next
            self.head=temp
            temp=None
    
a=SLL()
s=0
while s!=4:
    s=int(input('\n\t1.front\n\t2.Rear\n\t3.display\n\t4.Exit'))
    if s==1:
        data=input('Enter the data')
        a.front(data)
    if s==2:
        y=a.rear()
        if y==True:
            print('List underflow')
    if s==3:
        a.display()
