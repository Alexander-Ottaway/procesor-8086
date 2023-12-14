
dest_r = "46"
second_r = "0A"

dest_r = int(dest_r,16)
second_r = int(second_r,16)
new_value = dest_r + second_r
if new_value > 255:
    new_value -= 255 # overflow
    
new_value = str(hex(new_value))[2:]

if len(new_value) < 2: new_value = "0" + new_value

print( new_value.upper() )