lista = ["hello", "my", "name", "is", "kesav", "and", "I", "am", "in", "tution"]
"""
{}
"""
dict = {}
def dictmaker(listx):
    global dict
    for i in range(0, len(listx)):
        if hash(listx[i])%5 not in dict:
            dict[hash(listx[i])%5] = [listx[i]]
        else:
            dict[hash(listx[i]) % 5].append(listx[i])



def search(key):
    keymod = hash(key)%5
    if key in dict[keymod]:
        print(keymod)
        print("It's there.")
    else:
        print("Not there.")




dictmaker(lista)
search("keav")
print(dict)