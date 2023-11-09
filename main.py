class Calculator():
    operator_dic = {"+" : "plus", "-" : "minus", "*" : "multiply"}

    selected_operator = None

    prev_input = None
    current_input = None

    error_state = None

    def __init__(self):
        self.error_state = False
        self.is_calculate_done = False
        pass

    def calculate(self, n1, n2, op):
        pass

    def errorCheck(self):
        # TODO if prev_input is number then current_input must be operator, if prev_input is operator then current_input must be number

        # TODO if current_input is number but is not integer then error_state is True

        # TODO if current_input is operator but is not selected_operator then error_state is True

        if self.error_state:
            print("ERROR!")
            return

    def calculate_Start(self):
        while True:
            self.current_input = input()
            self.errorCheck()
            if self.is_calculate_done:
                # TODO 결과값 출력
                pass

            #if not (temp.isdigit() or temp in ['*', '-', '+']): # 숫자가 아니거나, 연산자가 아니면 error
                #error()
            #else :
                #if temp.isdigit() and (not flag):
                    #calculate(slef, n1, temp, op)
                #elif flag and (temp == '*' or temp=='-' or temp == '+') and temp == op:
                    #continue
                #else :
                    #error()

if __name__ == '__main__':
    calculator = Calculator()
    calculator.calculate_Start()