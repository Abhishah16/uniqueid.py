#ac= acc[0]
FN=input("Ënter the first name:")
fr_len=len(FN)
for i in range(0,fr_len):
    if FN.isalpha():
        break
    else:
        print("pls enter the valid input")
        FN = input("Enter your frist name: ")
        
        
        
LN=input("Enter the last name:")
la_len=len(LN)
for i in range(0,la_len):
    if LN.isalpha():
        break
    else:
        print("pls enter the valid input")
        LN= input("Enter your last name: ")
        
        

MN=input("pls enter the mobile number")
lenM=len(MN)
for i in range(0,lenM):
    if lenM==10:
        if MN.isdigit():
            break
        else:
            print("pls enter the valid input")
            MN=input("pls enter the mobile number")
    else:
        print("pls enter the valid input")
        MN=input("pls enter the mobile number")
        break
        
        
        
pin = (input("enter pincode: "))
lenp=len(pin)
for i in range(0,lenp):
    if lenp==6:
        if pin.isdigit():
            break
        else:
            print("pls enter the valid input")
            pin = (input("enter pincode: "))
    else:
        print("pls enter the valid input")
        pin = (input("enter pincode: "))
        break


        
ACC_TYPE_DIC={'personal':0,'private company':1,'CEO':2,'NGO':3,'govt':4,'defence':5}
print(ACC_TYPE_DIC)


acc = (input("enter your account type:")) 
#lena=len(acc)
#a=list(ACC_TYPE_DIC.values())
ab= ACC_TYPE_DIC.get(acc,"invalid type")
#while i<lena:
#        if ab!=a[i]:
#            print("pls enter the valid input")
#            acc = (input("enter your account type:")) 
#            break
#        else:
#            break


ac=str(ab)        
p= pin[:6]
fn= FN[0]
ln= LN[0]        
SMN=int(MN[0])+int(MN[1])+int(MN[2])+int(MN[3])+int(MN[4])+int(MN[5])+int(MN[6])+int(MN[7])+int(MN[8])+int(MN[9])
SMN1=str(SMN)
len1=len(SMN1)
if len1==2:
    SMN3=int(SMN1[0])+int(SMN1[1])
    SMN2=str(SMN3)
    len2=len(SMN2)
    if len2!=1:
        SMN4=int(SMN2[0])+int(SMN2[1])
        SMN5=str(SMN4)
        
        if SMN5=='1':
            unq= p+fn+ln+'!'+ac
            print("the unique ID is {0}".format(unq))
        if SMN5=='2':
            unq= p+fn+ln+'@'+ac
            print("the unique ID is {0}".format(unq))
        if SMN5=='3':
            unq= p+fn+ln+'#'+ac
            print("the unique ID is {0}".format(unq))
        if SMN5=='4':
            unq= p+fn+ln+'$'+ac
            print("the unique ID is {0}".format(unq))
        if SMN5=='5':
            unq= p+fn+ln+'%'+ac
            print("the unique ID is {0}".format(unq))
        if SMN5=='6':
            unq= p+fn+ln+'^'+ac
            print("the unique ID is {0}".format(unq))
        if SMN5=='7':
            unq= p+fn+ln+'&'+ac
            print("the unique ID is {0}".format(unq))
        if SMN5=='8':
            unq= p+fn+ln+'*'+ac
            print("the unique ID is {0}".format(unq))
        if SMN5=='9':
            unq= p+fn+ln+'('+ac
            print("the unique ID is {0}".format(unq))
    else:
        if SMN2=='1':
            unq= p+fn+ln+'!'+ac
            print("the unique ID is {0}".format(unq))
        if SMN2=='2':
            unq= p+fn+ln+'@'+ac
            print("the unique ID is {0}".format(unq))
        if SMN2=='3':
            unq= p+fn+ln+'#'+ac
            print("the unique ID is {0}".format(unq))
        if SMN2=='4':
            unq= p+fn+ln+'$'+ac
            print("the unique ID is {0}".format(unq))
        if SMN2=='5':
            unq= p+fn+ln+'%'+ac
            print("the unique ID is {0}".format(unq))
        if SMN2=='6':
            unq= p+fn+ln+'^'+ac
            print("the unique ID is {0}".format(unq))
        if SMN2=='7':
            unq= p+fn+ln+'&'+ac
            print("the unique ID is {0}".format(unq))
        if SMN2=='8':
            unq= p+fn+ln+'*'+ac
            print("the unique ID is {0}".format(unq))
        if SMN2=='9':
            unq= p+fn+ln+'('+ac
            print("the unique ID is {0}".format(unq))
