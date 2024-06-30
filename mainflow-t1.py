#operating on lists

lst=[1,2,4,6,8,11,12,14]            #declaration of list

lst.append(16)                      #addition of element in list

lst.remove(1)                       #removal of element from list

lst[4]=(10)                         #updating element in list

print("updated list is \n",lst)     #displaying the updated list

print("\n\n")


#operating on dictionaries

dic= {'Name':'Shivam','age':'19','city':'Jharkhand'}         #declaration of dictionary
 
dic['geder']='male'                                          #addition of element in dictionary

del dic['age']                                               #removal of element from dictionary

dic['city']='ranchi'                                         #updating element in dictionary

print("updated dictionary is\n ",dic)                        #displaying the updated dictionary

print("\n\n")


#opertating on sets

set={1,2,3,4,5,7}                               #declaration of set

set.add(9)                                      #addition of element in set

set.remove(1)                                   #removal of element from set

set.discard(4)                                  #removal of element from set

print("updated set is \n",set)                  #displaying the updated set

