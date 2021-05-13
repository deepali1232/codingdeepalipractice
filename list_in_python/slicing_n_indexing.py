numbers=[11,12,13,14,15,16,17,18,19,20]
print(numbers,'size =',len(numbers))
names=['divya','riya','priya','sita','gita','ayushi','deepali']
print(names,'size =',len(names))
heights=['divya',6,'riya',5.7,'ayushi',4.5]
print(heights,'size =',len(heights))
info=[True,False,True,False]
print(info,'size =',len(info))
marks=[[23,26,37],[78,56,66],[35,85,46],[53,89,88]]
print(marks,'size =',len(marks))
teams=[['divya','riya'],['fiza','kalpana','lalita'],['bindu','rajni','sudha']]
print(teams,'size =',len(teams))
primes=[2,3,5,7,11]
print(primes)
                                        #generating a large list

one_thousand_items=list(range(1,1001))
print(one_thousand_items)
even_list=list(range(2,101,2))
print(even_list)
odd_list=list(range(1,101,2))
print(odd_list)
                                            #indexing
x=numbers[4]
print(x)
y=names[3]
print(y)
print(heights[-1])
print(marks[0][1])
print(marks[-1][-2])
print(teams[0][-2])
                                            #slicing
first_two_no=numbers[:2]
print(first_two_no)
last_two_no=numbers[-2:]
print(last_two_no)
first_3_names=names[:3]
print(first_3_names)
even_idx_no=names[::2]
print(even_idx_no)
print(primes[::-1])
two_sub_marks=marks[0][:2]
print(two_sub_marks)
last_two_marks=marks[-1][-2:]
print(last_two_marks)