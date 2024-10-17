import math
plsolids = ["tetrahedron","cube","octahedron","icosahedron","dodecahedron"]
solid = int(input("Select a platonic solid: enter '0' for 'tetrahedron', '1' for 'cube', '2' for 'octahedron', '3' for 'icosahedron', '4' for 'dodecahedron': "))
a = 0
volume = 0
if solid == 0:
    print("You have chosen 'tetrahedron'")
    a = float(input("Enter the lenght of the solid (in metres): "))
    volume = str(((a*a*a)/(6*math.sqrt(2))))
    print("The volume of the tetrahedron is "+volume+ " m^3")
elif solid == 1:
    print("You have chosen 'cube'")
    a = float(input("Enter the lenght of the solid (in metres): "))
    volume = str(a*a*a)
    print("The volume of the cube is "+volume+ " m^3")
elif solid == 2:
    print("You have chosen 'octahedron'")
    a = float(input("Enter the lenght of the solid (in metres): "))
    volume = str((a*a*a)*(math.sqrt(2)/3))
    print("The volume of the octahedron is "+volume+ " m^3")
elif solid == 3:
    print("You have chosen 'icosahedron'")
    a = float(input("Enter the lenght of the solid (in metres): "))
    volume = str((a*a*a)*(5/12)*(3 + math.sqrt(5)))
    print("The volume of the icosahedron is "+volume+ " m^3")
elif solid == 4:
    print("You have chosen 'dodecahedron'")
    a = float(input("Enter the lenght of the solid (in metres): "))
    volume = str((a*a*a)*(1/4)*(15 + 7*math.sqrt(5)))
    print("The volume of the dodecahedron is "+volume+ " m^3")
else:
    print("Invalid input")