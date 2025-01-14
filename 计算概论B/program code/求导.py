class Polynomial:
    def __init__(self, polynomial_str):
        """
        Initialize the polynomial from a string representation.
        :param polynomial_str: A string representing the polynomial (e.g., "2x^3+3x^2+5x+1")
        """
        self.polynomial = polynomial_str
        self.part = []

    def parse_terms(self):
        """
        Parse the polynomial string into individual terms.
        :return: A list of tuples containing (coefficient, variable, exponent)
        """
        len1 = len(self.polynomial)
        parts = []
        temp1 = '0'
        temp2 = '0'
        variable = ''
        positive = 1
        state = 1
        for i in range(len1):
            if i == 0 and self.polynomial[i] == '-':
                positive = -1
            elif self.polynomial[i].isdigit() or self.polynomial[i]=='.':
                if state:
                    temp1 += self.polynomial[i]
                else:
                    temp2 += self.polynomial[i]
            else:
                if self.polynomial[i] not in {'+', '-', '^'}:
                    variable = self.polynomial[i]
                    if temp1 == '0':temp1 = '1'
                    if i == len1 - 1 or self.polynomial[i+1] != '^':
                        parts.append((positive*float(temp1), variable, 1))
                        temp1 = '0'
                        temp2 = '0'
                        state = 1
                        continue
                    state = 0
                if self.polynomial[i] in {'+', '-'}:
                    state = 1
                    parts.append((positive*float(temp1), variable, int(temp2)))
                    if self.polynomial[i] == '+':
                        positive = 1
                    else:
                        positive = -1
                    temp1 = '0'
                    temp2 = '0'
        parts.append((positive*float(temp1), variable, int(temp2)))
        x, y, z = parts[0]
        parts[0] = (x, variable, z)
        self.part = sorted(parts, key=lambda pair: pair[2], reverse=True)
        ans = ''
        for x, y, z in self.part:
            if x == 0 and z == 0:continue
            if ans:
                if x > 0:
                    ans = ans +'+'
            if abs(x) != 1:
                if z > 1:
                    ans = ans + str(x)+variable+'^'+str(z)
                if z == 1:
                    ans = ans + str(x)+variable
                if z == 0:
                    ans = ans +str(x)
            else:
                if z > 1:
                    ans = ans +variable+'^'+str(z)
                if z == 1:
                    ans = ans +variable
                if z == 0:
                    ans = ans +str(x)
        self.polynomial = ans
        # TODO: Implement polynomial parsing
        pass

    def derive_term(self, coefficient, variable, exponent):
        """
        Calculate the derivative of a single term.
        :param coefficient: The coefficient of the term
        :param variable: The variable (e.g., 'x')
        :param exponent: The exponent of the term
        :return: A string representing the derivative of the term
        """
        
        if exponent > 2:
            return str(coefficient*exponent)+variable+'^'+str(exponent-1)
        elif exponent == 2:
            return str(coefficient*exponent)+variable
        return str(coefficient*exponent)
        # TODO: Implement single term derivative
        pass

    def derivative(self):
        """
        Calculate the first derivative of the polynomial.
        :return: A string representing the derivative of the polynomial
        """
        # TODO: Implement polynomial derivative calculation
        self.parse_terms()
        ans = ''
        for x, y, z in self.part:
            if ans:
                if z > 0:
                    if x > 0:
                        ans = ans + '+'
                    ans = ans + self.derive_term(x,y,z)
                
            else:
                ans = ans + self.derive_term(x,y,z)
        return ans
        pass


# Example usage
if __name__ == '__main__':
    # Test cases
    poly1 = Polynomial("2x^3+3x^2+5x+1")
    print("Original polynomial:", poly1.polynomial)
    print("Derivative:", poly1.derivative())  # Should output: "6x^2+6x+5"

    poly2 = Polynomial("y^4-2y^2+3y-7")
    print("Original polynomial:", poly2.polynomial)
    print("Derivative:", poly2.derivative())  # Should output: "4y^3-4y+3"完成这个代码
    while True:
        poly3 = Polynomial(input())
        print("Original polynomial:", poly3.polynomial)
        print("Derivative:", poly3.derivative())