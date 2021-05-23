#wap to create a list of names and then remove names that contain 'a' or 'o'
names=['Ayushi','vivek','elex','oshi','preeti','anjali']
names_without_a_and_o=[name for name in names if ('a' not in name.lower()and 'o'not in name.lower())]
print(names_without_a_and_o)