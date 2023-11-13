import EasterEgg

class Calculator():
    operator_dic = {"+" : "plus", "-" : "minus", "*" : "multiply"} #연산자 Dictionary

    selected_operator = None #선택된 연산자종류
    prev_input = None #이전값
    current_input = None #현재값
    result = None #연산의 결과값

    error_state = None

    def __init__(self):
        self.error_state = False
        self.is_calculate_done = False
        self.result = 0
        self.prev_input = self.operator_dic["plus"] # 초기 current_input과의 충돌을 방지하기 위한 초기화 값. 의미 없는 값이므로 혼동하지 말 것.
        pass

    # TODO : result와 이전 값의 연산
    def addNumber(self):
        pass
    def subtractNumber(self):
        pass
    def multiplyNumber(self):
        pass

    def calculate(self):
        # TODO : 현재값이 존재해야만 아래의 계산이 수행되어야 함. 조건문으로 처리 해줄 것.
        # TODO : 조건문에서 현재 연산자와 +, -, * 비교 후, 각 조건문에서 함수 처리.
        # TODO : 연산값을 결과 값에 넣어주어야 함.
        pass


    def errorCheck(self):
        if self.selected_operator is None:
            self.result = self.current_input # 처음 숫자가 입력될 때, result을 current_input 바꿔준다.

        # TODO : 해당 로직 내에서, 에러가 발생했다면, error_state를 True로 설정하여라.

        if isinstance(self.prev_input, int): # prev_input이 정수인데
            if not self.current_input in self.operator_dic: # current_input이 연산자가 아닐 경우
                self.error_state = True
            else : # current_input이 연산자일 때..
                if self.selected_operator is not None and self.current_input != self.selected_operator:
                    # None이 아닐 때, 현재 연산자와 이전 연산자가 다르다면 에러.
                    self.error_state = True

        elif self.prev_input in self.operator_dic: # prev_input이 연산자인데
            if not isinstance(self.current_input, int) : # current_input이 정수가 아니라면
                self.error_state = True
        else: # prev_input이 정수도, 연산자도 아닌 경우
            self.error_state = True

        # TODO : prev_input이 정수라면, current_input은 연산자여야 함. 또한, prev_input이 연산자라면 current_input은 정수여야 함.
        # TODO : current_input이 숫자라면, 반드시 정수여야 함.
        # TODO : current_input이 연산자라면, selected_operator가 None이거나(초기 상태) selected_operator와 같아야 함.

        # TODO : edge케이스가 있다면 추가작성요망.

        if self.error_state:
            print("ERROR!")
            exit(0)

    def calculate_Start(self):
        while True:
            self.current_input = input()

            if self.current_input == EasterEgg.EASTEREGG_TRIGGER: # 이스터에그의 값일 시, 이스터에그 수행.
                EasterEgg.easterEgg() # 수행될 이스터에그

            self.errorCheck() # 에러체크
            self.prev_input = self.current_input # errorCheck를 위한 prev_input 계승

            if self.current_input == "=":
                    print(self.result) # 결과 값 출력 후 종료
                    return

            elif self.current_input not in self.operator_dic: # 숫자 입력시
                self.calculate()
            else: # 연산자 입력시
                self.selected_operator = self.current_input