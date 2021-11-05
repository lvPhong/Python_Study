from itertools import zip_longest


class Polynomial():
    """
    A Polynomial has a form:
    P_n(x) = a_0*x^n + a_1*x^(n-1) + ... + a_(n-1)*x + a_n
        has (n+1) coefficients a_i, for all i = 0 to n
        x : variable
        n : degree
    """

    def __init__(self, *coefficients):
        """
        *coefficients is  (a_0, a_1, ..., a_n)
        when enter Polynomial(a_0, a_1, ..., a_n) then (a_0, a_1, ..., a_n) is a tuple,
        should be convert it to the list to calculate easier.
        """
        self.coefficients = list(coefficients)

    @property
    def deg(self):
        poly_deg = len(self.coefficients) - 1
        return poly_deg

    def __repr__(self):
        coeffs = self.coefficients
        poly_deg = self.deg
        poly_str = ""
        for power, coeff in enumerate(coeffs):  # power is degree of x^i
            # convert a_k*x^(n-k) to coeff_str::string
            if power < poly_deg - 1:
                coeff_str = str(coeff) + "x^" + str(poly_deg - power)
            elif power == poly_deg - 1:
                coeff_str = str(coeff) + "x"
            else:
                coeff_str = str(coeff)
            # add coeff_str to poly_str
            if coeff > 0:
                poly_str += (" + " + coeff_str)
            elif coeff < 0:
                poly_str += (" - " + coeff_str.lstrip("-"))
            else:
                poly_str += ""
        # remove " + " in first coeff_str
        return poly_str.lstrip(" + ")

    # calculate the value of f at x
    def __call__(self, x):
        """
        P_n(x) = a_0*x^n + a_1*x^(n-1) + ... + a_(n-1)*x + a_n
        P_0(x) = a_0
        P_1(x) = x*P_0(x) + a_1
        ...
        P_(k+1)(x) = x*P_k(x) + a_(k+1)
        """
        coeffs = self.coefficients
        P_x = 0
        for coeff in coeffs:
            P_x = x*P_x + coeff
        return P_x

    def add_poly(self, other_poly):
        coeffs1_inv = self.coefficients[::-1]
        coeffs2_inv = other_poly.coefficients[::-1]
        coeffs_zip = zip_longest(coeffs1_inv, coeffs2_inv, fillvalue=0)
        coeffs_sum_inv = [(coeff1 + coeff2)
                          for coeff1, coeff2 in coeffs_zip]
        coeffs_sum = coeffs_sum_inv[::-1]
        return Polynomial(*coeffs_sum)

    def add_scalar(self, scalar):
        coeffs_add_scalar = self.coefficients
        coeffs_add_scalar[-1] += scalar
        return Polynomial(*coeffs_add_scalar)

    def sub_poly(self, other_poly):
        coeffs1_inv = self.coefficients[::-1]
        coeffs2_inv = other_poly.coefficients[::-1]
        coeffs_zip = zip_longest(coeffs1_inv, coeffs2_inv, fillvalue=0)
        coeffs_sub_inv = [(coeff1 - coeff2)
                          for coeff1, coeff2 in coeffs_zip]
        coeffs_sub = coeffs_sub_inv[::-1]
        return Polynomial(*coeffs_sub)

    def mul_scalar(self, scalar):
        coeffs = self.coefficients
        coeffs_mul_scalar = [scalar*coeff for coeff in coeffs]
        return Polynomial(*coeffs_mul_scalar)

    # def mul_poly
    def mul_poly(self, other_poly):
        coeffs1_inv = self.coefficients[::-1]
        coeffs2_inv = other_poly.coefficients[::-1]
        coeffs_mul_deg = self.deg + other_poly.deg
        # coeffs_mul[i] = a_i, for all i = 0 to coeffs_mul_deg
        coeffs_mul_inv = [0]*(coeffs_mul_deg + 1)
        for coeff1_deg, coeff1 in enumerate(coeffs1_inv):
            for coeff2_deg, coeff2 in enumerate(coeffs2_inv):
                coeffs_mul_inv[coeff1_deg + coeff2_deg] += coeff1*coeff2
        coeffs_mul = coeffs_mul_inv[::-1]
        return Polynomial(*coeffs_mul)


# def add_poly(self, other_poly):
#     deg1, deg2 = self.deg, other_poly.deg
#     diff_deg = abs(deg1 - deg2)
#     coeffs1 = self.coefficients
#     coeffs2 = other_poly.coefficients
#     if deg1 > deg2:
#         coeffs2 = [0]*diff_deg + coeffs2
#         coeffs_sum = [coeffs1[i] + coeffs2[i] for i in range(len(coeffs1))]
#     else:
#         coeffs1 = [0]*diff_deg + coeffs1
#         coeffs_sum = [coeffs1[i] + coeffs2[i] for i in range(len(coeffs2))]
#     return Polynomial(*coeffs_sum)
