# APPDAET Taylor Series Mathematical Explorer

A Python desktop application that demonstrates how Taylor and Maclaurin series can be used to approximate mathematical functions.

## 1. Project Description

The Taylor Series Mathematical Explorer is our final project for APPDAET Python Programming.

The purpose of this project is to show how mathematical functions can be approximated using Taylor and Maclaurin series. Instead of simply calculating a function's value, the application will show how the individual terms of a series contribute to the final answer.

Users will be able to select a mathematical function, enter an x-value, and choose how many terms to use in the calculation.

The application will then display the approximate answer, the actual reference value, the difference between the two values, a breakdown of the terms, and a graph comparing the original function with its approximation.

## 2. Project Objectives

The main objectives of this project are:

- To create a Python application that calculates Taylor and Maclaurin series.
- To support five mathematical functions: exponential, logarithm, sine, cosine, and tangent.
- To allow users to choose the number of terms used in the calculation.
- To show how each term contributes to the final answer.
- To compare the approximate answer with the actual function value.
- To display a graph showing the original function and its approximation.
- To practice using Python functions, loops, conditional statements, and GUI development.

## 3. Supported Mathematical Functions

The application will support the following functions based on the official project specifications.

| Mathematical Function | Expansion Center | Number of Terms | Allowed x-Values |
|---|---|---|---|
| Exponential (eˣ) | 0 | 1–12 | -2 to 2 |
| Natural Logarithm (ln x) | 1 | 1–20 | 0.5 to 1.5 |
| Sine (sin x) | 0 | 1–12 | -2 to 2 |
| Cosine (cos x) | 0 | 1–12 | -2 to 2 |
| Tangent (tan x) | 0 | 1–5 | -1 to 1 |

## 4. Main Application Features

The application will have the following features:

1. **Function Selection** – Users can select which mathematical function they want to calculate.

2. **Input Values** – Users can enter an x-value and select the number of terms to use.

3. **Series Calculation** – The program will calculate the approximation using our own Python functions and mathematical formulas.

4. **Result Comparison** – The application will show the approximate value, reference value, and absolute error.

5. **Term Breakdown** – Each term and its running total will be displayed to show how the approximation is calculated.

6. **Graph Visualization** – A graph will compare the original mathematical function with its Taylor or Maclaurin approximation.

7. **Input Validation** – The program will check whether the entered values are valid before performing calculations.

## 5. Technologies and Tools

| Technology | Purpose |
|---|---|
| Python 3.13 | Main programming language |
| PyCharm | Used to write, run, and debug the Python code |
| Tkinter | Used to create the application's interface |
| Matplotlib | Used to create the graphs |
| NumPy | Used to generate values for graph plotting |
| Git | Used to track changes in the project |
| GitHub | Used to store and share the project files |

## 6. Project Folder Structure

The project is organized into different folders and Python files to make the code easier to manage.

```text
APPDAET-Taylor-Series-Explorer/
│
├── src/
│   ├── main.py
│   ├── series.py
│   └── plotting.py
│
├── docs/
│
├── presentation/
│
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt
```

### Description of the Files

- **main.py** – The main file that will run the application. It will handle the interface and connect the different parts of the program.

- **series.py** – This file will contain the mathematical formulas and functions used to calculate the Taylor and Maclaurin series.

- **plotting.py** – This file will handle the graphs that compare the original mathematical functions with their approximations.

- **docs/** – This folder will contain the project documentation and reports.

- **presentation/** – This folder will contain the project's presentation files.

- **tests/** – This folder will contain test files used to check whether the calculations work correctly.

- **README.md** – Contains information about the project and instructions on how to run it.

- **requirements.txt** – Lists the additional Python libraries needed by the project.

- **.gitignore** – Contains files and folders that should not be uploaded to GitHub.

## 7. Installation and Setup

### Requirements

Before running the application, the following should be installed:

- Python 3.13
- PyCharm
- Git
- Matplotlib
- NumPy

### Step 1: Clone the Repository

Copy the repository URL from GitHub and run this command in the terminal:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace the placeholder with the actual repository URL.

### Step 2: Open the Project

Open the downloaded project folder in PyCharm and configure the Python interpreter.

### Step 3: Install the Required Libraries

Open the PyCharm terminal and execute:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

After the application has been developed, run the following command:

```bash
python src/main.py
```

## 8. How the Application Calculates the Results

The application will use Taylor and Maclaurin series to calculate approximate values of the selected mathematical functions.

Each series is made up of individual terms. The program will calculate these terms one at a time and add them together to get the final approximation.

The program will also calculate the actual function value using Python's math library. This value will be used as a reference to check how close the approximation is.

The absolute error will be calculated using:

**Absolute Error = |Reference Value − Approximate Value|**

The smaller the absolute error, the closer the approximation is to the reference value.

The mathematical approximation itself will be calculated using our own Python functions rather than built-in mathematical functions.

## 9. Testing and Validation

The group will test the application to make sure that the calculations and features work correctly.

The planned tests include:

- Checking whether each mathematical function produces the expected result.
- Testing different numbers of terms.
- Checking the minimum and maximum allowed x-values.
- Testing invalid or nonnumeric inputs.
- Checking whether invalid term counts are rejected.
- Comparing the calculated approximations with reference values.
- Checking whether the graphs display correctly.

The group will also use the acceptance tests provided in the official project specifications.

## 10. Current Development Status

**Current Phase: Progress Report 1 – Project Foundation, Planning, and GitHub Initialization**

The group has started preparing the project structure using PyCharm and has created the initial Python files and project documentation.

The next stages will focus on implementing the mathematical calculations, developing the graphical interface, creating the graphs, and testing the application.

## 11. Project Information

**Course:** APPDAET – Python Programming

**Project Title:** Taylor Series Mathematical Explorer

**Instructor:** Engr. Bob Mathew D. Sunga, MSc.

**Group Members:**
- Joson, Ezekiel Daniel
- Romulo, Joseph Chadwick
- Macatangay, Andrei Ronald

## 12. AI Assistance Disclosure

ChatGPT was used to help organize the project, explain concepts, and review the documentation, algorithms, and requirements to ensure correctness. 
The group members are responsible for creating, implementing, testing, and understanding the project.