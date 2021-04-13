
import sys
import numpy as np
from IPython import embed

print("Dice roller ready! Please input dice to be rolled:\n")
roll = 1;
while(True):
    in_data = input(f"\n# {roll}: ")
    multiple_roll =  False
    prefix_d = False
    try:
        if "d" in in_data:
            d = in_data.find("d")
            if(d==0):
                prefix_d = True
            else:
                multiple_roll = True
        if(multiple_roll):
            n = int(in_data[:d])
            d_type = int(in_data[d+1:])
            val = []
            for i in range(n):
                val.append(np.random.randint(1,d_type+1))
            msg=(f"\nRolling {n}d{d_type}! \nResult: ")
            print(msg, *val)
            print(f"Total: {sum(val)}")
            roll+=1
        else:
            if(prefix_d):
                n = int(in_data[1:])+1
            else:
                n = int(in_data)+1
            result = np.random.randint(1,n)
            if(n == 21 and result == 20):
                result = "20! Critical success!"
            if(result == 1):
                result = "1! Critical failure!"
            msg = f"Rolling a d{n-1} \nResult: {result}"
            print(msg)
            roll+=1
    except Exception as e:
        print("Invalid input. Please offer up the number of sides of the dice to be rolled.")
        print("Usage: [number]d[dice] OR d[number] OR [number]")
        print("Example: '4d6' or 'd6' or '6'")
