def display_current_value():
    global current_value
    print("Current value: ", current_value)
    
def add(to_add):
    global current_value
    global last_value
    last_value = current_value
    current_value = current_value + to_add
    
def mult(to_mult):
    global current_value
    global last_value
    last_value = current_value
    current_value = current_value * to_mult
    
def  div(to_div):
    global current_value
    global last_value
    last_value = current_value
    current_value = current_value / to_div
    
def memorize():
    global current_value
    global memory
    memory = current_value
    
def recall():
    global current_value
    global memory
    global last_value
    last_value = current_value
    current_value = memory
    
def undo():
    global current_value
    global last_value
    current_value, last_value = last_value, current_value
    

if __name__ == "__main__":
    current_value = 0
    memory = 0
    print("Welcome to the calcultor program")
    add(5)
    undo()
    memorize()
    mult(10)
    display_current_value()
    recall()
    display_current_value()
    


    
    
    