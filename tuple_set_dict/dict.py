emp={'name':'divya','roll no':1900530149001,'salary':{'basic':12000,'da':1000},'dept':'account'}

emp['phone']=783867426
print(emp)
emp['dept']='sales'
print(emp)
print(emp['name'])
print(emp['salary']['basic'])
print(emp['dept'])
print(emp['roll no'])


stockprices=dict(google=237,facebook=9998.7,netflix=203.23)
print(stockprices)

#add a value
stockprices['disney']=240.78
print(stockprices)

#update a value
stockprices['facebook']=232
print(stockprices)