from geometry import area_circle,area_rectangle

#user input
print("1.Area of circle")
print("2.Area of rectangle")
choice=int(input("Enter your choice: "))

if choice==1:
    r=float(input("Enter radius:"))
    print("Area of circle=",area_circle(r))

elif choice==2:
    l=float(input("Enter length:"))
    w=float(input("Enter width:"))
    print("Area of ractangle=",area_rectangle(l,w))

else:
    print("Invalid choice")