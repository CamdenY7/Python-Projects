def Binary_To_Decimal():
  total = 0
  number = 1
  Binary_Number = int(input("What's your binary number? "))
  Binary_Number = str(Binary_Number)[::-1]
  for i in Binary_Number:
    if i != "0":
      total += number
    number = number * 2
  print(total)

def Decimal_To_Binary():
  total = 0
  Decimal_Number = int(input("What's your decimal number? "))
  Decimal_Number = str(Decimal_Number)[::-1]
  print(Decimal_Number)