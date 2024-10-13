import sys

one=1
two=2
five=5
ten=10
twenty=20
fifty=50
selection={"A1": 18, "A2": 22, "A3": 8,"A4": 45, "B1": 19,"B2": 10, "B3": 20,"B4": 13, "C1": 43,"C2": 9, "C3": 34,"C4": 21, "D1": 25,"D2": 7, "D3": 10, "D4": 52}

selected=input("SELECT PRODUCT:")

if selected in selection:
    selected = selection[selected]
else:
    print("INCORRECT PRODUCT CODE")
    sys.exit()
print()
print("PRICE:", selected)

pay=selected
payed=int(input("INSERT MONEY:"))
if payed<pay:
    print()
    print("NOT ENOUGH MONEY")
    print("RETURNED", payed)
    sys.exit()
print("INSERTED:", payed)
returnn= payed-pay
returned=[]
if returnn > 0:
    print()
    print(returnn,"WILL BE RETURNED")
print()
print("THANK YOU FOR YOUR PURCHASE")

while returnn>49:
    returned.append(fifty)
    returnn-=fifty
while returnn>19:
    returned.append(twenty)
    returnn-=twenty
while returnn>9:
    returned.append(ten)
    returnn-=ten
while returnn>4:
    returned.append(five)
    returnn-=five
while returnn>1:
    returned.append(two)
    returnn-=two
while returnn>0:
    returned.append(one)
    returnn-=one
        

if returned[0]>0:
    print()
    print("COINS",returned)
