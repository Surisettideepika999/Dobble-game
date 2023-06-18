import string
import random
symbols=[]
symbols=list(string.ascii_letters)#it contains a-z and A-Z as well
card1=[0]*5
card2=[0]*5
ans=random.choice(symbols)
pos1=random.randint(0,4)#here 0 and 4 are inclusive
pos2=random.randint(0,4)
symbols.remove(ans)
if(pos1==pos2):
    card1[pos1]=card2[pos1]=ans
else:
    card1[pos1]=ans
    card2[pos2]=ans
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        card1[i]=random.choice(symbols)
        symbols.remove(card1[i])
        card2[i]=random.choice(symbols)
        symbols.remove(card2[i])
    i=i+1
print(card1)
print(card2)
sol=input("Enter which letter is common : ")
if(sol==ans):
    print("\"You won\"")
else:
    print("You lost!")

