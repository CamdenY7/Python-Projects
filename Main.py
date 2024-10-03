import Functions
yes = True
while yes:
  B_D = input("Is your number Binary or Decimal? ")
  if B_D == "Binary":
    Functions.Binary_To_Decimal()
  elif B_D == "Decimal":
    Functions.Decimal_To_Binary()
  else:
    print("Please put Binary or Decimal")