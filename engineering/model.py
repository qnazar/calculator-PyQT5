class EngineModel:
    def __init__(self):
        self.memory = 0

    @staticmethod
    def evaluate(expression):
        try:
            result = str(eval(expression))
        except Exception:
            return 'ERROR'
        return result

    @staticmethod
    def get_last_operand(expression):
        start = len(expression) - 1
        end = 0
        count = -1
        char = expression[start]

        if char == ')':
            stack = []
            stack.append(char)
            while stack:
                count -= 1
                start -= 1
                char = expression[start]
                if char == ')':
                    stack.append(')')
                if char == '(':
                    stack.pop()
            return expression[:count], expression[count:]

        while start >= end:
            char = expression[start]
            if char.isdigit() or char == '.':
                start -= 1
            else:
                break

        return expression[:start + 1], expression[start + 1:]

    @staticmethod
    def factorial(n):
        if not isinstance(n, int):
            return 'ERROR'
        if n == 1:
            return 1
        return n * EngineModel.factorial(n-1)

    @staticmethod
    def sqrt(n):
        return n ** 0.5
