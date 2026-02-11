def menyu():
    print("\n--- ATM ---")
    print("1. Balans")
    print("2. Pul yechish")
    print("3. Pul qo'shish")
    print("4. Chiqish")

def balans_kor(balance):
    print(f"Balans: {balance} so'm")

def pul_yech(balance, summa):
    if summa <= balance:
        return balance - summa
    else:
        print("Balans yetarli emas!")
        return balance

def pul_qosh(balance, summa):
    return balance + summa

balance = 500000

while True:
    menyu()
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        balans_kor(balance)
    elif tanlov == "2":
        s = int(input("Summa: "))
        balance = pul_yech(balance, s)
    elif tanlov == "3":
        s = int(input("Summa: "))
        balance = pul_qosh(balance, s)
    elif tanlov == "4":
        print("Chiqildi.")
        break
    else:
        print("Xato tanlov!")
