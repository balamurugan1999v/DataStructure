def enqueue(llist,val):
    llist.append(val)
def dequeue(llist):
    del llist[0]
def display(llist):
    for i in range(len(llist)-1):
        print(llist[i],end="->")
    print(llist[-1])
def search(llist,val):
    if val in llist:
        return True
    else:
        return False
def main():
    llist=[]
    choice=0
    while choice!=5:
        choice=int(input(('\n\t\t1.INSERT\n\t\t2.DELETE\n\t\t3.DISPLAY\n\t\t4.SEARCH\n\t\t5.EXIT\nEnter your Choice:')))
        if choice==1:
            val=input('enter the value')
            enqueue(llist,val)
        if choice==2:
            if len(llist)==0:
                print('Empty')
            else:
                dequeue(llist)
        if choice==3:
            if len(llist)==0:
                print('Empty')
            else:
                display(llist)
        if choice==4:
            if len(llist)==0:
                print('Empty')
            else:
                data=int(input('Enter the data to be search:'))
                y=search(llist,data)
                print(y)

main()
