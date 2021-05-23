#wap where user can add contacts  for contact book/display name
#user has to enter a contact name
#if the name is not given program quit
#if the contact is available then the number is shown
#else if the contact is n ot available the number is asked fro user to save
contacts={'help':100}
print('your temp contact book>')
while True:
    print('>>>>'*20)
    name=input('>>enter name>>')
    if name:
        if name in contacts:
            print('found')
            print(f'{name}:{contacts[name]}')
        else:
            print('contact not found')
            update=input('do you want to add the contact(y/n)>>')
            if update.lower()=='y':
                number=input(f'>.enter contact number for (name)')
                contacts[name]=number
                print(f'contact update for (name)')
    else:
        print('closing contact book')
        break