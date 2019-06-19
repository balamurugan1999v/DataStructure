class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def peek(self):
        return self.tail.data
    def push(self,data):
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
    def pop(self):
        abi=self.head
        c=0
        while abi is not None:
            c+=1
            abi=abi.next
        if(c==0):
            return True
        else:
            temp=self.head
            c=0
            while temp is not None:
                c+=1
                temp=temp.next
            temp=self.head
            for i in range(c-2):
                temp=temp.next
            temp.next=None
            self.tail=None
            self.tail=temp
            temp=None
          
a=SLL()
s=0
while s!=5:
    s=int(input('\n\t1.PUSH\n\t2.POP\n\t3.PEEK\n\t4.DISPLAY\n\t5.EXIT'))
    if s==1:
        data=input('Enter the data')
        a.push(data)
    if s==2:
        a.pop()
    if s==3:
        y=a.peek()
        print(y)
    if s==4:
        a.display()
