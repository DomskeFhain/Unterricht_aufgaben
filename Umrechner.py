def km2m(kilometer):
    meile = 0.621371
    kilometer = float(input("Gib die Kilometer als Zahl ein, die umgerechnet werden sollen: "))
    meilen = kilometer * meile
    print(f"{kilometer} Kilometer entsprechen " + str(meilen) +" Meilen.")
    
    return kilometer * meile 
def m2(width , height):
    width = float(input("Meter in Breite: "))
    height = float(input("Meter in Höhe: "))
    return width * height

def celsius2fahrenheit(c):
    print("Konvertiert Celsius in Fahrenheit.")

    c_input = float(input("Gib die Celsius als Zahl ein, die umgerechnet werden soll: "))
    fahrenheit_temp = celsius2fahrenheit(c_input)
    print(f"{c_input}°C sind {fahrenheit_temp}°F")
    return (c_input * 9/5) + 32

def fahrenheit2celsius(f):
    print("Konvertiert Fahrenheit in Celsius.")

    f_input = float(input("Gib die Fahrenheit als Zahl ein, die umgerechnet werden soll: "))
    celsius_temp = fahrenheit2celsius(f_input)
    print(f"{f_input}°F sind {celsius_temp}°C")
    return (f_input - 32) * 5/9
    
def umrechner():
    userinput =  input("Was möchtest du ausrechnen (km2m/m2/c2f/f2c): ")
    
    if  userinput == "km2m":
        km2m(userinput)
    elif userinput == "m2":
      m2(userinput)

    elif userinput == "c2f":
        celsius2fahrenheit(userinput)

    elif userinput == "f2c":
        fahrenheit2celsius(userinput)

    else:
        print("Eingabe konnte nicht verarbeitet werden. Vielleicht ein Tippfehler ist dabei.")

umrechner()