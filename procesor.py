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
                registers[selected_register] = register_input
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
    os.system('color 01')
    display_registers()
    selected_register = ""
    to_home = False
    
    print("\nWelcome to MOV menu. Here you can copy value from one register into the other\n")
    
    
    while to_home == False:
        
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
        break
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
    
    selected_option = input("Your choice --> ")
    
    match selected_option:
        case '1':
            os.system('cls')
            registers = reg_value_change(registers)
        case '2':
            os.system('cls')
            registers = MOV(registers)
        case '-1':
            break
        case default :
            print("Not a valid option")
            time.sleep(1)
    

print("Good bye !")
time.sleep(1)
# KONIEC PROGRAMU



