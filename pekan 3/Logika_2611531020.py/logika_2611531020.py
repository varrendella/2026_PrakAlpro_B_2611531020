a1 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1)
print("A2 =", a2)

hasil = a1 and a2
print("\nkonjungsi (AND)")
print("A1 and A2 =", hasil)

hasil = a1 or a2
print("\ndisjungsi (OR)")
print("A1 or A2 =", hasil)

hasil = not a1
print("\nNegasi (NOT)")
print("not A1 =", hasil)

hasil = not a2
print("Negasi A2 (NOT)")
print("not A2 =", hasil)

hasil = a1 != a2
print("\nDisjungsi Exclusive (XOR)")
print("A1 XOR A2 =", hasil)
