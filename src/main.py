
"""
APPDAET Final Project
Taylor Series Mathematical Explorer

Main application entry point.
"""

import math
import tkinter as tk
from tkinter import ttk, messagebox

from src.series import calculate_series
from src.plotting import plot_comparison


class TaylorSeriesExplorer:

    def __init__(self, root):
        self.root = root
        self.root.title("Taylor Series Mathematical Explorer")
        self.root.geometry("850x700")
        self.root.resizable(True, True)

        # Input variables
        self.function = tk.StringVar(value="exp")
        self.x_value = tk.StringVar()
        self.center_value = tk.StringVar(value="0")
        self.n_value = tk.StringVar()

        self.create_interface()

    def create_interface(self):

        # Main title
        title = ttk.Label(
            self.root,
            text="TAYLOR SERIES APPROXIMATION",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        # Input section
        input_frame = ttk.LabelFrame(
            self.root,
            text="Input Parameters",
            padding=15
        )
        input_frame.pack(fill="x", padx=20, pady=10)

        # Function selection
        ttk.Label(
            input_frame,
            text="Select Function:"
        ).grid(row=0, column=0, padx=10, pady=8, sticky="w")

        function_menu = ttk.Combobox(
            input_frame,
            textvariable=self.function,
            values=["exp", "ln", "sin", "cos", "tan"],
            state="readonly",
            width=20
        )
        function_menu.grid(row=0, column=1, padx=10, pady=8)

        function_menu.bind(
            "<<ComboboxSelected>>",
            self.update_center
        )

        # Input x
        ttk.Label(
            input_frame,
            text="Input Value (x):"
        ).grid(row=1, column=0, padx=10, pady=8, sticky="w")

        ttk.Entry(
            input_frame,
            textvariable=self.x_value,
            width=23
        ).grid(row=1, column=1, padx=10, pady=8)

        # Center of expansion
        ttk.Label(
            input_frame,
            text="Center of Expansion:"
        ).grid(row=2, column=0, padx=10, pady=8, sticky="w")

        ttk.Entry(
            input_frame,
            textvariable=self.center_value,
            width=23,
            state="readonly"
        ).grid(row=2, column=1, padx=10, pady=8)

        # Number of terms
        ttk.Label(
            input_frame,
            text="Number of Terms:"
        ).grid(row=3, column=0, padx=10, pady=8, sticky="w")

        ttk.Entry(
            input_frame,
            textvariable=self.n_value,
            width=23
        ).grid(row=3, column=1, padx=10, pady=8)

        # Buttons
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=15
        )

        ttk.Button(
            button_frame,
            text="Calculate Approximation",
            command=self.calculate
        ).pack(side="left", padx=8)

        ttk.Button(
            button_frame,
            text="Show Graph",
            command=self.show_graph
        ).pack(side="left", padx=8)

        # Results section
        result_frame = ttk.LabelFrame(
            self.root,
            text="Results",
            padding=15
        )
        result_frame.pack(fill="x", padx=20, pady=10)

        self.result_label = ttk.Label(
            result_frame,
            text="Enter your values and click Calculate Approximation.",
            font=("Arial", 11),
            justify="left"
        )
        self.result_label.pack(anchor="w")

        # Term contributions and partial sums
        table_frame = ttk.LabelFrame(
            self.root,
            text="Term Contributions / Running Partial Sums",
            padding=10
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        columns = ("term", "contribution", "partial_sum")

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )

        self.table.heading(
            "term",
            text="Term Number"
        )

        self.table.heading(
            "contribution",
            text="Term Contribution"
        )

        self.table.heading(
            "partial_sum",
            text="Running Partial Sum"
        )

        self.table.column(
            "term",
            width=110,
            anchor="center"
        )

        self.table.column(
            "contribution",
            width=250,
            anchor="center"
        )

        self.table.column(
            "partial_sum",
            width=250,
            anchor="center"
        )

        self.table.pack(
            fill="both",
            expand=True
        )

        # Set initial center
        self.update_center()

    def update_center(self, event=None):

        if self.function.get() == "ln":
            self.center_value.set("1")
        else:
            self.center_value.set("0")

    def validate_inputs(self):

        function = self.function.get()

        try:
            x = float(self.x_value.get())
            n = int(self.n_value.get())

        except ValueError:
            raise ValueError(
                "Please enter a valid number for x "
                "and a whole number for the number of terms."
            )

        if not math.isfinite(x):
            raise ValueError(
                "The value of x must be finite."
            )

        # Allowed number of terms
        term_limits = {
            "exp": (1, 12),
            "ln": (1, 20),
            "sin": (1, 12),
            "cos": (1, 12),
            "tan": (1, 5)
        }

        minimum_terms, maximum_terms = term_limits[function]

        if not minimum_terms <= n <= maximum_terms:
            raise ValueError(
                f"The number of terms for {function} "
                f"must be between {minimum_terms} "
                f"and {maximum_terms}."
            )

        # Allowed x range
        domains = {
            "exp": (-2, 2),
            "ln": (0.5, 1.5),
            "sin": (-2, 2),
            "cos": (-2, 2),
            "tan": (-1, 1)
        }

        minimum_x, maximum_x = domains[function]

        if not minimum_x <= x <= maximum_x:
            raise ValueError(
                f"For {function}, x must be between "
                f"{minimum_x} and {maximum_x}."
            )

        return function, x, n

    def calculate(self):

        try:
            function, x, n = self.validate_inputs()

            # Calculate Taylor series
            terms, partial_sums = calculate_series(
                function,
                x,
                n
            )

            approximation = partial_sums[-1]

            # Calculate reference value
            reference_functions = {
                "exp": math.exp,
                "ln": math.log,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan
            }

            reference = reference_functions[function](x)

            # Calculate absolute error
            absolute_error = abs(
                reference - approximation
            )

            # Display results
            self.result_label.config(
                text=(
                    f"Function: {function}\n"
                    f"Input x: {x}\n"
                    f"Center of Expansion: "
                    f"{self.center_value.get()}\n"
                    f"Number of Terms: {n}\n"
                    f"Taylor Approximation: "
                    f"{approximation:.10f}\n"
                    f"Reference Value: "
                    f"{reference:.10f}\n"
                    f"Absolute Error: "
                    f"{absolute_error:.10f}"
                )
            )

            # Clear previous table entries
            for item in self.table.get_children():
                self.table.delete(item)

            # Display individual terms and partial sums
            for index, (term, partial_sum) in enumerate(
                zip(terms, partial_sums),
                start=1
            ):

                self.table.insert(
                    "",
                    "end",
                    values=(
                        index,
                        f"{term:.10f}",
                        f"{partial_sum:.10f}"
                    )
                )

        except (ValueError, OverflowError) as error:

            messagebox.showerror(
                "Invalid Input",
                str(error)
            )

    def show_graph(self):

        try:
            function, x, n = self.validate_inputs()

            plot_comparison(
                function,
                x,
                n
            )

        except (ValueError, OverflowError) as error:

            messagebox.showerror(
                "Invalid Input",
                str(error)
            )


def main():

    root = tk.Tk()

    TaylorSeriesExplorer(root)

    root.mainloop()


if __name__ == "__main__":
    main()
