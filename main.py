def error():
    print("ERROR!")
    return

#TODO
def calculate(n1, n2, op):
    pass

def calculator():
    n1 = input()
    op = input()
    flag = False; # False 일 때가 숫자를 입력받아야 하는 상태임.

    if not n1.isdigit():
        error()
    if not (op =='*' or op=='-' or op=='+'):
        error()

    while True:
        temp = input()
        if not (temp.isdigit() or temp in ['*', '-', '+']): # 숫자가 아니거나, 연산자가 아니면 error
            error()
        else :
            if temp.isdigit() and (not flag):
                calculate(n1, temp, op)
            elif flag and (temp == '*' or temp=='-' or temp == '+') and temp == op:
                continue;
            else :
                error()

if __name__ == '__main__':
    calculator()

