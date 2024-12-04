# python weight calculator

# weight = float(input("Enter your weight : "))
# unit = input("(L)bs or (K)g: ")

# if unit.upper() == "L":
#     converted = round(weight * 0.45, 1)
#     print(f"You are {converted} kilos")
# elif unit.upper() == "K":
#     converted = round(weight / 0.45, 1)
#     print(f"You are {converted} pounds")
# else:
#     print("Invalid unit")

# # # Running the main event loop

def convert_weight(weight, unit):
    if unit.upper() == "L":
        return round(weight * 0.45, 1), "kilos"
    elif unit.upper() == "K":
        return round(weight / 0.45, 1), "pounds"
    else:
        return None, "Invalid unit"

def main():
    weight = float(input("Enter your weight: "))
    unit = input("(L)bs or (K)g: ")
    
    converted, unit_name = convert_weight(weight, unit)
    
    if converted is not None:
        print(f"You are {converted} {unit_name}")
    else:
        print(unit_name)

if __name__ == "__main__":
    main()