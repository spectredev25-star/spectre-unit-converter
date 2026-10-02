from colors import Colors
from messages import mass_converter_msg, length_converter_msg, temperature_converter_msg, time_converter_msg

intro = f'''
    =====================  
    {Colors.CYAN}SPECTRE UNIT CONVERTER{Colors.RESET}
    =====================
'''

dimension_menu = f'''
    {Colors.YELLOW}[1].{Colors.RESET} 📏Length
    {Colors.YELLOW}[2].{Colors.RESET} Mass
    {Colors.YELLOW}[3].{Colors.RESET} 🌡Temperature
    {Colors.YELLOW}[4].{Colors.RESET} ⌚Time
    {Colors.YELLOW}[0].{Colors.RESET} ❌Quit
'''

def getUnit():
    while True:
            try:
                unit = input("> ")
                unit = int(unit)
                return unit
            except ValueError:
                print('Please input a valid number.')

def getNum():
    while True:
            try:
                num = input("Input the number you would like to convert> ")
                num = float(num)
                return num
            except ValueError:
                print('Please input a number')

def getDimension():
    while True:
        try:
            dimension = input("> ")
            dimension = int(dimension)
            return dimension
        except ValueError:
            print('Type 1,2,3 or 4')


def mass_converters():
    unit = getUnit()
    num = getNum()
    if unit == 1:
        output = f"{num}KG is equivalent to {num * 1000}G"
    elif unit == 2:
         output = f"{num}G is equivalent to {num / 453.592}Lb"
    else:
         print("Oops! can't make this conversion now")
    return output
         

def temperature_converters():
    unit = getUnit()
    num = getNum()
    if unit == 1:
        output = f"{num - 273.15}K is equivalent to {num - 273.15}C"
    elif unit == 2:
        output = f"{num}C is equivalent to {(num * 1.8) + 32}F"
    elif unit == 3:
        output = f"{num}C is equivalent to {num + 273.15}K"
    elif unit == 4:
        output = f"{num}F is equivalent to {num + 273.15}C"
    else:
        print("Oops! can't make this conversion now")
    return output

def length_converters():
    unit = getUnit()
    num = getNum()
    if unit == 1:
        output = f"{num}Km is equivalent to {num * 0.6209}Miles"
    elif unit == 2:
        output = f"{num}m is equivalent to {num * 0.6209}feets"
    elif unit == 3:
        output = f"{num}feets is equivalent to {num * 0.3048}m"
    elif unit == 4:
        output = f"{num * 2.54}Inches is equivalent to {num * 2.54}cm"
    else:
        print("Oops! can't make this conversion now")
    return output

def time_converters():
    unit = getUnit()
    num = getNum()
    if unit == 1:
        output = f"{num}mins is equivalent to {num / 60}s"
    elif unit == 2:
        output = f"{num}mins is equivalent to {num * 60}hrs"
    elif unit == 3:
        output = f"{num}hr is equivalent to {num * 3600}s"
    else:
         print("Oops! can't make this conversion now")
    return output

def main():
    print(intro)
    while True:
        print(dimension_menu)
        dimension = getDimension()
        if dimension == 1:
            print(length_converter_msg)
            output = length_converters()
            print(output)
        elif dimension == 2:
            print(mass_converter_msg)
            output = mass_converters()
            print(output)
        elif dimension == 3:
            print(temperature_converter_msg)
            output = temperature_converters()
            print(output)
        elif dimension == 4:
            print(time_converter_msg)
            output = time_converters()
            print(output)
        elif dimension == 0:
            break
        else:
            print("Hmmm, I don't seem to understand")
    
    
if __name__ == '__main__':
    main()


