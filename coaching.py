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