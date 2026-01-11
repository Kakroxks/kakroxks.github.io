print("Nuke.")

def nuke():
    amount = int(input("How much nuke"))
    i = 0
    while i != amount:
        print("NUKE")   
        i += 1
    print("Everyone has died.")

a = 0

while a != "no":
    nuke()
    a = input("Want to nuke again? (yes/no):").lower()

print("alr. you killed everyone tho. :)")
