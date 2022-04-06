quetion_list = [
    [" in the game of iudo the discs or tokens are of how many colours?"],
    ["where was the BRICS summit held in 2014 ?"],
    ["which of these terms can only be used for women"],
    ["which of the following corresponds to ek bataa do ?"],
    [" who wrote the introduction to the english translation of rabindranath tagore's gitanjali"]
]

option=[
    ["one","two","three","four"],
    ["brazil","india","russia","china"],
    ["dirghaayu","suhagan","chiranjeevi","sushil"],
    ["pura","sawa","adha","pauna"],
    ["P.B.shelley","alfred tennyson","W.B yeats","T.S elliot"]
]

life_line=[
    ["4)four","2)tow"],
    ["1)brazil","3)russia"],
    ["2)suhagan","1)dirghaayu"],
    ["3)adha","2)sawa"],
    ["3)W.B yeats","4)T.S Elliot"]
]
ans_list=[4,1,1,3,3]
print("🌸🌻🌹 WELLCOME TO KBC🌹🌻🌸")
print("KON🤷🏾‍♀️BANEGA CHOR💸💵KA PATI")
i=0
c=0
s=10000
while i<len(quetion_list):
    print(quetion_list[i])
    a=0
    while a<len(option[i]):
        k=option[i][a]
        print(a+1,k)
        a=a+1
    if c==0:
        life_line=input("do you want to use life_line n/y:-")
        if life_line=="yes":
            c+=1
            print(life_line[i])
            s+=10000
    ans=int(input("enter your potion:-"))
    if ans_list[i]==ans:
        print("congratulationt you have earn😍🎉🥳",s)
        s+=10000
    else:
        print("uups you choose a ans😥👎 ")
        break
    i+=1


















    
