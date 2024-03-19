for i in range(3):
    for j in range(3):
        if j == 1:
            continue
    print(i, j)


for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)

languages = ["python", "java", "swift", "C", "c++"]
for language in languages:
  if language == "swift" or language == "c++":
    continue
  print(language)

  
name = "ada lovelace"
print(name.title())
print(name.upper())

name = "Albert Einstein"
print(name ,'once said,"a person who has never made a mistake has never tried a new thing"')

bike = ["tvs","honda","senke"]
print(len(bike))
print("i would like to own an",bike[1].title())


motor = ["tvs","honda","senke"]
del motor[2]
print(motor)


invites = ["ritah","sandra","vanessa"]
print("Hi welcome to my bd party", invites[0])
print("Hi welcome to my bd party", invites[1])
print("Hi welcome to my bd party", invites[2])