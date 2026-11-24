
import math
import numpy as np
import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from series import calculate_series


def get_reference_function(function):

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

    domains = {
        "exp": (-2, 2),
        "ln": (0.5, 1.5),
        "sin": (-2, 2),
        "cos": (-2, 2),
        "tan": (-1, 1)
    }

    return domains[function]


def plot_comparison(function, x, n):

    reference_function = get_reference_function(function)

    minimum, maximum = get_function_domain(function)

    x_values = np.linspace(minimum, maximum, 200)

    reference_values = []
    approximation_values = []

    for value in x_values:

        # Calculate actual function value
        reference_values.append(
            reference_function(float(value))
        )

        # Calculate Taylor approximation
        terms, partial_sums = calculate_series(
            function,
            float(value),
            n
        )

        approximation_values.append(partial_sums[-1])

    # Create graph
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        x_values,
        reference_values,
        label="Reference Function",
        linewidth=2
    )

    ax.plot(
        x_values,
        approximation_values,
        label="Taylor Approximation",
        linestyle="--",
        linewidth=2
    )

    ax.axvline(x=x, linestyle=":", alpha=0.6,
               label="Selected x")

    ax.set_title(f"Taylor Series Approximation - {function}")
    ax.set_xlabel("x")
    ax.set_ylabel("Function Value")

    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    # Display graph
    plt.show(block=True)
