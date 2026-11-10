import math
import numpy as np
import matplotlib.pyplot as plt

from src.series import calculate_series


def get_reference_function(function):
    """Return the actual mathematical function for comparison."""

    reference_functions = {
        "exp": math.exp,
        "ln": math.log,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan
    }

    if function not in reference_functions:
        raise ValueError("Unsupported mathematical function.")

    return reference_functions[function]


def get_function_domain(function):
    """Return the supported x-range of the selected function."""

    domains = {
        "exp": (-2, 2),
        "ln": (0.5, 1.5),
        "sin": (-2, 2),
        "cos": (-2, 2),
        "tan": (-1, 1)
    }

    return domains[function]


def plot_comparison(function, x, n):
    """Plot the reference function and its Taylor approximation."""

    reference_function = get_reference_function(function)

    minimum, maximum = get_function_domain(function)

    x_values = np.linspace(minimum, maximum, 200)

    reference_values = []
    approximation_values = []

    for value in x_values:

        # Calculate the actual function value
        reference_values.append(reference_function(value))

        # Calculate the Taylor series approximation
        terms, partial_sums = calculate_series(function, value, n)

        approximation_values.append(partial_sums[-1])

    # Create the graph
    plt.figure(figsize=(9, 5))

    plt.plot(
        x_values,
        reference_values,
        label="Reference Function",
        linewidth=2
    )

    plt.plot(
        x_values,
        approximation_values,
        label="Taylor Approximation",
        linestyle="--",
        linewidth=2
    )

    # Mark the selected input value
    plt.axvline(x=x, linestyle=":", alpha=0.6)

    plt.title(f"Taylor Series Approximation - {function}")
    plt.xlabel("x")
    plt.ylabel("Function Value")

    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
