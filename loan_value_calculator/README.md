# Loan_Value_Calculator

This repository contains a Python program designed to automate various tasks associated with valuing microlending loans. The program encompasses a range of functionalities including calculation automation, loan data analysis, financial calculations, conditional loan filtering, and result saving.

## Features

* __Automate Calculations:__
* Calculate total number of loans and total value of loans.
* Determine average loan price.
* __Analyze Loan Data:__
* Calculate the present value of a loan based on future value, remaining months, and a discount rate.
* __Perform Financial Calculations:__
* Encapsulate present value calculation in a function for reuse.
* __Conditionally Filter Lists of Loans:__
* Identify and collect loans priced at or below a specified amount.
* __Save the Results:__
* Output the list of filtered loans to a CSV file.

## Technologies Used
This project uses the following technologies:

* `Python` - The programming language used.
* `pathlib` - For constructing new paths from names of files and from relative paths.
* `csv` - Module for reading and writing CSV files.

## Installation
1. Ensure you have [Python 3.x](https://www.python.org/downloads/)installed on your local machine.
2. Clone the repository to your local machine using the following command:
```
git clone https://github.com/<your-username>/microlending-loan-valuation.git

```
3. Navigate to the project directory:
```
cd microlending-loan-valuation

```

4. (Optional) Create a virtual environment to manage dependencies for this project:

```
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

```

## Usage

Run the main program:
```
python loan_calculator.py

```

### Contributors
Alexander Likhachev

### License
This project is licensed under the MIT License- see the [License](LICENSE.md) file for details.