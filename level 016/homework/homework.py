# 1
def student(saxeli, asaki, qula):
    print(f"მოსწავლის სახელია {saxeli}, ასაკია {asaki}, ქულაა {qula}.")
student("Gio", 15, 95)


# 2
def shekreba(a, b, c):
    print(f"ჯამი: {a + b + c}")
    print(f"ნამრავლი: {a * b * c}")
shekreba(2, 3, 4)


# 3
def shefaseba(saxeli, qula):
    if qula >= 90:
        print(f"{saxeli}: შესანიშნავი")
    elif qula >= 70:
        print(f"{saxeli}: კარგი")
    else:
        print(f"{saxeli}: საჭიროა გაუმჯობესება")
shefaseba("Gio", 85)


# 4
def pasdakleba(produkti, pasi, procenti=15):
    axali_pasi = pasi - (pasi * procenti / 100)
    print(f"{produkti} ფასდაკლებით ღირს {axali_pasi} ლარი")
pasdakleba("ბურთი", 100)


# 5
def asaki(saxeli, dabadebis_weli):
    asaki = 2026 - dabadebis_weli
    print(f"{saxeli}-ის ასაკია {asaki} წელი")
asaki("Gio", 2011)


# 6
def ricxvis_shemowmeba(n):
    if n > 0:
        print("დადებითი")
    elif n < 0:
        print("უარყოფითი")
    else:
        print("ნულია")
ricxvis_shemowmeba(5)


# 7

def kalkulatori(a, b, operacia):
    if operacia == '+':
        print(a + b)
    elif operacia == '-':
        print(a - b)
    elif operacia == '*':
        print(a * b)
    elif operacia == '/':
        if b != 0:
            print(a / b)
        else:
            print('0 გაყობა არ შეიძლება')
    else:
        print('არასწორი მოქმენდება')
kalkulatori(15, 5, '*')



# 8
def sashualo(a, b, c, d):
    print(f"საშუალო არითმეტიკულია {(a + b + c + d) /4}")
sashualo(10, 20, 30, 40)


# 9

def paroli(saxeli, password, cda=3):
    if password == "deme123":
        print(f"{saxeli}, შესვლა წარმატებულია!")
    else:
        print(f"{saxeli}, პაროლი არასწორია. ცდების რაოდენობა: {cda}")
paroli("Gio", "deme123")