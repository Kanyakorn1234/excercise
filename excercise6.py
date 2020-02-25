usernameInput=input("username:")
passwordInput=input("password:")
if usernameInput==("admin") and passwordInput==("1234"):
    print("----welcome------")
    print("apple  30 THB")
    print("orange 20 THB")
    print("mango  40 THB")
    print("milk   20 THB")
    a = input("number apple:")
    result = (int(a))*30
    print("total apple")
    print(result)
    b = input("number orange:")
    result1 = (int(b))*20
    print("total orange")
    print(result1)
    c = input("number mango:")
    result2 = (int(c))*40
    print("total mango")
    print(result2)
    d = input("number milk:")
    result3 = (int(d))*20
    print("total milk")
    print(result3)
    print("---------------------------------")
    result4 = int(result)+int(result1)+int(result2)+int(result3)
    print("TOTAL")
    print(result4)
    print("---------------------------------")
    print("thank you")

