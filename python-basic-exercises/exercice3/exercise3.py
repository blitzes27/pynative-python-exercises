g = str(input("ge mig en sträng: "))
# lösning på en rad
z = g[::2]
print("du skrev ", g, "svaret är ", z)
# lösning neråt
print("om du föredrar att läsa upp -> ner")
for i in g[::2]:
    print(i)
