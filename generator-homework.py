def gensquares(N):
  for n in range(N):
    yield n**2
  
for eachNumber in gensquares(10):
  print (eachNumber)