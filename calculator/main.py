import scientific_calc.trig as st
import standard_calc.basics as sb
x = float(input("Enter x value: "))
y = float(input("Enter y value: "))
print("\n1. Scientific")
print("2. Standard")
choice = int(input("Enter the choice: "))
if choice == 1:
    print("\n1. sin")
    print("2. cos")
    print("3. tan")
    print("4. root")
    print("5. degrees")
    print("6. radians")
    ch1 = int(input("Enter your choice: "))
    if ch1 == 1:
        print(st.sin(x))
    elif ch1 == 2:
        print(st.cos(x))
    elif ch1 == 3:
        print(st.tan(x))
    elif ch1 == 4:
        print(st.root(x))
    elif ch1 == 5:
        print(st.degrees(x))
    elif ch1 == 6:
        print(st.radians(x))
    else:
        print("Invalid scientific operation choice.")
elif choice == 2:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Power")
    ch2 = int(input("Enter your choice: "))
    if ch2 == 1:
        print(sb.add(x, y))
    elif ch2 == 2:
        print(sb.sub(x, y))
    elif ch2 == 3:
        print(sb.mul(x, y))
    elif ch2 == 4:
        print(sb.div(x, y))
    elif ch2 == 5:
        print(sb.mod(x, y))
    elif ch2 == 6:
        print(sb.floor(x, y))
    elif ch2 == 7:
        print(sb.pow(x, y))
    else:
        print("Invalid standard operation choice.")
else:
    print("Invalid main menu choice.")
