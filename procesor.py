# Alexander Ottaway - Kasperek  #
# Symulacja procesora 8086      #
# ############################# #

# zewnetrzne biblioteki
import re
import os
import time

# funkcja sprawdza czy dobrze wpisano wartosc do rejestru
def check_register_input(register):
    if len(register) == 2:
        return bool(re.match(r'^[0-9a-fA-F]{2}', register))
    else:
        return False
    
# funkcja wypisywania rejestrow
def display_registers():
    for k, v in registers.items():
        print(f"{k.upper()} = {v}h")

# funkcja zamieniajaca 1 cyfrowa wartosc w 2 cyfrowa 1 -> 01
def digit_fix(value):
    if len(value) == 1:
        return "0" + value
    return value

# funkcja opcji #1 Zmiana wartosci rejestru
def reg_value_change(registers):
    os.system('cls')
    display_registers()
    selected_register = ""
    
    while selected_register != -1:
        selected_register = input("\nSelect a register to change it's value: (Type '-1' to save and exit menu)\n").lower()
        
        if selected_register in registers:
            register_input = input(f"Type in new value for register {selected_register.upper()} (double digit HEX value) --> ")
            if check_register_input(register_input): # czy wartosc jest w systemie HEX i 8 bitowa
                registers[selected_register] = register_input.upper()
            else:
                print("Not a proper input, try again...")
        elif selected_register == '-1':
            break
        else:
            print("Please select one of the listed registers")

        time.sleep(1)
        os.system('cls')
        display_registers()
        
    return registers     

# funkcja opcji #2 Kopiowanie wartosci rejestru
def MOV(registers):
    os.system('cls')
    os.system('color 03')
    display_registers()
    selected_register = ""

    print("\nWelcome to MOV menu. Here you can copy value from one register into the other\n")
        
    while selected_register not in registers:
        selected_register = input("Select a register to copy value FROM: ").lower()
        if selected_register in registers:
            memory = registers[selected_register]
        else:
            print("Not a proper input, try again...")
    
    selected_register = ""

    while selected_register not in registers:
        selected_register = input("Select a register to copy value TO: ").lower()
        if selected_register in registers:
            registers[selected_register] = memory
            del memory
        else:
            print("Not a proper input, try again...")

    os.system('cls')
    print("Moving value...\n")
    display_registers()
    time.sleep(1.5)

    return registers
    
# funkcja opcji #3 Wymiana wartości rejestrów
def XCHG(registers):
    os.system('cls')
    os.system('color 0D')
    display_registers()
    selected_register1 = ""
    selected_register2 = ""
    
    print("\nWelcome to XCHG menu. Here you can switch the values between two registers\n")
        
    while selected_register1 not in registers:
        selected_register1 = input("Select a register number one: ").lower()
        if selected_register1 in registers:
            memory = registers[selected_register1]
        else:
            print("Not a proper input, try again...")
    
    selected_register2 = ""

    while selected_register2 not in registers:
        selected_register2 = input("Select a register number two: ").lower()
        if selected_register2 in registers:
            registers[selected_register1] = registers[selected_register2]
            registers[selected_register2] = memory
            del memory
        else:
            print("Not a proper input, try again...")

    os.system('cls')
    print("Exchanging values...\n")
    display_registers()
    time.sleep(1.5)

    return registers

# funkcja opcji #4 Inkrementacja wartości rejestrów
def INC(registers):
    os.system('cls')
    os.system('color 0E')
    selected_register = ""
    while selected_register not in registers:
        display_registers()
        selected_register = input("Select a register to increment it's value (-1 to exit): ").lower()
        
        if selected_register == "-1":
            break
        
        elif selected_register in registers:
            if registers[selected_register] != "FF":
                registers[selected_register] = digit_fix(str(hex(int(registers[selected_register], 16) + 1))[2:].upper())
                os.system('cls')
            else:
                registers[selected_register] = "00"
            print(f"Incrementing register {selected_register.upper()}'s value")
            time.sleep(2)
            
        else:
            print("Not a proper input, try again...")
            time.sleep(1)
            os.system('cls')
            
    return registers

# funkcja opcji #5 Dekrementacja wartości rejestrów
def DEC(registers):
    os.system('cls')
    os.system('color 0E')
    selected_register = ""
    while selected_register not in registers:
        display_registers()
        selected_register = input("Select a register to decrement it's value (-1 to exit): ").lower()
        
        if selected_register == "-1":
            break
        
        elif selected_register in registers:
            if registers[selected_register] != "00":
                registers[selected_register] = digit_fix(str(hex(int(registers[selected_register], 16) - 1))[2:].upper())
                os.system('cls')
            else:
                registers[selected_register] = "FF"
            print(f"Decrementing register {selected_register.upper()}'s value")
            time.sleep(2)
            
        else:
            print("Not a proper input, try again...")
            time.sleep(1)
            os.system('cls')
            
    return registers

# funkcja opcji #6
def NOT(registers):
    os.system('cls')
    os.system('color 0E')
    selected_register = ""
    while selected_register not in registers:
        display_registers()
        selected_register = input("Select a register to invert it's value (-1 to exit): ").lower()
        
        if selected_register == "-1":
            break
        
        elif selected_register in registers:
            registers[selected_register] = digit_fix(hex(int(registers[selected_register], 16) ^ int('F' * len(registers[selected_register]), 16))[2:]).upper()
            print(f"Inverting register {selected_register.upper()}'s value")
            time.sleep(2)
            
        else:
            print("Not a proper input, try again...")
            time.sleep(1)
            os.system('cls')
            
    return registers

# funkcja opcji #7    
def NEG(registers):
    os.system('cls')
    os.system('color 0E')
    selected_register = ""
    while selected_register not in registers:
        display_registers()
        selected_register = input("Select a register to negate it's value (-1 to exit): ").lower()
        
        if selected_register == "-1":
            break
        
        elif selected_register in registers:
            value = digit_fix(hex(int(registers[selected_register], 16) ^ int('F' * len(registers[selected_register]), 16))[2:]).upper()
            if value != "FF":
                value = digit_fix(str(hex(int(value, 16) + 1))[2:].upper())
                os.system('cls')
            else:
                value = "00"
            print(f"Negating register {selected_register.upper()}'s value")
            time.sleep(2)
            
        else:
            print("Not a proper input, try again...")
            time.sleep(1)
            os.system('cls')
        
        registers[selected_register] = value
    return registers

# funkcja opcji #8
def AND(registers):
    os.system('cls')
    os.system('color 60')
    display_registers()
    selected_register = ""

    print("\nWelcome to AND menu. Perform a bitwise logical AND operation between two operands and stores the result in the destination operand\n")
    
    def and_operation(dest_r, second_r):
        new_value = ["0"] * 8
        dest_r = bin(int(dest_r,16))[2:]
        second_r = bin(int(second_r,16))[2:]

        if len(dest_r) < 8:
            for i in range(8-len(dest_r)):
                dest_r = "0" + dest_r
        if len(second_r) < 8:
            for i in range(8-len(second_r)):
                second_r = "0" + second_r

        for i in range(8):
            if dest_r[i] == "1" and second_r[i] == "1":
                new_value[i] = "1"

        new_value = str(hex(int("".join(new_value),2)))[2:]
        if len(new_value) < 2: new_value = "0" + new_value
        
        return new_value.upper()
        
    while selected_register not in registers:
        selected_register = input("Select the destination operand: ").lower()
        if selected_register in registers:
            destination_register = selected_register
        else:
            print("Not a proper input, try again...")
    
    selected_register = ""

    while selected_register not in registers:
        selected_register = input("Select the second operand: ").lower()
        if selected_register in registers:
            # Perform AND operation
            registers[destination_register] = and_operation(registers[destination_register], registers[selected_register])
        else:
            print("Not a proper input, try again...")

    os.system('cls')
    print("Working on it...\n")
    display_registers()
    time.sleep(1.5)

    return registers     

# funkcja opcji #9
def OR(registers):
    os.system('cls')
    os.system('color 60')
    display_registers()
    selected_register = ""

    print("\nWelcome to OR menu. Perform a bitwise logical OR operation between two operands and stores the result in the destination operand\n")
    
    def or_operation(dest_r, second_r):
        new_value = ["0"] * 8
        dest_r = bin(int(dest_r,16))[2:]
        second_r = bin(int(second_r,16))[2:]

        if len(dest_r) < 8:
            for i in range(8-len(dest_r)):
                dest_r = "0" + dest_r
        if len(second_r) < 8:
            for i in range(8-len(second_r)):
                second_r = "0" + second_r

        for i in range(8):
            if dest_r[i] == "1" or second_r[i] == "1":
                new_value[i] = "1"

        new_value = str(hex(int("".join(new_value),2)))[2:]
        if len(new_value) < 2: new_value = "0" + new_value
        
        return new_value.upper()
        
    while selected_register not in registers:
        selected_register = input("Select the destination operand: ").lower()
        if selected_register in registers:
            destination_register = selected_register
        else:
            print("Not a proper input, try again...")
    
    selected_register = ""

    while selected_register not in registers:
        selected_register = input("Select the second operand: ").lower()
        if selected_register in registers:
            # Perform OR operation
            registers[destination_register] = or_operation(registers[destination_register], registers[selected_register])
        else:
            print("Not a proper input, try again...")

    os.system('cls')
    print("Working on it...\n")
    display_registers()
    time.sleep(1.5)

    return registers     

# funkcja opcji #10
def XOR(registers):
    os.system('cls')
    os.system('color 60')
    display_registers()
    selected_register = ""

    print("\nWelcome to XOR menu. Perform a bitwise logical XOR operation between two operands and stores the result in the destination operand\n")
    
    def xor_operation(dest_r, second_r):
        new_value = ["0"] * 8
        dest_r = bin(int(dest_r,16))[2:]
        second_r = bin(int(second_r,16))[2:]

        if len(dest_r) < 8:
            for i in range(8-len(dest_r)):
                dest_r = "0" + dest_r
        if len(second_r) < 8:
            for i in range(8-len(second_r)):
                second_r = "0" + second_r

        for i in range(8):
            if dest_r[i] != second_r[i]:
                new_value[i] = "1"

        new_value = str(hex(int("".join(new_value),2)))[2:]
        if len(new_value) < 2: new_value = "0" + new_value
        
        return new_value.upper()
        
    while selected_register not in registers:
        selected_register = input("Select the destination operand: ").lower()
        if selected_register in registers:
            destination_register = selected_register
        else:
            print("Not a proper input, try again...")
    
    selected_register = ""

    while selected_register not in registers:
        selected_register = input("Select the second operand: ").lower()
        if selected_register in registers:
            # Perform XOR operation
            registers[destination_register] = xor_operation(registers[destination_register], registers[selected_register])
        else:
            print("Not a proper input, try again...")

    os.system('cls')
    print("Working on it...\n")
    display_registers()
    time.sleep(1.5)

    return registers     
 
# funkcja opcji #11
def ADD(registers):
    os.system('cls')
    os.system('color 60')
    display_registers()
    selected_register = ""
    
    print("\nWelcome to ADD menu. Perform addition on two operands and stores the result in the destination operand\n")

    def add_operation(dest_r, second_r):
        dest_r = int(dest_r,16)
        second_r = int(second_r,16)
        new_value = dest_r + second_r
        if new_value > 255:
            new_value -= 255 # overflow
            
        new_value = str(hex(new_value))[2:]
        if len(new_value) < 2: new_value = "0" + new_value
        
        return new_value.upper()
        

    while selected_register not in registers:
            selected_register = input("Select the destination operand: ").lower()
            if selected_register in registers:
                destination_register = selected_register
            else:
                print("Not a proper input, try again...")
        
    selected_register = ""

    while selected_register not in registers:
        selected_register = input("Select the second operand: ").lower()
        if selected_register in registers:
            # Perform ADD operation
            registers[destination_register] = add_operation(registers[destination_register], registers[selected_register])
        else:
            print("Not a proper input, try again...")

        os.system('cls')
        print("Adding...\n")
        display_registers()
        time.sleep(1.5)
        
    return registers
        
# funkcja opcji #12
def SUB(registers):
    os.system('cls')
    os.system('color 60')
    display_registers()
    selected_register = ""
    
    print("\nWelcome to SUB menu. Perform subtraction on two operands and stores the result in the destination operand\n")

    def sub_operation(dest_r, second_r):
        dest_r = int(dest_r,16)
        second_r = int(second_r,16)
        new_value = dest_r - second_r
        if new_value < 0:
            new_value =  256 + (new_value) # overflow
            
        new_value = str(hex(new_value))[2:]
        if len(new_value) < 2: new_value = "0" + new_value
        
        return new_value.upper()
        

    while selected_register not in registers:
            selected_register = input("Select the destination operand: ").lower()
            if selected_register in registers:
                destination_register = selected_register
            else:
                print("Not a proper input, try again...")
        
    selected_register = ""

    while selected_register not in registers:
        selected_register = input("Select the second operand: ").lower()
        if selected_register in registers:
            # Perform SUB operation
            registers[destination_register] = sub_operation(registers[destination_register], registers[selected_register])
        else:
            print("Not a proper input, try again...")

        os.system('cls')
        print("Subtracting...\n")
        display_registers()
        time.sleep(1.5)
        
    return registers
    
# START GLOWNEGO PROGRAMU
registers = {
    "al":"00",
    "ah":"00",
    "bl":"00",
    "bh":"00",
    "cl":"00",
    "ch":"00",
    "dl":"00",
    "dh":"00"
}




selected_option = ""
while selected_option != "-1":
    os.system('color 02')
    os.system('cls')
    print("------------------------------------------------------------------------------\n")
    print("Here are the registers and their current values\n(type -1 to turn off processor):\n")

    display_registers()

    # wypisanie menu opcji
    print("")
    print("What would you like to do ?")
    print("1 - Change register value")
    print("2 - Copy register value (MOV)")
    print("3 - Exchange register value (XCHG)")
    print("4 - Increment register value (INC)")
    print("5 - Decrement register value (DEC)")
    print("6 - Invert register value (NOT)")
    print("7 - Negate register value (NEG)")
    print("8 - use AND on registers (AND)")
    print("9 - use OR on registers (OR)")
    print("10 - use XOR on registers (XOR)")
    print("11 - Add register values (ADD)")
    print("12 - Subtract register values (SUB)")
    
    selected_option = input("Your choice --> ")
    
    # wybieranie operacji do wykonania
    match selected_option:
        case '1':
            os.system('cls')
            registers = reg_value_change(registers)
        case '2':
            os.system('cls')
            registers = MOV(registers)
        case '3':
            os.system('cls')
            registers = XCHG(registers)
        case '4':
            os.system('cls')
            registers = INC(registers)
        case '5':
            os.system('cls')
            registers = DEC(registers)
        case '6':
            os.system('cls')
            registers = NOT(registers)
        case '7':
            os.system('cls')
            registers = NEG(registers)
        case '8':
            os.system('cls')
            registers = AND(registers)
        case '9':
            os.system('cls')
            registers = OR(registers)
        case '10':
            os.system('cls')
            registers = XOR(registers)
        case '11':
            os.system('cls')
            registers = ADD(registers)
        case '12':
            os.system('cls')
            registers = SUB(registers)
        case '-1':
            break
        case default :
            print("Not a valid option")
            time.sleep(1)
    

print("Good bye !")
time.sleep(1)
# KONIEC PROGRAMU