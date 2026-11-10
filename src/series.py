import math


def calculate_exponential(x, n):
    """Calculate e^x using the Maclaurin series."""

    terms = []
    partial_sums = []
    total = 0

    for k in range(n):
        term = (x ** k) / math.factorial(k)

        total += term
        terms.append(term)
        partial_sums.append(total)

    return terms, partial_sums


def calculate_logarithm(x, n):
    """Calculate ln(x) using the Taylor series centered at 1."""

    terms = []
    partial_sums = []
    total = 0

    for k in range(1, n + 1):
        term = ((-1) ** (k + 1) * (x - 1) ** k) / k

        total += term
        terms.append(term)
        partial_sums.append(total)

    return terms, partial_sums


def calculate_sine(x, n):
    """Calculate sin(x) using the Maclaurin series."""

    terms = []
    partial_sums = []
    total = 0

    for k in range(n):
        term = ((-1) ** k * x ** (2 * k + 1)) / math.factorial(2 * k + 1)

        total += term
        terms.append(term)
        partial_sums.append(total)

    return terms, partial_sums


def calculate_cosine(x, n):
    """Calculate cos(x) using the Maclaurin series."""

    terms = []
    partial_sums = []
    total = 0

    for k in range(n):
        term = ((-1) ** k * x ** (2 * k)) / math.factorial(2 * k)

        total += term
        terms.append(term)
        partial_sums.append(total)

    return terms, partial_sums


def calculate_tangent(x, n):
    """Calculate tan(x) using the first five specified terms."""

    coefficients = [
        1,
        1 / 3,
        2 / 15,
        17 / 315,
        62 / 2835
    ]

    terms = []
    partial_sums = []
    total = 0

    for k in range(n):
        term = coefficients[k] * (x ** (2 * k + 1))

        total += term
        terms.append(term)
        partial_sums.append(total)

    return terms, partial_sums


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
