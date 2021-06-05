from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    lst=[]
    if direction=="decode":
        shift*=-1
    for letter in text:
        if letter not in alphabet:
            lst.append(letter)
            continue
        try:
            lst.append(alphabet[alphabet.index(letter)+shift])
        except:
            lst.append(alphabet[alphabet.index(letter)-26+shift])
    print(f"\nYour {direction}d message =","".join(lst))
print(logo)
while 1==1:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    if direction=="encode" or direction=="decode":
        caesar(text,shift,direction)

    else:
        print("Wrong Choice")
    
    c=input("\nDo you want to try again(y/n)? = ").lower()
    if c=='y':
        continue
    else:
        break
