class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertbeg(self,data):
        if (self.head==None):
            self.head=self.tail=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
            newnode=None
    def insertpos(self,data,pos):
        abi=self.head
        co=0
        while abi != self.tail:
            co+=1
            abi=abi.next
        if co<=pos-1:
            print('position not valid')
        else:
            newnode=Node(data)
            temp=self.head
            for i in range(pos-1):
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode
            temp=newnode=None
    def insertend(self,data):
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
    def deletebeg(self):
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
    def deleteend(self):
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
    def deletepos(self):
        c=0
        abi=self.head
        while abi is not None:
            c+=1
            abi=abi.next
        if(c==0):
            return True
        else:
            pos=int(input('Enter the position'))
            temp=self.head
            if(c==1):
                self.head=self.tail=None
            else:
                for i in range(pos-1):
                    temp=temp.next
                currentnode=temp.next
                temp.next=currentnode.next
                currentnode=None
            
a=SLL()
s=0
while s!=5:
    s=int(input('\n\t1.center\n\t2.Front\n\t3.End\n\t4.display\n\t5.Exit\n\t6.counter\n\t7.delbeg\n\t8.delend\n\t9.delpos'))
    if s==1:
        data=input('Enter the data')
        pos=int(input('Enter the position'))
        a.insertpos(data,pos)
    if s==2:
        data=input('Enter the data')
        a.insertbeg(data)
    if s==3:
        data=input('Enter the data')
        a.insertend(data)
    if s==4:
        a.display()
    if s==6:
        a.counter()
    if s==7:
        y=a.deletebeg()
        if y==True:
            print('Empty')
    if s==8:
        y=a.deleteend()
        if y==True:
            print('Empty')
    if s==9:
        
        y=a.deletepos()
        if y==True:
            print('Empty')
