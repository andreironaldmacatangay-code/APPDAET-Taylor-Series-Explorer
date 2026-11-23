import math

def build_series(term_function, n):
    terms = []
    partial_sums = []
    total = 0

    for k in range(n):
        term = term_function(k)
        total += term

        terms.append(term)
        partial_sums.append(total)

    return terms, partial_sums
def calculate_exponential(x, n):
    """Calculate e^x using the Maclaurin series."""

    return build_series(lambda k: (x ** k) / math.factorial(k), n)

def calculate_logarithm(x, n):
    """Calculate ln(x) using the Taylor series centered at 1."""
    
    if x <= 0:
        raise ValueError("x must be greater than 0 for ln(x).")

    return build_series(lambda k: ((-1) ** (k + 1)) * ((x - 1) ** k) / k, n, start=1)
   

def calculate_sine(x, n):
    """Calculate sin(x) using the Maclaurin series."""

    return build_series(lambda k: ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1), n)

def calculate_cosine(x, n):
    """Calculate cos(x) using the Maclaurin series."""

    return build_series(lambda k: ((-1) ** k) * (x ** (2 * k)) / math.factorial(2 * k), n)
def calculate_tangent(x, n):
    """Calculate tan(x) using the first five Taylor terms."""
    coefficients = [
        1,
        1 / 3,
        2 / 15,
        17 / 315,
        62 / 2835
    ]

    if n > len(coefficients):
        raise ValueError("Tangent is limited to 5 terms.")

    if x <= -math.pi / 2 or x >= math.pi / 2:
        raise ValueError("x must be in the range (-pi/2, pi/2).")

    return build_series(
        lambda k: coefficients[k] * x ** (2 * k + 1),
        n
    )
   

def calculate_series(function, x, n):
    """Select the appropriate series calculation."""

    if function == "exp":
        return calculate_exponential(x, n)

    elif function == "ln":
        return calculate_logarithm(x, n)

    elif function == "sin":
        return calculate_sine(x, n)

    elif function == "cos":
        return calculate_cosine(x, n)

    elif function == "tan":
        return calculate_tangent(x, n)

    else:
        raise ValueError("Unsupported mathematical function.")
