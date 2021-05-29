#for using values of fun use return
def mean(*numbers):
    if numbers:
        return sum(numbers)/len(numbers)

n1=mean(1,2,3,4,5,6)
print(mean(1,2,3,4,5,6))
n2=n1*10
print('mean *10',n2)


def word_counter(sentence=''):
    if sentence:
        words=sentence.split()
        count=len(words)
        return count



from string import punctuation
def clean_punc(sentence):
    for char in punctuation:
        sentence=sentence.replace(char,'')
        return sentence



c1=word_counter('')
c2=word_counter('hi , i am divya')



s='hi i am mca student,hj,sk.kis'
clean_s=clean_punc(s)
count=word_counter(clean_s)
print(s)
print(clean_s)
print(count)
c=word_counter(clean_punc(s))

