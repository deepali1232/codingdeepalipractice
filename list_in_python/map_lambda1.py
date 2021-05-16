cir = lambda r: 2 * r * 3.14
data=[3,3.23,46,467]
results=[]
#normal
for radius in data:
    out=cir(radius)
    results.append(out)
print(results)
#comprehension
results=[cir(radius) for radius in data]
print(results)
#map function
results=list(map(cir,data))
print(results)

