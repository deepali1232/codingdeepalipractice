#remove punctuation by using fun
def remove_pun(sentence,punctuation='!@#$%^&*"""'):
    for item in punctuation:
        if item in sentence:
            sentence=sentence.replace(item,'')
        print(sentence)

msg='hi i am divya**&**"'
remove_pun(msg,'**&*"')
remove_pun(msg)

#add by using fun

def summer(a,b,c=0,d=0):
    print(a+b+c+d)

summer(12,45)
summer(23,79,45)
summer(a=1,b=2,c=4)
summer(2,45,32,45)
summer(1,1,1)