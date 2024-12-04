
unit = input("Enter the unit of measurement(C/F): ")
temp = float(input("Enter the temperature: "))

if unit.upper() == "C":
    converted = round((temp * 9/5) + 32, 1)
    print(f"The temperature is {converted}F")
elif unit.upper() == "F":
    converted = round((temp - 32) * 5/9, 1)
    print(f"The temperature is {converted}C")
else:
    print("Invalid unit")
    
    
    
# def convert_temp(temp, unit):
#     if unit.upper() == "C":
#         return round((temp * 9/5) + 32, 1), "F"
#     elif unit.upper() == "F":
#         return round((temp - 32) * 5/9, 1), "C"
#     else:
#         return None, "Invalid unit"
    
# def main():
#     unit = input("Enter the unit of measurement(C/F): ")
#     temp = float(input("Enter the temperature: "))
    
#     converted, unit_name = convert_temp(temp, unit)
    
#     if converted is not None:
#         print(f"The temperature is {converted}{unit_name}")
#     else:
#         print(unit_name)
        
# if __name__ == "__main__":
#     main()
    
