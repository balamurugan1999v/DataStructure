def insertbeg(llist,val):
    llist.insert(0,val)
def insert_pos(llist,val,pos):
    llist.insert(pos-1,val)
def insert_end(llist,val):
    llist.append(val)
def delete_beg(llist):
    del llist[0]
def delete_pos(llist,pos):
    del llist[pos-1]
def display(llist):
    for i in range(len(llist)-1):
        print(llist[i],end="->")
    print(llist[-1])
def delete_end(llist):
    del llist[len(s1)-1]
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
            what=int(input('\n1.Begining\n2.Another position\n3.End\n:'))
            if what==1:
                val=input('enter the value')
                insertbeg(llist,val)
            if what==2:
                val=input('enter the value')
                pos=int(input('enter the position'))              
                insert_pos(llist,val,pos)
            if what==3:
                val=input('enter the value')
                insert_end(llist,val)
        if choice==2:
            if len(llist)==0:
                print('Empty')
            else:
                what=int(input('\n1.Beginning\n2.Another position\n3.End\n:'))
                if what==1:
                    delete_beg(llist)
                if what==2:
                    pos=int(input('enter the position'))
                    if pos<=len(llist):
                        delete_pos(llist,pos)
                    else:
                        print('Out of range')
                if what==3:
                    delete_end(llist)
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
