x = [1,2,3,4,5]
fruits = ['apple','pear','guava']
randomval = [69,83,122,10,9]
print("normal ->",x)
x.reverse()                                                     #reverse list
print("reverse ->",x)
x.reverse()                                                     #again reverse
print("back to normal ->",x)
print('normal',fruits)
fruits.sort()                                                   #sort list
print('alphabetical sort',fruits)
randomval.sort()                                                # ascending order
print("sorted",randomval)
randomval.sort(reverse=True)                                    # descending order
print("sorted",randomval)
                                # count function work the same as string count
y = [11,22,3,1,22,33,1,22,3,1,32,2,22,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,2,2,2,2,2,2,]
twenty_two_count = y.count(22)
three_count = y.count(3)
twenty_count =y.count(20)
print('22 occurs =>',twenty_two_count)
print('3 occurs =>',three_count)
print('200 occurs =>',twenty_count)