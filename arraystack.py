def push(llist,val):
    llist.append(val)
def pop(llist):
    del llist[len(llist)-1]
def peek(llist):
    return llist[-1]
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
        choice=int(input(('\n\t\t1.push\n\t\t2.pop\n\t\t3.DISPLAY\n\t\t4.peek\n\t\t5.EXIT\nEnter your Choice:')))
        if choice==1:
            val=input('enter the value')
            push(llist,val)
        if choice==2:
            if len(llist)==0:
                print('Empty')
            else:
                pop(llist)
        if choice==3:
            if len(llist)==0:
                print('Empty')
            else:
                display(llist)
        if choice==4:
            if len(llist)==0:
                print('Empty')
            else:
                y=peek(llist)
                print(y)

main()
