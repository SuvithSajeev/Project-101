import random

response = "y"
response = input("Do u want to roll a dice or not? ")

while response == "y" :
    no = random.randint(1,6)
    
    if(response == "y"):
        if(no == 1):
            print(" ----- ")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print(" ----- ")
            
        if(no == 2):
            print(" ----- ")
            print("[     ]")
            print("[ 0 0 ]")
            print("[     ]")
            print(" ----- ")
            
        if(no == 3):
            print(" ----- ")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print(" ----- ")
            
        if(no == 4):
            print(" ----- ")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print(" ----- ")
            
        if(no == 5):
            print(" ----- ")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print(" ----- ")
            
        if(no == 6):
            print(" ----- ")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print(" ----- ")
        
        response2 = input("Press y to roll again and n to exit.")
    
        if(response2 == "y"):
            response = "y"
            continue
        
    if(response2 == "n"):
        break
    
    break
        