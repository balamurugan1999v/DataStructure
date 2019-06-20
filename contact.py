c=0
a={}
print('****   Welcome   ****')
while c!=5:
    print('\nWhat you need to do:\n1.Add\n2.update\n3.delete\n4.search\n5.exit\n6.view contact list')
    val=int(input())
    x=bool(a)
    if val==1:
        name2=input('Enter the name:')
        name=name2.lower()
        num=input('Enter the number:')      
        numlen=len(num)
        a[name]={}
        if numlen!=10:
            print('Invalid number')
            continue
        else:
            a[name]['mobile']=num
        mailid=input('Enter your mailid')
        if '@' not in mailid:
            print('Invalid Mailid')
            continue
        else:
            a[name]['mail']=mailid
            print('Successfully Added!!!')
    if val==3:
        if x==True:
            nam=input('Whose Contact you going to delete?:')
            del a[nam]
            print('Number deleted Successfully')
            print('Successfully deleted!!!')
        else:
            print('No contact')
    if val==4:
        if x==False:
            print('No contact')
        else:
            name=input('Enter the name:')
            if name in a:
                print('Name:',name,'\ndetails:',a.get(sea))
            else:
                print('No contact Found')
    if val==2:
        if x==True:
            name=input('enter the whose contact:')
            inp=int(input('1.Name change\n2.Number change\n3.mailid change:'))
            if inp==1:
                name1=input('Enter the name:')
                a1=a[name]
                del a[name]
                a[name1]=a1
            elif inp==2:
                number=input('enter the number:')
                a[name]['mobile']=number
            else:
                nmail=input('Enter new mailId')
                if '@' not in nmail:
                    print('Invalid Mailid')
                else:
                    a[name]['mail']=nmail
            print('Successfully Updated!!!')
        else:
            print('No Contact Found')
    c=val
    if val==6:
        d=len(a)
        print('Total Contacts:',d)
        if x==False:
            print('No contacts')
        else:
            for x1,y1 in a.items():
                print('\nName:',x1)
                for q1,q2 in y1.items():
                    print(q1,":",q2)

print('Successfully exited!!!!!')
        
        
