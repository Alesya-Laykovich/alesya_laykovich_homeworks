class ArithmeticOperation:

    def validate_parameters(self, a, b):
        is_valid_a = isinstance(a, (int, float))
        is_valid_b = isinstance(b, (int, float))
        if is_valid_a and is_valid_b:
            return 'Valid'
        else:
            raise TypeError('Not valid')

    def sum(self, a, b):
        self.validate_parameters(a, b)
        return a + b


arithmetic_operation = ArithmeticOperation()
print(arithmetic_operation.sum(15, 4))
print(arithmetic_operation.validate_parameters(12, 'g'))