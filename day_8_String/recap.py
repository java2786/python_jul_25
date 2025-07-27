player = "saCHin rAMesh tENduLkar"

fs = player.index(" ") # 6
ss = player.index(" ", fs+1) # 13

print(player[0:fs].capitalize()) 
print(player[fs+1:ss].capitalize()) 
print(player[ss+1:].capitalize())

# print(player[0:fs].capitalize(),player[fs+1:ss].capitalize(),player[ss+1:].capitalize())

# print(" ".join(["mango","apple","grapes"]))
print(" ".join([player[0:fs].capitalize(),player[fs+1:ss].capitalize(),player[ss+1:].capitalize()]))
print(player.title())