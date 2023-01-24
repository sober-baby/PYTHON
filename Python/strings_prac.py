#f-string
x= 12

f"the value of x is {x}"

def gen_nested_loop(n):
    res = "def gen_passwords(alphabet):\n"
    for i in range(n):
        res += f"{(i+1)*' '}for letter{i} in alphabet:\n"
    add_line = "password = "
    for i in range(n):
        add_line += f"letter{i} + "
    add_line += "''\n"

    res += f"{' '*(n+1)}{add_line}"
    res += f"{' '*n}print(password)"
    return res

if __name__ == "main":
    code_15 = gen_nested_loop(15)
    exec(code 15)
    gen password("adcdefgh")




